---
weight: 300
title: "Dev Mobile"
description: "Le rôle et les actions concrètes d'un développeur mobile dans une démarche d'écoconception numérique."
icon: "smartphone"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur mobile est directement responsable de la durée de vie utile des smartphones et tablettes visés par le service : compatibilité avec les anciennes versions d'OS, gestion de la batterie, et mode hors ligne pour ne pas rendre l'application inutilisable en cas de connexion dégradée.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard et interopérables | Prioritaire | Évaluer une PWA (plus légère et rétro-compatible) avant de choisir une application native. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | Recommandé | Documenter et ouvrir les API du matériel piloté, pour permettre sa réutilisation au-delà de la fin de vie du service. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | Prioritaire | Tester les fonctionnalités critiques sur un smartphone réel mis sur le marché il y a 7 ans ou plus. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | Recommandé | Prévoir un mode hors ligne (stockage local, file d'attente de synchronisation) sur les fonctionnalités qui le permettent. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | Prioritaire | Maintenir la compatibilité avec des versions d'OS mobile vieilles de 5 ans. |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | Recommandé | Ajouter l'impact environnemental aux critères de revue de code : taille de l'application, requêtes, batterie. |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | Prioritaire | Publier des correctifs de sécurité pendant toute la durée de vie annoncée des terminaux pris en charge. |
| [3.5](../../../rgesn/architecture/3-5_dissociation-mises-a-jour/) — Dissociation des mises à jour correctives et évolutives | Modéré | Livrer les correctifs séparément des évolutions, pour ne pas imposer une version plus lourde. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | Modéré | Distribuer des mises à jour incrémentielles plutôt que l'application entière. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/) — Désactivation de la lecture automatique | Prioritaire | Désactiver la lecture automatique des vidéos, sons et animations. |
| [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/) — Absence de défilement infini | Prioritaire | Remplacer le défilement infini par une pagination ou un bouton « voir plus ». |
| [4.5](../../../rgesn/ux-ui/4-5_composants-natifs/) — Composants fonctionnels natifs | Modéré | Utiliser les composants natifs du système plutôt que des bibliothèques d'interface ajoutées. |
| [4.13](../../../rgesn/ux-ui/4-13_notifications/) — Limitation des notifications | Prioritaire | Limiter les notifications push au nécessaire, et laisser l'utilisateur les désactiver. |
| [4.15](../../../rgesn/ux-ui/4-15_controle-usages/) — Moyen de contrôle des usages et mode sobre | Recommandé | Donner à l'utilisateur un moyen de suivre et de réduire ses usages, par exemple un mode sobre. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.1](../../../rgesn/contenus/5-1_format-images/) — Format de fichier adapté à chaque image | Recommandé | Choisir le format de chaque image : vectoriel pour les icônes, AVIF ou WebP pour les photos. |
| [5.2](../../../rgesn/contenus/5-2_compression-images/) — Niveau de compression adapté à chaque image | Recommandé | Régler la compression de chaque image selon son contenu et son contexte d'affichage. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | Recommandé | Fixer un budget de poids et de requêtes par écran, et le mesurer à chaque version. |
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | Recommandé | Mettre en cache les réponses et les images dans l'application. |
| [6.4](../../../rgesn/frontend/6-4_dimensions-images/) — Dimensions des images adaptées à l'affichage | Recommandé | Télécharger des images aux dimensions de l'écran du terminal. |
| [6.5](../../../rgesn/frontend/6-5_chargement-ressources/) — Chargement des seules ressources utiles | Recommandé | Ne charger que les données et ressources de l'écran affiché. |
| [6.6](../../../rgesn/frontend/6-6_capteurs-terminaux/) — Usage des capteurs limité au besoin du service | Modéré | Ne solliciter GPS, caméra ou accéléromètre qu'au moment et à la fréquence nécessaires. |

---

Voir la page [Outils > Dev Mobile](../../../outils/par-metier/dev-mobile/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
