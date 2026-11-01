---
weight: 400
title: "UX Designer"
description: "Le rôle et les actions concrètes d'un UX designer dans une démarche d'écoconception numérique."
icon: "palette"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

La majorité des impacts environnementaux d'un service numérique sont déterminés avant la moindre ligne de code — au moment où l'UX designer questionne le besoin, cadre le périmètre fonctionnel et fait les premiers choix d'interface. C'est l'étape où une simplification coûte le moins cher à mettre en œuvre.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.1](../../../rgesn/strategie/1-1_evaluation-utilite/) — Évaluation de l'utilité | Prioritaire | Questionner l'utilité réelle du service et de chaque fonctionnalité avant de concevoir une solution. |
| [1.2](../../../rgesn/strategie/1-2_cibles-utilisatrices/) — Cibles utilisatrices | Prioritaire | Définir les cibles utilisatrices, leurs besoins réels et les équipements qu'elles utilisent réellement. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/) — Terminaux d'affichage | Prioritaire | Concevoir mobile first, avec une interface responsive plutôt qu'une déclinaison par terminal. |
| [2.9](../../../rgesn/specifications/2-9_composants-interface/) — Composants d'interface prêts à l'emploi | Modéré | Choisir ou concevoir un système de design léger, et n'en utiliser que les composants nécessaires. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/) — Désactivation de la lecture automatique | Prioritaire | Désactiver la lecture automatique des vidéos, sons et animations. |
| [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/) — Absence de défilement infini | Prioritaire | Remplacer le défilement infini par une pagination ou un bouton « voir plus ». |
| [4.3](../../../rgesn/ux-ui/4-3_parcours-navigation/) — Optimisation du parcours de navigation | Recommandé | Raccourcir le parcours de chaque fonctionnalité principale, d'après des tests utilisateurs. |
| [4.4](../../../rgesn/ux-ui/4-4_activation-service-tiers/) — Décision de l'utilisateur sur l'activation d'un service tiers | Recommandé | Ne charger un service tiers (vidéo, carte, réseau social…) qu'après une action de l'utilisateur. |
| [4.6](../../../rgesn/ux-ui/4-6_contenu-porteur-information/) — Contenu vidéo, audio et animé porteur d'information | Recommandé | Ne garder que les vidéos, sons et animations qui portent une information. |
| [4.7](../../../rgesn/ux-ui/4-7_choix-sobre-format/) — Choix du format le plus sobre | Modéré | Choisir le format le plus sobre qui répond au besoin : texte plutôt qu'image, image plutôt que vidéo. |
| [4.10](../../../rgesn/ux-ui/4-10_format-saisie/) — Information sur le format de saisie attendu | Modéré | Indiquer le format de saisie attendu, et contrôler le formulaire dans le navigateur avant de l'envoyer. |
| [4.11](../../../rgesn/ux-ui/4-11_poids-formats-fichiers/) — Information sur les poids et formats de fichier attendus | Modéré | Indiquer le poids et les formats de fichier acceptés avant le transfert, et les vérifier dans le navigateur. |
| [4.12](../../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) — Information sur les fonctionnalités à fort impact environnemental | Recommandé | Signaler à l'utilisateur, avant usage, les fonctionnalités à fort impact environnemental. |
| [4.13](../../../rgesn/ux-ui/4-13_notifications/) — Limitation des notifications | Prioritaire | Limiter les notifications au nécessaire, et laisser l'utilisateur les désactiver. |
| [4.14](../../../rgesn/ux-ui/4-14_dark-patterns/) — Absence de procédés manipulatoires (dark patterns) | Recommandé | Supprimer les procédés manipulatoires qui poussent à consommer plus : lecture enchaînée, relances, faux comptes à rebours. |
| [4.15](../../../rgesn/ux-ui/4-15_controle-usages/) — Moyen de contrôle des usages et mode sobre | Recommandé | Donner à l'utilisateur un moyen de suivre et de réduire ses usages, par exemple un mode sobre. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | Recommandé | Fixer dès la maquette un budget de poids et de requêtes par écran. |
| [6.4](../../../rgesn/frontend/6-4_dimensions-images/) — Dimensions des images adaptées à l'affichage | Recommandé | Prévoir les dimensions d'affichage des images, pour qu'elles soient produites à la bonne taille. |
| [6.5](../../../rgesn/frontend/6-5_chargement-ressources/) — Chargement des seules ressources utiles | Recommandé | Concevoir des écrans qui n'affichent que l'utile, le reste à la demande. |
| [6.6](../../../rgesn/frontend/6-6_capteurs-terminaux/) — Usage des capteurs limité au besoin du service | Modéré | Ne demander l'accès aux capteurs qu'au moment où la fonctionnalité en a besoin. |

---

Voir la page [Outils > UX Designer](../../../outils/par-metier/ux-designer/) pour les outils concrets qui permettent d'outiller ces décisions dès la phase de conception.
