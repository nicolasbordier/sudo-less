---
weight: 500
title: "Fin de vie"
description: "Tableau récapitulatif des outils et pratiques pour prolonger la durée de vie d'un service ou d'un matériel, ou en organiser la décommission de façon responsable."
icon: "recycling"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

La phase de **fin de vie** pose une question à double sens : comment **éviter** qu'un matériel fonctionnel devienne prématurément inutilisable ([critère 1.10](../../../rgesn/strategie/1-10_api-materiel/)), et comment **organiser** la décommission d'un service ou d'un équipement lorsqu'elle est réellement nécessaire — ce qui suppose de savoir au préalable **qui dépend encore de quoi** (voir [critère 2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/)).

| Outil / Pratique | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [Tasmota](https://tasmota.github.io/docs/) / [Home Assistant](https://www.home-assistant.io/) | Firmware et hub libres | Reprend la main sur un objet connecté dont le fabricant a fermé l'API ou le service cloud | Oui |
| [Murena](https://murena.com/your-fairphone-3-isnt-obsolete-heres-what-to-do-when-android-support-ends/) / [/e/OS](https://murena.com/) | OS mobile open source | Prolonge la durée de vie d'un smartphone au-delà de la fin de support officielle du fabricant | Oui/Payant selon modèle |
| [Règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act) | Référentiel légal | Impose des API ouvertes pour les objets connectés, condition légale pour éviter une fin de vie forcée | Oui (référentiel) |
| [GR491](https://gr491.isit-europe.org/crit.php?id=1-8006-hebergement-le-traitement-des-dechets-generes-par-un) — Hébergement n°1 | Critère « Incontournable » | Vérifie que les déchets matériels issus d'un datacenter sont valorisés ou recyclés plutôt qu'enfouis | Oui |
| [Ordi3.0](http://www.ordi3-0.fr/) | Réseau de réemploi | 300 000 ordinateurs reconditionnés par an (200 structures labellisées), avec logiciels libres pour prolonger leur durée de vie jusqu'à 18 ans | Oui (réseau associatif) |
| [Guide des licences libres](https://code.gouv.fr/fr/doc/licences-libres-dinum/) (DINUM) | Guide de référence | Publier le code source avant l'arrêt d'un service permet à des tiers de le maintenir au-delà de sa fin de vie officielle ([critère 1.8](../../../rgesn/strategie/1-8_efforts-open-source/)) | Oui |
| [GLPI](https://www.glpi-project.org/) / [iTop](https://www.itophub.io/) | CMDB open source | Cartographie déclarative des composants et de leurs dépendances, pour ne pas décommissionner un service dont un autre dépend encore | Oui |
| [OpenTelemetry](https://opentelemetry.io/) + [Grafana Tempo](https://grafana.com/oss/tempo/) / Jaeger | Traçage distribué | Observe les appels réellement effectués entre services en production, y compris les dépendances non documentées — plus fiable qu'un inventaire tenu à jour manuellement | Oui |
| [Backstage](https://backstage.io/) | Service catalog (CNCF) | Combine registre déclaratif des services/propriétaires et données de traçage réelles pour fiabiliser la décision de décommissionnement | Oui |

---

Les retours d'expérience de la page [critère 1.10](../../../rgesn/strategie/1-10_api-materiel/) (Revolv, Insteon, Wink) montrent qu'une fin de vie mal anticipée transforme du matériel fonctionnel en déchet du jour au lendemain. À l'inverse, ouvrir les API et le code **avant** l'arrêt d'un service (plutôt qu'au moment de l'arrêt) est la seule mesure qui donne une chance réelle à une communauté ou une structure de réemploi de prendre le relais — d'où le lien direct entre ce critère et celui de l'[open source](../../../rgesn/strategie/1-8_efforts-open-source/).
