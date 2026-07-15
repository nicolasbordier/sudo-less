---
weight: 100
title: "4.1 - Désactivation de la lecture automatique"
description: "Critère 4.1 du RGESN : pourquoi et comment désactiver par défaut la lecture automatique des animations, vidéos et sons pour limiter la captation de l'attention et les ressources mobilisées."
icon: "play_disabled"
date: "2026-07-15T00:00:00+01:00"
lastmod: "2026-07-15T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique comporte-t-il uniquement des animations, vidéos et sons dont la lecture automatique est désactivée ?

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
| **Critère**  | `4.1` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` `Responsable Qualité` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Plus un utilisateur passe de temps sur un site ou une application, plus l'empreinte environnementale associée à cet usage sera élevée, les ressources réseaux et systèmes sur le terminal étant mobilisées plus longtemps. S'il appartient bien entendu à l'utilisateur de décider quel temps il souhaite consacrer à tel ou tel usage, les pratiques de développement du site ou de l'application concernée peuvent avoir un impact direct sur cette durée d'utilisation, en particulier par l'exploitation de pratiques de captation de l'attention.

Le lancement automatique de contenus, en particulier de vidéos, fait partie des mécanismes mis en place pour garder l'utilisateur en état d'attention. Le déclenchement de contenus et leur pré-chargement sans consentement de l'utilisateur doit être évité dans une perspective de sobriété des usages.

Ce critère permet de donner le contrôle à l'utilisateur pour limiter l'usage de ressources non nécessaires.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Désactiver par défaut le chargement et la lecture automatiques de contenu vidéo et/ou sonores dans les paramètres du service. Si ce n'est pas possible, permettre à l'utilisateur de supprimer ces fonctionnalités avec un bouton ou une interface directement accessible et visible.

Autant que possible, ne pas utiliser de graphismes animés non contrôlables, ou encore partiellement contrôlables par l'utilisateur (images gif animées notamment). Les fonds vidéo et/ou audio en lecture automatique devront en particulier être évités, s'ils sont à visée purement esthétique.

Pour les animations jugées essentielles vis-à-vis des fonctionnalités du service, proposer une possibilité à l'utilisateur de mettre en pause ces éléments. Lorsque l'animation visuelle a une durée de plus de 4 secondes ou qu'un son a une durée de plus de 2 secondes, doter systématiquement l'objet multimédia des moyens de contrôle nécessaires : démarrage, arrêt, muet ou volume. Permettre de les désactiver simplement dès lors que ces contenus dépassent 4 secondes et minimiser leur taille (voir critères 5.3, 5.4 et 5.5).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier que le service n'inclut pas de lecture automatique de contenu par défaut. Si ce n'est pas possible, s'assurer que le service numérique donne la possibilité à l'utilisateur de supprimer facilement le chargement ou le lancement automatique de vidéos ou contenus audios. Les possibilités de suppression doivent être mises en évidence dans le service numérique (par exemple, avec un bouton de désactivation apparent dans l'interface utilisateur).

Il conviendra également de limiter au strict nécessaire le nombre d'animations visuelles non contrôlables et de fixer des objectifs quantitatifs à ne pas dépasser. Les animations non contrôlables jugées essentielles vis-à-vis des fonctionnalités du service devront pouvoir être mises en pause par l'utilisateur dès qu'elles dépassent 4 secondes pour l'animation visuelle et 2 secondes pour l'audio.

Le critère est validé si le service ne repose pas sur une fonctionnalité de lecture automatique par défaut et incontrôlée, limite le recours à des animations visuelles, clignotements ou défilements automatiques non contrôlables, en suivant les conditions susmentionnées.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le critère 4.1 rejoint la [recommandation n°9 de la famille Front-end](https://gr491.isit-europe.org/?famille=frontend&num_reco=9) du [GR491](https://gr491.isit-europe.org/) (INR), « Implémenter des solutions techniques dont l'impact est le plus faible », qui pose deux critères directement transposables : « Est-ce bien une action utilisateur qui déclenche le "play" ? » et « Les vidéos ou animations hors de la zone active sont-elles automatiquement mises en pause / stoppées ? ». Cette seconde question va au-delà du texte du RGESN, qui traite du déclenchement initial mais pas explicitement du cas d'une vidéo qui continue de tourner hors du champ de vision de l'utilisateur (défilement de page, changement d'onglet).

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) couvre ce critère avec deux fiches complémentaires :

- [**RWEB 0106 — « Éviter la lecture et le chargement automatique des vidéos et des sons »**](https://rweb.greenit.fr/fr/fiches/RWEB_0106-eviter-la-lecture-et-le-chargement-automatique-des-videos-et-des-sons) : traduit la recommandation en deux attributs HTML précis — retirer l'attribut `autoplay` des balises `<video>` et `<audio>`, et ajouter `preload="none"` pour empêcher le navigateur de télécharger le fichier média tant que l'utilisateur n'a pas déclenché la lecture. Principe de validation : zéro élément `<video>` ou `<audio>` sans l'un de ces deux attributs.
  ```html
  <video src="fichiervideo.webm" preload="none"></video>
  <audio controls src="fichieraudio.mp3" preload="none"></audio>
  ```
- [**RWEB 0099 — « Limiter l'utilisation des GIFs animés »**](https://rweb.greenit.fr/fr/fiches/RWEB_0099-limiter-l-utilisation-des-gifs-animes) : le GIF animé (format de 1995) est nettement plus lourd qu'une vidéo WebM ou MP4 équivalente — la fiche cite deux exemples mesurés, 90 Ko (GIF) contre 36-38 Ko (WebM/MP4), et surtout 5,45 Mo (GIF) contre 266-274 Ko (WebM/MP4), soit un facteur supérieur à 20 sur ce second exemple. L'alternative recommandée n'est pas de supprimer l'animation mais de la remplacer par une vidéo **spécifiquement paramétrée pour se comporter comme un GIF** : `<video autoplay loop muted playsinline>`. Ce cas est une exception assumée à l'interdiction générale de l'`autoplay` : une vidéo muette, en boucle, purement décorative, réduit la charge par rapport à un GIF équivalent tout en restant dans l'esprit du critère (aucun son, aucune captation d'attention active).

  La conversion elle-même se fait en une commande avec [**ffmpeg**](https://ffmpeg.org/), sans outil supplémentaire. D'après [ce guide de conversion](https://sidneyliebrand.io/blog/converting-gif-to-web-safe-video-formats-using-ffmpeg), qui détaille chaque option :
  ```bash
  # WebM (VP9) : environ 60 % plus léger qu'un GIF équivalent
  ffmpeg -i fichier.gif -c:v vp9 -b:v 0 -crf 40 fichier.webm

  # MP4 (H.264), pour les navigateurs sans support VP9 : environ 50 % plus léger qu'un GIF équivalent
  ffmpeg -i fichier.gif -movflags +faststart -pix_fmt yuv420p \
    -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" fichier.mp4
  ```
  `-crf` (0 à 63, plus bas = meilleure qualité mais fichier plus lourd) permet d'arbitrer qualité contre poids sur le WebM ; `-movflags +faststart` place les métadonnées en tête de fichier pour que le MP4 démarre sa lecture avant la fin du téléchargement ; `-pix_fmt yuv420p` et le `scale` associé évitent une erreur d'encodage sur les dimensions impaires, fréquente sur les GIF exportés depuis un outil de capture d'écran. En pratique, fournir les deux formats via la balise `<source>` (WebM en premier, MP4 en repli) permet à chaque navigateur d'utiliser le plus léger qu'il supporte :
  ```html
  <video autoplay loop muted playsinline>
    <source src="fichier.webm" type="video/webm">
    <source src="fichier.mp4" type="video/mp4">
  </video>
  ```

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques est le seul des six référentiels consultés à citer **explicitement et nommément le critère 4.1** du RGESN, dans deux sections distinctes :

- [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons) : « Désactiver la lecture automatique des vidéos et des sons permet de valider en partie le critère 4.1 du référentiel général de l'écoconception des services numériques. » Le guide rappelle que la vidéo en ligne représente **60 à 90 % du trafic internet**, et illustre le coût de l'autoplay par des cas mesurés : une page avec vidéo en fond a transféré plus de **17,8 Mo** de données avant même le moindre défilement (exemple Hennessy), et la page d'accueil de La Chaîne Météo atteignait **13,7 Mo** avec une vidéo en lecture automatique. Le guide ajoute un argument souvent oublié : désactiver l'autoplay profite aussi à l'accessibilité, en particulier pour les utilisateurs de lecteurs d'écran perturbés par un son ou une vidéo qui démarre sans prévenir.
- [**7.3 Animations**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-3-animations) : reprend l'interdiction des graphismes animés non contrôlables (GIF en particulier) et impose des moyens de contrôle dès qu'une animation visuelle dépasse **5 secondes** ou qu'un son dépasse **3 secondes** — des seuils très proches mais légèrement plus permissifs que ceux du RGESN (4 et 2 secondes), qui correspondent en réalité au seuil de 5 secondes du [critère WCAG 2.2.2 « Pause, Stop, Hide »](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html) (niveau A). Le guide relie aussi ce sujet au critère voisin 4.6 : une animation qui n'apporte aucune information utile est un candidat direct à la suppression pure et simple, plutôt qu'à l'ajout de contrôles.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent ce critère à travers trois recommandations complémentaires :

- [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) : « Disable autoplay for audio, video, and other media by default. Ensure users can control playback and resolution. Inform users about media length, format, and expected data use. »
- [**« Ensure animation is proportionate and easy to control »**](https://www.w3.org/TR/web-sustainability-guidelines/#ensure-animation-is-proportionate-and-easy-to-control) : « Let users start, pause, stop, or control animated and moving content » et limiter le nombre et la fréquence des animations pour réduire la distraction et la charge de rendu.
- [**« Use media queries that support sustainability goals »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-media-queries-that-support-sustainability-goals) : recommande d'exploiter la media query CSS `prefers-reduced-motion`, qui permet de désactiver ou d'atténuer automatiquement les animations pour les utilisateurs ayant explicitement demandé cette préférence au niveau du système d'exploitation — une mise en œuvre technique directe du contrôle utilisateur demandé par le critère.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Pour appliquer concrètement les seuils du critère (contrôles obligatoires au-delà de 4 secondes pour une animation visuelle, 2 secondes pour un son) :

- **Respecter la préférence système de l'utilisateur** via la media query CSS `prefers-reduced-motion`, citée par le W3C ci-contre :
  ```css
  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```
- **Ne jamais déclencher un média sans action explicite**, en combinant l'absence d'`autoplay` et `preload="none"` (RWEB 0106 ci-contre) — la mise en pause hors du champ de vision peut se faire simplement via l'[Intersection Observer API](https://developer.mozilla.org/fr/docs/Web/API/Intersection_Observer_API), native au navigateur, sans bibliothèque tierce, pour répondre au critère GR491 sur les vidéos hors zone active.
- **S'appuyer sur un standard d'accessibilité existant plutôt que de réinventer un seuil** : le [critère WCAG 2.2.2 « Pause, Stop, Hide »](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html) (niveau A, obligatoire pour tout site public en France au titre du RGAA) impose déjà un mécanisme de pause/arrêt/masquage pour tout contenu en mouvement de plus de 5 secondes présenté en parallèle d'autre contenu — un contrôle d'accessibilité déjà en place peut donc, à quelques secondes de seuil près, couvrir une bonne partie de l'exigence d'écoconception du critère 4.1.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec la justification la plus simple possible : « Le service numérique ne propose pas de contenus à base d'animations, de vidéos, ou de sons. » Un cas qui rappelle que la meilleure façon de respecter ce critère reste, comme souvent en écoconception, de ne pas avoir à se poser la question : un service de consultation de données textuelles n'a simplement pas ce risque à gérer, contrairement à un site à forte dimension éditoriale ou marketing.

{{% /tab %}}

{{< /tabs >}}
