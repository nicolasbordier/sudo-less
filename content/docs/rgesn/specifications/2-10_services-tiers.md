---
weight: 1000
title: "2.10 - Impacts environnementaux des services tiers"
description: "Critère 2.10 du RGESN : pourquoi et comment prendre en compte les impacts environnementaux des services tiers (analytics, vidéo, réseaux sociaux, captcha…) lors de leur sélection."
icon: "hub"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il pris en compte les impacts environnementaux des services tiers utilisés lors de leur sélection ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Spécifications` |
| **Critère**  | `2.10` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur des services tiers` |
| **Métiers concernés** | `Responsable Partenariats` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.10/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Les services de tiers sont des services proposés par des fournisseurs externes (développeurs, organismes ou entreprises) apportant des fonctionnalités prêtes à l'emploi (par exemple suivi d'audience, lecteur vidéo, fil d'actualité des réseaux sociaux, mécanisme de captcha…) et évitant ainsi de les redévelopper en interne. L'objectif est donc de réduire les impacts environnementaux des services tiers, donc non issus de développement interne.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Le plus souvent, une mesure d'outils analytiques A/B test permet de connaître les impacts environnementaux d'un service tiers afin d'aider à la prise de décision sur le facteur environnemental. Les mesures fournies par le service tiers sont aussi à prendre en compte pour effectuer des évaluations ou comparatifs validant le choix effectué.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Contrôler la mise en œuvre. Plus spécifiquement, il pourra être vérifié si les services tiers sur lesquels le service numérique repose valident les critères suivants :

- Pour tous les services tiers fournis, validation des critères 1.4 et 1.5 ;
- De façon complémentaire :
  - Si le service tiers analysé est une vidéo, validation des critères 4.4, 4.11, 4.12, 4.15, 5.3, 5.4 et 5.5 ;
  - Si le service tiers analysé est un réseau social, validation des critères 4.1, 4.6, 4.9, 4.12, 4.13 et 4.15 ;
  - Si le service tiers analysé est un générateur d'image, validation des critères 4.6, 4.11, 4.12, 4.13 et 4.15.

