---
weight: 600
title: "4.6 - Contenu vidéo, audio et animé porteur d'information"
description: "Critère 4.6 du RGESN : pourquoi et comment limiter le contenu vidéo, audio et animé aux seuls usages porteurs d'information, plutôt que purement décoratifs."
icon: "smart_display"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il uniquement du contenu vidéo, audio et animé porteur d'informations ?

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
| **Critère**  | `4.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Développeur` `Designer` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Une partie importante du trafic sur internet est liée au visionnage de vidéos. Les contenus audio et animés représentent également une taille plus importante que le texte et l'image.

Dans une démarche d'écoconception, il est pertinent de minimiser le recours à des contenus médias lourds ayant un but purement esthétique, pour favoriser des solutions alternatives quand elles sont possibles.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Vérifier la pertinence de l'usage de vidéos, animations et contenus audio, c'est-à-dire que ces médias sont fournis dans le cadre des fonctions critiques du service et/ou sont porteurs d'information. Ne pas recourir à des contenus vidéo, animés ou audio purement décoratifs et n'apportant aucune information à l'utilisateur.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Évaluer la pertinence du choix d'afficher une animation ou une vidéo ou encore un contenu audio.

Le critère est validé si le service ne contient pas de contenu vidéo, audio ou d'animation à but purement décoratif, c'est-à-dire ne concernant pas les fonctions critiques du service. Dans la déclaration d'écoconception du service, il faudra documenter le motif d'utilisation des contenus vidéo, animés et audio afin de démontrer qu'ils servent les fonctions critiques du service et/ou apportent de l'information à l'utilisateur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le critère 4.6 rejoint la [recommandation n°8 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=8) du [GR491](https://gr491.isit-europe.org/) (INR), « **Ingénierie média : alléger au maximum les médias du service numérique (images, animations, contenu…)** », dont l'un des critères pose littéralement la même question : 

- « Les vidéos et animations sont-elles utilisées uniquement lorsqu'elles apportent une valeur pour l'utilisateur ? ». 

La même recommandation couvre aussi des questions voisines et complémentaires : 

- « Est-ce que la fonctionnalité peut être proposée sans l'appel de scripts ou de bibliothèques externes ? », 
- « Est-ce que les fonctionnalités et composants natifs du système peuvent correspondre au besoin ? » 

Un rappel que la question de la pertinence du média (4.6) et celle du poids technique de son implémentation (proche du critère 4.5) sont souvent traitées ensemble dans la pratique.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement le critère 4.6** dans sa section [**7.3 Animations**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-3-animations) : 

- « N'utiliser les animations que si elles apportent une information permet de valider le critère 4.6 » — le guide précise que la même logique s'applique aux vidéos et aux sons. 

Les animations utilisées comme simples « fioritures décoratives » perturbent certains utilisateurs tout en alourdissant la page ; à l'inverse, le guide cite une **barre de progression de chargement** comme exemple d'animation légitime, puisqu'elle transmet une information réelle (l'avancement d'une opération) plutôt qu'un simple effet esthétique.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent ce critère à travers deux recommandations complémentaires :

- [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) : « Only include media when it supports user experience or improves understanding and keep the number of media items to a minimum. »
- [**« Design to assist and not to distract »**](https://www.w3.org/TR/web-sustainability-guidelines/#design-to-assist-and-not-to-distract) (déjà citée au critère 4.2) : « Use decorative design only when it improves the user experience, and make optional assets removable or turned off by default. »

Les deux fiches posent la même question de fond que le RGESN, sous un angle légèrement différent : plutôt que d'interdire le contenu décoratif dans l'absolu, elles conditionnent sa présence à une amélioration réelle et démontrable de l'expérience utilisateur — charge à l'équipe projet de documenter cette justification, exactement comme le demande le « Moyen de test » du critère RGESN.

{{% /tab %}}

{{% tab tabName="Gauthier Roussilhe" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le [guide d'écoconception rédigé par Gauthier Roussilhe et son équipe pour l'ADEME](https://gauthierroussilhe.com/book/ademe/VIDEOS.html) (accompagnement de la startup d'État « Territoires en Transitions », 2020-2022) pose directement la question du critère dans sa fiche sur les vidéos : 

- « Est-ce que ma vidéo a une réelle valeur pour l'utilisateur ou sert-elle plutôt à capter des données ? ». 

Le guide va jusqu'à relier la question à la captation de l'attention plutôt qu'au seul poids technique : 

- « La vidéo est parfois utilisée comme mécanisme de captation de l'attention à des fins commerciales »
- « Une vidéo qui attire l'attention de l'utilisateur n'est pas forcément une vidéo qui lui est utile ». 

Sa recommandation pratique, formulée sans détour : « Il est plus important d'avoir les bons mots plutôt qu'une vidéo de remplissage » — un rappel qu'un contenu textuel bien écrit peut parfois remplacer une vidéo, plutôt que la compléter ou l'habiller.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec une justification simple : « Le service numérique n'intègre pas de contenu vidéo, audio et animé. » Comme pour le critère voisin 4.5 sur cette même déclaration, il s'agit d'une conformité obtenue par l'absence du risque plutôt que par un arbitrage explicite entre contenu décoratif et contenu informatif — cohérent avec un service de consultation de données principalement textuel et graphique (histogrammes, camemberts, tableaux).

{{% /tab %}}

{{< /tabs >}}
