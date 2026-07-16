---
weight: 300
title: "4.3 - Optimisation du parcours de navigation"
description: "Critère 4.3 du RGESN : pourquoi et comment optimiser le parcours de navigation de chaque fonctionnalité principale, en s'appuyant sur des statistiques d'usage respectueuses de la vie privée."
icon: "route"
date: "2026-07-16T00:00:00+01:00"
lastmod: "2026-07-16T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique optimise-t-il le parcours de navigation pour chaque fonctionnalité principale ?

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
| **Critère**  | `4.3` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service ne repose pas sur un parcours de navigation` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` `Responsable Qualité` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Minimiser le temps passé par l'utilisateur sur le service numérique et maîtriser les impacts environnementaux des fonctionnalités principales du service, tout en améliorant l'expérience utilisateur.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Durant la phase de conception, éliminer les fonctionnalités non essentielles et optimiser le ou les parcours de navigation pour chaque unité fonctionnelle principale du service numérique. Observer ensuite les statistiques de fréquentation et d'usage, couplées aux moyens d'observation UX (expérience utilisateur), afin d'améliorer cette optimisation de parcours. Il s'agira de veiller à l'utilité et l'utilisation de chaque fonctionnalité par l'utilisateur. Par exemple, une unité fonctionnelle principale du service peut être « réserver un billet », « rechercher un terme », « trouver une adresse », « contacter le support », « discuter », etc.

Il s'agit d'abord d'une analyse qualitative à mettre en place et pouvant être complétée par une analyse quantitative :

