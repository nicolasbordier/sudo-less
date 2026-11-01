---
weight: 800
title: "Responsable RSE/Numérique soutenable"
description: "Le rôle et les actions concrètes d'un responsable RSE/numérique soutenable dans une démarche d'écoconception numérique."
icon: "eco"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le responsable RSE/numérique soutenable porte une vision transverse de la démarche, à cheval entre le cadrage stratégique et le suivi technique — c'est souvent le rôle le plus cité dans les fiches RGESN, précisément parce qu'il fait le lien entre les autres métiers.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.1](../../../rgesn/strategie/1-1_evaluation-utilite/) — Évaluation de l'utilité | Prioritaire | Challenger l'utilité du service au regard de ses impacts environnementaux. |
| [1.3](../../../rgesn/strategie/1-3_referent-ecoconception/) — Référent écoconception | Recommandé | Occuper ou outiller ce rôle de référent, en s'appuyant sur le [référentiel de compétences DINUM](../../../autres-referentiels/) (onglet « Communication / Sensibilisation »). |
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Prioritaire | Organiser des revues régulières et en assurer le suivi dans le temps. |
| [1.5](../../../rgesn/strategie/1-5_objectifs-environnementaux/) — Objectifs environnementaux | Prioritaire | Fixer et suivre des objectifs de réduction d'impact alignés sur une trajectoire climatique reconnue (SBTi/ITU-T). |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.1](../../../rgesn/specifications/2-1_profils-materiels/) — Profils de matériels | Prioritaire | Objectiver le profil matériel visé à partir de données réelles d'usage (Baromètre du numérique) plutôt que d'un choix arbitraire. |
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | Prioritaire | S'assurer que le service est testé sur un terminal ancien, et que ses caractéristiques figurent dans la déclaration. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | Recommandé | S'assurer que le service est testé en bas débit, et que le débit minimum figure dans la déclaration. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | Prioritaire | S'assurer que les versions minimales d'OS et de navigateurs sont testées et déclarées. |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | Recommandé | Veiller à ce que les revues de conception et de code intègrent la réduction des impacts. |
| [2.8](../../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) — Fournisseurs et impacts environnementaux | Prioritaire | Intégrer des critères environnementaux à la politique d'achat (guide des achats numériques responsables, ISO 20400). |
| [2.10](../../../rgesn/specifications/2-10_services-tiers/) — Impacts environnementaux des services tiers | Prioritaire | Lister dans la déclaration les services tiers et leur avancement sur les critères 1.4 et 1.5. |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.1](../../../rgesn/architecture/3-1_architecture-composants/) — Architecture, ressources et composants écoconçus | Prioritaire | Vérifier que le choix d'architecture et de composants est comparé à d'autres options et documenté. |
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | Recommandé | Vérifier que les ressources s'adaptent à la charge, et que rien ne tourne inutilement. |
| [3.3](../../../rgesn/architecture/3-3_evolution-protocoles/) — Évolution technique des protocoles | Modéré | Supporter les protocoles récents (HTTPS avec TLS 1.3, HTTP/2 ou HTTP/3, IPv6) et pouvoir en changer sans refonte. |
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | Prioritaire | Faire inscrire la durée des mises à jour correctives dans les engagements du service. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | Modéré | Distribuer des mises à jour incrémentielles plutôt que de remplacer tout le code à chaque version. |
| [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/) — Optimisation des environnements de développement, préproduction et test | Modéré | Suivre la consommation des environnements hors production, souvent oubliée. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.12](../../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) — Information sur les fonctionnalités à fort impact environnemental | Recommandé | Identifier les fonctionnalités à fort impact, et veiller à ce que l'utilisateur en soit informé. |
| [4.15](../../../rgesn/ux-ui/4-15_controle-usages/) — Moyen de contrôle des usages et mode sobre | Recommandé | Donner à l'utilisateur un moyen de suivre et de réduire ses usages, par exemple un mode sobre. |

## 8. Hébergement

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [8.1](../../../rgesn/hebergement/8-1_demarche-hebergeur/) — Hébergeur engagé dans la réduction de son empreinte | Prioritaire | Demander à l'hébergeur ses indicateurs environnementaux et son adhésion au Code de conduite européen sur les centres de données. |
| [8.2](../../../rgesn/hebergement/8-2_gestion-equipements/) — Gestion durable des équipements de l'hébergeur | Prioritaire | Demander à l'hébergeur sa politique de gestion des équipements, et la citer dans la déclaration. |
| [8.3](../../../rgesn/hebergement/8-3_pue/) — PUE de l'hébergement | Prioritaire | Vérifier le PUE réel du site d'hébergement : moins de 1,5. |
| [8.4](../../../rgesn/hebergement/8-4_wue/) — WUE de l'hébergement | Recommandé | Vérifier le WUE du site d'hébergement et sa méthode de calcul. |
| [8.5](../../../rgesn/hebergement/8-5_electricite-renouvelable/) — Électricité d'origine renouvelable | Recommandé | Demander les justificatifs de l'électricité renouvelable (contrats d'achat, garanties d'origine). |
| [8.6](../../../rgesn/hebergement/8-6_localisation/) — Localisation de l'hébergement | Recommandé | Héberger le service dans un pays dont l'électricité émet moins de 100 g CO2e/kWh, cohérent avec la localisation de ses utilisateurs. |
| [8.7](../../../rgesn/hebergement/8-7_chaleur-fatale/) — Traitement de la chaleur produite par les serveurs | Recommandé | Préférer un hébergeur qui récupère la chaleur de ses serveurs, ou dont le PUE réel est inférieur à 1,3. |
| [8.8](../../../rgesn/hebergement/8-8_donnees-chaudes-froides/) — Données chaudes et froides hébergées séparément | Modéré | Au-delà de 10 To, séparer les données courantes des archives et sauvegardes, sur un stockage froid. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | Recommandé | Décaler les calculs et transferts asynchrones aux heures où l'électricité est la moins carbonée et les réseaux les moins chargés. |

## 9. Algorithmie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [9.1](../../../rgesn/algorithmie/9-1_necessite-entrainement/) — Nécessité d'une phase d'entraînement | Prioritaire | Challenger la nécessité d'entraîner un modèle d'IA. |
| [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/) — Méthode d'apprentissage la plus sobre | Prioritaire | Choisir la méthode d'apprentissage la moins complexe qui suffit à l'usage réel. |
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | Prioritaire | Limiter la quantité d'entraînement, en partant si possible d'un modèle pré-entraîné. |
| [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) — Données d'apprentissage limitées au nécessaire | Prioritaire | Limiter les données d'entraînement au strict nécessaire. |
| [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) — Compression des modèles | Recommandé | Compresser les modèles : quantification, élagage, distillation. |

---

Voir la page [Outils > Responsable RSE/Numérique soutenable](../../../outils/par-metier/responsable-rse/) et le [référentiel de maturité Green IT](../../../autres-referentiels/) (onglet « Organisation et achats ») pour évaluer la démarche à l'échelle de toute une organisation.
