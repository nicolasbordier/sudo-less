---
weight: 100
title: "Dev Front"
description: "Le rôle et les actions concrètes d'un développeur front-end dans une démarche d'écoconception numérique."
icon: "code"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur front-end traduit en code les choix de conception — c'est à ce niveau que se jouent la plupart des critères de compatibilité (anciens terminaux, anciennes versions de navigateurs, connexions dégradées) et le poids réel envoyé au terminal de l'utilisateur.

| Critère | Phase | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Toutes les phases | Intégrer la réduction d'impact environnemental comme critère de revue de code, au même titre que la qualité ou la sécurité. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard | Conception | Préférer des technologies web standard et interopérables à des solutions propriétaires ou spécifiques à un environnement fermé. |
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | Conception | Tester les fonctionnalités critiques sur un terminal réel mis sur le marché il y a 10 ans ou plus (navigateur web). |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit | Conception | Réduire le poids transféré et le nombre de requêtes ; tester sous throttling 3G/512 Kbit/s. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions de navigateurs | Conception | Déclarer une plage de compatibilité explicite (Browserslist) et la faire respecter en CI. |
| [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/) — Terminaux d'affichage | Conception | Implémenter un responsive design mobile first plutôt que de dupliquer l'interface par terminal. |

---

Voir la page [Outils > Dev Front](../../../outils/par-metier/dev-front/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
