"""Évalue l'empreinte environnementale d'une lecture de fiche et d'une publication du site.

Usage : python3 scripts/estimate-footprint.py public

Méthode de la page « Empreinte environnementale » (À propos, critère RGESN 1.5), à relancer
chaque année en octobre après `hugo build`, puis à reporter dans cette page, dans la déclaration
d'écoconception, et dans hugo.toml pour l'empreinte affichée sous le titre des fiches. Le script interroge l'API de Boavizta et celle de GitHub : la
construction du site ne le lance pas.

Unité fonctionnelle : lire une fiche RGESN en entier, en France, sur un ordinateur portable
relié à une box ou sur un smartphone en 4G. La part de chaque équipement est attribuée au
temps d'utilisation pour les terminaux et au volume de données pour le réseau, selon les
règles par défaut du référentiel méthodologique de l'ADEME pour les services numériques.
"""
import datetime
import glob
import json
import os
import re
import statistics
import sys
import urllib.request

BOAVIZTA = "https://api.boavizta.org/v1"
GITHUB = "https://api.github.com/repos/nicolasbordier/sudo-less/actions"

# Terminaux : fabrication tirée de la Base IMPACTS de l'ADEME par l'API Boavizta, durée de vie
# (ans) et consommation (kWh/an) de l'étude ADEME-Arcep de 2022. Réseau : consommation par Go
# de la même étude, fixe hors box, mobile.
TERMINALS = {"Ordinateur portable": ("laptop", 5, 29.1, 0.0342),
             "Smartphone": ("smartphone", 2.5, 3.9, 0.237)}
# Part du temps où un terminal est utilisé : valeur par défaut de Boavizta, 7,2 h par jour
USE_RATIO = 0.3
# Électricité en France, kg CO2e/kWh : Base Empreinte de l'ADEME, 2025, mix moyen consommé,
# amont compris. Remplace la valeur de 2021 de l'API (0,098) ; à mettre à jour chaque année.
FRANCE_GWP = 0.0461
# Eau consommée par le refroidissement des centrales (SDES : 12 % de 4,1 milliards de m3
# par an) rapportée à la production d'électricité française (RTE : 542 TWh par an, 2010-2018)
WATER_L_PER_KWH = 0.12 * 4.1e9 * 1000 / 542e9
# Poids transféré : le budget par page, plutôt que la mesure, pour rester un plafond
PAGE_GO = 100 * 1024 / 1e9
# Hébergement, borne haute : un serveur Boavizta par défaut occupé à envoyer la page à 1 Gbit/s
SERVER = {"usage": {"usage_location": "USA", "time_workload": 100}}
SERVER_GBITS = 1
# Construction : runner GitHub pour dépôt public (4 vCPU, 16 Go), chargé à moitié
RUNNER = {"provider": "azure", "instance_type": "d4ads_v5",
          "usage": {"usage_location": "USA", "time_workload": 50}}
# Audience : hypothèse, faute de mesure (critère 1.6)
READINGS_PER_YEAR = 10_000
READING_TIME = re.compile(r"Temps de lecture : environ (\d+) minute")
# Indicateur, nom, puis échelle et unité par lecture et par an (l'API répond en kg, MJ, kg Sb, L)
INDICATORS = [("gwp", "Émissions de GES", (1e3, "g CO2e"), (1, "kg CO2e")),
              ("pe", "Énergie primaire", (1e3, "kJ"), (1, "MJ")),
              ("adpe", "Ressources abiotiques (minéraux, métaux)", (1e9, "µg Sb éq."), (1e6, "mg Sb éq.")),
              ("water", "Eau bleue (électricité seule)", (1e3, "mL"), (1, "L"))]


def get(url):
    return json.load(urllib.request.urlopen(url))


