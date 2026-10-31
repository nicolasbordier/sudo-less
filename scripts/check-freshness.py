"""Signale les pages dont la dernière mise à jour date de plus de 12 mois.

Usage : python3 scripts/check-freshness.py content

Applique la durée de vie des contenus décrite dans la page « Contribuer » : une page qui n'a
pas été mise à jour depuis 12 mois doit être relue, puis mise à jour, fusionnée ou retirée.
Le script lit la date `lastmod` (à défaut `date`) de chaque page publiée et affiche un
avertissement par page à relire, sans faire échouer le build.
"""
import datetime
import os
import re
import sys

MAX_AGE = datetime.timedelta(days=365)
GUIDE = "voir « Durée de vie des contenus » dans la page Contribuer"


def front_matter(path):
    with open(path, encoding="utf-8") as f:
        match = re.match(r"---\n(.*?)\n---(\n|$)", f.read(), re.S)
    return match.group(1) if match else ""


def field(meta, name):
    match = re.search(rf'^{name}:\s*"?([^"\n]+)"?\s*$', meta, re.M)
    return match.group(1) if match else None


def warn(path, message):
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"::warning file={path}::{message}")
    else:
        print(f"Attention : {path} : {message}")


def main(root):
    today = datetime.date.today()
    pages = []
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.endswith(".md"):
                path = os.path.join(dirpath, name)
                meta = front_matter(path)
                updated = field(meta, "lastmod") or field(meta, "date")
                if updated and field(meta, "draft") != "true":
                    pages.append((datetime.date.fromisoformat(updated[:10]), path))

    pages.sort()
    late = [(updated, path) for updated, path in pages if today - updated > MAX_AGE]
    for updated, path in late:
        warn(path, f"dernière mise à jour le {updated:%d/%m/%Y}, il y a plus de 12 mois : page à relire ({GUIDE})")
    if late:
        print(f"{len(late)} page(s) à relire sur {len(pages)}")
    elif pages:
        updated, path = pages[0]
        print(f"Aucune page à relire sur {len(pages)} ; prochaine échéance le "
              f"{updated + MAX_AGE:%d/%m/%Y} ({path})")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "content")
