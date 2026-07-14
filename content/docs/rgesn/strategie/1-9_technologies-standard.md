---
weight: 900
title: "1.9 - Technologies standard et interopérables"
description: "Critère 1.9 du RGESN : pourquoi privilégier des technologies standard et interopérables (web plutôt que natif) pour lutter contre l'obsolescence des terminaux."
icon: "article"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il été conçu avec des technologies standard interopérables plutôt que des technologies spécifiques et fermées ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Stratégie` |
| **Critère**  | `1.9` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable IT` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.9/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est de **lutter contre l'obsolescence des équipements induite par le logiciel**. Tout service numérique qui s'attache à être le plus **stable et pérenne dans le temps** permet d'allonger la durée pendant laquelle les terminaux restent utilisables.

Le recours à de **nouvelles API** ou à de **nouveaux standards non supportés par les terminaux plus anciens** est susceptible de favoriser une obsolescence rapide de ces derniers. L'**interopérabilité des standards** est donc un vecteur pour allonger leur durée d'utilisation et de vie. De même, les **applications natives** peuvent nécessiter les toutes dernières versions d'OS — voire les tout derniers modèles d'équipements — pour fonctionner, ce qui induit une obsolescence matérielle.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Évaluer, **bien en amont du développement**, la faisabilité de concevoir le service avec des **technologies standard** (par exemple le web plutôt qu'une application native) pour répondre au besoin des utilisateurs et des métiers. S'assurer également que les **API utilisées sont standard et bien supportées** (API JavaScript des navigateurs web, par exemple).

S'appuyer sur des technologies interopérables permet de lutter contre l'**obsolescence logicielle**. De même, construire son service à partir de **composants open source** permet de garder la main sur la maintenance du code utilisé, et donc d'améliorer sa durabilité.

Lorsqu'une **application native est nécessaire** (par exemple pour des traitements de données particulièrement sensibles), s'assurer qu'elle repose sur des standards **compatibles avec les principaux systèmes d'exploitation**.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier que le service numérique est **utilisable par une même interface sur l'ensemble des terminaux pertinents** (par exemple une Web App). Si le service est une application native, évaluer la **nécessité réelle** de ce choix : contraintes techniques ? Matériel cible maîtrisé ?

Le critère est **validé** si le service s'appuie sur des **standards interopérables communs aux principaux écosystèmes** (terminaux, systèmes d'exploitation, navigateurs…).

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="2">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Développeur`, `Architecte`

Le critère 1.9 du RGESN correspond directement à la [recommandation n°4 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR) : « Réduire les effets d'obsolescence », classée **« Incontournable »**. Elle pousse le questionnement au-delà du simple choix web/natif :

- **Rétrocompatibilité** : la plage de rétro-compatibilité visée est-elle explicitement définie ?
- **Version allégée** : une version plus légère du service existe-t-elle pour les équipements anciens ou les connexions limitées ?
- **Compatibilité future** : les équipements plus anciens resteront-ils compatibles, et dans quelles limites ?

La [recommandation n°3](https://gr491.isit-europe.org/?famille=frontend&num_reco=3) (« Utiliser des environnements et outils limitant les impacts ») de la même famille ajoute un critère directement actionnable : la fonctionnalité visée pourrait-elle être couverte par une **capacité native du navigateur**, plutôt que par une dépendance externe ?

{{% /tab %}}

{{% tab tabName="Outils" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte`

Pour vérifier concrètement qu'une API ou une fonctionnalité web est « standard et bien supportée » avant de l'adopter :

