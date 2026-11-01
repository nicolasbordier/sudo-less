---
weight: 300
title: "Implémentation"
description: "Les critères RGESN à appliquer lors de la phase d'implémentation d'un projet numérique."
icon: "code_blocks"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le RGESN ne rattache aucun critère à la phase d'**implémentation** : il classe presque tous ses critères en conception, où ils se décident. Beaucoup se mettent pourtant en œuvre et se vérifient au fil du développement. Cette page les regroupe, avec ce qu'il y a à faire à ce stade ; la phase officielle de chaque critère reste indiquée dans sa fiche.

## 1. Stratégie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [1.3](../../../rgesn/strategie/1-3_referent-ecoconception/) — Référent écoconception | `Porteur de projet` `Responsable RSE/Numérique soutenable` | S'assurer que le référent écoconception reste associé aux choix d'implémentation, pas seulement au cadrage initial. |
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | `Responsable RSE/Numérique soutenable` `Responsable IT` `Développeur` | Intégrer la réduction d'impact environnemental comme critère de revue de code, au fil de l'eau. |
| [1.8](../../../rgesn/strategie/1-8_efforts-open-source/) — Efforts d'open source | `Porteur de projet` `Responsable Développement` `Responsable Juridique` | Publier le code au fil du développement plutôt qu'en une seule fois à la fin. |

## 2. Spécifications

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Tester les fonctionnalités critiques sur un terminal ancien avant chaque version importante. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Tester chaque version en 3G et à 512 kbit/s, avec la limitation de débit du navigateur ou de l'émulateur. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Faire respecter la plage de navigateurs et d'OS visée dans l'intégration continue (par exemple avec Browserslist). |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | `Architecte Logiciel` `Développeur` `Responsable RSE/Numérique soutenable` | Faire de l'impact environnemental un critère de chaque revue de code. |
| [2.9](../../../rgesn/specifications/2-9_composants-interface/) — Composants d'interface prêts à l'emploi | `Designer` `Développeur` `Responsable IT` | N'importer que les composants utilisés, et retirer le CSS et le JavaScript inutilisés. |

## 4. UX/UI

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/) — Désactivation de la lecture automatique | `Développeur` `Concepteur UX / UI` `Responsable Qualité` | Désactiver la lecture automatique des vidéos, sons et animations. |
| [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/) — Absence de défilement infini | `Développeur` `Designer` `Concepteur UX / UI` | Remplacer le défilement infini par une pagination ou un bouton « voir plus ». |
| [4.4](../../../rgesn/ux-ui/4-4_activation-service-tiers/) — Décision de l'utilisateur sur l'activation d'un service tiers | `Développeur` `Responsable Qualité` `Responsable de la protection des données` | Remplacer les intégrations tierces (vidéo, carte, réseau social) par une façade, chargée au clic. |
| [4.5](../../../rgesn/ux-ui/4-5_composants-natifs/) — Composants fonctionnels natifs | `Développeur` `Architecte Logiciel` | Préférer les composants natifs du navigateur, du système ou du langage aux bibliothèques ajoutées. |
| [4.8](../../../rgesn/ux-ui/4-8_polices-caracteres/) — Limitation des polices de caractères téléchargées | `Développeur` `Architecte Logiciel` | Limiter le nombre de polices téléchargées, ou utiliser les polices du système. |
| [4.9](../../../rgesn/ux-ui/4-9_requetes-saisie-utilisateur/) — Limitation des requêtes serveur lors de la saisie utilisateur | `Développeur` `Architecte Logiciel` | Retarder les requêtes d'autocomplétion (délai, nombre minimal de caractères) et mettre leurs réponses en cache. |
| [4.10](../../../rgesn/ux-ui/4-10_format-saisie/) — Information sur le format de saisie attendu | `Concepteur UX / UI` `Développeur` | Valider les formulaires dans le navigateur (attributs HTML) avant l'envoi. |
| [4.11](../../../rgesn/ux-ui/4-11_poids-formats-fichiers/) — Information sur les poids et formats de fichier attendus | `Concepteur UX / UI` `Développeur` `Architecte Logiciel` | Vérifier le poids et le format des fichiers dans le navigateur avant le transfert. |
| [4.13](../../../rgesn/ux-ui/4-13_notifications/) — Limitation des notifications | `Concepteur UX / UI` `Développeur` | Limiter les notifications au nécessaire, et laisser l'utilisateur les désactiver. |

