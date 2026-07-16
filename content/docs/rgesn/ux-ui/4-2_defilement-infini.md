---
weight: 200
title: "4.2 - Absence de défilement infini"
description: "Critère 4.2 du RGESN : pourquoi et comment éviter le défilement infini et les murs de contenu, au profit d'une pagination ou d'un chargement à la demande."
icon: "format_list_numbered"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique affiche-t-il uniquement des contenus sans défilement infini ?

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
| **Critère**  | `4.2` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'interaction homme-machine (IHM)` |
| **Métiers concernés** | `Développeur` `Designer` `Concepteur UX / UI` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Les « murs de contenu » font partie des stratégies de captation de l'attention de certaines plateformes numériques qui contribuent à l'augmentation de l'empreinte environnementale des services numériques. L'objectif est donc de réduire la conception de services numériques reposant sur un design de « mur de contenus », de liste ou d'enchaînement infini de contenus, ce qui augmente le temps passé sur la page, et donc le poids de cette dernière ainsi que les ressources nécessaires.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Éviter le « mur de contenus », la proposition infinie ou l'enchaînement infini de contenus pour amoindrir le poids de la page utilisée et optimiser l'expérience utilisateur.

Mettre en place une navigation facile d'utilisation et proportionnée au contexte d'utilisation dont le chargement du contenu est à la demande de l'utilisateur (avec par exemple, un bouton « Voir plus » qui permet de poursuivre la navigation ou une pagination).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le design du service numérique repose sur un chargement à la demande du contenu proportionné au contexte d'utilisation (notamment la mise en place d'un bouton « Voir plus » pour continuer la navigation ou une pagination), ou peut s'afficher en entier sur un écran.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Designer`, `Concepteur UX / UI`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) couvre ce critère avec la fiche [**RWEB 0013 — « Préférer la pagination au défilement infini »**](https://rweb.greenit.fr/fr/fiches/RWEB_0013-preferer-la-pagination-au-defilement-infini) : plutôt que de charger indéfiniment une liste de produits ou d'articles au fil du défilement, mettre en place une pagination classique associée à un système de filtres efficace — ce qui améliore à la fois la performance, le référencement (SEO) et la conformité en accessibilité web. La fiche propose un exemple concret : afficher 10 éléments par défaut, tout en laissant l'utilisateur choisir d'en afficher 25, 50 ou 100 selon son besoin. Principe de validation retenu par RWEB : le nombre de listes sans pagination classique doit rester inférieur ou égal à 10 % de l'ensemble des listes du service.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Designer`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement et nommément le critère 4.2** du RGESN dans sa section [**7.8 Interactions**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-8-interactions) : « Bannir le défilement infini permet de valider le critère 4.2 du référentiel général de l'écoconception ». Le guide en détaille le mécanisme psychologique : « Scroller est tellement simple qu'il est difficile de se rendre compte ou de s'arrêter soi-même » — le défilement infini supprime la friction naturelle (le clic vers une page suivante) qui offrait auparavant un point de décision naturel pour l'utilisateur. La solution recommandée rejoint celle du RGESN : « Remplacer autant que possible le scroll infini par une action, comme une pagination, ou un bouton "Voir plus" ».

Le guide relie aussi ce critère à un enjeu plus large que la seule écoconception : le défilement infini y est cité comme un exemple de *dark pattern* — au même titre que l'enchaînement automatique de vidéos ou les mécaniques de « streaks » (séries de jours consécutifs, popularisées par Duolingo ou Snapchat) — c'est-à-dire un procédé manipulatoire conçu pour générer un usage disproportionné du service plutôt que pour répondre à un besoin réel de l'utilisateur.

Ce sujet a une dimension presque personnelle pour son inventeur : [Aza Raskin](https://en.wikipedia.org/wiki/Aza_Raskin) a créé le défilement infini en 2006 pour supprimer le clic vers une page suivante, et regrette publiquement cette invention depuis, notamment dans le documentaire Netflix *[The Social Dilemma](https://www.thesocialdilemma.com/)*. Il a évoqué, au fil de plusieurs interviews, un ordre de grandeur du temps collectif ainsi capté — tantôt 100 000 « vies humaines » par jour, tantôt 200 000, tantôt 500 000 par mois selon l'interview et l'année. Ces chiffres, à prendre avec précaution, sont des estimations personnelles données à l'oral et non le résultat d'une étude publiée ; leur intérêt est moins dans leur précision que dans le constat, assumé par son propre inventeur, que l'optimisation de la facilité d'usage ne sert pas nécessairement l'intérêt de l'utilisateur — un rappel direct de sa propre formule : « optimising something for ease-of-use does not mean best for the user or humanity. »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C recoupent ce critère dans la fiche [**« Design to assist and not to distract »**](https://www.w3.org/TR/web-sustainability-guidelines/#design-to-assist-and-not-to-distract) : « Avoid design patterns that engage users longer than necessary, such as infinite scroll or disabling standard browser controls and navigation features. » Le défilement infini y est cité comme l'exemple type d'un design qui maximise le temps passé plutôt que l'efficacité du parcours utilisateur — la même fiche recommande plus généralement de ne montrer que l'information pertinente à la tâche en cours, sans éléments compétant inutilement pour l'attention.

{{% /tab %}}

{{% tab tabName="Accessibilité : au-delà de l'écoconception" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le défilement infini pose un problème d'accessibilité documenté, indépendamment de son impact environnemental : en ajoutant du contenu en continu, il empêche souvent d'atteindre le pied de page (le raccourci clavier `Ctrl+Fin` ne fonctionne plus comme attendu), et peut créer un **piège au clavier** pour les utilisateurs qui naviguent par tabulation, si aucun mécanisme ne permet de déclencher le chargement suivant autrement qu'en scrollant à la souris — une situation qui peut être considérée comme un manquement au [critère WCAG 2.1.1 « Clavier »](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html). Ce n'est cependant pas un problème que les WCAG couvrent de façon parfaitement explicite : il n'existe pas de critère de succès dédié spécifiquement au défilement infini, ce qui en fait un point souvent négligé des audits d'accessibilité classiques alors même qu'il est explicitement visé par le RGESN.

Ce constat renforce l'intérêt d'une pagination classique ou d'un bouton « Voir plus » : ces deux mécanismes, contrairement au défilement infini, s'appuient sur des liens ou des boutons **nativement accessibles au clavier et aux lecteurs d'écran**, sans nécessiter de développement d'accessibilité spécifique.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Deux implémentations distinctes répondent au critère, selon le contexte :

- **Pagination classique**, avec une URL différente par page (`?page=2`) : chaque page est un lien `<a href>` réel, donc crawlable par les moteurs de recherche, accessible au clavier, et permet à l'utilisateur de revenir directement à une page précise via l'historique du navigateur — contrairement à un défilement infini où la position de lecture se perd au moindre retour en arrière.
- **Bouton « Voir plus »**, pour les cas où une continuité de lecture est réellement utile (fil d'actualité, résultats de recherche) : le chargement suivant reste déclenché par une action explicite de l'utilisateur (clic ou activation clavier sur un `<button>`), plutôt que par la seule position de défilement. C'est la différence essentielle avec le défilement infini automatique : la page ne charge du contenu supplémentaire que si l'utilisateur en fait la demande, ce qui correspond exactement au « chargement à la demande » exigé par le « Moyen de test » du critère.

Dans les deux cas, le point commun est de conserver un **élément d'interface standard** (lien ou bouton) comme déclencheur, plutôt qu'un événement de défilement — c'est précisément ce qui manque au défilement infini et qui explique à la fois son impact environnemental (chargement continu non borné) et son problème d'accessibilité (absence de point d'arrêt ou de contrôle explicite).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Validé »**, avec une justification factuelle et vérifiable : « Les contenus audités de ce service numérique sont paginés et aucun défilement infini n'a été détecté. » Un cas simple qui illustre bien le « Moyen de test » du critère : contrairement à d'autres critères plus qualitatifs de cette fiche, celui-ci se prête à une vérification quasi binaire — la présence ou l'absence de pagination sur les listes de contenu du service.

{{% /tab %}}

{{< /tabs >}}
