---
weight: 300
title: "Implémentation"
description: "Tableau récapitulatif des outils spécifiques à la phase d'implémentation : mesurer l'impact du code au fur et à mesure de son écriture, avant la mise en production."
icon: "code_blocks"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Une fois les choix de [conception](../conception/) arrêtés, la phase d'**implémentation** consiste à écrire le code en vérifiant, au fil de l'eau, qu'il respecte les budgets et standards définis en amont — voir les pages [Dev Front](../../par-metier/dev-front/), [Dev Back](../../par-metier/dev-back/) et [Dev Mobile](../../par-metier/dev-mobile/) pour le détail complet par métier.

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis) | Extension navigateur | Score EcoIndex en direct pendant le développement, y compris derrière authentification | Oui |
| [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) | Audit intégré CI | Fait échouer une pull request si un budget de performance est dépassé | Oui |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) / [GreenFrame](https://greenframe.io/) | Mesure backend | Consommation par processus (Scaphandre) ou par scénario API complet en conteneurs (GreenFrame) | Oui |
| [Maestro](https://maestro.dev/) + [Flashlight](https://flashlight.dev/) | CLI mobile | Automatise un parcours et mesure CPU/RAM/FPS pendant son exécution | Oui |
| [Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur) / [Datavizta](https://dataviz.boavizta.org/) | API et dashboard | Compare l'empreinte de plusieurs composants ou instances avant de les intégrer au code | Oui |
| [Baseline](https://web.dev/baseline) / [Can I Use](https://caniuse.com/) | Référence de compatibilité | Vérifie qu'une API utilisée dans le code est standard et largement supportée | Oui |
| [Guide ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) | Référentiel officiel | Implémente le niveau de chiffrement choisi en conception avec l'algorithme le moins coûteux à sécurité égale | Oui |

---

Le point commun de ces outils : ils s'utilisent **pendant que le code est encore modifiable à faible coût**, contrairement aux outils de la phase [Run](../run/) qui n'observent qu'un système déjà déployé. Intégrer ces vérifications en CI (Lighthouse CI, EcoSonar) plutôt qu'en revue manuelle ponctuelle permet de détecter une régression au moment précis où elle est introduite.
