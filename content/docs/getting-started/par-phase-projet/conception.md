---
weight: 200
title: "Conception"
description: "Les critères RGESN à appliquer lors de la phase de conception d'un projet numérique."
icon: "design_services"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

Le RGESN rattache 69 de ses 78 critères à la phase de **conception** : c'est là que se décident l'architecture, l'interface, les contenus et l'hébergement. Ils sont regroupés ci-dessous par famille. Les critères 1.3, 1.4 et 1.8 valent pour toutes les phases. Beaucoup se mettent ensuite en œuvre pendant l'[implémentation](../implementation/) et se vérifient pendant le [run](../run/).

## 1. Stratégie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [1.3](../../../rgesn/strategie/1-3_referent-ecoconception/) — Référent écoconception | `Porteur de projet` `Responsable RSE/Numérique soutenable` | Vérifier que le référent écoconception est bien associé aux arbitrages techniques de cette phase. |
| [1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) — Revue d'écoconception | `Responsable RSE/Numérique soutenable` `Responsable IT` `Développeur` | Intégrer la réduction d'impact environnemental comme critère de revue de conception. |
| [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) — Collecte de données | `Data Scientist` `Responsable Juridique` | Ne collecter que les données strictement nécessaires au fonctionnement du service. |
| [1.7](../../../rgesn/strategie/1-7_niveau-chiffrement/) — Niveau de chiffrement | `Expert en sécurité informatique` `Responsable de la protection des données` | Dimensionner le chiffrement au juste niveau de sécurité requis, ni sous- ni sur-dimensionné. |
| [1.8](../../../rgesn/strategie/1-8_efforts-open-source/) — Efforts d'open source | `Porteur de projet` `Responsable Développement` `Responsable Juridique` | Choisir une licence open source adaptée avant que le code ne soit déjà écrit. |
| [1.9](../../../rgesn/strategie/1-9_technologies-standard/) — Technologies standard et interopérables | `Responsable IT` `Développeur` | Préférer des technologies standard et interopérables aux solutions propriétaires ou fermées. |
| [1.10](../../../rgesn/strategie/1-10_api-materiel/) — API ouvertes pour le matériel | `Responsable IT` `Développeur` `Architecte Système` | Concevoir des API documentées et ouvertes pour tout matériel piloté par le service. |

## 2. Spécifications

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [2.2](../../../rgesn/specifications/2-2_anciens-terminaux/) — Anciens modèles de terminaux | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Tester les fonctionnalités critiques sur un terminal ancien : 7 ans pour un smartphone, un processeur de 10 ans pour un ordinateur. |
| [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) — Connexion bas débit ou hors connexion | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Tester le service en 3G et à 512 kbit/s, et prévoir un mode hors ligne quand c'est possible. |
| [2.4](../../../rgesn/specifications/2-4_anciennes-versions-os/) — Anciennes versions d'OS et de navigateurs | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` | Faire fonctionner les parcours critiques sur des navigateurs de 2 ans et des systèmes d'exploitation de 5 ans. |
| [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/) — Terminaux d'affichage | `Développeur` `Responsable IT` `Designer` | Implémenter un responsive design mobile first plutôt que de dupliquer l'interface par terminal. |
| [2.6](../../../rgesn/specifications/2-6_revue-conception-code/) — Revue de conception et de code | `Architecte Logiciel` `Développeur` `Responsable RSE/Numérique soutenable` | Inscrire la réduction des impacts de chaque fonctionnalité parmi les objectifs des revues de conception et de code. |
| [2.8](../../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) — Fournisseurs et impacts environnementaux | `Responsable Partenariats` `Responsable RSE/Numérique soutenable` `Porteur de projet` | Exiger des fournisseurs une démarche documentée de réduction de leurs impacts, dans les achats et les contrats. |
| [2.9](../../../rgesn/specifications/2-9_composants-interface/) — Composants d'interface prêts à l'emploi | `Designer` `Développeur` `Responsable IT` | Évaluer le poids des bibliothèques de composants d'interface, et n'en charger que les éléments utilisés. |
| [2.10](../../../rgesn/specifications/2-10_services-tiers/) — Impacts environnementaux des services tiers | `Responsable Partenariats` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Évaluer l'impact des services tiers (vidéo, carte, mesure d'audience…) avant de les intégrer, et vérifier leur démarche (critères 1.4 et 1.5). |

