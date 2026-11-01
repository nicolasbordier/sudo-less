---
weight: 700
title: "Porteur de projet"
description: "Le rôle et les actions concrètes d'un porteur de projet dans une démarche d'écoconception numérique."
icon: "flag"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le porteur de projet arbitre les décisions qui engagent tout le reste de la démarche : l'utilité même du service, les objectifs environnementaux visés, et les moyens humains dédiés à l'écoconception. Sans son engagement en amont, les efforts techniques ultérieurs restent isolés et fragiles.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.1](../../../rgesn/strategie/1-1_evaluation-utilite/) — Évaluation de l'utilité | Prioritaire | Questionner l'utilité réelle du service avant de lancer sa construction, et documenter cette analyse. |
| [1.2](../../../rgesn/strategie/1-2_cibles-utilisatrices/) — Cibles utilisatrices | Prioritaire | Définir les cibles utilisatrices et leurs besoins réels, en cohérence avec le périmètre du service. |
| [1.3](../../../rgesn/strategie/1-3_referent-ecoconception/) — Référent écoconception | Recommandé | Nommer un référent écoconception, avec le temps et les prérogatives nécessaires pour agir. |
| [1.5](../../../rgesn/strategie/1-5_objectifs-environnementaux/) — Objectifs environnementaux | Prioritaire | Fixer des objectifs chiffrés de réduction d'impact et en suivre l'avancement dans le temps. |
| [1.8](../../../rgesn/strategie/1-8_efforts-open-source/) — Efforts d'open source | Recommandé | Arbitrer une politique d'ouverture du code, y compris les aspects juridiques (licence). |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.8](../../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) — Fournisseurs et impacts environnementaux | Prioritaire | Inscrire des exigences environnementales dans les achats et les contrats des fournisseurs. |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | Prioritaire | S'engager sur une durée de mises à jour correctives, alignée sur la durée de vie des terminaux visés. |
| [3.5](../../../rgesn/architecture/3-5_dissociation-mises-a-jour/) — Dissociation des mises à jour correctives et évolutives | Modéré | Exiger que les correctifs puissent s'installer sans les évolutions. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | Modéré | Distribuer des mises à jour incrémentielles plutôt que de remplacer tout le code à chaque version. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.14](../../../rgesn/ux-ui/4-14_dark-patterns/) — Absence de procédés manipulatoires (dark patterns) | Recommandé | Exclure les procédés manipulatoires des objectifs marketing et produit. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.3](../../../rgesn/contenus/5-3_definition-videos/) — Définition vidéo adaptée au contenu et au terminal | Prioritaire | Arbitrer la définition des vidéos selon leur contenu, plutôt que la plus haute par défaut. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | Recommandé | Faire du budget de poids et de requêtes par écran une exigence du produit. |

## 7. Backend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | Recommandé | Décider des durées de conservation de chaque type de données. |

## 9. Algorithmie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [9.1](../../../rgesn/algorithmie/9-1_necessite-entrainement/) — Nécessité d'une phase d'entraînement | Prioritaire | Vérifier qu'un modèle d'IA à entraîner est réellement nécessaire avant de lancer le projet. |
| [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/) — Méthode d'apprentissage la plus sobre | Prioritaire | Arbitrer en faveur de la méthode d'apprentissage la moins complexe qui suffit à l'usage. |
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | Prioritaire | Limiter la quantité d'entraînement, en partant si possible d'un modèle pré-entraîné. |
| [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) — Fréquence de réentraînement des modèles | Prioritaire | Fixer la fréquence de réentraînement selon le besoin réel des utilisateurs. |
| [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) — Stratégie d'inférence sobre | Prioritaire | Choisir une stratégie d'inférence proportionnée à l'usage : le plus petit modèle qui suffit, cache des réponses. |

---

Voir la page [Outils > Porteur de projet](../../../outils/par-metier/porteur-de-projet/) pour les ressources et guides qui outillent ces arbitrages.
