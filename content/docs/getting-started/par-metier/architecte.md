---
weight: 500
title: "Architecte"
description: "Le rôle et les actions concrètes d'un architecte logiciel dans une démarche d'écoconception numérique."
icon: "account_tree"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

L'architecte pose les fondations techniques (choix des composants, dimensionnement, ouverture des interfaces) qui conditionnent tous les choix ultérieurs de l'équipe de développement — les corriger après coup revient bien plus cher que de les cadrer correctement dès le départ.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard et interopérables | Prioritaire | Choisir des technologies standard et interopérables plutôt que des solutions propriétaires ou fermées. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | Recommandé | Concevoir des API documentées et ouvertes pour tout matériel piloté par le service. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | Recommandé | Inscrire la réduction des impacts de chaque fonctionnalité parmi les objectifs des revues de conception. |
| [2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/) — Maintenance et décommissionnement | Prioritaire | Prévoir dès la conception la maintenance et le décommissionnement du service : inventaire, revue périodique, retrait de ce qui ne sert plus. |
| [2.10](../../../rgesn/specifications/2-10_services-tiers/) — Impacts environnementaux des services tiers | Prioritaire | Évaluer l'impact des services tiers (vidéo, carte, mesure d'audience…) avant de les intégrer, et vérifier leur démarche (critères 1.4 et 1.5). |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.1](../../../rgesn/architecture/3-1_architecture-composants/) — Architecture, ressources et composants écoconçus | Prioritaire | Choisir les frameworks et composants en comparant leur empreinte, et documenter ce choix dans la déclaration. |
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | Recommandé | Adapter automatiquement les ressources à la charge réelle : mise à l'échelle, extinction hors usage. |
| [3.3](../../../rgesn/architecture/3-3_evolution-protocoles/) — Évolution technique des protocoles | Modéré | Supporter les protocoles récents (HTTPS avec TLS 1.3, HTTP/2 ou HTTP/3, IPv6) et pouvoir en changer sans refonte. |
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | Prioritaire | Garantir des mises à jour correctives pendant toute la durée de vie prévue des équipements et logiciels liés au service. |
| [3.5](../../../rgesn/architecture/3-5_dissociation-mises-a-jour/) — Dissociation des mises à jour correctives et évolutives | Modéré | Livrer les correctifs séparément des évolutions, pour qu'un utilisateur puisse sécuriser son terminal sans l'alourdir. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | Modéré | Distribuer des mises à jour incrémentielles plutôt que de remplacer tout le code à chaque version. |
| [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/) — Optimisation des environnements de développement, préproduction et test | Modéré | Dimensionner les environnements de développement, de préproduction et de test au besoin, et les éteindre quand ils ne servent pas. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.5](../../../rgesn/ux-ui/4-5_composants-natifs/) — Composants fonctionnels natifs | Modéré | Préférer les composants natifs du navigateur, du système ou du langage aux bibliothèques ajoutées. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | Recommandé | Définir une stratégie d'archivage et de suppression des contenus obsolètes, automatique ou manuelle. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | Recommandé | Concevoir la stratégie de cache (navigateur, CDN) de toutes les ressources dont le service a le contrôle. |
| [6.7](../../../rgesn/frontend/6-7_domaine-unique/) — Ressources statiques sur un même domaine | Modéré | Servir les ressources statiques depuis le domaine du service plutôt que depuis plusieurs domaines tiers. |

## 7. Backend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [7.1](../../../rgesn/backend/7-1_cache-serveur/) — Cache serveur pour les données les plus utilisées | Recommandé | Mettre en cache côté serveur les données les plus demandées. |
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | Recommandé | Fixer une durée de conservation pour chaque type de données, puis les supprimer ou les archiver. |
| [7.4](../../../rgesn/backend/7-4_mecanisme-consensus/) — Mécanisme de consensus sobre | Prioritaire | Choisir, pour une chaîne de blocs, un mécanisme de consensus sobre plutôt que la preuve de travail. |

## 8. Hébergement

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [8.8](../../../rgesn/hebergement/8-8_donnees-chaudes-froides/) — Données chaudes et froides hébergées séparément | Modéré | Au-delà de 10 To, séparer les données courantes des archives et sauvegardes, sur un stockage froid. |
| [8.9](../../../rgesn/hebergement/8-9_duplication-donnees/) — Duplication des données selon le besoin | Recommandé | Ne dupliquer les données que selon un niveau de service (SLA) ajusté au besoin. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | Recommandé | Décaler les calculs et transferts asynchrones aux heures où l'électricité est la moins carbonée et les réseaux les moins chargés. |

## 9. Algorithmie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/) — Méthode d'apprentissage la plus sobre | Prioritaire | Choisir la méthode d'apprentissage la moins complexe qui suffit à l'usage réel. |
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | Prioritaire | Limiter la quantité d'entraînement, en partant si possible d'un modèle pré-entraîné. |
| [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) — Compression des modèles | Recommandé | Compresser les modèles : quantification, élagage, distillation. |

---

Voir la page [Outils > Architecte](../../../outils/par-metier/architecte/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
