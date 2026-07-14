---
weight: 400
title: "2.4 - Anciennes versions d'OS et de navigateurs"
description: "Critère 2.4 du RGESN : pourquoi et comment garantir l'utilisabilité d'un service numérique sur d'anciennes versions de systèmes d'exploitation (5 ans) et de navigateurs web (2 ans)."
icon: "update"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique est-il utilisable sur d'anciennes versions de système d'exploitation et de navigateurs web ?

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
| **Critère**  | `2.4` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service ne repose pas sur un OS ou un navigateur web` |
| **Métiers concernés** | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est de permettre à des **systèmes d'exploitation ou navigateurs web anciens** d'être utilisés, afin d'allonger leur durée de vie. Les systèmes d'exploitation et les navigateurs étant parfois liés à un terminal, cette pratique peut donc **partiellement permettre de réduire la contribution du service numérique à leur obsolescence**.

Ce critère prend en compte les **dispositions européennes** visant à garantir la mise à disposition de mises à jour correctives pour les systèmes d'exploitation de cinq ans.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Si le service numérique est une **application native**, il doit prendre en charge les dernières versions des systèmes d'exploitation supportés et être utilisable sur les **versions anciennes** de ces systèmes d'exploitation (hors mises à jour correctives), jusqu'à **cinq ans**, en prenant en compte la première date de mise à disposition en version stable.

Si le service numérique fonctionne sur un **navigateur web**, il doit prendre en charge les dernières versions des navigateurs web (hors mises à jour correctives) et être utilisable sur les versions anciennes des principaux navigateurs web, jusqu'à **deux ans**, en prenant en compte la première date de mise à disposition en version stable.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la mise en œuvre selon la nature du service :

- **Application native** : tester les fonctionnalités critiques du service sur les systèmes d'exploitation supportés ayant cinq ans, en prenant en compte la première date de mise à disposition en version stable.
- **Navigateur web** : s'assurer que les fonctionnalités critiques fonctionnent sur les principaux navigateurs web dans une version datée d'au moins deux ans, en prenant en compte la première date de mise à disposition en version stable.

La **déclaration d'écoconception** devrait spécifier :

- **Application native** : les versions minimales des systèmes d'exploitation supportés.
- **Navigateur web** : les prérequis logiciels et les versions minimales des navigateurs web compatibles, ainsi que leur année de sortie. Il est pertinent de rajouter la cause de l'incompatibilité de la version précédente, s'il est possible d'en diagnostiquer la cause.

Si certaines fonctionnalités requièrent une version plus récente, indiquer les versions minimales avec et sans support de ces fonctionnalités.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="3">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Développeur`

Le critère 2.4 rejoint la même [recommandation n°4 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR), « Réduire les effets d'obsolescence », déjà citée au [critère 2.2](../2-2_anciens-terminaux/) pour le matériel : la plage de rétro-compatibilité visée est-elle définie ? Ici appliquée aux versions logicielles plutôt qu'au matériel, la question devient : jusqu'à quelle ancienneté de navigateur ou d'OS le service reste-t-il garanti fonctionnel, et cette limite est-elle documentée ?

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Le chapitre [« Tester, évaluer et maintenir »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/8-tester-evaluer-et-maintenir) du guide des Designers Éthiques mentionne explicitement ce critère, dans la continuité directe du critère 2.2 : « il conviendra aussi au critère 2.4 de tester sur de vieilles versions de navigateurs et systèmes d'exploitation ». Le même effort de test sur matériel ancien (2.2) doit donc être complété par un test sur **versions logicielles anciennes**, les deux dimensions (matériel et logiciel) pouvant diverger : un terminal ancien peut tourner un navigateur à jour, et inversement.

{{% /tab %}}

{{% tab tabName="Outils de test" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Pour définir et vérifier une plage de compatibilité logicielle plutôt que de la découvrir après coup :

- [Browserslist](https://browsersl.ist/) (open source) permet de déclarer, dans un seul fichier de configuration partagé par tout l'écosystème JavaScript/CSS (Autoprefixer, Babel, ESLint, PostCSS...), la plage exacte de navigateurs supportés (ex. `> 0.5%, last 2 versions, not dead`). Les outils de build appliquent alors automatiquement les polyfills et préfixes CSS nécessaires à cette plage — la compatibilité devient une configuration explicite plutôt qu'un test manuel a posteriori.
- [BrowserStack](https://www.browserstack.com/) (payant), déjà cité au [critère 2.2](../2-2_anciens-terminaux/), donne aussi accès à un catalogue de **versions anciennes de navigateurs et d'OS réels**, utile pour valider manuellement les fonctionnalités critiques sur les versions limites définies dans Browserslist.
- Pour **automatiser cette vérification en CI/CD** plutôt que de la découvrir en production, [eslint-plugin-compat](https://github.com/amilajack/eslint-plugin-compat) (open source) lit directement la configuration Browserslist du projet et fait échouer le lint dès qu'une API JavaScript non supportée par la plage déclarée est utilisée dans le code. Son équivalent côté CSS, [doiuse](https://github.com/anandthakker/doiuse) (plugin PostCSS), fonctionne sur le même principe pour les propriétés CSS. Les deux s'exécutent comme n'importe quel linter dans un pipeline existant, sans navigateur réel à provisionner.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) documente précisément le niveau d'information attendu par ce critère, avec une liste chiffrée de versions minimales et leur date de sortie : « Le service numérique, sous forme d'application web, s'affiche correctement sur les navigateurs suivants : Firefox 109.0 (janvier 2023) ou supérieur, Chrome/Chromium/Edge 110.0 (janvier 2023) ou supérieur, Safari 14.1 (avril 2021) ou supérieur, c'est-à-dire sur des ordinateurs Apple datant de 2012 ou au-delà. » Le seuil de janvier 2023 pour Firefox/Chrome, comparé à la date de déclaration (janvier 2025), correspond exactement aux deux ans de rétro-compatibilité minimale exigés par le critère — et la mention explicite de Safari illustre le lien direct entre version de navigateur et âge du terminal (ici, des Mac de 2012), qui rejoint le [critère 2.2](../2-2_anciens-terminaux/).

La [déclaration d'écoconception de « Les entreprises s'engagent »](https://lesentreprises-sengagent.gouv.fr/eco-conception) (dernière mise à jour le 25 novembre 2022) va au-delà du minimum exigé par ce critère : « Le service supporte toutes les versions navigateurs qui ont moins de **5 ans** et qui couvrent plus de 0,2 % des parts de marché en France » — soit deux fois et demi la rétro-compatibilité minimale de deux ans demandée par le RGESN. À noter que cette déclaration s'appuie sur la version 1 du référentiel (79 critères) plutôt que sur la v2 utilisée dans ce guide, sans table de correspondance fiable entre les deux versions.

Le [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) (Nantes Métropole, sur la v2 du RGESN) marque ce critère « Validé » avec une précision comparable à FACE, en listant six navigateurs et leur version minimale exacte : Google Chrome 63+, Internet Explorer 9+, Microsoft Edge 16+, Mozilla Firefox 52+, Firefox Quantum ESR 60+, Safari 11+ — une liste publiée dans les mentions légales du site plutôt que dans la seule déclaration d'écoconception, ce qui la rend directement vérifiable par n'importe quel visiteur.

{{% /tab %}}

{{< /tabs >}}
