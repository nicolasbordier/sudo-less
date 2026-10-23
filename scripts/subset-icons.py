"""Réduit la police d'icônes Material Symbols aux seules icônes utilisées par le site.

Usage : python3 scripts/subset-icons.py public

À lancer après `hugo build`. Le script relève dans le site généré :
- les icônes appelées par ligature dans le HTML (<i class="material-icons">eco</i>) ;
- les icônes appelées par point de code dans le CSS (content:"\\e5cc").
Il remplace ensuite public/docs/fonts/material-symbols-outlined.woff2 par un
sous-ensemble ne contenant que ces glyphes. Une icône absente de la police est
signalée par un avertissement, sans faire échouer le build.

Dépendances : fonttools et brotli (pip install fonttools brotli).
"""
import io
import os
import re
import sys
from html.parser import HTMLParser

from fontTools import subset
from fontTools.ttLib import TTFont

FONT = "docs/fonts/material-symbols-outlined.woff2"
ICON_CLASSES = {"material-icons", "material-symbols-outlined"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class IconCollector(HTMLParser):
    """Relève le texte des éléments portant une classe d'icône."""

    def __init__(self):
        super().__init__()
        self.icons = []
        self.depth = 0
        self.text = ""

    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        if self.depth:
            self.depth += 1
        elif ICON_CLASSES & set((dict(attrs).get("class") or "").split()):
            self.depth, self.text = 1, ""

    def handle_endtag(self, tag):
        if self.depth and tag not in VOID_TAGS:
            self.depth -= 1
            if not self.depth and self.text.strip():
                self.icons.append(self.text.strip())

    def handle_data(self, data):
        if self.depth:
            self.text += data


def site_files(root, ext):
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.endswith(ext):
                yield os.path.join(dirpath, name)


def ligatures(font):
    """Associe chaque suite de glyphes à son glyphe de ligature."""
    table = {}
    for lookup in font["GSUB"].table.LookupList.Lookup:
        for st in lookup.SubTable:
            lookup_type = lookup.LookupType
            if lookup_type == 7:
                lookup_type, st = st.ExtensionLookupType, st.ExtSubTable
            if lookup_type == 4:
                for first, ligs in st.ligatures.items():
                    for lig in ligs:
                        table[(first, *lig.Component)] = lig.LigGlyph
    return table


def warn(message):
    prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") else "Attention : "
    print(prefix + message)


def main(root):
    font_path = os.path.join(root, FONT)
    font = TTFont(font_path)
    cmap = font.getBestCmap()

    # Icônes appelées par ligature, avec les pages qui les utilisent
    used = {}
    for path in site_files(root, ".html"):
        parser = IconCollector()
        with open(path, encoding="utf-8") as f:
            parser.feed(f.read())
        for name in parser.icons:
            used.setdefault(name, set()).add(os.path.relpath(path, root))

    # Icônes appelées par point de code (zones à usage privé de la police)
    codepoints = set()
    for path in site_files(root, ".css"):
        with open(path, encoding="utf-8") as f:
            for hexa in re.findall(r"\\([0-9a-fA-F]{4,6})", f.read()):
                cp = int(hexa, 16)
                if cp in cmap and (0xE000 <= cp <= 0xF8FF or cp >= 0xF0000):
                    codepoints.add(cp)

    table = ligatures(font)
    glyphs, chars = set(), set()
    for name, pages in sorted(used.items()):
        lig = table.get(tuple(cmap.get(ord(c)) for c in name))
        if lig:
            glyphs.add(lig)
            chars.update(name)
        else:
            warn(f"l'icône « {name} » n'existe pas dans Material Symbols ({', '.join(sorted(pages)[:3])})")

    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["liga", "rlig", "calt", "ccmp"]
    # Sans cela, toutes les ligatures composées des lettres conservées seraient gardées
    options.layout_closure = False
    options.name_IDs = ["*"]
    options.notdef_outline = True
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=sorted({ord(c) for c in chars} | codepoints), glyphs=sorted(glyphs))
    subsetter.subset(font)

    before = os.path.getsize(font_path)
    buffer = io.BytesIO()
    font.save(buffer)
    with open(font_path, "wb") as f:
        f.write(buffer.getvalue())
    print(f"{FONT} : {len(glyphs)} ligatures et {len(codepoints)} points de code conservés, "
          f"{before / 1024:.1f} Ko -> {os.path.getsize(font_path) / 1024:.1f} Ko")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
