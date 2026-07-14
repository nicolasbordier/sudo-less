---
weight: 500
title: "2.5 - Terminaux d'affichage"
description: "Critère 2.5 du RGESN : pourquoi et comment adapter un service numérique à différents types de terminaux d'affichage (responsive design), pour limiter le renouvellement de matériel."
icon: "responsive_layout"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique s'adapte-t-il à différents types de terminaux d'affichage ?

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
| **Critère**  | `2.5` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service ne propose pas d'interface utilisateur sur écran` |
| **Métiers concernés** | `Développeur` `Responsable IT` `UX Designer` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Le service numérique devrait participer à **limiter l'achat de nouveaux terminaux** en fonctionnant sur des équipements aux **dimensions d'écran variées**, dont les plus petites (smartphones anciens par exemple). La possibilité pour un service numérique de s'adapter aux écrans avec une faible définition peut contribuer à lutter contre l'**obsolescence des équipements induite par le logiciel**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Uniquement lorsque cela est applicable, rendre l'interface du service numérique **adaptable à la taille de l'écran sans perte d'utilisabilité** (« responsive design »).

Dans l'objectif d'éviter la multiplication des terminaux pour accéder à différents services, il est recommandé que les services numériques soient **adaptatifs** et capables de s'afficher parfaitement sur le petit écran d'un mobile comme sur le grand écran d'un PC. Il vaut mieux éviter de **dupliquer le service numérique** avec une version spécifique pour chaque terminal. Il est également préférable que les menus soient **utilisables en mode tactile tout autant que via un clavier**.

Lorsque c'est pertinent, le développement du design de la version mobile en premier (**mobile first**) peut permettre l'adoption d'une interface plus sobre.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Tester les fonctionnalités critiques du service numérique sur différentes tailles d'affichage (ordinateur de bureau, tablette et mobile) :