def boavizta(path, hours, body):
    """Impacts d'un équipement sur `hours` heures, par phase. À défaut d'énergie primaire
    (non calculée pour la fabrication des terminaux), retient les ressources fossiles (adpf)."""
    query = "&".join(f"criteria={c}" for c in ("gwp", "pe", "adpe", "adpf"))
    request = urllib.request.Request(f"{BOAVIZTA}/{path}?verbose=true&duration={hours}&{query}",
                                     data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
    result = json.load(urllib.request.urlopen(request))
    impacts = {}
    for phase in ("embedded", "use"):
        values = {k: v[phase]["value"] if isinstance(v[phase], dict) else None
                  for k, v in result["impacts"].items()}
        impacts[phase] = {"gwp": values["gwp"], "pe": values["pe"] if values["pe"] is not None
                          else values["adpf"], "adpe": values["adpe"]}
    return impacts, {k: result["verbose"][k + "_factor"]["value"] for k in ("gwp", "pe", "adpe")}


def reading(device, life_years, kwh_per_year, kwh_per_go, minutes):
    active_hours = 8760 * USE_RATIO
    impacts, factors = boavizta(f"terminal/{device}", minutes / 60, {"usage": {
        "usage_location": "FRA", "elec_factors": {"gwp": FRANCE_GWP},
        "hours_life_time": life_years * active_hours,
        "use_time_ratio": 1, "avg_power": kwh_per_year * 1000 / active_hours}})
    use_kwh = kwh_per_year / active_hours * minutes / 60
    net_kwh = kwh_per_go * PAGE_GO
    impacts["embedded"]["water"] = 0
    impacts["use"]["water"] = use_kwh * WATER_L_PER_KWH
    impacts["network"] = {k: net_kwh * f for k, f in factors.items()}
    impacts["network"]["water"] = net_kwh * WATER_L_PER_KWH
    return impacts


def total(impacts, key):
    return sum(phase.get(key) or 0 for phase in impacts.values())


def publications():
    since = datetime.date.today() - datetime.timedelta(days=365)
    runs, page = [], 1
    while True:
        batch = get(f"{GITHUB}/runs?per_page=100&page={page}&created=%3E%3D{since}")["workflow_runs"]
        runs += batch
        if len(batch) < 100:
            break
        page += 1
    seconds = sum((datetime.datetime.fromisoformat(r["updated_at"])
                   - datetime.datetime.fromisoformat(r["run_started_at"])).total_seconds() for r in runs)
    latest = next(r for r in runs if r["conclusion"] == "success")
    jobs = get(f"{GITHUB}/runs/{latest['id']}/jobs")["jobs"]
    last = sum((datetime.datetime.fromisoformat(j["completed_at"])
                - datetime.datetime.fromisoformat(j["started_at"])).total_seconds() for j in jobs)
    return len(runs), seconds, last, latest["created_at"][:10]


def header():
    print("| | " + " | ".join(name for _, name, _, _ in INDICATORS) + " |")
    print("|---|" + "---:|" * len(INDICATORS))


def show(label, impacts, count=1, per_year=False):
    cells = []
    for key, _, per_reading, yearly in INDICATORS:
        scale, unit = yearly if per_year else per_reading
        value = total(impacts, key) * count * scale
        cells.append(f"{value:.3g} {unit}" if key != "water" or value else "non évaluée")
    print(f"| {label} | " + " | ".join(cells) + " |")


def main(root):
    times = [int(m.group(1)) for path in glob.glob(os.path.join(root, "docs/rgesn/*/*/index.html"))
             if (m := READING_TIME.search(open(path, encoding="utf-8").read()))]
    if not times:
        sys.exit(f"Aucun temps de lecture trouvé dans {root} : lancer `hugo build` d'abord")
    minutes = statistics.mean(times)
    print(f"API Boavizta {get(BOAVIZTA + '/utils/version')}, le {datetime.date.today():%d/%m/%Y}")
    print(f"Lecture : {minutes:.1f} min en moyenne sur {len(times)} fiches (maximum {max(times)}), "
          f"{PAGE_GO * 1e9 / 1024:.0f} Ko ; eau de l'électricité : {WATER_L_PER_KWH:.2f} L/kWh\n")
    header()
    readings, shares = {}, []
    for label, terminal in TERMINALS.items():
        impacts = readings[label] = reading(*terminal, minutes)
        show(f"Lecture, {label.lower()}", impacts)
        gwp = total(impacts, "gwp")
        shares.append(f"{label} : fabrication {impacts['embedded']['gwp'] / gwp:.1%}, "
                      f"usage {impacts['use']['gwp'] / gwp:.1%}, réseau {impacts['network']['gwp'] / gwp:.2%}")
    server, _ = boavizta("server/", PAGE_GO * 8 / SERVER_GBITS / 3600, SERVER)
    show("Hébergement, borne haute", server)
    count, seconds, last, date = publications()
    show(f"Publication du {date} ({last:.0f} s)", boavizta("cloud/instance", last / 3600, RUNNER)[0])
    print("\nRépartition des GES d'une lecture :\n" + "\n".join(shares))
    per_minute = statistics.mean(total(i, "gwp") for i in readings.values()) / minutes * 1e3
    print(f"Sous le titre des fiches (params.footprint.gco2ePerMinute) : {per_minute:.2f} g CO2e par minute")

    print(f"\nPar an, hypothèse de {READINGS_PER_YEAR} lectures :\n")
    header()
    for label, impacts in readings.items():
        show(f"{READINGS_PER_YEAR} lectures, {label.lower()}", impacts, READINGS_PER_YEAR, per_year=True)
    show(f"{count} publications en 12 mois ({seconds / 60:.0f} min)",
         boavizta("cloud/instance", seconds / 3600, RUNNER)[0], per_year=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