- [**Baseline**](https://web.dev/baseline) (initiative intersectorielle du W3C WebDX Community Group, soutenue par Google, Microsoft, Apple et Mozilla) donne un verdict unique et normalisé par fonctionnalité web : **Widely available** (supportée par tous les navigateurs majeurs depuis au moins 2,5 ans), **Newly available** (récente, pas encore fiable sur les anciens terminaux) ou **Limited** (support partiel). Ce statut est directement visible sur les pages [MDN Web Docs](https://developer.mozilla.org/) et [Can I Use](https://caniuse.com/).
- Une **Web App** (voire une [Progressive Web App](https://web.dev/learn/pwa/progressive-web-apps)) reste, par construction, la façon la plus directe de répondre au critère : une seule base de code HTML/CSS/JS, interopérable nativement entre systèmes d'exploitation et terminaux, sans passer par un magasin d'applications ni imposer de version d'OS minimale. Deux retours d'expérience chiffrés, documentés par leurs propres équipes d'ingénierie, confirment ce gain de légèreté et de compatibilité :
  - [**Twitter Lite**](https://web.dev/case-studies/twitter) : la PWA ne pesait que **600 Ko** contre **23,5 Mo** pour l'application Android native équivalente — 1 à 3 % de sa taille — avec un chargement 30 % plus rapide et une consommation de données réduite de 70 %.
  - [**Uber (m.uber.com)**](https://www.uber.com/en-GB/blog/m-uber/) : conçue pour ne peser que **50 Ko** afin de rester utilisable sur des réseaux 2G, l'équipe d'ingénierie précise explicitement que cette PWA est « compatible avec tous les navigateurs modernes, y compris sur des terminaux non pris en charge par l'application native » — l'illustration la plus directe du gain de rétrocompatibilité visé par ce critère.

Côté mobile, trois repères complémentaires :

- [**Can I Use**](https://caniuse.com/) et **Baseline** couvrent aussi les navigateurs mobiles (Chrome Android, Safari iOS, Samsung Internet) : une fonctionnalité « Widely available » l'est aussi sur mobile, pas seulement sur desktop.
- **Android System WebView**, le moteur de rendu utilisé par les applications embarquant du contenu web, est mis à jour **via le Play Store indépendamment de la version d'Android** depuis Android 5 (2014) — un argument concret en faveur du web embarqué : un ancien téléphone bloqué sur une vieille version d'OS peut malgré tout bénéficier d'un moteur de rendu à jour, contrairement à des API natives figées par la version du système.
- [**PWABuilder**](https://www.pwabuilder.com/) (Microsoft, open source) empaquette une Progressive Web App existante en application installable pour l'App Store et le Play Store via [Bubblewrap](https://github.com/GoogleChromeLabs/bubblewrap) — utile lorsqu'une présence en magasin d'applications est requise, sans pour autant renoncer à une base de code web unique et interopérable.

Si une application réellement native reste nécessaire, éviter de fixer un `minSdkVersion` (Android) ou une version minimale d'iOS supérieure au strict besoin technique : chaque palier relevé sans justification exclut immédiatement les terminaux plus anciens du service, à rebours de l'objectif du critère.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 30 janvier 2025) valide ce critère avec une justification simple et directement transposable : « Le service numérique est une application web qui s'appuie sur des standards interopérables communs aux principaux écosystèmes (terminaux, systèmes d'exploitation, navigateurs…). »

Ce cas illustre bien la logique du critère : contrairement à d'autres critères de cette fiche (1.7, 1.8) où la conformité demande un effort dédié, le choix d'une **architecture web standard dès la conception** rend ce critère 1.9 quasiment automatique — alors qu'une application native nécessiterait, a posteriori, de justifier ce choix et d'en documenter les limites de compatibilité dans la déclaration d'écoconception.

Plus radical encore, [Low-tech Magazine](https://solar.lowtechmagazine.com/fr/2018/09/how-to-build-a-low-tech-website/) pousse la même logique de sobriété technologique à l'extrême, tout en restant sur des standards ouverts : site **statique** (pas de génération à chaque visite), pas de framework JavaScript, poids d'images réduit au minimum, aucun logo, aucune vidéo, aucun cookie ni publicité. Le site va jusqu'à être hébergé sur un **serveur alimenté à 100 % à l'énergie solaire** — ce qui implique une disponibilité dépendante de l'ensoleillement, revendiquée comme telle plutôt que masquée (source : [ADEME, État des lieux et perspectives des démarches low-tech — fiche Numérique](https://librairie.ademe.fr/consommer-autrement/5421-demarches-low-tech.html), 2021). Un exemple utile pour rappeler que « technologie standard » n'impose pas un plafond de sobriété : les deux peuvent aller de pair bien au-delà du minimum attendu par ce critère.

{{% /tab %}}

{{< /tabs >}}
