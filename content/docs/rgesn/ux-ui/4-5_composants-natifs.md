---
weight: 500
title: "4.5 - Composants fonctionnels natifs"
description: "Critère 4.5 du RGESN : pourquoi et comment privilégier les composants fonctionnels natifs du système d'exploitation, du navigateur ou du langage, plutôt que des composants développés en surcouche."
icon: "layers_clear"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il majoritairement des composants fonctionnels natifs du système d'exploitation, du navigateur ou du langage utilisé ?

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
| **Critère**  | `4.5` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Les composants fonctionnels sont par exemple des composants d'interface (menu, bouton, formulaire…). Généralement, les composants natifs d'un système n'ont besoin que de peu de ressources pour fonctionner, contrairement à des composants développés en surcouche. Dans cette perspective, il peut donc être préférable d'encourager l'utilisation de composants natifs d'un système plutôt que le recours à des composants développés en surcouche.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Privilégier l'utilisation des composants fonctionnels natifs du système d'exploitation, du navigateur ou du langage utilisé pour répondre au besoin.

En complément, il est préférable de ne charger les ressources et les composants que lorsqu'ils sont effectivement utilisés.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service favorise le recours à des composants fonctionnels natifs lorsque cela est possible.

De plus, dans l'éventualité du recours à des composants non natifs, il convient d'évaluer la nécessité d'utiliser ces composants (contraintes techniques par exemple) et, le cas échéant, de documenter dans la déclaration d'écoconception les raisons de les utiliser. Leur recours devra être régulièrement suivi en vérifiant le contenu des ressources chargées et leur utilisation effective.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le critère 4.5 rejoint la [recommandation n°3 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Utiliser les environnements et outils qui permettent de limiter les impacts » — déjà citée à la page [critère 2.9](../../specifications/2-9_composants-interface/) sur ce site. La question posée est directement transposable : « Est-ce que la fonctionnalité attendue ne pourrait pas être mise en place avec les capacités natives du navigateur ? » Cette recommandation cadre bien la logique du critère : avant de charger une bibliothèque ou un design system pour un composant donné, la première question à se poser reste de vérifier si un équivalent HTML natif ne suffirait pas déjà.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent ce critère à travers deux recommandations complémentaires :

- [**« Use the most efficient solution for your service »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-the-most-efficient-solution-for-your-service) : « Favor native components and file systems over WYSIWYG editors, visual page builders, or heavy frameworks. Be mindful of the performance, maintenance, and environmental impact of third-party solutions. » La même fiche recommande de livrer du contenu statique plutôt que dynamique lorsque c'est possible, et de privilégier les générateurs de site statique (SSG) lorsqu'une génération de code reste nécessaire — par exemple [Hugo](https://gohugo.io/) (le générateur utilisé par ce site même, en Go, connu pour la rapidité de ses builds), [Eleventy](https://www.11ty.dev/) (zéro JavaScript côté client par défaut, sans imposer de framework) ou [Astro](https://astro.build/) (architecture en « îlots » : zéro JS par défaut, seuls les composants explicitement interactifs sont hydratés côté client) — ce dernier illustre particulièrement bien le « ne charger les composants que lorsqu'ils sont effectivement utilisés » demandé par la « Mise en œuvre » du critère RGESN.
- [**« Use dependencies sparingly and maintain them »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-dependencies-sparingly-and-maintain-them) : « Limit the use of external libraries and frameworks to what is necessary, as this reduces the amount of code that must be downloaded and parsed by the browser. Prioritize plain code where possible. »

{{% /tab %}}

{{% tab tabName="Gauthier Roussilhe" %}}

Profil(s) métier concerné(s) : `Développeur`

Le sujet est traité de façon plus nuancée que le RGESN dans le [guide d'écoconception rédigé par Gauthier Roussilhe et son équipe](https://gauthierroussilhe.com/book/ademe/JS.html) pour le compte de l'[ADEME](https://www.ademe.fr/), dans le cadre de l'accompagnement de la startup d'État « Territoires en Transitions » (2020-2022). Sur le choix d'une librairie JavaScript, le guide relativise l'opposition tranchée entre natif et framework : « La manipulation du DOM est une opération coûteuse, que ce soit en Vanilla JavaScript (sans framework) ou à l'aide d'un framework » — le vanilla JS reste généralement plus performant, mais le choix d'un framework ne devrait pas se réduire à ce seul critère de performance brute.

Sa recommandation pratique rejoint néanmoins directement le « Moyen de test » du critère RGESN sur le recours documenté aux composants non natifs : lorsqu'une bibliothèque est malgré tout utilisée, vérifier si elle propose un découpage permettant de n'importer que les modules effectivement nécessaires plutôt que la bibliothèque dans son ensemble.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Quelques équivalents HTML natifs, souvent ignorés au profit d'une bibliothèque JavaScript, pour les composants d'interface les plus courants :

| Besoin | Composant non natif courant | Équivalent natif |
|---|---|---|
| Fenêtre modale | Bibliothèque de modales (React Modal, etc.) | [`<dialog>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/dialog) |
| Contenu repliable / accordéon | Composant accordéon JS | [`<details>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/details) / `<summary>` |
| Auto-complétion de champ | Bibliothèque d'autocomplete | [`<datalist>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/datalist) |
| Barre de progression | Composant JS animé | [`<progress>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/progress) |
| Sélecteur de date | Datepicker JS | `<input type="date">` |
| Validation de formulaire | Bibliothèque de validation | attributs natifs `required`, `pattern`, `min`/`max` |

Pour les cas où un vrai composant réutilisable est nécessaire et qu'aucun élément HTML natif ne convient, les [**Web Components**](https://developer.mozilla.org/fr/docs/Web/API/Web_components) (Custom Elements, Shadow DOM, HTML Templates) permettent d'obtenir la réutilisabilité d'un framework sans en payer le poids : le support natif de ces trois specs atteint aujourd'hui 98,7 % des navigateurs, et le Shadow DOM déclaratif permet désormais un rendu initial sans JavaScript côté client. C'est une option à considérer avant d'ajouter un framework complet pour un besoin de composant isolé.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Ce critère est le pendant « composant par composant » du [critère 2.9](../../specifications/2-9_composants-interface/) (composants d'interface prêts à l'emploi), déjà publié sur ce site : le 2.9 porte sur la **comparaison des impacts environnementaux** entre plusieurs composants ou design systems équivalents une fois le choix fait de ne pas utiliser de solution native, tandis que le 4.5 porte sur l'étape logiquement antérieure — se demander si un composant natif ne suffirait pas avant même d'envisager cette comparaison. Un design system peut être le plus sobre de sa catégorie au sens du critère 2.9, tout en restant non conforme au 4.5 s'il remplace systématiquement des éléments qu'un simple HTML natif aurait suffi à couvrir.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec une justification concise : « Aucun recours à des composants non natifs n'ont été détectés pour ce service numérique web. » Un des rares critères de cette déclaration validé sans nuance ni réserve, ce qui en dit aussi long sur la simplicité fonctionnelle du service audité (principalement des pages de consultation de données) que sur un effort de conception spécifique autour de ce critère.

{{% /tab %}}

{{< /tabs >}}
