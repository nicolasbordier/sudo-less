---
weight: 200
title: "Dev Back"
description: "Tableau récapitulatif des outils gratuits et payants pour mesurer et piloter l'écoconception d'une application côté backend, API et infrastructure."
icon: "dns"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-23T00:00:00+01:00"
draft: false
toc: true
---

Cette page récapitule les outils déjà présentés dans les fiches RGESN, spécifiques au développement backend, aux API et aux traitements batch : mesure de consommation par processus, mesure en CI/CD, estimation de l'empreinte matérielle, poids des dépendances et allègement de ce que le serveur envoie (voir notamment le [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/)).

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de contenu, un écosystème ou un fournisseur particulier), sont payants, ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [Scaphandre](https://github.com/hubblo-org/scaphandre) | Agent de métrologie open source | Puissance consommée en temps réel, par machine hôte et par **processus**, exportable vers Prometheus/Grafana | Oui | Oui (bare metal, VM, Kubernetes) |
| [GreenFrame](https://greenframe.io/) | CLI open source | Consommation (CPU, mémoire, réseau) d'un scénario API rejoué dans une stack Dockerisée complète (API + base de données) | Oui (CLI) | Oui — bloque une PR en cas de dépassement d'un seuil d'émissions |
| [Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur) (Boavizta) | API ouverte | Empreinte fabrication **et** usage (GWP, énergie primaire, ressources abiotiques) d'un serveur ou d'une instance cloud, à partir de son type | Oui | Oui (interrogeable par code) |

## Outils complémentaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [PowerAPI](https://powerapi.org/) | Framework Python open source | Estimation de la consommation électrique par modèle (sans capteur matériel requis), à différents niveaux (VM, conteneur, application, processus, code) — maintenu par Inria/Université de Lille | Oui | Oui |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) | Outil open source (Thoughtworks) | Estimation d'émissions à partir des données de facturation, vue unifiée **multi-cloud** (AWS, Azure, GCP) avec recommandations d'optimisation | Oui | Oui |
| [CodeCarbon](https://github.com/mlco2/codecarbon) (Data For Good) | Package Python open source | Estime la consommation CPU, GPU et RAM d'une fonction, marquée d'un simple décorateur `@track_emissions`, et la convertit en kg de CO2e selon l'intensité carbone du réseau électrique local — adapté aux algorithmes d'apprentissage, rarement mesurés en pratique. Limité au code Python. Utile pour le critère [3.1](../../../rgesn/architecture/3-1_architecture-composants/) | Oui | Oui |
| [TechEmpower Framework Benchmarks](https://github.com/TechEmpower/FrameworkBenchmarks) | Benchmark open source | Compare des frameworks d'API d'un même écosystème (texte brut, sérialisation JSON, requêtes en base de données). Projet archivé en mars 2026 : ses derniers résultats donnent un ordre de grandeur mais ne sont plus mis à jour. Utile pour le critère [3.1](../../../rgesn/architecture/3-1_architecture-composants/) | Oui | Non (consultation) |
| [python-package-size](https://pypi.org/project/python-package-size/) / [Dependency Analysis Gradle Plugin](https://github.com/autonomousapps/dependency-analysis-gradle-plugin) | Outils en ligne de commande | python-package-size mesure le poids sur disque d'une dépendance Python avec ses dépendances transitives ; le plugin Gradle détecte les dépendances inutilisées ou mal déclarées et repère les plus lourdes. Équivalents de Bundlephobia hors de l'écosystème npm. Utiles pour le critère [2.9](../../../rgesn/specifications/2-9_composants-interface/) | Oui (open source) | Oui |
| Compression des réponses : [ngx_brotli](https://github.com/google/ngx_brotli) (Nginx), [`mod_brotli`](https://httpd.apache.org/docs/2.4/mod/mod_brotli.html) (Apache), directive [`encode`](https://caddyserver.com/docs/caddyfile/directives/encode) (Caddy), `gzip` et `brotli` en ligne de commande | Modules serveur / outils de précompression | Compressent les ressources texte (HTML, CSS, JavaScript, SVG) à la volée, ou une seule fois au déploiement pour les fichiers statiques (`gzip -k -9`, `brotli -k -q 11`). Nginx ne propose nativement que gzip : Brotli passe par le module ngx_brotli. Utile pour le critère [6.3](../../../rgesn/frontend/6-3_compression-ressources/) | Oui (open source) | Oui (configuration serveur, étape de déploiement) |
| [ImageMagick](https://imagemagick.org/) | Outil en ligne de commande | Redimensionne une seule fois, à l'enregistrement, les images envoyées trop grandes (`magick envoi.jpg -auto-orient -resize '1920x1920>'`) : le suffixe `>` ne réduit que celles qui dépassent la limite. Utile pour le critère [6.4](../../../rgesn/frontend/6-4_dimensions-images/) | Oui (open source) | Oui |
| [qpdf](https://qpdf.readthedocs.io/), [LibreOffice](https://www.libreoffice.org/) (export en ligne de commande), `pdfinfo` / `pdfimages` ([Poppler](https://poppler.freedesktop.org/)) | Outils en ligne de commande | LibreOffice exporte un PDF balisé, donc accessible, avec une compression des images réglée à la source ; qpdf l'optimise et le linéarise ensuite sans perte ; `pdfinfo` et `pdfimages` contrôlent le balisage, la linéarisation et la résolution des images. À l'inverse, Ghostscript supprime le balisage. Utiles pour le critère [5.7](../../../rgesn/contenus/5-7_format-documents/) | Oui (logiciels libres) | Oui |

---

**Scaphandre** et **PowerAPI** répondent au même besoin (mesure de la consommation par processus) avec des approches différentes : Scaphandre s'appuie sur les compteurs RAPL du processeur, quand PowerAPI privilégie une approche par modèle, plus portable mais moins directement liée au matériel réel. **GreenFrame** se distingue en mesurant un scénario applicatif complet (API + dépendances) plutôt qu'un processus isolé — pertinent en CI, avant mise en production. **Boaviztapi** et **Cloud Carbon Footprint** interviennent à un niveau différent : le choix et le dimensionnement de l'infrastructure plutôt que le code applicatif lui-même — voir aussi le détail de ces outils au [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/). Les outils de compression, d'images et de documents ne mesurent rien : ils réduisent directement le volume de ce que le serveur envoie.
