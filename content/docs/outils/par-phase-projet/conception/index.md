---
weight: 200
title: "Conception"
description: "Tableau récapitulatif des outils spécifiques à la phase de conception : minimisation des données, dimensionnement du chiffrement, choix de technologies standard et ouverture des API matérielles."
icon: "design_services"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-23T00:00:00+01:00"
draft: false
toc: true
---

La phase de **conception** est celle où se prennent les choix techniques structurants qui ne relèvent plus d'une décision « poursuivre ou arrêter » ([phase d'exploration](../exploration/)), mais qui restent réversibles avant l'écriture du code : quelles données collecter ([critère 1.6](../../../rgesn/strategie/1-6_collecte-donnees/)), quel niveau de chiffrement ([critère 1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/)), quelles technologies standard ([critère 1.9](../../../rgesn/strategie/1-9_technologies-standard/)) et quelles API matérielles ouvrir ([critère 1.10](../../../rgesn/strategie/1-10_api-materiel/)), mais aussi quels fournisseurs, composants et services tiers retenir ([critères 2.8](../../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) à [2.10](../../../rgesn/specifications/2-10_services-tiers/)), quelle architecture (famille [Architecture](../../../rgesn/architecture/)) et quels motifs d'interface (famille [UX/UI](../../../rgesn/ux-ui/)). Voir aussi les pages [Architecte](../../par-metier/architecte/) et [Dev Back](../../par-metier/dev-back/) pour une vue par métier.

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de contenu, un écosystème ou un fournisseur particulier), sont payants, ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil / Référentiel | Critère RGESN | Rôle typique | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|---|
| [Baseline](https://web.dev/baseline) / Can I Use / MDN | 1.9 | Dev Front | Vérifie qu'une API web est standard et largement supportée avant de l'adopter | Oui |
| [Guide pratique pour des achats numériques responsables](https://ecoresponsable.numerique.gouv.fr/publications/guide-pratique-achats-numeriques-responsables/) (Direction des Achats de l'État, INR, DINUM…) | 2.8 | Responsable RSE / Partenariats | Fiches par segment d'achat avec exemples de clauses et questionnaires réutilisables en appel d'offres | Oui |
| [Request Map Generator](https://requestmap.webperf.tools/) | 2.10 | Architecte / Dev Front | Carte de toutes les requêtes d'une page, qui distingue les domaines tiers et les requêtes qu'ils déclenchent en cascade, pour statuer sur chaque service tiers | Oui |
| Alternatives légères aux services tiers : [Plausible](https://plausible.io/), [Umami](https://umami.is/), [Matomo](https://matomo.org/), [lite-youtube-embed](https://github.com/paulirish/lite-youtube-embed), [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) / [hCaptcha](https://www.hcaptcha.com/) | 2.10, 4.4 | Dev Front | Remplacent un service tiers lourd (mesure d'audience, lecteur vidéo, captcha) par un équivalent plus léger : par exemple une vignette cliquable d'une centaine de Ko au lieu d'un lecteur YouTube d'environ 1,3 Mo | Oui (offres hébergées payantes pour Matomo et Plausible) |
| [Matrice de captologie](https://docs.google.com/spreadsheets/d/1dj_KIKzyPlSND1-fSYNb0BgupCmh2XoYTPkFTKPiaq0/edit?gid=1991215211#gid=1991215211) (Designers Éthiques) | 4.1, 4.2, 4.13, 4.14 | UX Designer | Évalue par des questions oui/non la captation de l'attention d'un service (lecture automatique, défilement infini, notifications, dark patterns…), avec un score de A à G | Oui (CC-BY) |

## Outils complémentaires

| Outil / Référentiel | Critère RGESN | Rôle typique | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|---|
| [RWEB 0023](https://rweb.greenit.fr/fr/fiches/RWEB_0023-reduire-le-volume-de-donnees-stockees-au-strict-necessaire) (Collectif GreenIT) | 1.6 | Dev Back | Ne stocker que les données strictement nécessaires, avec archivage à froid et suppression des doublons | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=backend&num_reco=1) — Backend n°1 | 1.6 | Architecte | Vérifie l'utilité réelle des données collectées et leur cycle de vie (dates de suppression, données obsolètes) | Oui |
| [Cahier IP n°9](https://linc.cnil.fr/cahier-ip9-donnees-empreinte-et-libertes) (CNIL) | 1.6 | Responsable RSE | Documente les tensions entre obligations de chiffrement/protection des données et sobriété numérique | Oui |
| [Guide ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) | 1.7 | Architecte | Dimensionne un chiffrement adapté au besoin réel (taille de clé, durée de protection) plutôt que systématiquement maximal | Oui |
| [7-Zip](https://www.7-zip.org/) / [Zed!](https://www.primx.eu/en/encryption-software/zed-en/) / [PeaZip](https://peazip.github.io/) / [VeraCrypt](https://veracrypt.io/) | 1.7 | Architecte | Compressent et chiffrent ensemble dans une même archive plutôt que de conserver des fichiers chiffrés isolés | Oui (Zed! gratuit jusqu'à 200 Mo par fichier) |
| [Socle interministériel des logiciels libres (SILL)](https://code.gouv.fr/sill/) | 1.8 | Architecte / Responsable RSE | Logiciels libres recommandés pour l'administration, à privilégier lors du choix de composants tiers | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=frontend&num_reco=4) — Frontend n°4 | 1.9 | Architecte | Définit la plage de rétro-compatibilité visée et la disponibilité d'une version allégée pour anciens équipements | Oui |
| [PWABuilder](https://www.pwabuilder.com/) / [Bubblewrap](https://github.com/GoogleChromeLabs/bubblewrap) | 1.9 | Dev Mobile | Empaquette une Progressive Web App en application installable depuis les magasins, sans renoncer à une base de code web unique | Oui |
| [Règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act) | 1.10 | Architecte / Juridique | Impose depuis 2025 des API ouvertes et documentées pour les données générées par un objet connecté | Oui (référentiel) |
| [Tasmota](https://tasmota.github.io/docs/) / Home Assistant | 1.10 | Dev Back | Reprend la main sur un objet connecté dont l'API reste fermée, via un firmware libre | Oui |
| [EcoVadis](https://ecovadis.com/) / écolabels ([EPEAT](https://www.epeat.net/), [TCO Certified](https://tcocertified.com/), [Blue Angel](https://www.blauer-engel.de/en)…) | 2.8 | Responsable RSE / Partenariats | Comparent les fournisseurs candidats (notation RSE d'EcoVadis, payante) ou fournissent un critère de sélection vérifié par un tiers (écolabels) | Selon l'outil (EcoVadis payant) |
| [Bundlephobia](https://bundlephobia.com/) / [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) (npm), [python-package-size](https://pypi.org/project/python-package-size/) (Python), [Dependency Analysis Gradle Plugin](https://github.com/autonomousapps/dependency-analysis-gradle-plugin) (Java) | 2.9 | Dev Front / Dev Back | Mesurent le poids d'une bibliothèque ou de ses dépendances avant de l'adopter, ou repèrent les dépendances inutilisées | Oui |
| [Système de design de l'État (DSFR)](https://www.systeme-de-design.gouv.fr/) / [GOV.UK Design System](https://design-system.service.gov.uk/) | 2.9, 4.10, 4.11 | UX Designer | Composants et règles prêts à l'emploi (poids et format des fichiers à télécharger, validation des formulaires) ; le DSFR est réservé à l'administration française | Oui |
| [TechEmpower Framework Benchmarks](https://github.com/TechEmpower/FrameworkBenchmarks) | 3.1 | Architecte / Dev Back | Compare des frameworks d'API d'un même écosystème (projet archivé en mars 2026, résultats non mis à jour) | Oui |
| [endoflife.date](https://endoflife.date/) | 3.5 | Architecte | Dates de fin de support des systèmes, langages et logiciels, pour choisir des composants dont le support couvre la durée de vie du service | Oui |
| [Semantic Versioning](https://semver.org/lang/fr/) / [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) | 3.5 | Architecte | Conventions de numérotation et de journal des modifications qui distinguent mises à jour correctives et évolutives | Oui |
| [Hugo](https://gohugo.io/), [Eleventy](https://www.11ty.dev/), [Astro](https://astro.build/) | 4.5 | Dev Front / Architecte | Générateurs de sites statiques : des pages produites au build plutôt qu'à chaque visite | Oui |
| [Impact CO2](https://impactco2.fr/outils/usagenumerique) (ADEME) | 4.12 | UX Designer / Responsable RSE | Équivalences d'impact des usages numériques sourcées par la Base Empreinte de l'ADEME, limitées aux émissions de CO2e | Oui |

---

Contrairement à la phase d'exploration où les outils sont surtout des grilles de questionnement, cette phase mobilise des **référentiels techniques précis** (ANSSI, GR491, Data Act) qui engagent des choix coûteux à revenir en arrière une fois le développement lancé — dimensionnement cryptographique, schéma de données, choix web vs natif. C'est pourquoi le critère 1.9 recommande d'évaluer ces choix « bien en amont du développement », et non au moment de le livrer. Il en va de même pour les services tiers, les dépendances et les fournisseurs : un composant intégré ou un contrat signé se remplace bien plus difficilement qu'il ne se choisit.
