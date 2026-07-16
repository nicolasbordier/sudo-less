---
weight: 700
title: "4.7 - Choix du format le plus sobre"
description: "Critère 4.7 du RGESN : pourquoi et comment choisir le format le plus sobre entre texte, image, audio ou vidéo selon les besoins utilisateurs."
icon: "compress"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique opte-t-il pour les choix les plus sobres entre le texte, l'image, l'audio ou la vidéo, selon les besoins utilisateurs ?

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
| **Critère**  | `4.7` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Développeur` `Designer` `Responsable Qualité` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire la taille des ressources utilisées, sachant qu'une vidéo, même encodée avec le procédé le plus efficace, pèse généralement beaucoup plus lourd qu'un texte contenant des images.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Mettre en question et documenter le besoin d'afficher un média (vidéo, animation ou enregistrement audio). Le cas échéant, choisir la solution la plus sobre possible tout en répondant au besoin de l'utilisateur. À titre indicatif, de façon générale : un texte pèse moins qu'une image, une image pèse moins qu'un audio et un audio pèse moins qu'une vidéo.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Évaluer la pertinence du choix d'affichage d'une vidéo, d'une animation ou d'un enregistrement audio.

Le critère est validé si le service n'utilise pas de contenu vidéo, audio ou animé, ou si le recours à la vidéo, à l'audio ou à l'animation a été décidé en optant pour le choix de la solution la plus sobre disponible, au regard des besoins et des fonctionnalités essentiels du service. Les choix effectués sont à justifier dans un document public (par exemple, dans la déclaration d'écoconception). La justification prendra en compte les besoins des cibles utilisatrices (voir le critère 1.2.) et à l'impact environnemental du contenu audiovisuel choisi.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le critère 4.7 rejoint la [recommandation n°3 de la famille Contenus](https://gr491.isit-europe.org/crit.php?id=3-4030-contenus-les-informations-apportees-par-la-video-sont) du [GR491](https://gr491.isit-europe.org/) (INR) : « Est-ce que l'information portée par la vidéo peut être remplacée par une alternative (infographie…) ? ». Le GR491 pose la question spécifiquement du côté vidéo → alternative statique, plutôt que la hiérarchie complète texte/image/audio/vidéo du RGESN, mais avec la même logique : évaluer si le format le plus lourd choisi par défaut transporte réellement une information qu'un format plus léger ne pourrait pas transmettre tout aussi bien.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe et explicitement étiquetée « RGESN 4.7 » : la fiche [**RWEB 0030 — « Fournir une transcription textuelle aux contenus multimédias »**](https://rweb.greenit.fr/fr/fiches/RWEB_0030-fournir-une-alternative-textuelle-aux-contenus-multimedias), notée à **5/5** sur l'échelle d'impact environnemental. Elle chiffre précisément l'écart entre les formats évoqué par le RGESN : une vidéo de 30 minutes pèse en moyenne **500 Mo**, un podcast équivalent **30 Mo**, et le texte correspondant **moins de 1 Mo** — un rapport de poids qui dépasse 500 entre la vidéo et le texte pour transmettre une information de nature comparable. La fiche ajoute un double bénéfice : accessibilité (les transcriptions permettent aux personnes sourdes ou malvoyantes d'accéder au contenu) et référencement (les moteurs de recherche indexent mieux le texte que l'audio ou la vidéo). Principe de validation : le nombre de fichiers multimédias sans transcription textuelle doit rester inférieur ou égal à 10 %.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Les Designers Éthiques ont publié une ressource dédiée, [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), distincte de leur guide d'écoconception général : elle traduit les 78 critères du RGESN en actions concrètes pour les designers, organisées par phase de projet. Le passage consacré au critère 4.7 reprend presque mot pour mot le RGESN, avec un exemple qui inverse volontairement la hiérarchie de sobriété habituelle pour illustrer le principe : « Privilégier le texte ou l'image au lieu de l'animation, la vidéo ou le son lorsque cela est possible. Choisir la solution au besoin utilisateur la plus sobre possible (texte plutôt qu'image, animation plutôt que vidéo par exemple). »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Ce critère est le prolongement direct du [critère 4.6](../4-6_contenu-porteur-information/) (contenu porteur d'information), déjà publié sur ce site : le 4.6 pose la question « ce média est-il utile ? » ; une fois la réponse « oui » établie, le 4.7 pose la question suivante, « une fois ce média jugé utile, quel est le format le plus léger capable de porter la même information ? ». Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C, déjà citées pour le 4.6 dans la fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use), couvrent d'ailleurs implicitement ce prolongement dans la même recommandation : « Provide the option to disable data-intensive media or offer lower-bandwidth alternatives » — sans dédier de fiche séparée à la hiérarchie texte/image/audio/vidéo du RGESN.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec une justification qui va au-delà du simple constat d'absence : « Les contenus apportés par le service numérique sont essentiellement textuels, et via des pièces jointes bureautique de taille modérée à moyenne. » Contrairement aux critères voisins 4.5 et 4.6 sur cette même déclaration — validés par absence totale de composants ou de médias concernés — celui-ci documente un choix positif (contenu textuel et pièces jointes de taille maîtrisée) plutôt qu'une simple absence de risque.

{{% /tab %}}

{{< /tabs >}}
