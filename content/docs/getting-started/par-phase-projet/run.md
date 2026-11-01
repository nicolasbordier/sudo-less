---
weight: 400
title: "Run"
description: "Les critères RGESN à appliquer lors de la phase de run d'un projet numérique."
icon: "monitoring"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le RGESN ne rattache aucun critère à la phase de **run**. Une fois le service en production, plusieurs critères décidés en conception se vérifient pourtant dans la durée : c'est la seule phase où l'on observe les usages et la consommation réels, plutôt qu'une estimation.

## 1. Stratégie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | `Responsable RSE/Numérique soutenable` `Responsable IT` `Développeur` | Observer la consommation réelle du service en production et corriger un dimensionnement excessif ou obsolète, plutôt qu'un audit ponctuel isolé. |

## 2. Spécifications

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/) — Maintenance et décommissionnement | `Responsable IT` `Architecte Logiciel` | Revoir chaque année l'inventaire des fonctionnalités et des composants, et retirer ce qui ne sert plus. |

## 3. Architecture

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` | Observer la charge réelle et ajuster les ressources, y compris à la baisse. |
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | `Porteur de projet` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Publier les correctifs de sécurité pendant toute la durée de vie annoncée. |
| [3.5](../../../rgesn/architecture/3-5_dissociation-mises-a-jour/) — Dissociation des mises à jour correctives et évolutives | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` | Livrer les correctifs séparément des évolutions. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` `Responsable RSE/Numérique soutenable` | Distribuer les mises à jour de façon incrémentielle. |
| [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/) — Optimisation des environnements de développement, préproduction et test | `Architecte Système` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Éteindre les environnements hors production quand ils ne servent pas. |

## 4. UX/UI

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [4.3](../../../rgesn/ux-ui/4-3_parcours-navigation/) — Optimisation du parcours de navigation | `Développeur` `Concepteur UX / UI` `Responsable Qualité` | Observer les usages (tests utilisateurs, statistiques respectueuses de la vie privée) et raccourcir les parcours. |

## 5. Contenus

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | `Architecte Logiciel` `Data Scientist` `Responsable de la sécurité informatique` `Responsable Juridique` | Archiver ou supprimer régulièrement les contenus obsolètes. |

## 6. Frontend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | `Développeur` `Concepteur UX / UI` `Responsable Produit` | Surveiller que les contenus ajoutés ne font pas dériver le poids des écrans. |

## 7. Backend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | `Administrateur Système` `Développeur` `Responsable Produit` `Architecte Logiciel` | Appliquer les durées de conservation : purges automatiques, sauvegardes comprises. |

## 8. Hébergement

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [8.1](../../../rgesn/hebergement/8-1_demarche-hebergeur/) — Hébergeur engagé dans la réduction de son empreinte | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` `Administrateur Système` | Réévaluer chaque année les indicateurs publiés par l'hébergeur (PUE, WUE, électricité), qui changent d'un exercice à l'autre. |
| [8.9](../../../rgesn/hebergement/8-9_duplication-donnees/) — Duplication des données selon le besoin | `Responsable de l'hébergement` `Ingénieur en stockage de données` `Responsable de la sécurité informatique` `Architecte/Ingénieur Systèmes` | Vérifier que le nombre de copies et de sauvegardes reste ajusté au niveau de service. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | `Responsable de la programmation` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Planifier les traitements asynchrones aux heures où l'électricité est la moins carbonée. |

## 9. Algorithmie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) — Fréquence de réentraînement des modèles | `Porteur de projet` `Data Scientist` `Chef de produit marketing` | Réentraîner les modèles quand les données ou les besoins changent vraiment, pas à date fixe par habitude. |
| [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) — Stratégie d'inférence sobre | `Porteur de projet` `Data Scientist` `Développeur` | Suivre la consommation de l'inférence, et mettre en cache les réponses fréquentes. |

---

Voir la page [Outils > Run](../../../outils/par-phase-projet/run/) pour les outils concrets de supervision continue déjà documentés sur ce site (Kepler, Scaphandre, Cloud Carbon Footprint...).
