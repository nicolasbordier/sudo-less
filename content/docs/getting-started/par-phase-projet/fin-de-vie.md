---
weight: 500
title: "Fin de vie"
description: "Les critères RGESN à appliquer lors de la fin de vie d'un projet numérique."
icon: "recycling"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le RGESN ne rattache qu'un critère à la **fin de vie** d'un service, le 2.7. D'autres critères, décidés en conception, trouvent ici leur aboutissement :

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [1.8](../../../rgesn/strategie/1-8_efforts-open-source/) — Efforts d'open source | `Porteur de projet` `Responsable Développement` `Responsable Juridique` | Publier le code sous licence libre avant l'arrêt, pour qu'une communauté puisse reprendre le service. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | `Responsable IT` `Développeur` `Architecte Système` | Documenter et ouvrir les API du matériel piloté **avant** la fin de vie du service, pour donner une chance réelle à une communauté ou une structure de réemploi de prendre le relais. |
| [2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/) — Maintenance et décommissionnement | `Responsable IT` `Architecte Logiciel` | Appliquer la stratégie de décommissionnement prévue : arrêt du service, devenir des données et des équipements. |
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | `Porteur de projet` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Assurer les correctifs jusqu'à la fin de vie annoncée, et prévenir les utilisateurs à l'avance. |
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | `Architecte Logiciel` `Data Scientist` `Responsable de la sécurité informatique` `Responsable Juridique` | Archiver ce qui doit l'être, et supprimer le reste des contenus. |
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | `Administrateur Système` `Développeur` `Responsable Produit` `Architecte Logiciel` | Supprimer les données, sauvegardes comprises, ou les archiver selon leurs durées de conservation. |
| [8.9](../../../rgesn/hebergement/8-9_duplication-donnees/) — Duplication des données selon le besoin | `Responsable de l'hébergement` `Ingénieur en stockage de données` `Responsable de la sécurité informatique` `Architecte/Ingénieur Systèmes` | Supprimer les copies et les sauvegardes devenues inutiles. |

---

Voir la page [Outils > Fin de vie](../../../outils/par-phase-projet/fin-de-vie/) pour les outils et pratiques déjà documentés sur ce site (réseau Ordi3.0, OS mobile open source, guide des licences libres...).
