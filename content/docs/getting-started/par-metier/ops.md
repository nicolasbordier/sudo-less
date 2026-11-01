---
weight: 600
title: "OPS"
description: "Le rôle et les actions concrètes d'un OPS dans une démarche d'écoconception numérique."
icon: "monitoring"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

L'OPS surveille le service une fois en production — c'est la seule phase où l'on observe la consommation réelle plutôt qu'une estimation, et où un dimensionnement excessif ou obsolète peut être corrigé sans attendre la prochaine version.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Prioritaire | Mettre en place une revue régulière plutôt qu'un audit ponctuel isolé, avec un suivi d'indicateurs dans le temps. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.7](../../../rgesn/specifications/2-7_maintenance-decommissionnement/) — Maintenance et décommissionnement | Prioritaire | Tenir l'inventaire des composants et des environnements, et retirer ce qui ne sert plus. |

## 3. Architecture

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | Recommandé | Ajuster les ressources à la charge réelle : mise à l'échelle automatique, extinction hors usage. |
| [3.3](../../../rgesn/architecture/3-3_evolution-protocoles/) — Évolution technique des protocoles | Modéré | Maintenir les protocoles à jour côté serveur : TLS 1.3, HTTP/2 ou HTTP/3, IPv6. |
| [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/) — Optimisation des environnements de développement, préproduction et test | Modéré | Dimensionner les environnements de développement, de préproduction et de test au besoin, et les éteindre quand ils ne servent pas. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | Recommandé | Configurer les en-têtes de cache du serveur ou du CDN. |
| [6.3](../../../rgesn/frontend/6-3_compression-ressources/) — Compression des ressources transférées | Modéré | Activer la compression gzip ou Brotli sur le serveur. |
| [6.7](../../../rgesn/frontend/6-7_domaine-unique/) — Ressources statiques sur un même domaine | Modéré | Servir les ressources statiques depuis le domaine du service plutôt que depuis plusieurs domaines tiers. |

## 7. Backend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [7.1](../../../rgesn/backend/7-1_cache-serveur/) — Cache serveur pour les données les plus utilisées | Recommandé | Mettre en place le cache serveur (proxy inverse, cache applicatif) des données les plus demandées. |
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | Recommandé | Appliquer les durées de conservation, y compris aux journaux et aux sauvegardes. |

## 8. Hébergement

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [8.1](../../../rgesn/hebergement/8-1_demarche-hebergeur/) — Hébergeur engagé dans la réduction de son empreinte | Prioritaire | Choisir un hébergeur qui publie ses indicateurs environnementaux et s'engage à les réduire. |
| [8.2](../../../rgesn/hebergement/8-2_gestion-equipements/) — Gestion durable des équipements de l'hébergeur | Prioritaire | Vérifier que l'hébergeur a une politique de gestion durable de ses équipements : durée de vie, réemploi, fin de vie. |
| [8.3](../../../rgesn/hebergement/8-3_pue/) — PUE de l'hébergement | Prioritaire | Choisir un hébergement dont le PUE réel est inférieur à 1,5. |
| [8.4](../../../rgesn/hebergement/8-4_wue/) — WUE de l'hébergement | Recommandé | Choisir un hébergement qui suit et réduit sa consommation d'eau (WUE, objectif de 0,4 L/kWh). |
| [8.5](../../../rgesn/hebergement/8-5_electricite-renouvelable/) — Électricité d'origine renouvelable | Recommandé | Vérifier que l'électricité de l'hébergeur est documentée et majoritairement renouvelable, avec ses justificatifs. |
| [8.6](../../../rgesn/hebergement/8-6_localisation/) — Localisation de l'hébergement | Recommandé | Héberger le service dans un pays dont l'électricité émet moins de 100 g CO2e/kWh, cohérent avec la localisation de ses utilisateurs. |
| [8.7](../../../rgesn/hebergement/8-7_chaleur-fatale/) — Traitement de la chaleur produite par les serveurs | Recommandé | Préférer un hébergeur qui récupère la chaleur de ses serveurs, ou dont le PUE réel est inférieur à 1,3. |
| [8.8](../../../rgesn/hebergement/8-8_donnees-chaudes-froides/) — Données chaudes et froides hébergées séparément | Modéré | Au-delà de 10 To, séparer les données courantes des archives et sauvegardes, sur un stockage froid. |
| [8.9](../../../rgesn/hebergement/8-9_duplication-donnees/) — Duplication des données selon le besoin | Recommandé | Ne dupliquer les données que selon un niveau de service (SLA) ajusté au besoin. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | Recommandé | Décaler les calculs et transferts asynchrones aux heures où l'électricité est la moins carbonée et les réseaux les moins chargés. |

---

Voir la page [Outils > OPS](../../../outils/par-metier/ops/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
