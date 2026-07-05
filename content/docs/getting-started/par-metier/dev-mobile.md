---
weight: 300
title: "Dev Mobile"
description: "Le rôle et les actions concrètes d'un développeur mobile dans une démarche d'écoconception numérique."
icon: "smartphone"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur mobile est directement responsable de la durée de vie utile des smartphones et tablettes visés par le service : compatibilité avec les anciennes versions d'OS, gestion de la batterie, et mode hors ligne pour ne pas rendre l'application inutilisable en cas de connexion dégradée.

| Critère | Phase | Ce qu'il y a à faire |
|---|---|---|
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard | Conception | Évaluer une PWA (plus légère et rétro-compatible) avant de choisir une application native. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | Conception | Documenter et ouvrir les API du matériel piloté, pour permettre sa réutilisation au-delà de la fin de vie du service. |
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | Conception | Tester les fonctionnalités critiques sur un smartphone réel mis sur le marché il y a 7 ans ou plus. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit | Conception | Prévoir un mode hors ligne (stockage local, file d'attente de synchronisation) sur les fonctionnalités qui le permettent. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS | Conception | Maintenir la compatibilité avec des versions d'OS mobile vieilles de 5 ans. |

---

Voir la page [Outils > Dev Mobile](../../../outils/par-metier/dev-mobile/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