- Bien définir les unités fonctionnelles principales du service (au sens de l'analyse de cycle de vie).
- Exploiter toutes les ressources et tous les outils disponibles en UX afin de comprendre au mieux les usages des utilisateurs, notamment en ce qui concerne leurs parcours de navigation de chaque unité fonctionnelle principale.
- Mettre en place un système d'analyse non intrusif et respectueux de la vie privée afin d'identifier les parcours-type sur le service numérique. Analyser de temps en temps ces statistiques pour pouvoir améliorer l'expérience utilisateur et les impacts environnementaux de ces « chemins critiques ».
- Mesurer également les indicateurs techniques des parcours identifiés : nombre de requêtes, poids des ressources téléchargées.

À partir de l'analyse de ces éléments, concevoir et maintenir un parcours de navigation optimisé et des fonctionnalités véritablement utilisées par les utilisateurs.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la mise en place d'outils UX de conception, d'optimisation et de contrôle continu : tri de carte, sondage, interviews, enquêtes utilisateurs, tests-U, etc.

Contrôler la mise en place de marqueurs destinés à collecter des informations pour alimenter des statistiques d'usage et à suivre les parcours de navigation des utilisateurs : en s'appuyant par exemple sur des outils d'analyse d'audience qui fournissent des informations sur les pages visitées, le temps passé sur chaque page, les actions effectuées, etc.

Il est important de définir des indicateurs techniques pour les parcours identifiés et de vérifier l'optimisation du parcours de navigation ainsi que des fonctionnalités vis-à-vis des besoins et usages des utilisateurs.

Le critère est validé si (conditions cumulatives) :

- Les parcours de navigation sont optimisés et recentrés autour des fonctionnalités essentielles d'après les outils UX et les statistiques d'usages effectuées ;
- Des indicateurs techniques pour les parcours identifiés ont été ou sont en cours de mise en place pour assurer l'optimisation dans le temps du parcours de navigation, à la lumière des retours récoltés.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le critère 4.3 rejoint la [recommandation n°7 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=7) du [GR491](https://gr491.isit-europe.org/) (INR), « **"Barebone Iteration" : Itérer votre solution jusqu'au minimalisme "acceptable" par vos utilisateurs** », qui pose des questions directement transposables : 
- « La solution a-t-elle été prototypée en amont, incluant le parcours utilisateur et les interactions ? », 
- « Les comportements et retours des utilisateurs ont-ils été étudiés pour mieux répondre à leurs besoins ? », 
- « Le chemin d'accès au service est-il le plus rapide et le plus simple possible ? », 
- « Un processus d'amélioration continue a-t-il été mis en place ? ». 

Cette recommandation formalise, sous un nom différent, exactement la démarche itérative (prototypage → observation des usages → amélioration continue) décrite par la « Mise en œuvre » du critère RGESN.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) couvre ce critère avec la fiche [**RWEB 0005 — « Optimiser le parcours utilisateur »**](https://rweb.greenit.fr/fr/fiches/RWEB_0005-optimiser-le-parcours-utilisateur), notée au maximum sur les deux échelles de la fiche : **priorité d'implémentation 5/5** et **impact environnemental 5/5** — la fiche indique explicitement que le temps passé par l'utilisateur sur son terminal représente la deuxième plus grande source d'impact environnemental d'un service web. 

La méthode proposée : 
- Cibler les parcours les plus fréquents,
- Réduire le nombre d'étapes, 
- Éliminer les éléments superflus, 
- Identifier les points de friction,
- Fournir des messages d'erreur clairs. 

Principe de validation, volontairement radical : le nombre de points de friction identifiés doit être ramené à zéro. 

Exemples concrets cités : 
- Faciliter les commandes répétées à partir de l'historique, 
- Permettre un achat sans création de compte obligatoire, 
- Autoriser une saisie directe plutôt qu'un import de fichier, 
- Prioriser les filtres et champs les plus utilisés.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Designer`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement le critère 4.3** dans sa section [**4. Simplifier le parcours et fluidifier l'expérience**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/4-simplifier-le-parcours-et-fluidifier-l-experience) : « Optimiser le parcours de navigation pour chaque fonctionnalité principale permet de valider le critère 4.3 » du RGESN. 

Le guide résume la démarche à quatre questions : 
- Quelle est l'unité fonctionnelle ? 
- Combien d'étapes sont nécessaires ? 
- Le parcours est-il accessible ?
- Comment améliorer le taux de conversion tout en raccourcissant le chemin ?

Le guide illustre cette approche par un exemple concret et vérifiable : le site du gouvernement britannique ([GOV.UK](https://www.gov.uk/)) permet de trouver une information fiscale en seulement **4 pages**, chacune notée A ou B sur [EcoIndex](https://www.ecoindex.fr/) — la preuve qu'un parcours institutionnel à fort volume de trafic peut rester à la fois court et sobre, sans sacrifier l'exhaustivité de l'information disponible.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent ce critère à travers deux recommandations complémentaires :

- [**« Design efficient and streamlined user journeys »**](https://www.w3.org/TR/web-sustainability-guidelines/#design-efficient-and-streamlined-user-journeys) : « Design user journeys that are clear and efficient. Use established design patterns that people already understand. » La même fiche recommande de fournir un plan de site lisible par un humain pour les services complexes, et une navigation claire permettant de trouver rapidement le contenu recherché.
- [**« Audit and test for bugs or issues requiring resolution »**](https://www.w3.org/TR/web-sustainability-guidelines/#audit-and-test-for-bugs-or-issues-requiring-resolution) : recommande d'« identifier et résoudre les points de blocage dans le code ou l'infrastructure sous-jacente qui pourraient affecter la durabilité et la performance, pour favoriser un parcours utilisateur fluide et sans friction », en s'appuyant à la fois sur des métriques simulées et réelles, suivies à chaque cycle de publication — ce qui correspond directement au suivi dans la durée demandé par le « Moyen de test » du critère RGESN.

{{% /tab %}}

{{% tab tabName="Gauthier Roussilhe" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Contrairement aux critères précédents de cette catégorie, celui-ci trouve une correspondance directe et vérifiée dans les propos de [Gauthier Roussilhe](https://gauthierroussilhe.com/), au travers d'une [interview donnée aux Designers Éthiques](https://livre-ethique-numerique.designersethiques.org/content/interviews/interview-gauthier_roussilhe.html) (2019) : « Quand je participe à des ateliers avec des UX Designers, j'aime leur demander de concevoir un site web pour 3 Watts heure pour 1000 visites. Ils ne savent pas faire. » Il y voit un manquement de fond dans la formation des designers, plutôt qu'un problème de bonne volonté individuelle : contraindre un parcours utilisateur par un budget énergétique explicite (plutôt que par la seule ergonomie ou le taux de conversion) suppose des outils et des repères chiffrés qui ne font, à ce jour, pas partie du bagage standard d'un designer UX — ce qui rejoint directement l'esprit du critère 4.3, qui demande de mesurer des « indicateurs techniques » (nombre de requêtes, poids des ressources) en plus des indicateurs purement UX classiques.

{{% /tab %}}

{{% tab tabName="Outils d'analyse respectueux de la vie privée" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Qualité`

Pour la partie « système d'analyse non intrusif et respectueux de la vie privée » explicitement demandée par la « Mise en œuvre » du critère, deux alternatives à Google Analytics sont couramment citées :

- [**Matomo**](https://matomo.org/) : solution open source, auto-hébergeable, offrant un contrôle complet sur les données collectées. Configuré sans cookie de suivi, Matomo fait partie des rares outils de mesure d'audience **exemptés de recueil du consentement par la CNIL**, ce qui simplifie sa mise en conformité pour un service numérique français.
- [**Plausible Analytics**](https://plausible.io/) : ne dépose aucun cookie et ne génère aucun identifiant persistant — l'identification d'un visiteur repose sur un hash quotidien (IP + user-agent) qui n'est jamais conservé au-delà de 24 heures. Les données sont hébergées et traitées dans l'Union européenne.

Ces deux outils permettent de collecter les statistiques de fréquentation et de suivi de parcours demandées par le critère (pages visitées, temps passé, actions effectuées) sans les mécanismes intrusifs (cookies tiers, empreinte numérique persistante) des solutions d'analytics grand public, et sans bandeau de consentement à charge de l'utilisateur dans le cas de Matomo correctement configuré.

{{% /tab %}}

{{% tab tabName="Détection technique d'un allongement de parcours" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Qualité`

En complément des outils d'analyse d'audience ci-contre, le critère demande aussi de mesurer des « indicateurs techniques des parcours identifiés » et de les suivre dans le temps. Trois outils permettent de répondre spécifiquement à ce volet, à des étapes différentes du cycle de vie :

- [**Lighthouse CI**](https://github.com/GoogleChrome/lighthouse-ci) (Google, open source) s'intègre au pipeline d'intégration continue et fait échouer le build si des métriques comme le Time to Interactive, le LCP ou le TBT se dégradent au-delà d'un budget défini — il compare automatiquement chaque commit à la référence précédente, ce qui permet de détecter un allongement de parcours **avant** qu'il n'atteigne la production.
- [**WebPageTest**](https://www.webpagetest.org/) permet de programmer des tests récurrents qui rejouent un parcours utilisateur scripté complet (« critical user flows »), depuis plusieurs localisations, avec suivi de tendance dans la durée et alertes configurables en cas de dégradation — l'outil le plus direct pour surveiller un allongement progressif en conditions réelles.
- [**PostHog**](https://posthog.com/) (open source, auto-hébergeable) ajoute, au-dessus des statistiques d'audience classiques, l'enregistrement de session et une analyse de « user paths » : il permet de voir concrètement à quelle étape et pour quelle raison un parcours s'allonge, plutôt que de seulement constater que sa durée a augmenté.

Les deux premiers relèvent d'une logique de test (synthétique, scripté, reproductible), le troisième d'une logique d'observation (utilisateurs réels, en production) — les deux approches sont complémentaires plutôt que substituables : la première prévient une régression avant mise en production, la seconde permet de comprendre un allongement déjà constaté chez de vrais utilisateurs.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, avec une justification très concise : « Aucune analyse UX du produit en production n'a été identifiée à ce jour. » Ce cas illustre un profil différent des critères voisins 4.1 et 4.2 de cette même fiche, plus faciles à valider par une simple inspection du service : celui-ci demande une démarche organisationnelle continue (études UX, suivi de statistiques dans la durée) qui ne peut pas se déduire d'un simple examen technique du produit fini — d'où une évaluation « Non validé » qui reflète une absence de démarche documentée plutôt qu'un défaut du service lui-même.

{{% /tab %}}

{{< /tabs >}}
