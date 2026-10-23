---
weight: 100
title: "6.1 - Poids maximum et limite de requêtes par écran"
description: "Critère 6.1 du RGESN : calculer un budget de poids et de requêtes à partir de la connexion visée, le mesurer sans oublier workers et iframes, l'automatiser dans l'intégration continue et le publier dans la déclaration d'écoconception."
icon: "speed"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique s'astreint-il à un poids maximum et une limite de requête par écran ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Frontend` |
| **Critère**  | `6.1` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur l'utilisation d'un écran` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` `Responsable Produit` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire ou limiter les données téléchargées.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Par écran, il est entendu ici « écran virtuel » et non physique. Si le service numérique est un site web, l'écran désigne la page, pour une API, l'écran désigne la réponse du serveur.

Définir et suivre des indicateurs de :

- Poids maximum par écran, en tenant compte de toutes les ressources téléchargées (composants d'interface, données, contenus, scripts, feuilles de style...). Par exemple pour une page web (avec toutes les ressources chargées) qui pèse 2 Mo, l'objectif serait de descendre à 1 Mo. Selon le contexte, cet objectif peut être beaucoup plus bas.
- Requêtes client/serveur maximum par écran, en tenant compte de toutes les ressources téléchargées (composants d'interface, données, contenus, scripts, feuilles de style...). Par exemple, pour un site web, il serait intéressant d'avoir moins de 30 requêtes par page au lieu de 100.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Afficher dans la déclaration d'écoconception :

- Le poids maximum par écran défini et proportionné, et respecter cette limite ;
- Le nombre de requêtes maximum par écran défini, en précisant si la limitation du nombre de requêtes porte sur le seul chargement de la page web ou également sur son fonctionnement (par exemple : pour une page web comportant un formulaire de saisie ; est-ce que le nombre de requêtes intègre les requêtes de contrôle de champs ?).

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche sur le poids des pages étiquetée « RGESN 6.1 », mais trois fiches sur les requêtes :

- [**RWEB 0047 — « Limiter le nombre de requêtes HTTP »**](https://rweb.greenit.fr/fr/fiches/RWEB_0047-limiter-le-nombre-de-requetes-http), rattachée aux critères 6.1 et 4.9, fixe un seuil chiffré : **40 requêtes HTTP** au plus par page. Le RGESN donne pour exemple moins de 30. La fiche justifie ce seuil côté serveur : « plus le nombre de requêtes par page est important, moins vous pourrez servir de pages par serveur ». Ses techniques (concaténer les fichiers JS et CSS, regrouper les icônes, charger les images à la demande) datent en partie d'avant HTTP/2, qui fait passer plusieurs requêtes par une même connexion. Le coût d'une requête a baissé côté réseau, mais chacune reste un échange que le serveur doit traiter.
- [**RWEB 0112 — « Éviter les redirections »**](https://rweb.greenit.fr/fr/fiches/RWEB_0112-eviter-les-redirections) : chaque redirection est une requête de plus, sans contenu utile. Principe de validation : **une** redirection au plus.
- [**RWEB 0062 — « Optimiser la taille des cookies »**](https://rweb.greenit.fr/fr/fiches/RWEB_0062-optimiser-la-taille-des-cookies) rappelle qu'un cookie « est inclus dans chaque requête HTTP » : son poids se multiplie par le nombre de requêtes de l'écran.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

Le [GR491](https://gr491.isit-europe.org/) (INR) pose la question du poids dans la [recommandation n°10 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=10), en priorité **High** : [« Le volume des données présentes sur le poste utilisateurs est-il limité ? »](https://gr491.isit-europe.org/crit.php?id=10-frontend-lensemble-des-elements-transferes-sur-le-poste-d6474c) Son test est presque celui du RGESN : « Un volume maximum des composants transférés vers le device utilisateur est-il défini ? » Il rappelle que ces éléments pèsent deux fois : sur les transferts réseau et « sur les traitements nécessaires pour les manipuler sur le terminal utilisateur ».

Pour les requêtes, le conseil [« Est-ce qu'il y a un suivi du nombre de requêtes ? »](https://gr491.isit-europe.org/crit.php?id=6-frontend-les-operations-realisees-sur-le-front-end-835a00), dans la [recommandation n°6](https://gr491.isit-europe.org/?famille=frontend&num_reco=6), change d'échelle : « Combien de requêtes sont utilisées pour un parcours utilisateur ? » Un écran léger peut faire partie d'un parcours lourd s'il faut dix écrans pour accomplir une tâche. C'est le lien avec le [critère 4.3](../../ux-ui/4-3_parcours-navigation/) (parcours de navigation).

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Responsable Produit`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 6.1 dans sa section [**3. Évaluer et mesurer**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/3-evaluer-et-mesurer), rubrique « Établir un budget environnemental ».

Il propose de raisonner à l'envers : « Au lieu de concevoir sa page puis de la mesurer », se demander « quel est le poids maximum que ma page doit peser pour être visionnée rapidement quelles que soient les conditions (réseau, appareil) ? ». Son exemple est un site d'horaires de train, consulté depuis un smartphone dans le train, « avec un réseau potentiellement faible », et qui doit s'afficher en moins de 3 secondes. Le poids maximum découle de ces conditions (voir l'onglet « Calculer son budget »).

Parmi les questions à se poser, la dernière donne le sens du critère : « Qui est-ce que j'exclus actuellement si mon service requiert le transfert de X Mo de données ? »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

La fiche [**« Set goals based on performance and energy impact »**](https://www.w3.org/TR/web-sustainability-guidelines/#set-goals-based-on-performance-and-energy-impact) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) demande, dans son critère de succès « Performance goals », de « Set clear performance and environmental goals for the project, including limits on requests, elements rendered, or other measurable resource use ».

Le W3C retient les mêmes limites que le RGESN (requêtes, ressources consommées) et en ajoute une : le nombre d'**éléments affichés**. Une page peut rester légère à transférer et coûter cher au terminal si elle comporte des milliers d'éléments à mettre en page. Le second critère de la fiche, « Energy intensity », va dans le même sens : les rendus complexes, riches en scripts et en médias, « increase the computational complexity of rendering ».

{{% /tab %}}

{{% tab tabName="Calculer son budget" %}}

Profil(s) métier concerné(s) : `Responsable Produit`, `Concepteur UX / UI`

Le RGESN demande un poids maximum « proportionné ». Le calcul proposé par les Designers Éthiques le rend concret : le poids qu'une connexion transfère en un temps donné vaut **débit × durée ÷ 8**. Sans compter la latence, qui ajoute un délai à chaque aller-retour :

| Débit de la connexion | En 3 s | En 5 s | En 10 s |
|---|---:|---:|---:|
| 512 kbit/s (connexion fixe bas débit du [critère 2.3](../../specifications/2-3_connexion-bas-debit/)) | 192 Ko | 320 Ko | 640 Ko |
| 750 kbit/s (« Regular 3G ») | 281 Ko | 469 Ko | 938 Ko |
| 1,5 Mbit/s | 563 Ko | 938 Ko | 1 875 Ko |

Le calcul inverse est tout aussi parlant : à 512 kbit/s, une page de 1 Mo demande au moins **16 secondes**.

Pour situer ces valeurs, l'[HTTP Archive](https://httparchive.org/reports/page-weight) mesure chaque mois des millions de pages. En octobre 2026, la page médiane pèse environ **2,6 Mo pour 69 requêtes** sur mobile (3 Mo et 74 requêtes sur ordinateur). Un quart des pages mobiles pèse moins de 1,3 Mo environ, un dixième moins de 520 Ko. Les exemples du RGESN (1 Mo, 30 requêtes) placent donc une page parmi les plus légères du web, environ le cinquième le plus léger.

Le calcul permet aussi de vérifier qu'un budget publié tient ses promesses. La déclaration de [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) vise un service « utilisable confortablement pour le niveau « Regular 3G », c'est-à-dire 750 kbps », et fixe pour cela 2 Mo par page. À 750 kbit/s, 2 Mo demandent plus de **21 secondes**. Le budget est respecté (voir les retours d'expériences), mais il ne garantit pas le confort annoncé : il faudrait viser environ 470 Ko pour un affichage en 5 secondes.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

**1. Mesurer un écran à la main.** Dans les outils de développement du navigateur, onglet **Réseau** :

- cocher **Désactiver le cache**, pour mesurer un premier chargement ;
- recharger la page et lire le bas du panneau : nombre de requêtes, octets **transférés** (le poids réseau, celui du critère) et taille des ressources une fois décompressées ;
- faire défiler la page et utiliser ses fonctions : les ressources chargées à la demande (images différées, carte, recherche) s'ajoutent au compteur.

**2. Ne rien oublier.** Le RGESN demande de compter « toutes les ressources téléchargées ». Trois pièges, rencontrés en mesurant les sites des retours d'expériences :

- **les workers** : une carte MapLibre charge ses tuiles depuis un Web Worker. Un outil qui n'observe que la page elle-même les ignore. Sur la carte de DiaLog, la mesure passe ainsi de 36 à 57 requêtes une fois les workers pris en compte ;
- **les iframes d'un autre domaine** (vidéo, carte, formulaire intégrés) : ce sont des pages à part entière, avec leurs propres requêtes, qui comptent dans l'écran (voir le [critère 2.10](../../specifications/2-10_services-tiers/) sur les services tiers) ;
- **les protections anti-robots** : un outil automatisé peut recevoir une page de vérification au lieu du site. Lors des mesures des retours d'expériences, l'un des sites a renvoyé une page de vérification de plus de 1 Mo : le résultat ne disait rien du site lui-même.

**3. Automatiser le contrôle** dans l'intégration continue. Le fichier `budget.json` de Lighthouse a été supprimé dans sa version 12 ; les assertions de [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md) sur l'audit `resource-summary` restent disponibles :

```json
{
  "ci": {
    "collect": {
      "url": ["http://localhost:8080/", "http://localhost:8080/carte"]
    },
    "assert": {
      "assertions": {
        "resource-summary:total:size": ["error", {"maxNumericValue": 900000}],
        "resource-summary:total:count": ["error", {"maxNumericValue": 40}]
      }
    }
  }
}
```

Le poids s'exprime ici en **octets**. Le contrôle échoue dès qu'un écran dépasse le budget, avant la mise en production. Il faut lister les écrans les plus lourds, pas seulement la page d'accueil, et vérifier une fois à la main, dans l'onglet Réseau, que l'outil compte bien les workers et les iframes de ces écrans.

**4. Pour une API**, l'« écran » est la réponse du serveur. Le budget porte alors sur la taille des réponses : pagination avec une taille de page par défaut raisonnable, sélection des champs utiles, compression ([critère 6.3](../6-3_compression-ressources/)).

**5. Préciser le périmètre**, comme l'exige le moyen de test : le budget porte-t-il sur le seul chargement, ou aussi sur l'utilisation de l'écran ? Pour un formulaire, les contrôles de champs envoient des requêtes (voir le [critère 4.9](../../ux-ui/4-9_requetes-saisie-utilisateur/)) ; pour une carte, chaque déplacement charge de nouvelles tuiles.

**6. Documenter** dans la déclaration d'écoconception. Par exemple : « Budget par écran, mesuré au premier chargement, cache désactivé, sans interaction : 900 Ko transférés et 40 requêtes au plus, workers et iframes compris. Les requêtes de contrôle des champs de formulaire ne sont pas comptées. Contrôle automatique à chaque fusion avec Lighthouse CI sur les 5 écrans les plus lourds. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

Le critère 6.1 fixe la contrainte ; d'autres critères donnent les moyens de la tenir.

Critères déjà publiés sur ce site :

- le [critère 1.5](../../strategie/1-5_objectifs-environnementaux/) (objectifs environnementaux) : les budgets techniques y sont présentés comme la forme la plus courante d'objectif chiffré, avec les budgets publiés par DiaLog, SPOTE, le Musée d'arts de Nantes et Alt Impact ;
- le [critère 2.3](../../specifications/2-3_connexion-bas-debit/) (connexion bas débit) donne le débit de référence pour calculer le budget ;
- le [critère 4.3](../../ux-ui/4-3_parcours-navigation/) (parcours de navigation) étend le raisonnement de l'écran au parcours, et présente aussi Lighthouse CI ;
- les critères [5.1](../../contenus/5-1_format-images/) à [5.4](../../contenus/5-4_compression-videos/) (images et vidéos) traitent les ressources qui pèsent le plus lourd ;
- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) : leurs ressources comptent dans le budget de l'écran.

Les critères suivants de la famille Frontend sont les leviers techniques du budget : le [6.2](../6-2_cache-navigateur/) (cache) et le [6.3](../6-3_compression-ressources/) (compression), le [6.4](../6-4_dimensions-images/) (dimensions des images), puis, pas encore publié sur ce site, le 6.5 (chargement des seules ressources utiles).

Les [outils pour le développement front-end](../../../outils/par-metier/dev-front/) récapitulent les outils de mesure et de définition de budget déjà présentés sur ce site.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Trois services publics ont publié un budget par écran, présenté au [critère 1.5](../../strategie/1-5_objectifs-environnementaux/). Leurs pages ont été mesurées le 20 octobre 2026 : premier chargement dans Chromium 155, cache désactivé, sans défilement ni interaction, workers et iframes compris, sur un écran d'ordinateur (1366 × 768 pixels).

| Service et budget déclaré | Écran mesuré | Requêtes | Poids transféré |
|---|---|---:|---:|
| [DiaLog](https://dialog.beta.gouv.fr/ecoconception) : 40 requêtes, 900 Ko | Accueil | 36 | 1 034 Ko |
| | Carte des restrictions | 57 | 2 041 Ko |
| | Liste des arrêtés | 31 | 821 Ko |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) : 30 requêtes, 750 Ko | Accueil | 53 | 1 472 Ko |
| [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) : 120 requêtes, 2 Mo, 5 domaines | Accueil | 46 (2 domaines) | 1 039 Ko |

Sur un écran de smartphone (390 × 844), les résultats sont proches : 37 requêtes et 1 034 Ko pour l'accueil de DiaLog, 52 requêtes et 1 265 Ko pour celui du Musée d'arts de Nantes, 46 requêtes et 1 030 Ko pour SPOTE.

- **DiaLog** marque d'ailleurs le critère **« Non validé »** dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf) : « Ce critère ne peut pas être validé à l'heure actuelle à cause du chargement de la carte qui nécessite plus de requêtes. » La mesure lui donne raison. La carte dépasse le budget en requêtes comme en poids, et l'accueil dépasse de peu le poids prévu. La liste des arrêtés le respecte.
- Le **Musée d'arts de Nantes** affiche dans sa déclaration « Pas plus de 750 ko de données transférées au premier chargement de chaque page » et « Pas plus de 30 requêtes ». Sa page d'accueil dépasse les deux, d'environ deux fois en poids.
- **SPOTE** respecte largement son budget, mais ce budget est généreux au regard de la connexion visée (voir l'onglet « Calculer son budget »).

Un budget ne vaut que s'il est mesuré dans la durée : c'est l'intérêt du contrôle automatique de l'onglet « Mise en œuvre technique ».

{{% /tab %}}

{{< /tabs >}}
