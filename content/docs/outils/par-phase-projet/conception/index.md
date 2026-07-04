---
weight: 200
title: "Conception"
description: "Tableau récapitulatif des outils spécifiques à la phase de conception : minimisation des données, dimensionnement du chiffrement, choix de technologies standard et ouverture des API matérielles."
icon: "design_services"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

La phase de **conception** est celle où se prennent les choix techniques structurants qui ne relèvent plus d'une décision « poursuivre ou arrêter » ([phase d'exploration](../exploration/)), mais qui restent réversibles avant l'écriture du code : quelles données collecter ([critère 1.6](../../../rgesn/strategie/1-6_collecte-donnees/)), quel niveau de chiffrement ([critère 1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/)), quelles technologies standard ([critère 1.9](../../../rgesn/strategie/1-9_technologies-standard/)) et quelles API matérielles ouvrir ([critère 1.10](../../../rgesn/strategie/1-10_api-materiel/)). Voir aussi les pages [Architecte](../../par-metier/architecte/) et [Dev Back](../../par-metier/dev-back/) pour une vue par métier.

| Outil / Référentiel | Critère RGESN | Rôle typique | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|---|
| [Guide ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) | 1.7 | Architecte | Dimensionne un chiffrement adapté au besoin réel (taille de clé, durée de protection) plutôt que systématiquement maximal | Oui |
| [RWEB 0023](https://rweb.greenit.fr/fr/fiches/RWEB_0023-reduire-le-volume-de-donnees-stockees-au-strict-necessaire) (Collectif GreenIT) | 1.6 | Dev Back | Ne stocker que les données strictement nécessaires, avec archivage à froid et suppression des doublons | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=backend&num_reco=1) — Backend n°1 | 1.6 | Architecte | Vérifie l'utilité réelle des données collectées et leur cycle de vie (dates de suppression, données obsolètes) | Oui |
| [Baseline](https://web.dev/baseline) / Can I Use / MDN | 1.9 | Dev Front | Vérifie qu'une API web est standard et largement supportée avant de l'adopter | Oui |
| [GR491](https://gr491.isit-europe.org/?famille=frontend&num_reco=4) — Frontend n°4 | 1.9 | Architecte | Définit la plage de rétro-compatibilité visée et la disponibilité d'une version allégée pour anciens équipements | Oui |
| [Règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act) | 1.10 | Architecte / Juridique | Impose depuis 2025 des API ouvertes et documentées pour les données générées par un objet connecté | Oui (référentiel) |
| [Tasmota](https://tasmota.github.io/docs/) / Home Assistant | 1.10 | Dev Back | Reprend la main sur un objet connecté dont l'API reste fermée, via un firmware libre | Oui |
| [Cahier IP n°9](https://linc.cnil.fr/cahier-ip9-donnees-empreinte-et-libertes) (CNIL) | 1.6 | Responsable RSE | Documente les tensions entre obligations de chiffrement/protection des données et sobriété numérique | Oui |

---

Contrairement à la phase d'exploration où les outils sont surtout des grilles de questionnement, cette phase mobilise des **référentiels techniques précis** (ANSSI, GR491, Data Act) qui engagent des choix coûteux à revenir en arrière une fois le développement lancé — dimensionnement cryptographique, schéma de données, choix web vs natif. C'est pourquoi le critère 1.9 recommande d'évaluer ces choix « bien en amont du développement », et non au moment de le livrer.
