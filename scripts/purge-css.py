"""Retire des feuilles de style les règles qui ne s'appliquent à aucun élément du site.

Usage : python3 scripts/purge-css.py public

À lancer après `hugo build` et avant subset-icons.py (qui relève les icônes dans le CSS
purgé). Le thème compile Bootstrap en entier ; le script relève dans le site généré :
- les balises, classes et identifiants présents dans le HTML ;
- les mots des scripts (fichiers .js et scripts en ligne), pour garder les classes
  ajoutées par JavaScript (show, collapsing, active…).
Un sélecteur est conservé si toutes ses balises, classes et identifiants sont relevés ;
le contenu des pseudo-classes fonctionnelles (:not(), :is()…) et les sélecteurs
d'attributs ne sont pas examinés. Sont ensuite retirées les @keyframes qu'aucune règle
conservée ne nomme et les variables CSS que rien ne lit.

Hugo calcule l'empreinte et l'attribut integrity avant ce traitement : le script renomme
chaque feuille avec l'empreinte de son nouveau contenu et met à jour le HTML.

Dépendance : tinycss2 (pip install tinycss2).
"""
import base64
import hashlib
import os
import re
import sys
from html.parser import HTMLParser

import tinycss2
from tinycss2.ast import LiteralToken

# Classes composées par JavaScript, absentes telles quelles des scripts
# (Bootstrap Tooltip ajoute `bs-${NAME}-auto`)
SAFELIST = re.compile(r"^bs-tooltip-")
# Règles groupantes dont le contenu est purgé à son tour
GROUPING_RULES = {"media", "supports", "layer", "container"}
KEYFRAMES = {"keyframes", "-webkit-keyframes"}
# Longueur de l'empreinte hexadécimale ajoutée par `fingerprint` -> algorithme
DIGESTS = {32: "md5", 64: "sha256", 96: "sha384", 128: "sha512"}
WORD = re.compile(r"[\w-]+")
VAR = re.compile(r"var\(\s*(--[\w-]+)")
# Caractère non ASCII, et le caractère suivant s'il prolongerait l'échappement
NON_ASCII = re.compile(r"[^\x00-\x7f](?=([0-9a-fA-F\s])?)")


class Collector(HTMLParser):
    """Relève les balises, classes et identifiants du HTML, et les mots des scripts et styles."""

    def __init__(self, used):
        super().__init__()
        self.used = used
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        self.used["tags"].add(tag)
        attrs = dict(attrs)
        self.used["classes"].update((attrs.get("class") or "").split())
        if attrs.get("id"):
            self.used["ids"].add(attrs["id"])
        self.used["words"].update(WORD.findall(attrs.get("style") or ""))
        self.in_code = tag in ("script", "style")

    def handle_endtag(self, tag):
        self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.used["words"].update(WORD.findall(data))


def site_files(root, ext):
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.endswith(ext):
                yield os.path.join(dirpath, name)


def collect(root):
    used = {"tags": set(), "classes": set(), "ids": set(), "words": set()}
    for path in site_files(root, ".html"):
        with open(path, encoding="utf-8") as f:
            Collector(used).feed(f.read())
    for path in site_files(root, ".js"):
        with open(path, encoding="utf-8") as f:
            used["words"].update(WORD.findall(f.read()))
    return used


def split(tokens, separator):
    """Découpe une liste de jetons aux séparateurs de premier niveau."""
    parts = [[]]
    for token in tokens:
        if token.type == "literal" and token.value == separator:
            parts.append([])
        else:
            parts[-1].append(token)
    return parts


def join(parts, separator):
    tokens = []
    for part in parts:
        if tokens:
            tokens.append(LiteralToken(0, 0, separator))
        tokens.extend(part)
    return tokens


def selector_used(selector, used):
    words = used["words"]
    previous = None
    for token in selector:
        if token.type == "ident":
            after = previous.value if previous is not None and previous.type == "literal" else None
            if after == ".":
                if token.value not in used["classes"] and token.value not in words \
                        and not SAFELIST.match(token.value):
                    return False
            elif after != ":" and token.value.lower() not in used["tags"] and token.value not in words:
                # balise, sauf après « : » (pseudo-classe ou pseudo-élément)
                return False
        elif token.type == "hash" and token.value not in used["ids"] and token.value not in words:
            return False
        previous = token
    return True


