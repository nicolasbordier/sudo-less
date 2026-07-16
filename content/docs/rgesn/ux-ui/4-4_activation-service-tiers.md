---
weight: 400
title: "4.4 - Décision de l'utilisateur sur l'activation d'un service tiers"
description: "Critère 4.4 du RGESN : pourquoi et comment laisser l'utilisateur décider de l'activation d'un service tiers, plutôt que de le charger systématiquement par défaut."
icon: "cookie"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique permet-il à l'utilisateur de décider de l'activation d'un service tiers ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Expérience et Interface utilisateur (UX / UI)` |
| **Critère**  | `4.4` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service ne repose pas sur un service tiers` |
| **Métiers concernés** | `Développeur` `Responsable Qualité` `Responsable de la protection des données` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Limiter le chargement de services tiers non nécessaires au bon fonctionnement du service. Par exemple, sans activation des cookies, certains lecteurs vidéo sont désactivés et en attente de consentement pour le visionnage la vidéo.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

En l'absence de criticité vis-à-vis des fonctionnalités essentielles du service, charger uniquement à la demande explicite de l'utilisateur les services tiers sous-jacents au service numérique.

Si le service tiers nécessite de traiter des données personnelles, ce critère s'inscrit dans la continuité de l'une des obligations du RGPD sur la demande de consentement avant l'éventuel traitement de données personnelles, y compris dans le cadre de la fourniture d'un service tiers.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si l'activation des services tiers intégrés au service numérique est conditionnée au consentement clair et explicite de l'utilisateur, du point de vue de la protection des données lorsque applicable, avec également une information spécifique sur le possible coût environnemental.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable de la protection des données`

Le chapitre [« 7.5 Plugins et widgets (service tiers) »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-5-plugins-et-widgets) du guide des Designers Éthiques cite **explicitement le critère 4.4** : « Laisser l'utilisateur décider de l'activation d'un service tiers permet de valider le critère 4.4 » du RGESN. Le guide en fait un prolongement logique de sa réflexion sur les plugins et widgets tiers (déjà croisée avec le critère 2.10 sur ce site) : au-delà de la question de savoir si un service tiers est réellement nécessaire, se pose celle de savoir s'il doit se charger automatiquement pour tous les visiteurs ou seulement à la demande explicite de ceux qui en ont réellement besoin.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Qualité`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent ce critère dans la fiche [**« Treat third parties the same as first parties »**](https://www.w3.org/TR/web-sustainability-guidelines/#treat-third-parties-the-same-as-first-parties), déjà citée pour le critère 2.10 : au-delà du choix du service tiers lui-même, la guideline recommande explicitement de ne charger le contenu tiers **qu'au moment où l'utilisateur interagit avec lui**, plutôt qu'au chargement de la page — c'est très exactement la mécanique de chargement conditionné à une action explicite que demande le critère 4.4, appliquée cette fois à l'activation plutôt qu'à la seule sélection du service tiers.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Deux mécanismes concrets permettent de subordonner l'activation d'un service tiers à une action explicite de l'utilisateur :

- **Gestion du consentement** : [tarteaucitron.js](https://tarteaucitron.io/fr/) est un gestionnaire de consentement open source (licence MIT) développé par un développeur français, qui bloque par défaut plus d'une centaine de services tiers reconnus (YouTube, Google Analytics, Facebook Pixel…) jusqu'à ce que l'utilisateur ait donné son consentement explicite — utilisé sur plus de 35 000 sites, dont des sites de l'État français. Il répond directement à la partie RGPD du critère : aucun traitement de données personnelles par un service tiers avant consentement.
- **Motif de remplacement (« facade »)** : pour les services tiers sans traitement de données personnelles à proprement parler mais dont le seul chargement est déjà coûteux (lecteur vidéo, carte interactive), la technique déjà documentée sur ce site au [critère 2.10](../../specifications/2-10_services-tiers/) avec [lite-youtube-embed](https://github.com/paulirish/lite-youtube-embed) illustre exactement l'exemple donné par la « Mise en œuvre » du critère : n'afficher qu'une vignette statique cliquable, et ne charger le lecteur vidéo complet (avec son propre cortège de requêtes tierces) qu'au moment où l'utilisateur clique dessus pour le visionner.

Dans les deux cas, le principe reste le même : le service tiers existe bien dans le code du service numérique, mais son activation réelle — et donc son coût réseau — est différée jusqu'à une action univoque de l'utilisateur.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable de la protection des données`

Ce critère est le pendant « activation » du [critère 2.10](../../specifications/2-10_services-tiers/) (impacts environnementaux des services tiers), déjà publié sur ce site : le 2.10 porte sur le **choix** du service tiers (comparer les alternatives, mesurer leur poids, se demander s'il est réellement nécessaire), tandis que le 4.4 porte sur la **temporalité de son activation** une fois ce choix fait — chargé pour tout le monde dès l'arrivée sur la page, ou seulement pour les utilisateurs qui en expriment le besoin. Un service tiers peut donc être parfaitement conforme au 2.10 (le plus sobre de sa catégorie) tout en restant non conforme au 4.4 s'il se charge systématiquement sans action de l'utilisateur, et inversement.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non applicable »**, avec la même justification que pour le critère 2.10 sur ce même service : « Le service tiers Chorus est nécessaire au fonctionnement du produit à des fins de vérifications réglementaires. » Chorus Pro, la plateforme interministérielle de facturation électronique, est ici traité comme une dépendance technique obligatoire plutôt qu'un choix optionnel de confort — l'utilisateur ne peut logiquement pas être mis en position de décider d'activer ou non un service tiers dont dépend une vérification réglementaire imposée par ailleurs.

{{% /tab %}}

{{< /tabs >}}
