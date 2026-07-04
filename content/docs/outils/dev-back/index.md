---
weight: 200
title: "Dev Back"
description: "Tableau récapitulatif des outils gratuits et payants pour mesurer et piloter l'écoconception d'une application côté backend, API et infrastructure."
icon: "dns"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Ce tableau récapitule les outils déjà présentés dans les fiches RGESN, spécifiques au développement backend, aux API et aux traitements batch : mesure de consommation par processus, mesure en CI/CD et estimation de l'empreinte matérielle (voir notamment le [critère 1.4](../../rgesn/strategie/1-4_revue-ecoconception/)).

| Outil | Catégorie | Ce qu'il mesure | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [Scaphandre](https://github.com/hubblo-org/scaphandre) | Agent de métrologie open source | Puissance consommée en temps réel, par machine hôte et par **processus**, exportable vers Prometheus/Grafana | Oui | Oui (bare metal, VM, Kubernetes) |
| [PowerAPI](https://powerapi.org/) | Framework Python open source | Estimation de la consommation électrique par modèle (sans capteur matériel requis), à différents niveaux (VM, conteneur, application, processus, code) — maintenu par Inria/Université de Lille | Oui | Oui |
| [GreenFrame](https://greenframe.io/) | CLI open source | Consommation (CPU, mémoire, réseau) d'un scénario API rejoué dans une stack Dockerisée complète (API + base de données) | Oui (CLI) | Oui — bloque une PR en cas de dépassement d'un seuil d'émissions |
| [Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur) (Boavizta) | API ouverte | Empreinte fabrication **et** usage (GWP, énergie primaire, ressources abiotiques) d'un serveur ou d'une instance cloud, à partir de son type | Oui | Oui (interrogeable par code) |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) | Outil open source (Thoughtworks) | Estimation d'émissions à partir des données de facturation, vue unifiée **multi-cloud** (AWS, Azure, GCP) avec recommandations d'optimisation | Oui | Oui |

---

**Scaphandre** et **PowerAPI** répondent au même besoin (mesure de la consommation par processus) avec des approches différentes : Scaphandre s'appuie sur les compteurs RAPL du processeur, quand PowerAPI privilégie une approche par modèle, plus portable mais moins directement liée au matériel réel. **GreenFrame** se distingue en mesurant un scénario applicatif complet (API + dépendances) plutôt qu'un processus isolé — pertinent en CI, avant mise en production. **Boaviztapi** et **Cloud Carbon Footprint** interviennent à un niveau différent : le choix et le dimensionnement de l'infrastructure plutôt que le code applicatif lui-même — voir aussi le détail de ces outils au [critère 1.4](../../rgesn/strategie/1-4_revue-ecoconception/).
