---
weight: 900
title: "2.9 - Composants d'interface prêts à l'emploi"
description: "Critère 2.9 du RGESN : pourquoi et comment comparer les impacts environnementaux des composants d'interface et des design systems prêts à l'emploi."
icon: "widgets"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il pris en compte les impacts environnementaux des composants d'interface prêts à l'emploi utilisés ?

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
| **Critère**  | `2.9` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur des composants d'interface prêts à l'emploi` |
| **Métiers concernés** | `Designer` `Développeur` `Responsable IT` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.9/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Connaître les impacts environnementaux des composants d'interface (boutons, formulaires…), des systèmes de design qui sont des surcouches aux interfaces du système d'exploitation, utilisés dans le service numérique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Comparer les impacts environnementaux des composants d'interface prêts à l'emploi utilisés dans le service numérique afin d'être en mesure d'utiliser les solutions les plus sobres. Par exemple, mesurer et comparer leur poids en termes d'utilisation de ressources (taille des fichiers, quantité de données transférées).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier si les composants d'interface utilisés sont conçus de manière à réduire leurs impacts environnementaux.

Pour cela, prendre en compte ou effectuer, le cas échéant, des mesures comparatives entre les différents composants similaires et choisir ceux qui présentent les meilleures performances environnementales. Les éléments suivants peuvent être considérés : l'utilisation de méthodes de compression efficaces, l'optimisation des ressources, la minimisation des transferts de données, l'utilisation de techniques de conception légère, etc.

Le critère est validé si la majorité des composants d'interfaces utilisés par le service sont estimés performants écologiquement, en prenant notamment en compte les critères susmentionnés lorsque applicables à la fonctionnalité visée. Les choix effectués et la minimisation de l'empreinte environnementale des composants devrait également être documentée dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="3">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le critère 2.9 rejoint la [recommandation n°3 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Utiliser les environnements et outils qui permettent de limiter les impacts », qui pose des questions directement transposables aux design systems et bibliothèques de composants : « Les bibliothèques utilisées permettent-elles de ne prendre que les composants effectivement utiles ? », « Les dépendances non utilisées sont-elles identifiées et retirées ? », « Est-ce que la fonctionnalité attendue ne pourrait pas être mise en place avec les capacités natives du navigateur ? ».

Cette dernière question rejoint directement le critère 4.5 (« Le service numérique utilise-t-il majoritairement des composants fonctionnels natifs du système d'exploitation, du navigateur ou du langage utilisé ? ») : avant de charger un design system complet, la question à se poser est si un composant HTML natif (`<dialog>`, `<details>`, validation de formulaire native) ne suffirait pas.

{{% /tab %}}

{{% tab tabName="Outils de mesure" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Pour comparer objectivement le poids de composants d'interface avant de les intégrer, plutôt que de le découvrir une fois le service en production :

- [Bundlephobia](https://bundlephobia.com/) donne, pour n'importe quel package npm, sa taille minifiée et gzippée, son temps de téléchargement estimé, ses sous-dépendances et sa compatibilité avec le tree-shaking — utile pour comparer deux bibliothèques de composants avant de choisir (ex. une librairie de date-picker complète face à une alternative plus légère).
- [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) (extension VS Code, basée sur le même principe que Bundlephobia) affiche directement dans l'éditeur, ligne par ligne, le poids réel de chaque import — en tenant compte du tree-shaking, donc du composant effectivement importé plutôt que de la bibliothèque entière.

Ces deux outils sont **spécifiques à l'écosystème JavaScript/npm** (Import Cost s'appuie sur webpack) : ils ne s'appliquent qu'aux composants distribués comme packages npm, pas aux design systems ou bibliothèques d'autres langages/écosystèmes. Ils objectivent néanmoins concrètement la question posée par le GR491 ci-contre : un design system complet importé pour n'utiliser qu'un seul composant est un signal direct de dépendance non optimisée.

**Java et Python** n'ont pas d'équivalent aussi direct, mais le même réflexe de mesure reste possible :

- **Python** : [PyPI](https://pypi.org/) publie directement, pour chaque package, la taille exacte du wheel/sdist (visible sur la page du projet ou via son [API JSON](https://pypi.org/pypi/requests/json), champ `size`), sans outil tiers. Pour mesurer le poids réel **avec ses dépendances transitives**, [python-package-size](https://pypi.org/project/python-package-size/) installe chaque dépendance dans un environnement virtuel isolé et rapporte sa taille totale sur disque.
- **Java/Maven** : le [Dependency Analysis Gradle Plugin](https://github.com/autonomousapps/dependency-analysis-gradle-plugin) (2 000+ étoiles, activement maintenu) ne donne pas un poids en Ko comme Bundlephobia, mais détecte les dépendances inutilisées, mal déclarées ou transitives non explicites, et peut afficher un « dominator tree » pour repérer les dépendances les plus lourdes. Pour la taille brute d'un artefact, [Maven Central](https://repo1.maven.org/maven2/) expose directement le poids du jar (`Content-Length` visible via une simple requête `HEAD` sur son URL), sans passer par un outil dédié.

Ces deux écosystèmes sont moins concernés par les design systems (plutôt un sujet frontend), mais le principe reste le même pour toute bibliothèque prête à l'emploi, quel que soit le langage.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C consacrent une recommandation dédiée aux design systems, [**« Use a design system for interface consistency »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-a-design-system-for-interface-consistency) : utiliser un design system pour les projets importants ou à contributeurs multiples, en s'appuyant sur des composants réutilisables basés sur les standards du web, en ne chargeant que les composants effectivement nécessaires à chaque page ou fonctionnalité, et en maintenant le système via une gouvernance claire (propriété, versionnage, documentation à jour).

Une seconde recommandation, [**« Use optimized web typography »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-optimized-web-typography), complète le critère sur un point précis et souvent oublié des design systems : limiter le nombre et la complexité des polices chargées, et restreindre les axes des polices variables aux seuls besoins réels du projet pour réduire la taille du fichier — exactement le type d'optimisation évoquée dans le retour d'expérience DSFR ci-dessous.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »** : « Le service numérique a recours à des composants prêts à l'emploi basés sur Bootstrap 4. Aucune information n'a été trouvée sur la minimisation de l'impact environnemental de cette technologie. »

Ce cas illustre bien la situation la plus fréquente : un design system largement adopté (Bootstrap) est utilisé par défaut, sans qu'aucune comparaison n'ait jamais été faite avec des alternatives plus légères ou avec les composants natifs du navigateur — le critère ne demande pas nécessairement d'abandonner Bootstrap, mais de documenter que ce choix a au moins été questionné.

À l'inverse, le [DSFR (Système de Design de l'État)](https://www.systeme-de-design.gouv.fr/), obligatoire pour tous les sites de l'administration française depuis juillet 2023, illustre la démarche côté fournisseur du design system plutôt que côté service qui le consomme. Dans une [interview donnée à la mission Numérique écoresponsable](https://ecoresponsable.numerique.gouv.fr/actualites/parolesdexperts-episode7-DSFR/), Maxime Beaugrand (responsable du DSFR) explique : « on va travailler avec l'équipe en charge du RGESN pour pouvoir l'appliquer au design system composant par composant et critère par critère. » Il cite un exemple concret déjà engagé pour la V2 : l'intégration d'une **typographie variable**, pour que les utilisateurs du DSFR n'aient plus à charger 3 ou 4 fichiers de police différents mais un seul fichier gérant tous les niveaux de graisse et de taille — une optimisation qui rejoint directement la guideline W3C sur la typographie citée ci-contre.

{{% /tab %}}

{{< /tabs >}}