Les services tiers utilisés sont à lister, en renseignant leur avancement au regard de ces critères (si applicables), dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Le critère 2.10 rejoint un des critères de la [recommandation n°5 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=5) du [GR491](https://gr491.isit-europe.org/) (INR), « "Less is More" : concentrez-vous sur les fonctionnalités essentielles et simplifiez votre interface » : « Est-ce que les services tiers (fils réseaux sociaux, social wall, carrousels, Google Maps etc.) ne sont pas utilisés par facilité pour pallier le manque de ressources de production de contenus ? »

Cette question précède logiquement celle du critère 2.10 : avant même de comparer les impacts environnementaux de deux services tiers, la première option à évaluer reste de se passer du service tiers lorsqu'il n'est là que par confort.

{{% /tab %}}

{{% tab tabName="Critères associés" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Le « Moyen de test » du critère 2.10 renvoie vers une dizaine d'autres critères RGESN, ce qui en fait l'un des critères les plus transversaux du référentiel :

- Pour **tout** service tiers : les critères [1.4](../../strategie/1-4_revue-ecoconception/) (revue d'écoconception) et [1.5](../../strategie/1-5_objectifs-environnementaux/) (objectifs environnementaux) s'appliquent systématiquement — le service tiers doit être traité comme une brique du service numérique à part entière, pas comme une boîte noire externe qu'on peut ignorer.
- Selon le **type** de service tiers, des critères UX/UI et médias supplémentaires s'appliquent (vidéo : 4.4, 4.11, 4.12, 4.15, 5.3, 5.4, 5.5 ; réseau social : 4.1, 4.6, 4.9, 4.12, 4.13, 4.15 ; générateur d'image : 4.6, 4.11, 4.12, 4.13, 4.15). Ces portent notamment sur la lecture automatique, le chargement différé et le poids des médias.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe avec ce critère : la fiche [**RWEB 0059 — « Remplacer les boutons officiels de partage des réseaux sociaux »**](https://rweb.greenit.fr/fr/fiches/RWEB_0059-remplacer-les-boutons-officiels-de-partage-des-reseaux-sociaux) constate que les plug-ins officiels Facebook, X ou Pinterest sont des bibliothèques JavaScript lourdes à télécharger et génératrices de nombreuses requêtes, et recommande de les remplacer par un lien HTML direct vers la page de partage, par exemple :

```html
<button type="button" onclick="window.open('https://www.facebook.com/sharer/sharer.php?u=XXXXX', '', 'menubar=no, toolbar=no, resizable=yes, scrollbars=yes, height=500, width=700')">
    Je partage cette page sur Facebook
</button>
```

La fiche précise elle-même que cette bonne pratique « ne se limite pas aux réseaux sociaux » — le même principe (lien direct plutôt que widget embarqué) s'applique aux autres services tiers évoqués ci-contre.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le chapitre [« 7.5 Plugins et widgets (service tiers) »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-5-plugins-et-widgets) du guide des Designers Éthiques cite explicitement les critères **2.10 et 4.4** du RGESN. Il recommande de limiter l'utilisation de widgets et plugins (icônes de réseaux sociaux, Google Maps, vidéos incrustées…) et donne un exemple chiffré parlant : le plugin Google Maps pèse à lui seul environ 1 Mo, à comparer avec la valeur réelle qu'il apporte à l'utilisateur.

Trois questions posées par le guide, directement transposables en checklist : Est-ce que tous les utilisateurs ont besoin de cette carte ? Sa valeur ajoutée justifie-t-elle son poids ? Un simple lien ne suffirait-il pas pour les utilisateurs réellement intéressés ? Comme alternative à Google Maps, le guide suggère un lien vers [OpenStreetMap](https://www.openstreetmap.org/) ou Qwant Maps plutôt qu'un plugin intégré.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont une recommandation qui recoupe le critère 2.10 presque point par point, [**« Treat third parties the same as first parties »**](https://www.w3.org/TR/web-sustainability-guidelines/#treat-third-parties-the-same-as-first-parties) : passer en revue les contenus et services tiers (plugins, widgets, feeds, cartes, carrousels, scripts de tracking) dès la conception, en utiliser le moins possible en préférant les options les plus légères, et exiger des fournisseurs tiers les mêmes standards de conformité, sécurité et rétention de données que pour le code interne.

La guideline ajoute deux points concrets qui recoupent les autres onglets de cette fiche : ne charger le contenu tiers qu'au moment où l'utilisateur interagit avec lui (plutôt qu'au chargement de la page), et privilégier des alternatives simples comme un lien vers un formulaire plutôt que d'embarquer un widget complet.

{{% /tab %}}

{{% tab tabName="Alternatives légères" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Pour les familles de services tiers les plus courantes, des alternatives plus sobres et souvent plus respectueuses de la vie privée existent :

- **Analytics** : [Matomo](https://matomo.org/) (open source, auto-hébergeable, conforme RGPD nativement) reste plus lourd (~22 Ko gzippé) que [Plausible](https://plausible.io/) (~2,5 Ko gzippé, sans cookies) ou [Umami](https://umami.is/) (open source, auto-hébergeable, minimaliste) — un facteur x9 sur le seul script de suivi, avant même de compter les requêtes réseau évitées par l'absence de bannière cookie.
- **Vidéo** : un lecteur YouTube embarqué classique charge environ 1,3 Mo dès l'affichage de la page, contre une centaine de Ko pour [lite-youtube-embed](https://github.com/paulirish/lite-youtube-embed) (Paul Irish), qui n'affiche qu'une vignette cliquable et ne charge le lecteur complet qu'au clic — un audit cité par Frontend Masters a mesuré jusqu'à 9,7 Mo attribuables aux lecteurs YouTube embarqués sur une page de 20 Mo.
- **Captcha** : [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) et [hCaptcha](https://www.hcaptcha.com/) sont plus légers que reCAPTCHA et ne reposent pas sur le profilage comportemental publicitaire de Google.

Ces alternatives rejoignent directement la logique du GR491 ci-contre : avant de comparer plusieurs services tiers entre eux, il est souvent possible de choisir une alternative structurellement plus légère pour la même fonction.

{{% /tab %}}

{{% tab tabName="Outils de mesure" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Pour objectiver le poids réel des services tiers déjà en place plutôt que de le découvrir a posteriori, [Request Map Generator](https://requestmap.webperf.tools/) (Simon Hearne, basé sur l'API WebPageTest) génère une carte interactive de toutes les requêtes déclenchées par une page, en distinguant les domaines internes des domaines tiers et les requêtes que ces derniers déclenchent à leur tour en cascade — utile pour visualiser concrètement l'ampleur des services tiers avant de statuer sur leur avancement au regard des critères ci-dessus.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non applicable »** — une évaluation différente des « Non validé » habituels sur ce même service. Leur justification : « Le service numérique s'appuie sur le service tiers interne Chorus (par API), pour : Batchs, Vérifications diverses. Aucune étude d'impact environnementale n'existe à ce jour sur ce service tiers. Cependant, ce service n'est pas public et fournit des informations détenues uniquement par lui. »

Ce cas illustre une zone grise du critère : Chorus (plateforme interministérielle de facturation) est un service tiers au sens technique (externe à l'équipe projet), mais interne à l'État au sens organisationnel, sans étude d'impact publique disponible et sans levier réel pour en changer. FACE en conclut logiquement une non-applicabilité plutôt qu'une non-conformité — à la différence d'un service tiers commercial (analytics, vidéo, réseau social) où un choix alternatif reste possible.

[Alt Impact](https://altimpact.fr/ecoconception-du-site/) (site porté par l'ADEME, audit Conserto) marque quant à lui ce critère **« Non validé »** de façon nette, en nommant précisément les deux services tiers en cause : « L'intégration de deux services tiers impactants sont à questionner : Google Tag Manager, Calculateur d'impact impactco2.fr. » Ce cas complète directement le [critère 2.9](../2-9_composants-interface/) sur ce même service, où le même calculateur impactco2.fr est identifié comme mal optimisé (66 requêtes, 2 Mo) — les deux critères convergent ici vers le même composant tiers problématique, illustrant qu'un seul widget mal intégré peut faire échouer plusieurs critères RGESN à la fois.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent ce critère « Validé » avec un périmètre volontairement restreint à deux services tiers, chacun justifié individuellement : Matomo, auto-hébergé sur leur propre serveur avec l'option d'archivage activée pour éviter toute surcharge de la base de données, et Mailchimp, sollicité uniquement via un appel API ponctuel lorsqu'un·e visiteur·se s'inscrit à la newsletter. Un nombre de services tiers réduit à l'essentiel, plutôt qu'une accumulation progressive et non questionnée — la même logique que celle défendue par le GR491 ci-contre.

{{% /tab %}}

{{< /tabs >}}
