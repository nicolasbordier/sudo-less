---
weight: 400
title: "Run"
description: "Tableau récapitulatif des outils spécifiques à la phase de run : surveiller en continu la consommation d'un service déjà en production et ajuster son dimensionnement."
icon: "monitoring"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-23T00:00:00+01:00"
draft: false
toc: true
---

Une fois le service déployé, la phase de **run** consiste à le surveiller en continu plutôt qu'à le mesurer ponctuellement — la logique de revue régulière du [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/). Voir la page [OPS](../../par-metier/ops/) pour le détail complet.

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de contenu, un écosystème ou un fournisseur particulier), sont payants, ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [Kepler](https://github.com/sustainable-computing-io/kepler) (CNCF Sandbox) | Exporter Prometheus | Consommation énergétique par conteneur, pod et nœud dans un cluster Kubernetes | Oui |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) / [PowerAPI](https://powerapi.org/) | Agents de métrologie | Puissance par processus, en continu, exportable vers Prometheus/Grafana | Oui |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) | Dashboard open source | Suivi dans le temps des émissions multi-cloud à partir des données de facturation | Oui |
| [Android Vitals](https://developer.android.com/topic/performance/vitals) / [MetricKit](https://developer.apple.com/documentation/MetricKit) | Natif mobile | Réveils excessifs, wake locks, impact énergétique, remontés depuis les terminaux réels en production | Oui |
| Recommandations de redimensionnement des clouds : [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) et [Trusted Advisor](https://aws.amazon.com/trustedadvisor/), [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations), [GCP Recommender](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) | Recommandations natives des fournisseurs | Signalent les ressources sous-utilisées ou surdimensionnées et proposent un redimensionnement ou une extinction ([critères 2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/) et [3.2](../../../rgesn/architecture/3-2_architecture-elastique/)) | Oui (certains contrôles Trusted Advisor demandent un plan de support payant) |
| Extinction planifiée hors production : [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html), [Azure DevTest Labs](https://learn.microsoft.com/en-us/azure/devtest-labs/devtest-lab-auto-shutdown), [KEDA](https://keda.sh/) (déclencheur `cron`), [DailyClean](https://github.com/AxaFrance/dailyclean) (AXA France) | Planification d'arrêt et de redémarrage | Éteignent les environnements de développement et de test en dehors des horaires ouvrés et les rallument automatiquement ([critère 3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/)) | Oui (services cloud facturés aux ressources consommées) |

## Outils complémentaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| Tableaux de bord natifs — [AWS](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Google Cloud](https://cloud.google.com/carbon-footprint), [Azure](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) | Dashboards fournisseurs | Suivi mensuel natif, sans agent à déployer | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) — Hébergement n°3 | Grille de questionnement | Vérifie que les ressources (CPU, mémoire) allouées sont ajustées dynamiquement à l'usage réel | Oui |
| [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) / [KEDA](https://keda.sh/) / [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) | Auto-scaling | Ajustent le nombre de pods ou d'instances à la charge réelle, jusqu'à zéro réplique pour un service sans trafic avec KEDA ([critère 3.2](../../../rgesn/architecture/3-2_architecture-elastique/)) | Oui |
| [VMware Aria Operations](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations.html) | Supervision de virtualisation (commerciale) | Signale les VM surdimensionnées ou inactives d'un parc vSphere sur site et chiffre leur impact environnemental ([critères 3.2](../../../rgesn/architecture/3-2_architecture-elastique/) et [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/)) | Non |
| [IBM Turbonomic](https://www.ibm.com/products/turbonomic) | Plateforme commerciale | Redimensionne et replace en continu VM, conteneurs et répliques Kubernetes sur un périmètre hybride, chaque action étant simulée avant exécution ([critère 3.2](../../../rgesn/architecture/3-2_architecture-elastique/)) | Non |
| [Review Apps de GitLab](https://docs.gitlab.com/ci/review_apps/) / [Terraform](https://www.hashicorp.com/en/products/terraform) / [Ansible](https://docs.ansible.com/) | Environnements à la demande | Remplacent les préproductions permanentes par des environnements créés pour un besoin puis supprimés ([critère 3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/)) | Oui |
| [Matomo](https://matomo.org/) / [Plausible Analytics](https://plausible.io/) / [PostHog](https://posthog.com/) | Mesure d'audience respectueuse de la vie privée | Mesurent les parcours réels sans cookies tiers, pour repérer les étapes qui allongent la navigation ([critère 4.3](../../../rgesn/ux-ui/4-3_parcours-navigation/)) | Oui en auto-hébergement (offres hébergées payantes) |
| [EcoIndex Badge](https://github.com/cnumr/ecoindex_badge) (CNUMR) | Badge à intégrer aux pages | Affiche en production le score EcoIndex de la page, mis en cache 7 jours, avec un lien vers le détail de la mesure ; ajoute une requête vers un service tiers à chaque affichage | Oui (licence CC BY-NC-ND 3.0, usage non commercial) |

---

Ces mesures n'ont d'intérêt que si elles déclenchent une action de dimensionnement (autoscaling, arrêt de ressources inutilisées) plutôt que de rester un tableau de bord ignoré — voir le détail de cette logique sur la page [OPS](../../par-metier/ops/). C'est aussi durant cette phase que se détecte un signal d'alerte propre à la phase suivante : un service qui ne justifie plus son maintien en l'état amorce sa [fin de vie](../fin-de-vie/).
