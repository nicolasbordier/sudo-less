---
weight: 200
title: "Conception"
description: "Les critères RGESN à appliquer lors de la phase de conception d'un projet numérique."
icon: "design_services"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

---

Lors de la phase de **conception** du cycle de vie d'un projet, il est possible de mettre en place ces recommandations :

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) — Collecte de données | `Data Scientist` `Responsable Juridique` | Ne collecter que les données strictement nécessaires au fonctionnement du service. |
| [1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/) — Niveau de chiffrement | `Expert en sécurité informatique` `Responsable de la protection des données` | Dimensionner le chiffrement au juste niveau de sécurité requis, ni sous- ni sur-dimensionné. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard | `Responsable IT` `Développeur` | Préférer des technologies standard et interopérables aux solutions propriétaires ou fermées. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | `Responsable IT` `Développeur` `Architecte Système` | Concevoir des API documentées et ouvertes pour tout matériel piloté par le service. |
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Prévoir la compatibilité avec un terminal réel mis sur le marché il y a 7 à 10 ans. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Réduire le poids transféré et prévoir un mode dégradé ou hors ligne sous connexion limitée. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Maintenir la compatibilité avec des versions d'OS et de navigateurs vieilles de 2 à 5 ans. |
| [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/) — Terminaux d'affichage | `Développeur` `Responsable IT` `UX Designer` | Implémenter un responsive design mobile first plutôt que de dupliquer l'interface par terminal. |
| [1.3](../../../rgesn/strategie/1-3_referent-ecoconception/) — Référent écoconception | `Porteur de projet` `Responsable RSE/Numérique soutenable` | Vérifier que le référent écoconception est bien associé aux arbitrages techniques de cette phase. |
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | `Responsable RSE/Numérique soutenable` `Responsable IT` `Développeur` | Intégrer la réduction d'impact environnemental comme critère de revue de conception. |
| [1.8](../../../rgesn/strategie/1-8_efforts-open-source/) — Efforts d'open source | `Porteur de projet` `Responsable Développement` `Responsable Juridique` | Choisir une licence open source adaptée avant que le code ne soit déjà écrit. |

---

Voir la page [Outils > Conception](../../../outils/par-phase-projet/conception/) pour les outils concrets utilisables à ce stade.