def purge_rules(rules, used, keyframes):
    kept = []
    for rule in rules:
        if rule.type == "qualified-rule":
            selectors = [s for s in split(rule.prelude, ",") if selector_used(s, used)]
            if not selectors:
                continue
            rule.prelude = join(selectors, ",")
        elif rule.type == "at-rule" and rule.content is not None:
            name = rule.lower_at_keyword
            if name in GROUPING_RULES:
                rule.content = purge_rules(
                    tinycss2.parse_rule_list(rule.content, skip_comments=True, skip_whitespace=True),
                    used, keyframes)
                if not rule.content:
                    continue
            elif name in KEYFRAMES:
                keyframes.append(rule)
        kept.append(rule)
    return kept


def variable(declaration):
    """Nom de la variable CSS déclarée, ou None pour une propriété ordinaire."""
    for token in declaration:
        if token.type != "whitespace":
            return token.value if token.type == "ident" and token.value.startswith("--") else None
    return None


def drop_variables(rules, read):
    """Retire les déclarations de variables CSS absentes de `read`."""
    kept, changed = [], False
    for rule in rules:
        if rule.type == "qualified-rule":
            declarations = split(rule.content, ";")
            useful = [d for d in declarations if variable(d) is None or variable(d) in read]
            if len(useful) < len(declarations):
                changed = True
                if all(t.type == "whitespace" for d in useful for t in d):
                    continue
                rule.content = join(useful, ";")
        elif rule.type == "at-rule" and rule.lower_at_keyword in GROUPING_RULES and rule.content is not None:
            rule.content, inner = drop_variables(rule.content, read)
            changed |= inner
            if not rule.content:
                continue
        kept.append(rule)
    return kept, changed


def purge(css, used):
    keyframes = []
    rules = purge_rules(
        tinycss2.parse_stylesheet(css, skip_comments=True, skip_whitespace=True), used, keyframes)
    # Animations encore nommées par les règles conservées, y compris via une variable
    named = set(WORD.findall(tinycss2.serialize(r for r in rules if r not in keyframes)))
    rules = [r for r in rules
             if r not in keyframes or tinycss2.parse_one_component_value(r.prelude).value in named]
    # Retirer une variable peut rendre inutiles celles qu'elle lisait : jusqu'à stabilité
    changed = True
    while changed:
        read = set(VAR.findall(tinycss2.serialize(rules))) | used["words"]
        rules, changed = drop_variables(rules, read)
    # tinycss2 réécrit les chaînes à partir de leur valeur : "\e5cc" deviendrait un caractère
    # brut, que subset-icons.py ne relève pas. Les échappements sont rétablis.
    return NON_ASCII.sub(lambda m: f"\\{ord(m.group(0)):x}" + (" " if m.group(1) else ""),
                         tinycss2.serialize(rules))


def integrity(algorithm, data):
    return f"{algorithm}-{base64.b64encode(hashlib.new(algorithm, data).digest()).decode()}"


def main(root):
    used = collect(root)
    renamed = {}
    for path in list(site_files(root, ".css")):
        with open(path, "rb") as f:
            before = f.read()
        after = purge(before.decode("utf-8"), used).encode("utf-8")

        new_path = path
        match = re.fullmatch(r"(.*\.)([0-9a-f]+)(\.css)", path)
        algorithm = match and DIGESTS.get(len(match.group(2)))
        if algorithm:
            new_path = match.group(1) + hashlib.new(algorithm, after).hexdigest() + match.group(3)
            renamed[os.path.basename(path)] = os.path.basename(new_path)
            renamed[integrity(algorithm, before)] = integrity(algorithm, after)
            os.remove(path)
        with open(new_path, "wb") as f:
            f.write(after)
        print(f"{os.path.relpath(new_path, root)} : {len(before) / 1024:.1f} Ko -> {len(after) / 1024:.1f} Ko")

    if renamed:
        pattern = re.compile("|".join(re.escape(old) for old in renamed))
        for path in site_files(root, ".html"):
            with open(path, encoding="utf-8") as f:
                html = f.read()
            updated = pattern.sub(lambda m: renamed[m.group(0)], html)
            if updated != html:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(updated)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