- Le service doit adapter son mode d'affichage de manière dynamique selon la taille de l'écran (« responsive web design »).
- Vérifier que les différents composants de type menus soient accessibles via tout type d'interface, y compris tactile ou non, avec ou sans souris.
- S'assurer de l'affichage complet du service dans une zone de visualisation de **1 200 pixels de large** (ce qui correspond à la définition des écrans d'ordinateurs standard de 17 pouces au format 5/4 avec 80 pixels utilisés par une barre de lancement).
- Pour les interfaces qui ne permettent pas de faire défiler de haut en bas l'affichage, vérifier l'affichage complet du service dans une zone de visualisation de **720 pixels de hauteur** (écrans d'ordinateur de 800 pixels de haut, avec 80 pixels utilisés par une barre de lancement).

Le critère est **validé** si les conditions susmentionnées sont remplies. Les tests effectués sont à documenter dans la **déclaration d'écoconception**.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `UX Designer`, `Développeur`

Le chapitre [« Concevoir en mobile first »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/5-concevoir-en-mobile-first) du guide des Designers Éthiques cite explicitement ce critère : « Concevoir un service **responsive**, autrement dit s'adaptant à différents types de terminaux d'affichage, permet de valider le critère 2.5 ». 

Concevoir d'abord pour mobile plutôt que pour desktop contraint l'équipe à se concentrer sur l'essentiel dès la conception, ce qui réduit à la fois les fonctionnalités superflues et l'empreinte environnementale — plutôt que d'ajouter après coup une adaptation mobile à une interface pensée pour desktop.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `UX Designer`, `Responsable IT`

Le critère 2.5 recoupe partiellement la [recommandation n°3 de la famille UX-UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Rendre disponible et accessible le service numérique au plus grand nombre d'utilisateurs » : une stratégie de compatibilité avec les terminaux est-elle définie ? 

Les versions cibles (appareils, OS, navigateurs) sont-elles précisées dans les personas ? 

Cette recommandation élargit la question au-delà du seul responsive design, en la reliant à l'inclusivité générale d'accès au service.

{{% /tab %}}

{{% tab tabName="Patterns UX" %}}

Profil(s) métier concerné(s) : `UX Designer`, `Développeur`

Des patterns de navigation éprouvés permettent de concevoir « mobile first » sans dupliquer l'interface par terminal :

- **[Priority+](https://bradfrost.com/blog/post/revisiting-the-priority-pattern/)** (Brad Frost) : n'afficher que les liens de navigation prioritaires, et regrouper le reste derrière un bouton « Plus » — le nombre de liens visibles augmente automatiquement avec l'espace disponible, sans jamais dupliquer le menu par taille d'écran. Exemple réel : la navigation par rubriques du site du Guardian.
- **Tab bar / navigation hub** plutôt que **menu hamburger** dès que possible : selon les études [Nielsen Norman Group](https://www.nngroup.com/articles/hamburger-menus/), masquer la navigation derrière une icône réduit sa découvrabilité de plus de 20 % par rapport à une navigation visible ou partiellement visible — un coût à mettre en balance avec le gain d'espace à l'écran, en particulier sur les petits terminaux visés par ce critère.
- **Cibles tactiles dimensionnées** : au moins 44×44 points ([Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)) ou 48×48 dp ([Material Design](https://m2.material.io/develop/web/supporting/touch-target)) pour tout élément cliquable — un prérequis direct à l'exigence du critère que « les menus soient utilisables en mode tactile tout autant que via un clavier ».

{{% /tab %}}

{{% tab tabName="Techniques Front" %}}

Profil(s) métier concerné(s) : `Développeur`

Côté implémentation, quatre techniques permettent de construire un site réellement adaptatif plutôt que d'empiler des correctifs par terminal :

- **Media queries en mobile first** (`min-width`) : écrire d'abord le CSS de base pour le petit écran, puis surcharger progressivement pour les écrans plus grands, plutôt que l'inverse (`max-width` en partant du desktop). Le navigateur mobile ne télécharge et n'applique alors que le strict nécessaire, sans règles pensées pour desktop à annuler.
- **Unités relatives et layouts flexibles** (`%`, `rem`, `clamp()`, Flexbox, CSS Grid) plutôt que des dimensions fixes en pixels : le contenu se réorganise nativement selon l'espace disponible, sans dupliquer les règles à chaque nouveau palier de largeur.
- **[Images responsives](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)** (`srcset`, `sizes`, `<picture>`) : servir une image dimensionnée pour l'écran réel de l'utilisateur plutôt qu'une seule image lourde pour tous les terminaux — un gain de bande passante qui rejoint directement la sobriété visée au [critère 2.3](../2-3_connexion-bas-debit/).
- La balise **[`meta viewport`](https://developer.mozilla.org/fr/docs/Web/HTML/Viewport_meta_tag)** (`<meta name="viewport" content="width=device-width, initial-scale=1">`) reste un prérequis technique : sans elle, un navigateur mobile affiche par défaut une page pensée pour desktop réduite à l'échelle, rendant les media queries inopérantes.

Une technique plus récente, les **[container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)**, permet d'adapter un composant à la taille de son conteneur plutôt qu'à celle de l'écran entier — utile pour un composant réutilisé dans des contextes différents (barre latérale, pleine largeur), au prix d'une compatibilité navigateur plus récente à vérifier via [Can I Use](https://caniuse.com/).

{{% /tab %}}

{{% tab tabName="Outils de test" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Pour vérifier concrètement les seuils chiffrés du critère (1 200 x 800 px, 720 px de hauteur) :

- Le **mode responsive des DevTools** (Chrome, Firefox, Edge — gratuit) permet de simuler n'importe quelle taille d'écran en local, y compris les seuils exacts du critère.
- Pour **automatiser ce test en CI/CD**, [Playwright](https://playwright.dev/) (open source) permet de fixer une taille de fenêtre précise par script (`page.setViewportSize({ width: 1200, height: 800 })`) et de vérifier automatiquement, à chaque pull request, l'absence de débordement ou de perte de fonctionnalité — plutôt que de rejouer ce test manuellement à chaque changement d'interface.
- [BrowserStack](https://www.browserstack.com/), déjà cité aux critères [2.2](../2-2_anciens-terminaux/) et [2.4](../2-4_anciennes-versions-os/), complète ces tests automatisés par une vérification manuelle sur de vrais terminaux (tactile, résolutions réelles de smartphones anciens).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 3 avril 2025) illustre un cas de **non-conformité documentée**, plutôt qu'une réussite : « Le service numérique web propose un affichage qui adapte les dimensions des composants sans être réellement responsive [...] Sur une configuration de 1200 x 800, le composant "Notes" en jaune déborde hors de la fenêtre horizontalement [...] Le composant "Notes" s'affiche correctement qu'à partir d'environ 1760 pixels, donc sur une configuration de type 1080p ou supérieur. »

Ce cas est cité ici comme « Non validé » — précisément sur le seuil de 1 200 pixels fixé par le critère — et montre qu'une adaptation partielle des dimensions (fluid layout) ne suffit pas si un composant isolé reste conçu pour une largeur bien supérieure au seuil testé.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent ce critère « Validé » avec des tests sur des terminaux réels plutôt que des seules simulations : écran TV LG M2362DP 23 pouces, iPhone 5SE (320×568), iPad sous iOS 14.7 (1080×810) et Mac Pro M1 13 pouces, chacun avec une capture d'écran à l'appui. La déclaration reste honnête sur les limites malgré la validation globale : en « Évolutions potentielles », elle note un problème d'accessibilité identifié sur les tablettes en format portrait, au niveau des boutons du menu — un défaut mineur documenté plutôt que dissimulé derrière un statut « Validé » sans nuance.

{{% /tab %}}

{{< /tabs >}}
