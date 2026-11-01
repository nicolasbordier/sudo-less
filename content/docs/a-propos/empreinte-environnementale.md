---
weight: 320
title: "Empreinte environnementale"
description: "Empreinte environnementale de sudo-less.dev : méthode, résultats par lecture et par an, hypothèses, limites, objectifs de réduction et budget par page."
icon: "eco"
date: "2026-11-01T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

Cette page détaille l'empreinte environnementale de **sudo-less.dev**, ses objectifs et son budget par page. Elle complète la [déclaration d'écoconception](../declaration-ecoconception/), pour les critères 1.5, 4.15 et 6.1.

## Méthode

Évaluée le 1er novembre 2026, pour le critère 1.5. C'est une évaluation simplifiée, pas une analyse de cycle de vie complète : elle repose sur des données génériques, et GitHub ne publie rien sur son hébergement. Elle suit les règles d'allocation par défaut du [référentiel méthodologique de l'ADEME pour les services numériques](https://codde.fr/wp-content/uploads/2023/01/Referentiel-services-numeriques_v1.0_FR.pdf) (version 1.0, 2023) : la part d'un terminal est attribuée au temps d'utilisation, celle du réseau au volume de données transférées. Les impacts de fabrication des terminaux viennent de la Base IMPACTS de l'ADEME, via l'[API de Boavizta](https://api.boavizta.org/) 2.5.0, et non des déclarations des fabricants, dont les périmètres diffèrent. Les durées de vie, les consommations et le réseau viennent de l'[étude ADEME-Arcep](https://www.arcep.fr/uploads/tx_gspublication/etude-numerique-environnement-ademe-arcep-volet02-synthese_janv2022.pdf) de 2022. Le script [`scripts/estimate-footprint.py`](https://github.com/nicolasbordier/sudo-less/blob/main/scripts/estimate-footprint.py) refait tout le calcul.

**Unité fonctionnelle : lire une fiche RGESN en entier**, en France, sur un ordinateur portable relié à une box ou sur un smartphone en 4G. Une fiche se lit en 6,7 minutes en moyenne (78 fiches, temps de lecture affiché sous leur titre). Le calcul compte 100 Ko transférés : le [budget par page](#budget-par-page).

## Par lecture d'une fiche

| Par lecture d'une fiche | Ordinateur portable | Smartphone |
|---|---:|---:|
| Émissions de gaz à effet de serre | 1,6 g CO2e | 1,4 g CO2e |
| Énergie primaire | 34 kJ | 21 kJ |
| Ressources abiotiques (minéraux et métaux) | 73 µg Sb éq. | 35 µg Sb éq. |
| Eau bleue, pour l'électricité seulement | 1,1 mL | 0,17 mL |

La fabrication du terminal fait 96 % des émissions d'une lecture sur ordinateur portable, et 99 % sur smartphone. Le reste vient presque entièrement de l'électricité du terminal : le réseau compte pour moins de 0,1 %, l'hébergement pour moins de 0,01 %. L'empreinte d'une lecture dépend donc de sa durée, pas du poids de la page. Une fiche de 10 minutes, la plus longue autorisée, émet 2,4 g CO2e sur ordinateur portable. Chaque fiche affiche l'empreinte de sa lecture sous son titre, à côté de son temps de lecture : 0,23 g CO2e par minute, la moyenne de l'ordinateur portable et du smartphone (critère 4.15).

## Projection annuelle

Le site ne mesure pas son audience (critère 1.6) : la projection prend pour hypothèse 10 000 lectures de fiche par an.

| Par an | Gaz à effet de serre | Énergie primaire | Ressources abiotiques | Eau, électricité seule |
|---|---:|---:|---:|---:|
| 10 000 lectures, toutes sur ordinateur portable | 16 kg CO2e | 344 MJ | 731 mg Sb éq. | 11 L |
| 10 000 lectures, toutes sur smartphone | 14 kg CO2e | 210 MJ | 348 mg Sb éq. | 1,7 L |
| Construction et publication du site : 113 publications en 12 mois, depuis le 3 juillet 2026 | 0,011 kg CO2e | 0,3 MJ | 0,05 mg Sb éq. | Non évaluée |

Selon la part des smartphones, le site émettrait donc de 14 à 16 kg CO2e par an, environ 6 % de l'empreinte numérique annuelle d'un habitant en France (253 kg CO2e selon l'étude ADEME-Arcep). Les publications en représentent moins de 0,1 %. Une publication sur GitHub Actions dure 244 secondes (31 octobre 2026) et émet 0,37 g CO2e, 10 kJ et 1,6 µg Sb éq. La vérification du budget par page en occupe 199 secondes.

## Hypothèses

| Élément | Hypothèse | Source |
|---|---|---|
| Ordinateur portable | 175 kg CO2e à la fabrication, 5 ans de vie, 29,1 kWh par an | Base IMPACTS de l'ADEME via l'API Boavizta, ADEME-Arcep |
| Smartphone | 84 kg CO2e à la fabrication, 2,5 ans de vie, 3,9 kWh par an | Base IMPACTS de l'ADEME via l'API Boavizta, ADEME-Arcep |
| Utilisation d'un terminal | 7,2 heures par jour. Une lecture reçoit une part de la fabrication et de la consommation au prorata de sa durée. | Boavizta (valeur par défaut), référentiel de l'ADEME |
| Électricité en France | Par kWh : 46 g CO2e, pour le mix moyen consommé en 2025, amont des combustibles et construction des centrales compris ; 11,3 MJ d'énergie primaire ; 0,9 L d'eau, soit l'eau du refroidissement des centrales (12 % des 4,1 milliards de m³ d'eau douce consommés chaque année en France) rapportée aux 542 TWh produits par an de 2010 à 2018 | Base Empreinte de l'ADEME, [reprise par Nos Gestes Climat](https://nosgestesclimat.fr/documentation/commun/mix-%C3%A9lectrique/empreinte-carbone) (GES) ; Boavizta (énergie primaire) ; [SDES](https://www.statistiques.developpement-durable.gouv.fr/leau-en-france-ressource-et-utilisation-synthese-des-connaissances-en-2021) et RTE (eau) |
| Réseau | 0,034 kWh par Go sur le réseau fixe, hors box ; 0,24 kWh par Go sur le réseau mobile | ADEME-Arcep |
| Hébergement | Borne haute : un serveur entier, occupé à envoyer la page à 1 Gbit/s | Boavizta (serveur par défaut) |
| Construction | Machine GitHub Actions de 4 processeurs et 16 Go de mémoire, chargée à moitié, aux États-Unis | Boavizta (instance Azure d4ads_v5) |
| Audience | 10 000 lectures de fiche par an | Hypothèse, faute de mesure |

## Limites

- **Énergie primaire** : l'API ne la calcule pas pour la fabrication des terminaux. L'indicateur « ressources fossiles » (`adpf`), qui inclut l'uranium, la remplace. Dans l'étude ADEME-Arcep, les deux indicateurs diffèrent de 3 % sur l'ensemble du numérique français.
- **Eau** : seule l'eau consommée pour produire l'électricité en France est comptée. Aucune source ouverte ne donne l'eau consommée par la fabrication des terminaux : la valeur de la Base IMPACTS, fournie par Boavizta, est négative, et l'étude ADEME-Arcep ne mesure pas l'eau. La valeur publiée est donc un minimum, sans doute très inférieur à la réalité. Le référentiel de l'ADEME range d'ailleurs cet indicateur parmi ceux dont la méthode n'est pas encore mûre. L'eau de la construction, aux États-Unis, n'est pas évaluée.
- **Temps d'utilisation** : avec 3,6 heures par jour au lieu de 7,2, la part de fabrication attribuée à une lecture double.
- **Réseau** : la box, allumée en permanence, n'est comptée qu'au volume de données, selon la convention du référentiel, et la fabrication du réseau n'est pas comptée. Même multipliée par dix, la part du réseau resterait sous 1 %.

## Objectifs

| Objectif | Indicateurs | Départ (novembre 2026) | Cible | Moyens |
|---|---|---|---|---|
| Ne pas alourdir la lecture d'une fiche | Les quatre | Tableau [« Par lecture d'une fiche »](#par-lecture-dune-fiche) | Aucune hausse jusqu'en 2030, à hypothèses constantes | Temps de lecture moyen des fiches de 6,7 minutes au plus, 10 minutes au plus pour chacune (page [Contribuer](../contribuer/)) ; budget par page vérifié à chaque publication |
| Réduire l'empreinte d'une publication | Gaz à effet de serre, énergie primaire, ressources abiotiques | 0,37 g CO2e, 10 kJ, 1,6 µg Sb éq. | −50 % d'ici octobre 2027 | Accélérer la vérification du budget par page |

Pour la lecture, l'objectif est une limitation, pas une réduction. Une baisse de 6 % par an, alignée sur l'ITU-T L.1470, obligerait à raccourcir les fiches chaque année : la fabrication du terminal fait plus de 90 % de l'empreinte et ne dépend pas du site. Le site agit pourtant sur elle en restant utilisable sur des appareils anciens (critères 2.2 et 2.4), ce qui allonge leur durée de vie ; ce calcul ne mesure pas cet effet.

L'évaluation est refaite chaque année en octobre, avec la déclaration d'écoconception : le script donne les nouvelles valeurs, le temps de lecture moyen, la durée d'une publication et l'empreinte par minute affichée sous le titre des fiches.

## Budget par page

Chaque page du site doit respecter ce budget au premier chargement : cache désactivé, page entièrement défilée, sans interaction.

| | Budget | Maximum mesuré | Page la plus lourde |
|---|---:|---:|---|
| Poids transféré | 100 Ko | 73 Ko | Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) |
| Requêtes | 10 | 7 | Toutes les pages, sauf la page d'erreur |
| Éléments du DOM | 1 500 | 1 389 | Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) |

Mesuré le 31 octobre 2026 dans Chromium 155 sur les 132 pages du site, page d'erreur comprise, à 1 366 × 768 et 390 × 844 pixels : toutes respectent le budget. Le DOM compte toutes les balises de la page, y compris celles des images SVG.

Le budget est vérifié à chaque publication, avant la mise en ligne : le site construit est servi en local, compressé comme par GitHub Pages, et chaque page est chargée dans Chrome aux deux tailles d'écran. Si une page dépasse le budget, la publication échoue. Chaque page affiche en pied de page son propre poids et son nombre de requêtes, issus de cette mesure et arrondis au Ko supérieur.

À 512 kbit/s, le débit testé pour le critère 2.3, 100 Ko se transfèrent en 1,6 seconde environ.

Le budget porte sur le chargement de la page. Il ne compte pas la recherche : à la première saisie, elle télécharge sa bibliothèque et son index, en 2 requêtes et 344 Ko, un poids annoncé dès son ouverture (critère 4.12).

Avec le cache, passer d'une page à l'autre ne télécharge que le HTML : 1 requête et 22 Ko au plus. Une page revue dans les 10 minutes ne demande aucune requête ; au-delà, le navigateur revérifie ses 7 fichiers sans les télécharger de nouveau (critère 6.2).
