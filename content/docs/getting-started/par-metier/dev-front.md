---
weight: 100
title: "Dev Front"
description: "Le rôle et les actions concrètes d'un développeur front-end dans une démarche d'écoconception numérique."
icon: "code"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le développeur front-end traduit en code les choix de conception — c'est à ce niveau que se jouent la plupart des critères de compatibilité (anciens terminaux, anciennes versions de navigateurs, connexions dégradées) et le poids réel envoyé au terminal de l'utilisateur.

Les critères sont classés par famille du RGESN. Commencez par les critères **prioritaires** : ce sont ceux que le référentiel pondère le plus dans le [score d'avancement](../../../declaration/).

## 1. Stratégie

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | Prioritaire | Intégrer la réduction d'impact environnemental comme critère de revue de code, au même titre que la qualité ou la sécurité. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard et interopérables | Prioritaire | Préférer des technologies web standard et interopérables à des solutions propriétaires ou spécifiques à un environnement fermé. |

## 2. Spécifications

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | Prioritaire | Tester les fonctionnalités critiques sur un ordinateur équipé d'un processeur mis sur le marché il y a 10 ans ou plus. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | Recommandé | Réduire le poids transféré et le nombre de requêtes ; tester avec un débit limité à 512 kbit/s et en 3G. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | Prioritaire | Déclarer une plage de compatibilité explicite (Browserslist) et la faire respecter en CI. |
| [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/) — Terminaux d'affichage | Prioritaire | Implémenter un responsive design mobile first plutôt que de dupliquer l'interface par terminal. |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | Recommandé | Ajouter l'impact environnemental aux critères de revue de code : poids ajouté, requêtes, dépendances. |
| [2.9](../../../rgesn/specifications/2-9_composants-interface/) — Composants d'interface prêts à l'emploi | Modéré | N'importer que les composants utilisés de la bibliothèque d'interface, et retirer le CSS et le JavaScript inutilisés. |

## 4. UX/UI

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/) — Désactivation de la lecture automatique | Prioritaire | Désactiver la lecture automatique des vidéos, sons et animations. |
| [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/) — Absence de défilement infini | Prioritaire | Remplacer le défilement infini par une pagination ou un bouton « voir plus ». |
| [4.4](../../../rgesn/ux-ui/4-4_activation-service-tiers/) — Décision de l'utilisateur sur l'activation d'un service tiers | Recommandé | Remplacer les intégrations tierces (vidéo, carte, réseau social) par une façade, chargée au clic. |
| [4.5](../../../rgesn/ux-ui/4-5_composants-natifs/) — Composants fonctionnels natifs | Modéré | Préférer les composants natifs du navigateur, du système ou du langage aux bibliothèques ajoutées. |
| [4.8](../../../rgesn/ux-ui/4-8_polices-caracteres/) — Limitation des polices de caractères téléchargées | Modéré | Limiter le nombre de polices téléchargées, ou utiliser les polices du système. |
| [4.9](../../../rgesn/ux-ui/4-9_requetes-saisie-utilisateur/) — Limitation des requêtes serveur lors de la saisie utilisateur | Modéré | Retarder les requêtes d'autocomplétion (délai, nombre minimal de caractères) et mettre leurs réponses en cache. |
| [4.10](../../../rgesn/ux-ui/4-10_format-saisie/) — Information sur le format de saisie attendu | Modéré | Indiquer le format attendu et valider le formulaire dans le navigateur (attributs HTML) avant l'envoi. |
| [4.11](../../../rgesn/ux-ui/4-11_poids-formats-fichiers/) — Information sur les poids et formats de fichier attendus | Modéré | Afficher le poids et les formats acceptés, et vérifier le fichier dans le navigateur avant le transfert. |
| [4.12](../../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) — Information sur les fonctionnalités à fort impact environnemental | Recommandé | Signaler à l'utilisateur, avant usage, les fonctionnalités à fort impact environnemental. |
| [4.13](../../../rgesn/ux-ui/4-13_notifications/) — Limitation des notifications | Prioritaire | Limiter les notifications au nécessaire, et laisser l'utilisateur les désactiver. |
| [4.15](../../../rgesn/ux-ui/4-15_controle-usages/) — Moyen de contrôle des usages et mode sobre | Recommandé | Donner à l'utilisateur un moyen de suivre et de réduire ses usages, par exemple un mode sobre. |

## 5. Contenus

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [5.1](../../../rgesn/contenus/5-1_format-images/) — Format de fichier adapté à chaque image | Recommandé | Choisir pour chaque image le format adapté : SVG pour les illustrations vectorielles, AVIF ou WebP pour les photos. |
| [5.2](../../../rgesn/contenus/5-2_compression-images/) — Niveau de compression adapté à chaque image | Recommandé | Régler la compression de chaque image selon son contenu et son contexte d'affichage. |
| [5.3](../../../rgesn/contenus/5-3_definition-videos/) — Définition vidéo adaptée au contenu et au terminal | Prioritaire | Proposer chaque vidéo en plusieurs définitions, et laisser le lecteur choisir selon l'écran et la connexion. |
| [5.5](../../../rgesn/contenus/5-5_ecoute-seule/) — Mode « écoute seule » pour les vidéos | Prioritaire | Proposer dans le lecteur un mode « écoute seule » qui ne télécharge que la piste son. |

## 6. Frontend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | Recommandé | Fixer un budget de poids et de requêtes par écran, et le vérifier dans l'intégration continue. |
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | Recommandé | Configurer la mise en cache des ressources : en-têtes Cache-Control, noms de fichiers versionnés. |
| [6.3](../../../rgesn/frontend/6-3_compression-ressources/) — Compression des ressources transférées | Modéré | Vérifier que les ressources texte sont servies compressées (gzip, Brotli). |
| [6.4](../../../rgesn/frontend/6-4_dimensions-images/) — Dimensions des images adaptées à l'affichage | Recommandé | Servir les images aux dimensions de leur affichage, avec les attributs srcset et sizes. |
| [6.5](../../../rgesn/frontend/6-5_chargement-ressources/) — Chargement des seules ressources utiles | Recommandé | Charger à la demande les images, scripts et contenus hors écran ou propres à une interaction. |
| [6.6](../../../rgesn/frontend/6-6_capteurs-terminaux/) — Usage des capteurs limité au besoin du service | Modéré | Ne solliciter les capteurs (géolocalisation, caméra, accéléromètre…) qu'au moment et à la fréquence où le service en a besoin. |
| [6.7](../../../rgesn/frontend/6-7_domaine-unique/) — Ressources statiques sur un même domaine | Modéré | Héberger polices, scripts et styles sur le domaine du service plutôt que sur des CDN tiers. |

## 7. Backend

| Critère | Priorité | Ce qu'il y a à faire |
|---|---|---|
| [7.3](../../../rgesn/backend/7-3_traitement-arriere-plan/) — Information sur un traitement en cours | Modéré | Afficher l'état d'un traitement en cours, pour que l'utilisateur ne relance pas sa demande. |

---

Voir la page [Outils > Dev Front](../../../outils/par-metier/dev-front/) pour les outils concrets qui permettent de mesurer et vérifier chacun de ces points.
