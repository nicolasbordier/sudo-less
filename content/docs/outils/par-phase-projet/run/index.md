---
weight: 400
title: "Run"
description: "Tableau récapitulatif des outils spécifiques à la phase de run : surveiller en continu la consommation d'un service déjà en production et ajuster son dimensionnement."
icon: "monitoring"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Une fois le service déployé, la phase de **run** consiste à le surveiller en continu plutôt qu'à le mesurer ponctuellement — la logique de revue régulière du [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/). Voir la page [OPS](../../par-metier/ops/) pour le détail complet.

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [Kepler](https://github.com/sustainable-computing-io/kepler) (CNCF Sandbox) | Exporter Prometheus | Consommation énergétique par conteneur, pod et nœud dans un cluster Kubernetes | Oui |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) / [PowerAPI](https://powerapi.org/) | Agents de métrologie | Puissance par processus, en continu, exportable vers Prometheus/Grafana | Oui |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) | Dashboard open source | Suivi dans le temps des émissions multi-cloud à partir des données de facturation | Oui |
| Tableaux de bord natifs — [AWS](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Google Cloud](https://cloud.google.com/carbon-footprint), [Azure](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) | Dashboards fournisseurs | Suivi mensuel natif, sans agent à déployer | Oui |
| [Android Vitals](https://developer.android.com/topic/performance/vitals) / [MetricKit](https://developer.apple.com/documentation/MetricKit) | Natif mobile | Réveils excessifs, wake locks, impact énergétique, remontés depuis les terminaux réels en production | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) — Hébergement n°3 | Grille de questionnement | Vérifie que les ressources (CPU, mémoire) allouées sont ajustées dynamiquement à l'usage réel | Oui |

---

Ces mesures n'ont d'intérêt que si elles déclenchent une action de dimensionnement (autoscaling, arrêt de ressources inutilisées) plutôt que de rester un tableau de bord ignoré — voir le détail de cette logique sur la page [OPS](../../par-metier/ops/). C'est aussi durant cette phase que se détecte un signal d'alerte propre à la phase suivante : un service qui ne justifie plus son maintien en l'état amorce sa [fin de vie](../fin-de-vie/).
