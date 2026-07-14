---
weight: 100
title: "3.1 - Architecture, ressources et composants écoconçus"
description: "Critère 3.1 du RGESN : pourquoi et comment vérifier que l'architecture, les frameworks et les composants utilisés sont eux-mêmes conçus pour réduire leurs impacts environnementaux."
icon: "extension"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique repose-t-il sur une architecture, des ressources ou des composants conçus pour réduire leurs propres impacts environnementaux ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Architecture` |
| **Critère**  | `3.1` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service ne repose pas sur des composants` |
| **Métiers concernés** | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Le service numérique peut dépendre d'une architecture, de composants qui ne sont pas développés par la même équipe ou qui sont fournis par des frameworks de production. Il s'agit alors de s'assurer que ces dépendances sont également conçues de manière à réduire leurs propres impacts environnementaux.

Certains composants sont particulièrement intensifs en termes de consommation énergétique et en ressources, et devraient être évités (par exemple : minage, réalité virtuelle/augmentée requérant l'acquisition d'un terminal dédié, certains algorithmes d'apprentissage…).

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

S'assurer que l'architecture, les ressources et les composants utilisés dans le service numérique, notamment les frameworks pour le frontend et backend, sont délibérément conçus pour minimiser leurs impacts environnementaux. Ceux-ci respectent-ils les critères du référentiel ? Plus spécifiquement :

- **Évaluation des frameworks** : examiner les frameworks utilisés pour le développement du frontend et du backend en termes d'écoconception. L'analyse pourra notamment prendre en compte : l'utilisation efficace des ressources matérielles et énergétiques, l'utilisation de technique de compression efficace, l'optimisation des requêtes client-serveur.
- **Évaluation des composants** : vérifier si les composants, qu'ils soient internes ou externes, suivent des principes d'écoconception. L'analyse pourra notamment prendre en compte : l'utilisation efficace des ressources matérielles et énergétiques, l'utilisation de technique de compression efficace, l'optimisation des requêtes client-serveur.

Voir aussi les critères 2.9 et 2.10 pour la prise en compte des impacts des composants d'interface et des services tiers.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérification de la mise en œuvre en analysant et optimisant l'empreinte environnementale pour évaluer la performance énergétique des composants et des frameworks. S'assurer notamment que le service ne s'appuie pas sur des briques technologiques particulièrement énergivores et consommatrices en ressources (apprentissage automatique, minage, métavers en particulier). En cas de recours à ce type de technologie, la solution la plus sobre en termes de consommation en ressources doit être utilisée par défaut, et le choix doit être documenté dans la déclaration d'écoconception du service numérique.

Le choix d'architecture et de composants est à documenter dans la déclaration d'écoconception au regard de l'impact environnemental (en vérifiant notamment la validation par ces éléments des critères 2.9 et 2.10 de ce référentiel), en intégrant un comparatif avec les autres options possibles.

Le critère est validé si le choix de frameworks et composants de l'architecture a été fait en prenant en compte leur empreinte environnementale et l'écoconception, et qu'il est documenté dans la déclaration d'écoconception du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Le critère 3.1 rejoint la [recommandation n°2 de la famille Back-end](https://gr491.isit-europe.org/?famille=backend&num_reco=2) du [GR491](https://gr491.isit-europe.org/) (INR), « Utiliser les composants techniques qui améliorent les aspects NR, sécurité et performance », qui décline la question « évaluation des frameworks » en critères directement actionnables : « Existe-t-il un framework/library plus léger répondant au besoin fonctionnel ? », « Est-ce qu'une solution Open Source est disponible pour le besoin fonctionnel ? », « Peut-on réduire les dépendances avec un composant alternatif ? », « A-t-on évalué l'arbre de dépendance des composants intégrés ? »

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Systèmes`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) est la source la plus riche en correspondances sur ce critère (13 fiches au total). En voici trois particulièrement représentatives du critère 3.1 :

- [**RWEB 0029 — « Utiliser la version la plus récente du langage et de la plate-forme »**](https://rweb.greenit.fr/fr/fiches/RWEB_0029-utiliser-la-version-la-plus-recente-du-langage) : chaque nouvelle version d'un langage serveur apporte des gains de performance et de gestion mémoire — exemple donné : PHP 8.0 et son compilateur JIT (Just in Time), qui compile et met en cache certaines parties du code, améliorant à la fois la performance et la gestion mémoire.
- [**RWEB 0068 — « Utiliser certains forks applicatifs orientés "performance" »**](https://rweb.greenit.fr/fr/fiches/RWEB_0068-utiliser-certains-forks-applicatifs-orientes-performance) : un fork optimisé d'un logiciel open source offre généralement le même périmètre fonctionnel pour une consommation de ressources réduite — exemple donné : préférer [KeyDB](https://docs.keydb.dev/) (fork multi-thread de Redis) à Redis lui-même.
- [**RWEB 0086 — « Utiliser un serveur asynchrone »**](https://rweb.greenit.fr/fr/fiches/RWEB_0086-utiliser-un-serveur-asynchrone) : les serveurs asynchrones ([Nginx](https://nginx.org/), Node.js…) évitent de créer un processus ou un thread par requête. Chiffres donnés : Nginx sert 2 fois plus de requêtes par seconde qu'[Apache](https://httpd.apache.org/) ; [Gwan](http://gwan.com/) (peu utilisé mais cité en exemple) sert 4 fois plus de requêtes par seconde que Nginx, en 4 fois moins de temps, pour 2 fois moins de RAM consommée.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont trois recommandations qui recoupent directement le critère 3.1 :

- [**« Use the latest stable language version »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-the-latest-stable-language-version) : utiliser la dernière version stable du langage et du framework choisis — exactement la même recommandation que RWEB 0029 ci-contre, formulée indépendamment par deux référentiels différents.
- [**« Use dependencies sparingly and maintain them »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-dependencies-sparingly-and-maintain-them) : revoir régulièrement les dépendances pour retirer les bibliothèques inutilisées, limiter les dépendances externes au strict nécessaire, et ne pas remplacer des bibliothèques de sécurité éprouvées par des implémentations maison au nom de la sobriété.
- [**« Use the most efficient solution for your service »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-the-most-efficient-solution-for-your-service) : privilégier l'approche la plus performante pour le besoin réel, en pesant effort de développement contre performance et impact environnemental — un code sur-mesure bien maîtrisé n'est pas toujours le choix le plus sobre face à une solution existante déjà optimisée.

{{% /tab %}}

{{% tab tabName="Critères associés" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Responsable RSE/Numérique soutenable`

Le texte du critère renvoie lui-même explicitement aux critères [2.9](../../specifications/2-9_composants-interface/) (impacts des composants d'interface prêts à l'emploi) et [2.10](../../specifications/2-10_services-tiers/) (impacts des services tiers) : le 3.1 porte sur les briques d'architecture et les frameworks frontend/backend, quand 2.9 et 2.10 portent respectivement sur les composants d'interface (design systems) et les services tiers fonctionnels (analytics, vidéo…). Les trois critères se complètent pour couvrir l'ensemble des dépendances externes d'un service numérique, à des niveaux différents de la stack.

{{% /tab %}}

{{% tab tabName="Étude énergie par langage" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Pour objectiver le choix d'un langage ou d'un framework backend, l'étude de référence [« Ranking Programming Languages by Energy Efficiency »](https://haslab.github.io/SAFER/scp21.pdf) (Pereira et al., Science of Computer Programming, Elsevier, 2021) mesure la consommation énergétique de 27 langages sur des benchmarks identiques. Résultats normalisés par rapport au langage le plus efficace (C = 1,00) : Rust 1,03, Java 1,98, JavaScript 4,45, Python 75,88 — un facteur supérieur à 75 entre les deux extrêmes du classement.

Ce chiffre ne dit pas qu'il faut réécrire son backend en Rust : le choix d'un langage dépend aussi de l'écosystème, des compétences de l'équipe et de la maintenabilité. Mais il objective le fait qu'un langage interprété comme Python ou Ruby a un coût énergétique structurellement supérieur, à budgétiser dans le choix d'architecture plutôt qu'à découvrir après coup.

{{% /tab %}}

{{% tab tabName="Benchmarks frameworks API" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Une fois le langage choisi, l'écart entre deux frameworks du **même** écosystème peut lui aussi être significatif. [TechEmpower Framework Benchmarks](https://github.com/TechEmpower/FrameworkBenchmarks) reste la référence la plus large pour comparer des frameworks API entre eux (plaintext, sérialisation JSON, requêtes base de données) : elle couvre notamment [Actix](https://actix.rs/), [Axum](https://github.com/tokio-rs/axum) et [Rocket](https://rocket.rs/) côté Rust, Quarkus côté Java, [FastAPI](https://fastapi.tiangolo.com/) côté Python, ainsi que plusieurs frameworks Go. À noter : le projet a été **archivé en mars 2026** — les derniers résultats publiés restent utilisables pour comparer l'ordre de grandeur entre frameworks d'un même écosystème, mais ne sont plus mis à jour.

Côté Java spécifiquement, [Quarkus](https://quarkus.io/) compilé en natif avec [GraalVM](https://www.graalvm.org/) change la donne par rapport à un déploiement JVM classique : la documentation officielle de Quarkus donne l'exemple d'une application `getting-started` démarrant en **0,009 s** en mode natif (contre plusieurs secondes en JVM traditionnelle), la JVM embarquée étant réduite et les métadonnées de classes résolues à la compilation plutôt qu'à l'exécution. C'est une manière, pour l'écosystème Java, de rejoindre la logique du **fork orienté performance** déjà cité côté RWEB : Quarkus natif se comporte davantage comme un binaire compilé (proche de Go ou Rust en démarrage et en empreinte mémoire) que comme une JVM traditionnelle.

Un débit de requêtes plus élevé n'est pas strictement équivalent à une consommation énergétique plus faible (cela dépend aussi du profil de charge et du matériel), mais traiter plus de requêtes avec le même CPU va structurellement dans le même sens que l'étude Pereira et al. ci-contre : moins de temps CPU par requête, c'est moins d'énergie consommée pour un même service rendu.

{{% /tab %}}

{{% tab tabName="Outils de mesure" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Pour mesurer directement la consommation d'un composant ou d'un algorithme plutôt que de se fier à un classement générique, [CodeCarbon](https://github.com/mlco2/codecarbon) (projet Data For Good, initié notamment par Yoshua Bengio) est un package Python léger qui s'installe via `pip install codecarbon` et s'utilise avec un simple décorateur `@track_emissions` sur la fonction à mesurer. Il estime la consommation CPU/GPU/RAM réelle et la convertit en kg de CO2 équivalent selon l'intensité carbone du réseau électrique local — particulièrement pertinent pour les « algorithmes d'apprentissage » mentionnés dans l'objectif du critère, dont le coût énergétique est rarement mesuré en pratique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, en nommant précisément sa stack technique : « Le développement du backend et frontend s'appuient sur Spring Boot (Java 8) et Angular 17. Aucune étude n'est disponible démontrant un engagement de ces frameworks dans une démarche d'écoconception. »

Ce cas est révélateur : Spring Boot (Java) et Angular ne sont pas des choix technologiques déraisonnables d'un point de vue énergétique — Java se classe dans la moyenne haute du classement Pereira et al. ci-contre, loin devant les langages interprétés — mais le critère ne porte pas sur la performance brute du langage : il exige une démarche documentée. FACE se retrouve donc « Non validé » non pas pour un mauvais choix technique, mais pour l'absence de comparatif formalisé dans la déclaration d'écoconception, exactement comme pour les critères [2.6](../../specifications/2-6_revue-conception-code/) et [2.7](../../specifications/2-7_maintenance-decommissionnement/) sur ce même service.

À l'inverse, le cabinet [Davidson](https://www.davidson.fr/blog/on-a-reussi-a-mesurer-une-pratique-deco-conception) documente une démarche de comparaison réellement menée : une même application testée en architecture monolithe (PHP/MySQL) puis en microservices (Rust), toutes deux conteneurisées avec Docker, mesurée sur 20 exécutions via leur outil interne ETSDiff couplé à Selenium (énergie en joules via VJoule, transfert réseau et stockage en octets). Résultat : Rust réduit nettement la consommation d'énergie par rapport à PHP, mais le passage en microservices augmente le trafic réseau — les échanges internes au monolithe devenant des appels réseau externes entre services. Davidson pose en conclusion la question du **retour sur investissement carbone** d'une telle réécriture : si mobiliser une équipe pendant un an ne permet de gagner que quelques watts, il devient nécessaire de calculer la durée de fonctionnement minimale pour amortir le coût carbone du projet de refonte lui-même.

{{% /tab %}}

{{< /tabs >}}
