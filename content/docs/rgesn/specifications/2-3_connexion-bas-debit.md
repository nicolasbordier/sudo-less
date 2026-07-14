---
weight: 300
title: "2.3 - Connexion bas débit ou hors connexion"
description: "Critère 2.3 du RGESN : pourquoi et comment garantir l'utilisabilité d'un service numérique via une connexion bas débit (3G, 512 Kbit/s) ou hors connexion."
icon: "wifi_off"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique est-il utilisable via une connexion bas débit ou hors connexion ?

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
| **Critère**  | `2.3` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Si le service numérique s'adresse à un large public, le **niveau de connectivité n'est pas maîtrisé**. Il est nécessaire de veiller à **ne pas exclure certains publics** qui n'ont pas accès à de hauts débits : en plus de réduire la fracture numérique, il s'agit d'une bonne pratique pour l'environnement.

Les utilisateurs n'ont pas toujours conscience de ce qui ralentit un service numérique : la connexion réseau, le service lui-même, ou le terminal utilisé ? Un service numérique **plus léger** a beaucoup moins besoin de ressources réseau pour fonctionner.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

**Tester l'utilisabilité du service avec des connexions bas débit**, mesurer et améliorer le temps de réponse. Les contenus peuvent être servis en **qualité dégradée** lorsque cela s'avère nécessaire.

Il est recommandé aux **applications natives** de prévoir un **mode hors ligne** sur les fonctionnalités qu'il est techniquement possible de fournir hors ligne.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

L'utilisabilité du service devra être testée avec des connexions bas débit — **3G en mobilité** et **512 Kbit/s en fixe** — ou hors connexion.

Le critère est **validé** si le service numérique est utilisable **sans connexion au réseau** ou avec une **connexion bas débit**. Le débit minimum testé sera présenté dans la **déclaration d'écoconception**.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable RSE/Numérique soutenable`

Le critère 2.3 rejoint la [recommandation n°6 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=6) du [GR491](https://gr491.isit-europe.org/) (INR), « S'assurer que l'utilisation du service permet le contrôle des impacts », qui porte directement sur les flux échangés — le levier concret pour rendre un service utilisable à bas débit : les flux échangés sont-ils limités ? Le nombre de requêtes fait-il l'objet d'un suivi ? Les volumétries d'échange sont-elles évaluées et réduites (compression, minification) ? Y a-t-il des fichiers en double ? Combien de domaines différents sont sollicités ?

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Le chapitre [« Tester, évaluer et maintenir »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/8-tester-evaluer-et-maintenir) du guide des Designers Éthiques cite explicitement ce critère 2.3, avec une recommandation directement actionnable : « vérifier que le service fonctionne bien sur des connexions dégradées, par exemple 3G ». L'objectif rappelé est le même que celui du RGESN : éviter que les utilisateurs se sentent contraints de renouveler leur matériel ou leur abonnement pour accéder au service.

{{% /tab %}}

{{% tab tabName="Mode Hors Ligne" %}}

Profil(s) métier concerné(s) : `Développeur`

Pour les **applications natives**, le mode hors ligne recommandé par le critère repose concrètement sur une architecture dite **offline-first**, articulée autour de trois briques :

- **Stockage local persistant** : conserver en local (base [Room](https://developer.android.com/training/data-storage/room) sur Android, [Core Data](https://developer.apple.com/documentation/coredata) sur iOS, ou solution cross-platform comme Realm/WatermelonDB) les données déjà consultées, pour que l'application les affiche même sans réseau plutôt que d'échouer sur un écran vide.
- **File d'attente des actions écrites hors ligne** (« outbox ») : toute action de l'utilisateur nécessitant le réseau (envoi d'un formulaire, like, modification) est enregistrée localement puis rejouée automatiquement dès la reconnexion, via une tâche différée — [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) sur Android, [Background Tasks](https://developer.apple.com/documentation/backgroundtasks) sur iOS — plutôt que d'échouer silencieusement ou de bloquer l'utilisateur.
- **Indication claire de l'état de synchronisation** : signaler à l'utilisateur qu'il consulte des données en cache ou que des actions sont en attente d'envoi, pour éviter toute confusion sur ce qui a réellement été pris en compte côté serveur.

La **gestion des conflits** (une même donnée modifiée hors ligne puis à nouveau côté serveur entre-temps) doit être anticipée dès la conception : stratégie « la dernière écriture gagne », fusion, ou résolution manuelle par l'utilisateur selon la criticité de la donnée.

{{% /tab %}}

{{% tab tabName="Outils de test" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Pour tester ce critère, trois approches complémentaires :

- Les **DevTools des navigateurs** (Chrome, Edge, Firefox — gratuits) permettent de simuler un débit réseau directement en local, sans matériel ni configuration réseau particulière. Voir le détail de la manipulation pour Firefox sur la fiche [critère 2.2](../2-2_anciens-terminaux/), onglet « Outils de test ».
- [WebPageTest](https://www.webpagetest.org/) (gratuit) va plus loin : il exécute le test depuis de vrais serveurs répartis dans le monde, sur un choix de profils de connexion réels (dont 3G), et restitue un temps de chargement mesuré plutôt que simulé localement.
- Pour **automatiser ce test en CI/CD** plutôt que de le rejouer manuellement, [sitespeed.io](https://www.sitespeed.io/documentation/sitespeed.io/connectivity/) (open source) propose une option de connectivité dédiée : `sitespeed.io -c 3g https://mon-service.fr` simule directement un débit 3G, avec une image Docker documentée pour l'exécuter dans un pipeline (`docker run --network=3g sitespeedio/sitespeed.io -c 3g ...`). [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) (déjà utilisé pour les budgets de performance en page [Implémentation](../../../outils/par-phase-projet/implementation/)) permet aussi de définir un débit personnalisé via `settings.throttling`, pour les équipes qui l'utilisent déjà.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 30 janvier 2025) documente précisément le test attendu par ce critère, avec des chiffres concrets : « La page d'accueil non authentifiée, d'un poids total d'environ 1,35 Mo de données transférées (compressées), met environ 15 secondes pour être chargée complètement, et être utilisable, sur un profil de connexion **Regular 3G (750 kbps)**. » — un profil de connexion directement paramétrable dans les DevTools mentionnés ci-dessus. Le service étant construit comme une SPA (Single Page Application), la déclaration précise aussi que les pages suivant ce premier chargement restent, elles, nettement plus réactives.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) documentent un test allant plus loin que la seule simulation en DevTools : testé sous Firefox en 2G Regular après vidage du cache, puis validé en conditions réelles **en train, y compris dans des tunnels et lors de coupures réseau** (vidéo à l'appui). Grâce à Next.js et une architecture PWA, le texte se charge en priorité, les images suivent en lazy loading, et un système de cache permet une consultation hors connexion des contenus déjà chargés — « ce qui est pratique dans le train par exemple. »

{{% /tab %}}

{{< /tabs >}}
