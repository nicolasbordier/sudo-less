---
weight: 200
title: "Dev Back"
description: "Le rôle et les actions concrètes d'un développeur back-end dans une démarche d'écoconception numérique."
icon: "dns"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur back-end arbitre les choix qui déterminent le volume de données échangées et stockées, le dimensionnement des ressources serveur et le niveau de chiffrement appliqué — des choix coûteux à revenir une fois le service en production.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Prioritaire | Intégrer la réduction d'impact environnemental comme critère de revue de code. |
| [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) — Collecte de données | Recommandé | Ne collecter que les données strictement nécessaires au fonctionnement du service. |
| [1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/) — Niveau de chiffrement | Modéré | Dimensionner le chiffrement (taille de clés, algorithmes) au juste niveau de sécurité requis, ni sous- ni sur-dimensionné. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard et interopérables | Prioritaire | Préférer des technologies standard et interopérables aux solutions propriétaires ou fermées. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | Recommandé | Limiter les flux échangés (compression, pagination, cache) plutôt que de reporter l'effort sur le seul frontend. |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | Recommandé | Ajouter l'impact environnemental aux critères de revue de code : requêtes en base, volume de données, appels externes. |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.1](../../../rgesn/architecture/3-1_architecture-composants/) — Architecture, ressources et composants écoconçus | Prioritaire | Comparer les frameworks et composants serveur sur leur consommation, et documenter le choix. |
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | Recommandé | Concevoir des services qui s'adaptent à la charge : mise à l'échelle automatique, mise en veille hors usage. |
| [3.3](../../../rgesn/architecture/3-3_evolution-protocoles/) — Évolution technique des protocoles | Modéré | Supporter les protocoles récents (HTTPS avec TLS 1.3, HTTP/2 ou HTTP/3, IPv6) et pouvoir en changer sans refonte. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.4](../../../rgesn/contenus/5-4_compression-videos/) — Mode de compression des vidéos efficace et adapté | Prioritaire | Encoder les vidéos avec un codec efficace (AV1, VP9 ou HEVC) et plusieurs débits adaptés au contenu. |
| [5.6](../../../rgesn/contenus/5-6_compression-audio/) — Compression des contenus audio adaptée | Modéré | Encoder les contenus audio avec un codec et un débit adaptés : parole ou musique. |
| [5.7](../../../rgesn/contenus/5-7_format-documents/) — Format de fichier adapté à chaque document | Modéré | Générer les documents dans un format adapté et compressé, sans perdre leur accessibilité. |
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | Recommandé | Automatiser l'archivage et la suppression des contenus obsolètes. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | Recommandé | Envoyer des en-têtes de cache adaptés à chaque type de ressource. |
| [6.3](../../../rgesn/frontend/6-3_compression-ressources/) — Compression des ressources transférées | Modéré | Activer la compression des réponses texte (gzip, Brotli). |

## 7. Backend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [7.1](../../../rgesn/backend/7-1_cache-serveur/) — Cache serveur pour les données les plus utilisées | Recommandé | Mettre en cache côté serveur les données les plus demandées. |
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | Recommandé | Implémenter les durées de conservation : suppression ou archivage automatique passé le délai. |
| [7.3](../../../rgesn/backend/7-3_traitement-arriere-plan/) — Information sur un traitement en cours | Modéré | Exposer l'état des traitements longs, pour que l'interface informe l'utilisateur au lieu de relancer la demande. |
| [7.4](../../../rgesn/backend/7-4_mecanisme-consensus/) — Mécanisme de consensus sobre | Prioritaire | Choisir, pour une chaîne de blocs, un mécanisme de consensus sobre plutôt que la preuve de travail. |

## 8. Hébergement

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [8.8](../../../rgesn/hebergement/8-8_donnees-chaudes-froides/) — Données chaudes et froides hébergées séparément | Modéré | Au-delà de 10 To, séparer les données courantes des archives et sauvegardes, sur un stockage froid. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | Recommandé | Planifier les traitements asynchrones aux heures où l'électricité est la moins carbonée. |

## 9. Algorithmie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) — Données d'apprentissage limitées au nécessaire | Prioritaire | Limiter les données d'entraînement au strict nécessaire. |
| [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) — Stratégie d'inférence sobre | Prioritaire | Optimiser l'inférence : le plus petit modèle qui suffit, cache des réponses. |

---

Voir la page [Outils > Dev Back](../../../outils/par-metier/dev-back/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
