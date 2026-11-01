---
weight: 550
title: "Data Scientist"
description: "Le rôle et les actions concrètes d'un data scientist dans une démarche d'écoconception numérique."
icon: "model_training"
date: "2026-11-01T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le data scientist décide s'il faut entraîner un modèle, sur quelles données, avec quelle méthode et à quelle fréquence. Ce sont les choix les plus coûteux en énergie d'un service qui utilise l'IA : la famille Algorithmie du RGESN demande de les justifier, mesures à l'appui.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) — Collecte de données | Recommandé | Ne collecter que les données strictement nécessaires, y compris pour entraîner un modèle. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | Recommandé | Archiver ou supprimer les jeux de données et les modèles devenus obsolètes. |

## 8. Hébergement

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [8.6](../../../rgesn/hebergement/8-6_localisation/) — Localisation de l'hébergement | Recommandé | Entraîner et faire tourner l'inférence dans un pays dont l'électricité est peu carbonée. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | Recommandé | Planifier les entraînements qui peuvent attendre aux heures où l'électricité est la moins carbonée. |

## 9. Algorithmie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [9.1](../../../rgesn/algorithmie/9-1_necessite-entrainement/) — Nécessité d'une phase d'entraînement | Prioritaire | Vérifier qu'une règle, une recherche classique ou un modèle existant ne suffit pas, avant d'entraîner. |
| [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/) — Méthode d'apprentissage la plus sobre | Prioritaire | Établir une référence simple (régression, Naive Bayes, arbre de décision) et n'augmenter la complexité que si la précision l'exige, mesure à l'appui. |
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | Prioritaire | Partir d'un modèle pré-entraîné, mesurer l'énergie de chaque entraînement, et l'arrêter quand la qualité ne progresse plus. |
| [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) — Données d'apprentissage limitées au nécessaire | Prioritaire | Tracer la courbe d'apprentissage sur les données disponibles avant toute nouvelle collecte. |
| [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) — Fréquence de réentraînement des modèles | Prioritaire | Fixer des conditions de déclenchement du réentraînement (baisse de qualité, dérive des données) plutôt qu'un calendrier. |
| [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) — Compression des modèles | Recommandé | Essayer la quantification après entraînement, 8 puis 4 bits, en mesurant la qualité à chaque étape. |
| [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) — Stratégie d'inférence sobre | Prioritaire | Choisir le plus petit modèle suffisant, plafonner la longueur des réponses et estimer l'énergie de chaque réponse. |

---

Voir la page [Outils > Data Scientist](../../../outils/par-metier/data-scientist/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
