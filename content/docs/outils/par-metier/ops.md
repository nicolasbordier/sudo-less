---
weight: 600
title: "OPS"
description: "Tableau récapitulatif des outils pour surveiller en continu la consommation d'une infrastructure et ajuster son dimensionnement au besoin réel."
icon: "monitoring"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Contrairement aux outils de choix d'infrastructure de la page [Architecte](../architecte/), les ressources ci-dessous s'utilisent en **surveillance continue**, une fois le service en production — la même logique de revue régulière que le [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/).

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégré à l'observabilité existante ? |
|---|---|---|---|---|
| [Kepler](https://github.com/sustainable-computing-io/kepler) (CNCF Sandbox) | Exporter Prometheus | Consommation énergétique par **conteneur, pod et nœud** dans un cluster Kubernetes, via lecture de compteurs matériels (RAPL, ACPI, GPU) | Oui | Oui (Prometheus/Grafana natif) |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) (Hubblo) | Agent de métrologie | Puissance par machine hôte et par **processus**, en dehors ou en complément d'un cluster Kubernetes | Oui | Oui (Prometheus/Grafana) |
| [PowerAPI](https://powerapi.org/) (Inria/Université de Lille) | Framework Python | Estimation par modèle (sans capteur matériel requis) à plusieurs niveaux : VM, conteneur, application, processus | Oui | Oui (plugins de sortie configurables) |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) (Thoughtworks) | Dashboard open source | Suivi dans le temps des émissions multi-cloud à partir des données de facturation | Oui | Oui |
| Tableaux de bord natifs — [AWS](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Google Cloud](https://cloud.google.com/carbon-footprint), [Azure](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) | Dashboards fournisseurs | Suivi mensuel natif, sans agent à déployer | Oui | Selon fournisseur |

---

Ces mesures n'ont d'intérêt que si elles débouchent sur une action : la [recommandation n°3 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Adapter l'utilisation des équipements techniques aux besoins », donne la checklist correspondante — mémoire et cœurs CPU alloués selon l'usage réel, cœurs inutilisés désactivés, provisionnement/déprovisionnement dynamique selon la charge. Les mécanismes d'autoscaling (HPA/VPA Kubernetes, autoscaling groups cloud) sont l'implémentation technique la plus courante de cette recommandation, à condition de dimensionner leurs seuils sur la base des métriques remontées par Kepler ou Scaphandre plutôt que sur des marges de sécurité arbitraires.
