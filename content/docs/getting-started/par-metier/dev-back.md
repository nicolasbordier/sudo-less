---
weight: 200
title: "Dev Back"
description: "Le rôle et les actions concrètes d'un développeur back-end dans une démarche d'écoconception numérique."
icon: "dns"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur back-end arbitre les choix qui déterminent le volume de données échangées et stockées, le dimensionnement des ressources serveur et le niveau de chiffrement appliqué — des choix coûteux à revenir une fois le service en production.

| Critère | Phase | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Toutes les phases | Intégrer la réduction d'impact environnemental comme critère de revue de code. |
| [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) — Collecte de données | Conception | Ne collecter que les données strictement nécessaires au fonctionnement du service. |
| [1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/) — Niveau de chiffrement | Conception | Dimensionner le chiffrement (taille de clés, algorithmes) au juste niveau de sécurité requis, ni sous- ni sur-dimensionné. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard | Conception | Préférer des technologies standard et interopérables aux solutions propriétaires. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit | Conception | Limiter les flux échangés (compression, pagination, cache) plutôt que de reporter l'effort sur le seul frontend. |

---

Voir la page [Outils > Dev Back](../../../outils/par-metier/dev-back/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
