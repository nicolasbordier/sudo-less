---
weight: 800
title: "4.8 - Limitation des polices de caractères téléchargées"
description: "Critère 4.8 du RGESN : pourquoi et comment limiter le nombre et le poids des polices de caractères téléchargées, en privilégiant les polices nativement disponibles."
icon: "font_download"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique limite-t-il le nombre des polices de caractères téléchargées ?

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
| **Critère**  | `4.8` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas de texte` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.8/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Le téléchargement de polices de caractères peut alourdir un service numérique et les ressources informatiques nécessaires à son fonctionnement. Minimiser le nombre de polices téléchargées permet d'accélérer le chargement du service numérique, de potentiellement diminuer les transferts de données à des tiers et de réduire l'empreinte environnementale du service.

L'objectif est donc de limiter le nombre de polices de caractères utilisées pour privilégier, lorsque cela est possible, des polices nativement disponibles, afin de ne pas avoir besoin d'un téléchargement spécifique de la police utilisée. Il s'agit également de réduire la taille des polices téléchargées.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Se fixer comme objectif de n'utiliser au maximum que deux polices différentes et au maximum quatre variantes au total par page ou « unité d'affichage » si la pagination n'est pas utilisée (ou si un seuil par taille de fichier est plus adapté, viser une taille maximale de 400 Ko pour les polices téléchargées). Vérifier la compression des polices ou l'usage des glyphes nécessaires. Dans un contexte de site web, prêter aussi attention sur le mode de chargement : bloquant, non bloquant…

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le nombre et le poids des polices de caractères utilisées sont à évaluer. Le critère est validé si les polices téléchargées pour le service respectent au moins l'une de ces conditions :

- Le nombre de polices téléchargées est limité à deux (avec au maximum quatre variantes au total) par page ou « unité d'affichage » (si la pagination n'est pas utilisée pour le service) ;
- La taille des polices téléchargées ne dépasse pas 400 Ko par page ou « unité d'affichage ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le critère 4.8 rejoint la même [recommandation n°8 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=8) du [GR491](https://gr491.isit-europe.org/) (INR), « Ingénierie média », déjà citée pour le [critère 4.6](../4-6_contenu-porteur-information/) sur ce site, mais via l'un de ses autres critères : « Le nombre de polices de caractères (fonts) et les variantes de polices appelées (graisse, caractères utilisés dans le projet) sont-ils limités ? ». Une même recommandation GR491 couvre ainsi deux critères RGESN distincts (4.6 et 4.8), preuve que le référentiel INR regroupe par famille de sujet (ici : l'ingénierie des médias) plutôt que critère par critère.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe : la fiche [**RWEB 0032 — « Favoriser les polices standards »**](https://rweb.greenit.fr/fr/fiches/RWEB_0032-favoriser-les-polices-standards) recommande de préférer les polices déjà présentes sur le terminal de l'utilisateur (listées sur [systemfontstack.com](https://www.systemfontstack.com/)) pour éviter tout téléchargement. Si une police personnalisée reste nécessaire, la fiche recommande de l'auto-héberger, de privilégier les polices variables, et propose un exemple concret de chargement conditionnel via une media query CSS :

```css
@media (prefers-reduced-data: no-preference) {
  @font-face {
    font-family: "Montserrat";
    src: url("montserrat.woff2") format("woff2");
  }
}
```

Avec ce code, la police Montserrat n'est téléchargée que si l'utilisateur n'a pas activé sa préférence de réduction des données ; dans le cas contraire, une police système (Arial par exemple) s'affiche sans aucun téléchargement. Principe de validation retenu par RWEB : le nombre de polices téléchargées doit être inférieur ou égal à deux — exactement le seuil du critère RGESN.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement et avec les mêmes seuils numériques** le critère 4.8 dans sa section [**7.4 Polices**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-4-polices) : 

- « Limiter le nombre de polices téléchargées à 2 et à 400 Ko maximum permet de valider le critère 4.8 ». 

Le guide recommande de se limiter à 1 ou 2 polices (par exemple une pour les titres, une pour le corps de texte), et cite un chiffre qui contextualise l'enjeu : **le poids moyen d'une police web est de 138 Ko**, une valeur qui a doublé depuis 2010. Il recommande le format **WOFF2** (le plus compressé disponible) et les polices sans-serif pour l'accessibilité, tout en rappelant que les polices système les plus courantes (Arial, Georgia, Times New Roman) sont préinstallées sur la quasi-totalité des systèmes depuis 2009-2011.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont une fiche dédiée, [**« Use optimized web typography »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-optimized-web-typography), déjà mentionnée au critère 2.9 sur ce site : « Limit the number and complexity of downloaded fonts. When using variable fonts, restrict supported axes and ranges to only those required by the project to reduce file size. » 

Elle ajoute un levier que le RGESN ne détaille pas explicitement : 

- « Remove unused font styles, weights, and character sets. Subset fonts based on explicitly supported languages, scripts, and Unicode ranges required by the project. » 

Pour du contenu dynamique ou saisi par l'utilisateur où le sous-ensemble de caractères ne peut être connu à l'avance, l'usage de l'**Incremental Font Transfer (IFT)**, qui ne charge que les segments de police réellement nécessaires, à la demande.

L'**IFT** ([spécification W3C](https://www.w3.org/TR/IFT/), au stade de *Candidate Recommendation*) répond précisément à la limite du sous-ensemble statique évoqué ci-dessus (via pyftsubset/glyphhanger dans l'onglet "Mise en oeuvre technique") : celui-ci doit être généré à l'avance en connaissant les caractères utilisés, ce qui devient impossible pour du contenu généré par les utilisateurs ou dans des langues à très grand nombre de glyphes (Chinois, japonais et coréen notamment, plusieurs milliers de caractères). L'IFT fonctionne selon deux méthodes :

- **Patch Subset** : le serveur ne conserve du fichier de police que ce que le client a déjà téléchargé, puis génère à la volée un patch binaire entre ce sous-ensemble existant et le sous-ensemble étendu requis par le nouveau texte à afficher — seul ce patch, généralement de quelques Ko, est transféré.
- **Range Request** : s'appuie sur les requêtes HTTP par plage (`Range`) pour ne récupérer que les octets nécessaires dans le fichier de police d'origine.

Le W3C a constaté que Patch Subset est globalement plus efficace que Range Request, en performance comme en volume de données transférées. **Point de vigilance** : à la date de rédaction de cette fiche, l'IFT n'est pas encore largement supporté par les navigateurs — l'implémentation dans Chrome était encore en cours en 2026. C'est une technologie à surveiller plutôt qu'à déployer en production dès aujourd'hui, en particulier pour des services à fort besoin d'internationalisation.

{{% /tab %}}

{{% tab tabName="Gauthier Roussilhe" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le [guide d'écoconception rédigé par Gauthier Roussilhe et son équipe pour l'ADEME](https://gauthierroussilhe.com/book/ademe/FONT.html) (accompagnement de la startup d'État « Territoires en Transitions », 2020-2022) recommande, dans sa fiche dédiée aux polices, un trio suffisant pour la quasi-totalité des besoins : « un trio regular + italique + gras, combiné à une gamme restreinte de corps typographiques et de couleurs, suffisent amplement ». 

Le guide met en avant la stratégie du **System Font Stack** (utiliser en priorité les polices déjà installées par le système d'exploitation) comme valeur par défaut de `font-family`, recommande le format **WOFF2**, et rappelle le principe du sous-ensemble de glyphes : « Plus le nombre de glyphes sera faible, plus le fichier de police sera léger ». Il cite un exemple chiffré tiré d'une étude de cas Shopify : la seule mise en place du préchargement (`preload`) des polices a permis un gain de **50 %** sur la vitesse de chargement.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Pour synthétiser les recommandations ci-contre en un exemple concret, une déclaration de police personnalisée conforme aux seuils du critère combine format compressé, sous-ensemble de caractères et stratégie de chargement non bloquante :

```css
@font-face {
  font-family: "MaPolice";
  src: url("mapolice-subset.woff2") format("woff2");
  font-display: swap;
  unicode-range: U+0000-00FF; /* sous-ensemble latin de base uniquement */
}
```

- **`format("woff2")`** : le format le plus compressé, cité par les Designers Éthiques et Gauthier Roussilhe.
- **`unicode-range`** : ne déclenche le téléchargement que si le texte affiché contient effectivement des caractères de la plage définie — mais cette déclaration seule ne réduit pas le poids du fichier lui-même, elle ne fait qu'indiquer au navigateur dans quel cas aller le chercher.
- **`font-display: swap`** : affiche immédiatement le texte avec une police de repli (système) le temps que la police personnalisée se charge, plutôt que de bloquer l'affichage — la traduction technique du « mode de chargement non bloquant » demandé par la « Mise en œuvre » du critère RGESN.

Pour que le fichier `mapolice-subset.woff2` soit réellement plus léger (et pas seulement déclaré comme tel), encore faut-il l'avoir généré par un **sous-ensemble (subset)** ne contenant que les glyphes réellement utilisés — l'usage du sous-ensemble de glyphes recommandé par le W3C et Roussilhe ci-contre. Deux outils courants :

- [**pyftsubset**](https://fonttools.readthedocs.io/en/latest/subset/) (module `fontTools`, Python — `pip install fonttools brotli`) génère directement un fichier ne contenant que les caractères demandés :
  ```bash
  pyftsubset police-complete.ttf \
    --unicodes="U+0020-007E" \
    --flavor=woff2 \
    --output-file="mapolice-subset.woff2"
  ```
  La plage `U+0020-007E` correspond aux caractères ASCII imprimables de base (lettres non accentuées, chiffres, ponctuation) — à élargir selon la langue réelle du contenu (`U+00C0-00FF` pour les caractères accentués français, par exemple).
- [**glyphhanger**](https://github.com/zachleat/glyphhanger) (créé par Zach Leatherman) automatise l'étape précédente en amont : il **analyse directement une ou plusieurs pages du service** pour détecter les caractères effectivement affichés, puis génère le sous-ensemble correspondant via pyftsubset en interne — évitant de deviner à la main la bonne plage `--unicodes`.

Le sous-ensemble ainsi produit peut ensuite être servi avec la déclaration `unicode-range` correspondante : les deux mécanismes sont complémentaires, l'un réduit le poids du fichier, l'autre évite de le télécharger quand il n'est pas nécessaire.

Et pour ne recourir à aucun téléchargement, la pile de polices système (« System Font Stack ») citée par RWEB et Gauthier Roussilhe :

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
```

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec une précision intéressante : « L'analyse montre que seules deux polices sont téléchargées et concerne uniquement des icônes : Fontawesome, Prime Icons (Angular). » Ce cas illustre une nuance que le critère ne traite pas explicitement : les deux « polices » comptabilisées ne sont pas des polices de texte à proprement parler, mais des **polices d'icônes** ([Font Awesome](https://fontawesome.com/), PrimeIcons).

À nuancer toutefois : ce n'est pas Font Awesome en tant que tel qui pose problème, mais le **mode de livraison** choisi ici — le webfont CSS classique, qui télécharge l'intégralité du jeu d'icônes pour n'en afficher qu'une poignée. Font Awesome propose lui-même une alternative plus sobre, son mode **SVG + JS**, qui permet, avec un bundler compatible (Webpack, Rollup) et des imports ES6 explicites (`import { faCoffee } from '@fortawesome/free-solid-svg-icons'`), de ne charger dans le bundle final que les icônes réellement importées — un *tree-shaking* qui atteint le même objectif de sobriété que des SVG à la demande, sans changer de bibliothèque.

{{% /tab %}}

{{< /tabs >}}
