"""Écrit dans les pages le poids transféré de la recherche, annoncé avant son téléchargement.

Usage : python3 scripts/search-weight.py public

À lancer après `hugo build`. À l'ouverture de la recherche, chaque page annonce le poids de
l'index et de la bibliothèque FlexSearch, téléchargés à la première saisie (critère RGESN 4.12).
Hugo ne connaît que leur poids non compressé : le script remplace l'attribut data-search-weight
par leur poids une fois compressés en gzip, comme les sert GitHub Pages.
"""
import gzip
import os
import re
import sys

# Niveau de compression de GitHub Pages (mêmes tailles à l'octet près, voir check-budget.py)
GZIP_LEVEL = 5
FILES = {"index": re.compile(r"search-index\.[0-9a-f]+\.json$"),
         "bibliothèque": re.compile(r"flexsearch\.bundle\.min\.[0-9a-f]+\.js$")}
ATTRIBUTE = re.compile(r'data-search-weight="?\d+"?')


def site_files(root, ext):
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.endswith(ext):
                yield os.path.join(dirpath, name)


def main(root):
    raw = weight = 0
    for label, pattern in FILES.items():
        paths = [p for p in site_files(root, "") if pattern.search(os.path.basename(p))]
        if len(paths) != 1:
            sys.exit(f"Recherche : {len(paths)} fichier(s) de {label} trouvé(s) au lieu d'un")
        with open(paths[0], "rb") as f:
            data = f.read()
        raw += len(data)
        weight += len(gzip.compress(data, GZIP_LEVEL))

    pages = 0
    for path in site_files(root, ".html"):
        with open(path, encoding="utf-8") as f:
            html = f.read()
        updated = ATTRIBUTE.sub(f'data-search-weight="{weight}"', html)
        if updated != html:
            pages += 1
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated)
    print(f"Recherche : {raw / 1024:.0f} Ko -> {weight / 1024:.0f} Ko transférés, annoncés dans {pages} pages")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
