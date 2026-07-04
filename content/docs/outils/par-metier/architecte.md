---
weight: 500
title: "Architecte"
description: "Tableau récapitulatif des outils pour dimensionner une infrastructure, choisir un hébergeur et sécuriser un service en tenant compte de l'empreinte environnementale."
icon: "account_tree"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Contrairement aux outils de mesure applicative des pages [Dev Back](../dev-back/) et [Dev Mobile](../dev-mobile/), les ressources ci-dessous interviennent au niveau des **choix d'infrastructure et de dimensionnement** : type d'instance, hébergeur, algorithme de chiffrement (voir le [critère 1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/) et le détail infra du [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/)).

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Utilisable par API/code ? |
|---|---|---|---|---|
| [Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur) (Boavizta) | API ouverte | Empreinte fabrication **et** usage (GWP, énergie primaire, ressources abiotiques) d'un serveur ou d'une instance cloud, par analyse de cycle de vie | Oui | Oui |
| [Datavizta](https://dataviz.boavizta.org/) (Boavizta) | Dashboard d'exploration | Explore la base de données brute des fabricants pour comparer plusieurs équipements avant de choisir, sans déploiement préalable | Oui | Non (interface web) |
| [Cloud Scanner](https://www.sfeir.dev/cloud/surveillez-limpact-environnemental-de-vos-instances-ec2-avec-cloud-scanner-de-boavizta/) (Boavizta) | Outil open source | Applique la méthodologie Boavizta aux instances AWS EC2 déjà déployées, avec export par région et type d'instance | Oui | Oui |
| [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) (Thoughtworks) | Outil open source | Estimation d'émissions à partir des données de facturation, vue unifiée **multi-cloud** (AWS, Azure, GCP) avec recommandations d'optimisation | Oui | Oui |
| Tableaux de bord natifs — [AWS](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Google Cloud](https://cloud.google.com/carbon-footprint), [Azure](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) | Dashboards fournisseurs | Émissions par service/région/mois, rapides à consulter mais moins précis que Boavizta pour arbitrer entre choix techniques | Oui | Selon fournisseur |
| [OVHcloud Impact Tracker](https://www.ovhcloud.com/en/about-us/environmental-impact-tracker/) / [Scaleway Environmental Footprint Calculator](https://www.scaleway.com/en/environmental-footprint-calculator/) | Dashboards hébergeurs souverains | Émissions (et eau pour Scaleway) par produit/région, méthode validée indépendamment pour OVHcloud (GHG Protocol, ISO 14067) | Oui | Oui (API pour OVHcloud) |
| [Guide ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) | Référentiel officiel | Dimensionne un chiffrement adapté au besoin réel (taille de clé, durée de protection) plutôt que systématiquement maximal | Oui | Non (document) |

---

Deux logiques distinctes coexistent dans ce tableau : les outils **Boavizta** (Boaviztapi, Datavizta, Cloud Scanner) et **Cloud Carbon Footprint** permettent d'objectiver un choix *avant* ou *après* déploiement, indépendamment du fournisseur — utile pour comparer plusieurs options. Les **tableaux de bord natifs** sont plus rapides à consulter mais enferment dans l'écosystème d'un seul fournisseur. Le **guide ANSSI**, enfin, ne mesure rien : il évite de surdimensionner un mécanisme de sécurité au détriment de la sobriété — voir le tableau comparatif complet des algorithmes au [critère 1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/).