## 3. Architecture

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [3.1](../../../rgesn/architecture/3-1_architecture-composants/) — Architecture, ressources et composants écoconçus | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` | Choisir les frameworks et composants en comparant leur empreinte, et documenter ce choix dans la déclaration. |
| [3.2](../../../rgesn/architecture/3-2_architecture-elastique/) — Architecture élastique et adaptation des ressources | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` | Adapter automatiquement les ressources à la charge réelle : mise à l'échelle, extinction hors usage. |
| [3.3](../../../rgesn/architecture/3-3_evolution-protocoles/) — Évolution technique des protocoles | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` | Supporter les protocoles récents (HTTPS avec TLS 1.3, HTTP/2 ou HTTP/3, IPv6) et pouvoir en changer sans refonte. |
| [3.4](../../../rgesn/architecture/3-4_mises-a-jour-correctives/) — Mises à jour correctives des équipements | `Porteur de projet` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Garantir des mises à jour correctives pendant toute la durée de vie prévue des équipements et logiciels liés au service. |
| [3.5](../../../rgesn/architecture/3-5_dissociation-mises-a-jour/) — Dissociation des mises à jour correctives et évolutives | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` | Livrer les correctifs séparément des évolutions, pour qu'un utilisateur puisse sécuriser son terminal sans l'alourdir. |
| [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) — Mises à jour incrémentielles | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` `Responsable RSE/Numérique soutenable` | Distribuer des mises à jour incrémentielles plutôt que de remplacer tout le code à chaque version. |
| [3.7](../../../rgesn/architecture/3-7_environnements-developpement-test/) — Optimisation des environnements de développement, préproduction et test | `Architecte Système` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Dimensionner les environnements de développement, de préproduction et de test au besoin, et les éteindre quand ils ne servent pas. |

## 4. UX/UI

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/) — Désactivation de la lecture automatique | `Développeur` `Concepteur UX / UI` `Responsable Qualité` | Désactiver la lecture automatique des vidéos, sons et animations. |
| [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/) — Absence de défilement infini | `Développeur` `Designer` `Concepteur UX / UI` | Remplacer le défilement infini par une pagination ou un bouton « voir plus ». |
| [4.3](../../../rgesn/ux-ui/4-3_parcours-navigation/) — Optimisation du parcours de navigation | `Développeur` `Concepteur UX / UI` `Responsable Qualité` | Raccourcir le parcours de chaque fonctionnalité principale, d'après des tests utilisateurs et des statistiques d'usage. |
| [4.4](../../../rgesn/ux-ui/4-4_activation-service-tiers/) — Décision de l'utilisateur sur l'activation d'un service tiers | `Développeur` `Responsable Qualité` `Responsable de la protection des données` | Ne charger un service tiers (vidéo, carte, réseau social…) qu'après une action de l'utilisateur. |
| [4.5](../../../rgesn/ux-ui/4-5_composants-natifs/) — Composants fonctionnels natifs | `Développeur` `Architecte Logiciel` | Préférer les composants natifs du navigateur, du système ou du langage aux bibliothèques ajoutées. |
| [4.6](../../../rgesn/ux-ui/4-6_contenu-porteur-information/) — Contenu vidéo, audio et animé porteur d'information | `Développeur` `Designer` | Ne garder que les vidéos, sons et animations qui portent une information. |
| [4.7](../../../rgesn/ux-ui/4-7_choix-sobre-format/) — Choix du format le plus sobre | `Développeur` `Designer` `Responsable Qualité` | Choisir le format le plus sobre qui répond au besoin : texte plutôt qu'image, image plutôt que vidéo. |
| [4.8](../../../rgesn/ux-ui/4-8_polices-caracteres/) — Limitation des polices de caractères téléchargées | `Développeur` `Architecte Logiciel` | Limiter le nombre de polices téléchargées, ou utiliser les polices du système. |
| [4.9](../../../rgesn/ux-ui/4-9_requetes-saisie-utilisateur/) — Limitation des requêtes serveur lors de la saisie utilisateur | `Développeur` `Architecte Logiciel` | Limiter les requêtes envoyées pendant la saisie (autocomplétion, vérification) : délai, nombre minimal de caractères. |
| [4.10](../../../rgesn/ux-ui/4-10_format-saisie/) — Information sur le format de saisie attendu | `Concepteur UX / UI` `Développeur` | Indiquer le format de saisie attendu, et contrôler le formulaire dans le navigateur avant de l'envoyer. |
| [4.11](../../../rgesn/ux-ui/4-11_poids-formats-fichiers/) — Information sur les poids et formats de fichier attendus | `Concepteur UX / UI` `Développeur` `Architecte Logiciel` | Indiquer le poids et les formats de fichier acceptés avant le transfert, et les vérifier dans le navigateur. |
| [4.12](../../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) — Information sur les fonctionnalités à fort impact environnemental | `Concepteur UX / UI` `Développeur` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Signaler à l'utilisateur, avant usage, les fonctionnalités à fort impact environnemental. |
| [4.13](../../../rgesn/ux-ui/4-13_notifications/) — Limitation des notifications | `Concepteur UX / UI` `Développeur` | Limiter les notifications au nécessaire, et laisser l'utilisateur les désactiver. |
| [4.14](../../../rgesn/ux-ui/4-14_dark-patterns/) — Absence de procédés manipulatoires (dark patterns) | `Concepteur UX / UI` `Développeur` `Responsable Marketing` | Supprimer les procédés manipulatoires qui poussent à consommer plus : lecture enchaînée, relances, faux comptes à rebours. |
| [4.15](../../../rgesn/ux-ui/4-15_controle-usages/) — Moyen de contrôle des usages et mode sobre | `Concepteur UX / UI` `Développeur` `Responsable RSE/Numérique soutenable` | Donner à l'utilisateur un moyen de suivre et de réduire ses usages, par exemple un mode sobre. |

## 5. Contenus

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [5.1](../../../rgesn/contenus/5-1_format-images/) — Format de fichier adapté à chaque image | `Développeur` `Architecte Logiciel` | Choisir pour chaque image le format adapté : SVG pour les illustrations vectorielles, AVIF ou WebP pour les photos. |
| [5.2](../../../rgesn/contenus/5-2_compression-images/) — Niveau de compression adapté à chaque image | `Développeur` `Architecte Logiciel` | Régler la compression de chaque image selon son contenu et son contexte d'affichage. |
| [5.3](../../../rgesn/contenus/5-3_definition-videos/) — Définition vidéo adaptée au contenu et au terminal | `Développeur` `Architecte Logiciel` `Porteur de projet` | Adapter la définition de chaque vidéo à son contenu et au terminal qui la lit. |
| [5.4](../../../rgesn/contenus/5-4_compression-videos/) — Mode de compression des vidéos efficace et adapté | `Développeur` `Architecte Logiciel` | Encoder les vidéos avec un codec efficace (AV1, VP9 ou HEVC) et un débit adapté au contenu. |
| [5.5](../../../rgesn/contenus/5-5_ecoute-seule/) — Mode « écoute seule » pour les vidéos | `Développeur` `Responsable IT` | Proposer un mode « écoute seule » qui ne télécharge que la piste son. |
| [5.6](../../../rgesn/contenus/5-6_compression-audio/) — Compression des contenus audio adaptée | `Développeur` `Responsable IT` | Compresser les contenus audio selon leur nature : parole ou musique. |
| [5.7](../../../rgesn/contenus/5-7_format-documents/) — Format de fichier adapté à chaque document | `Développeur` `Responsable IT` | Choisir pour chaque document le format adapté à son usage (HTML pour la lecture en ligne), et le compresser sans perdre son accessibilité. |
| [5.8](../../../rgesn/contenus/5-8_archivage-suppression/) — Archivage et suppression des contenus obsolètes | `Architecte Logiciel` `Data Scientist` `Responsable de la sécurité informatique` `Responsable Juridique` | Définir une stratégie d'archivage et de suppression des contenus obsolètes, automatique ou manuelle. |

## 6. Frontend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [6.1](../../../rgesn/frontend/6-1_poids-requetes-ecran/) — Poids maximum et limite de requêtes par écran | `Développeur` `Concepteur UX / UI` `Responsable Produit` | Fixer un budget de poids et de requêtes par écran, et le vérifier à chaque version. |
| [6.2](../../../rgesn/frontend/6-2_cache-navigateur/) — Mise en cache côté utilisateur | `Administrateur Système` `Développeur` `Architecte Logiciel` | Mettre en cache dans le navigateur tous les contenus dont le service a le contrôle. |
| [6.3](../../../rgesn/frontend/6-3_compression-ressources/) — Compression des ressources transférées | `Développeur` `Administrateur Système` `Architecte Logiciel` | Compresser les ressources texte transférées (gzip, Brotli). |
| [6.4](../../../rgesn/frontend/6-4_dimensions-images/) — Dimensions des images adaptées à l'affichage | `Développeur` `Concepteur UX / UI` | Servir des images aux dimensions de leur affichage, avec plusieurs tailles selon l'écran. |
| [6.5](../../../rgesn/frontend/6-5_chargement-ressources/) — Chargement des seules ressources utiles | `Développeur` `Concepteur UX / UI` | Ne charger que les ressources utiles à la fonctionnalité affichée, et différer les autres. |
| [6.6](../../../rgesn/frontend/6-6_capteurs-terminaux/) — Usage des capteurs limité au besoin du service | `Développeur` `Concepteur UX / UI` | Ne solliciter les capteurs (géolocalisation, caméra, accéléromètre…) qu'au moment et à la fréquence où le service en a besoin. |
| [6.7](../../../rgesn/frontend/6-7_domaine-unique/) — Ressources statiques sur un même domaine | `Administrateur Système` `Développeur` `Architecte Logiciel` | Servir les ressources statiques depuis le domaine du service plutôt que depuis plusieurs domaines tiers. |

## 7. Backend

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [7.1](../../../rgesn/backend/7-1_cache-serveur/) — Cache serveur pour les données les plus utilisées | `Administrateur Système` `Développeur` `Architecte Logiciel` | Mettre en cache côté serveur les données les plus demandées. |
| [7.2](../../../rgesn/backend/7-2_durees-conservation/) — Durées de conservation des données | `Administrateur Système` `Développeur` `Responsable Produit` `Architecte Logiciel` | Fixer une durée de conservation pour chaque type de données, puis les supprimer ou les archiver. |
| [7.3](../../../rgesn/backend/7-3_traitement-arriere-plan/) — Information sur un traitement en cours | `Développeur` `Responsable Produit` | Informer l'utilisateur d'un traitement en cours en arrière-plan, pour éviter qu'il ne le relance. |
| [7.4](../../../rgesn/backend/7-4_mecanisme-consensus/) — Mécanisme de consensus sobre | `Développeur` `Administrateur Système` `Architecte Logiciel` | Choisir, pour une chaîne de blocs, un mécanisme de consensus sobre plutôt que la preuve de travail. |

## 8. Hébergement

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [8.1](../../../rgesn/hebergement/8-1_demarche-hebergeur/) — Hébergeur engagé dans la réduction de son empreinte | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` `Administrateur Système` | Choisir un hébergeur qui publie ses indicateurs environnementaux et s'engage à les réduire. |
| [8.2](../../../rgesn/hebergement/8-2_gestion-equipements/) — Gestion durable des équipements de l'hébergeur | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` | Vérifier que l'hébergeur a une politique de gestion durable de ses équipements : durée de vie, réemploi, fin de vie. |
| [8.3](../../../rgesn/hebergement/8-3_pue/) — PUE de l'hébergement | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` | Choisir un hébergement dont le PUE réel est inférieur à 1,5. |
| [8.4](../../../rgesn/hebergement/8-4_wue/) — WUE de l'hébergement | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` | Choisir un hébergement qui suit et réduit sa consommation d'eau (WUE, objectif de 0,4 L/kWh). |
| [8.5](../../../rgesn/hebergement/8-5_electricite-renouvelable/) — Électricité d'origine renouvelable | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` | Vérifier que l'électricité de l'hébergeur est documentée et majoritairement renouvelable, avec ses justificatifs. |
| [8.6](../../../rgesn/hebergement/8-6_localisation/) — Localisation de l'hébergement | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable Logistique` | Héberger le service dans un pays dont l'électricité émet moins de 100 g CO2e/kWh, cohérent avec la localisation de ses utilisateurs. |
| [8.7](../../../rgesn/hebergement/8-7_chaleur-fatale/) — Traitement de la chaleur produite par les serveurs | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` | Préférer un hébergeur qui récupère la chaleur de ses serveurs, ou dont le PUE réel est inférieur à 1,3. |
| [8.8](../../../rgesn/hebergement/8-8_donnees-chaudes-froides/) — Données chaudes et froides hébergées séparément | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Architecte de bases de données` | Au-delà de 10 To, séparer les données courantes des archives et sauvegardes, sur un stockage froid. |
| [8.9](../../../rgesn/hebergement/8-9_duplication-donnees/) — Duplication des données selon le besoin | `Responsable de l'hébergement` `Ingénieur en stockage de données` `Responsable de la sécurité informatique` `Architecte/Ingénieur Systèmes` | Ne dupliquer les données que selon un niveau de service (SLA) ajusté au besoin. |
| [8.10](../../../rgesn/hebergement/8-10_decalage-asynchrone/) — Calculs et transferts asynchrones au bon moment | `Responsable de la programmation` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Décaler les calculs et transferts asynchrones aux heures où l'électricité est la moins carbonée et les réseaux les moins chargés. |

## 9. Algorithmie

| Critère | Métiers concernés | Ce qu'il y a à faire |
|---|---|---|
| [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/) — Méthode d'apprentissage la plus sobre | `Porteur de projet` `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Choisir la méthode d'apprentissage la moins complexe qui suffit à l'usage réel. |
| [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) — Limiter la quantité d'entraînement | `Porteur de projet` `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Limiter la quantité d'entraînement, en partant si possible d'un modèle pré-entraîné. |
| [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) — Données d'apprentissage limitées au nécessaire | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` `Responsable de la protection des données` `Développeur` | Limiter les données d'entraînement au strict nécessaire. |
| [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) — Fréquence de réentraînement des modèles | `Porteur de projet` `Data Scientist` `Chef de produit marketing` | Réentraîner les modèles à la fréquence que le besoin justifie, pas par habitude. |
| [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) — Compression des modèles | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` | Compresser les modèles : quantification, élagage, distillation. |
| [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) — Stratégie d'inférence sobre | `Porteur de projet` `Data Scientist` `Développeur` | Optimiser l'inférence : le plus petit modèle qui suffit, cache des réponses. |

---

Voir la page [Outils > Conception](../../../outils/par-phase-projet/conception/) pour les outils concrets utilisables à ce stade.