## 5. Contenus

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [5.1](../../../rgesn/contenus/5-1_format-images/) — Format de fichier adapté à chaque image | `Développeur` `Architecte Logiciel` | Convertir chaque image dans le format adapté, de préférence automatiquement à la publication. |
| [5.2](../../../rgesn/contenus/5-2_compression-images/) — Niveau de compression adapté à chaque image | `Développeur` `Architecte Logiciel` | Régler la compression de chaque image, et l'automatiser dans la chaîne de publication. |
| [5.3](../../../rgesn/contenus/5-3_definition-videos/) — Définition vidéo adaptée au contenu et au terminal | `Développeur` `Architecte Logiciel` `Porteur de projet` | Produire chaque vidéo dans les définitions utiles, pas au-delà de ce que le contenu demande. |
| [5.4](../../../rgesn/contenus/5-4_compression-videos/) — Mode de compression des vidéos efficace et adapté | `Développeur` `Architecte Logiciel` | Encoder les vidéos avec un codec efficace (AV1, VP9 ou HEVC) et un débit adapté au contenu. |
| [5.6](../../../rgesn/contenus/5-6_compression-audio/) — Compression des contenus audio adaptée | `Développeur` `Responsable IT` | Compresser les contenus audio selon leur nature : parole ou musique. |
| [5.7](../../../rgesn/contenus/5-7_format-documents/) — Format de fichier adapté à chaque document | `Développeur` `Responsable IT` | Compresser les documents à la source, sans perdre leur accessibilité. |

## 6. Frontend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | `Développeur` `Concepteur UX / UI` `Responsable Produit` | Vérifier le budget de poids et de requêtes de chaque écran dans l'intégration continue. |
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | `Administrateur Système` `Développeur` `Architecte Logiciel` | Configurer la mise en cache des ressources : en-têtes Cache-Control, noms de fichiers versionnés. |
| [6.3](../../../rgesn/frontend/6-3_compression-ressources/) — Compression des ressources transférées | `Développeur` `Administrateur Système` `Architecte Logiciel` | Vérifier que les ressources texte sont servies compressées (gzip, Brotli). |
| [6.4](../../../rgesn/frontend/6-4_dimensions-images/) — Dimensions des images adaptées à l'affichage | `Développeur` `Concepteur UX / UI` | Servir les images aux dimensions de leur affichage, avec les attributs srcset et sizes. |
| [6.5](../../../rgesn/frontend/6-5_chargement-ressources/) — Chargement des seules ressources utiles | `Développeur` `Concepteur UX / UI` | Charger à la demande les images, scripts et contenus hors écran ou propres à une interaction. |
| [6.6](../../../rgesn/frontend/6-6_capteurs-terminaux/) — Usage des capteurs limité au besoin du service | `Développeur` `Concepteur UX / UI` | Ne solliciter les capteurs (géolocalisation, caméra, accéléromètre…) qu'au moment et à la fréquence où le service en a besoin. |
| [6.7](../../../rgesn/frontend/6-7_domaine-unique/) — Ressources statiques sur un même domaine | `Administrateur Système` `Développeur` `Architecte Logiciel` | Héberger polices, scripts et styles sur le domaine du service plutôt que sur des CDN tiers. |

## 7. Backend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [7.1](../../../rgesn/backend/7-1_cache-serveur/) — Cache serveur pour les données les plus utilisées | `Administrateur Système` `Développeur` `Architecte Logiciel` | Mettre en cache côté serveur les données les plus demandées. |
| [7.3](../../../rgesn/backend/7-3_traitement-arriere-plan/) — Information sur un traitement en cours | `Développeur` `Responsable Produit` | Afficher l'état des traitements longs, pour que l'utilisateur ne relance pas sa demande. |

## 9. Algorithmie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | `Porteur de projet` `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Limiter la quantité d'entraînement, en partant si possible d'un modèle pré-entraîné. |
| [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) — Données d'apprentissage limitées au nécessaire | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` `Responsable de la protection des données` `Développeur` | Limiter les données d'entraînement au strict nécessaire. |
| [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) — Compression des modèles | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Compresser les modèles : quantification, élagage, distillation. |

---

Voir la page [Outils > Implémentation](../../../outils/par-phase-projet/implementation/) pour les outils concrets déjà documentés à ce stade (mesure d'impact au fil de l'eau, budgets de performance en CI).
