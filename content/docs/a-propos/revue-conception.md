---
weight: 350
title: "Revue de conception"
description: "Revue de conception de sudo-less.dev : l'arbre des conséquences de chaque fonctionnalité, selon le niveau 1 de la méthode Empreinte Projet de l'ADEME (critère RGESN 2.6)."
icon: "account_tree"
date: "2026-10-31T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

Cette page est la revue de conception de **sudo-less.dev**, demandée par le critère [2.6](../../rgesn/specifications/2-6_revue-conception-code/) du RGESN. Pour chaque fonctionnalité, elle décrit les conséquences environnementales du site par rapport à un scénario sans le site, puis la décision prise. Elle suit le niveau 1, qualitatif, de la méthode [Empreinte Projet](https://base-empreinte.ademe.fr/empreinte-projet) de l'ADEME.

| | |
|---|---|
| **Date** | 31 octobre 2026 |
| **Réalisée par** | Le mainteneur du site |
| **Prochaine revue** | À chaque nouvelle fonctionnalité, et au plus tard en octobre 2027 |

L'arbre est présenté en listes plutôt qu'en diagramme : un diagramme demanderait une bibliothèque JavaScript de plus.

---

## Scénario de référence

Sans sudo-less, une équipe qui applique le RGESN part du PDF du référentiel (131 pages, 4,18 Mo) ou de ses pages critère par critère. Elle cherche ensuite elle-même, site par site, les référentiels complémentaires (GR491, RWEB, W3C…), les outils et des exemples réels.

---

## Arbre des conséquences

### 1. Fiches RGESN

- **Conséquences directes**
  - Chaque fiche transfère environ 100 Ko (HTML, CSS, JavaScript et police d'icônes), servis par un CDN, sans calcul sur un serveur.
  - Chaque publication reconstruit le site sur GitHub Actions.
- **Conséquences indirectes**
  - (+) Les équipes appliquent le RGESN avec des mises en œuvre testées et des exemples réels, ce qui peut réduire l'empreinte de leurs propres services. C'est la raison d'être du site, mais ce gain n'est pas mesuré.
  - (+) Pour chaque critère, une fiche réunit ce que disent plusieurs référentiels : le lecteur n'a pas à les chercher un par un.
  - (−) Les mesures publiées obligent à charger plusieurs fois les sites étudiés dans des navigateurs automatisés, au moment de la rédaction.
  - (−) Effet rebond possible : une fiche peut pousser à multiplier les audits et les outils de mesure, qui consomment eux aussi.
- **Décision** : garder. Chaque fiche se lit en 10 minutes au plus, et chaque mesure est faite une fois, datée, puis citée plutôt que refaite.

### 2. Recherche

- **Conséquences directes**
  - La première recherche télécharge un index de 336 Ko compressés ; tout se passe ensuite dans le navigateur, sans requête au serveur.
  - La bibliothèque de recherche, FlexSearch (6,4 Ko), se charge sur chaque page, même sans recherche.
- **Conséquences indirectes**
  - (+) Trouver directement la bonne fiche évite d'en ouvrir plusieurs.
  - (−) Pour une seule recherche, l'index pèse plus de quatre fois le poids d'une page.
- **Décision** : garder, avec l'index chargé seulement à l'ouverture de la recherche, ce qui est déjà fait. Charger aussi FlexSearch à ce moment, et annoncer le poids de l'index (action 1 du [plan d'avancement](../declaration-ecoconception/#plan-davancement)).

### 3. Pages de synthèse : Getting Started, Outils, Retours d'expérience, Autres référentiels

- **Conséquences directes**
  - Environ 100 Ko par page, comme une fiche.
- **Conséquences indirectes**
  - (+) Elles orientent vers les fiches utiles selon le métier ou la phase du projet.
  - (−) La page Outils présente des outils de mesure, dont l'usage répété a lui aussi un coût.
- **Décision** : garder.

### 4. « Rédiger ma déclaration » et la déclaration du site

- **Conséquences directes**
  - Deux pages de texte.
- **Conséquences indirectes**
  - (+) Elles incitent à publier une déclaration, critères non validés compris.
  - (−) Une déclaration peut servir d'affichage plus que de démarche. Le site limite ce risque en citant des déclarations réelles, avec leurs critères non validés.
- **Décision** : garder.

### 5. Page d'accueil

- **Conséquences directes**
  - L'illustration pesait 45 Ko, en 1 600 pixels de large pour 522 affichés sur un ordinateur.
  - Le badge Ecoindex se chargeait depuis un service tiers sans IPv6, à qui il transmettait l'adresse IP de chaque visiteur.
- **Décision** : alléger, ce qui a été fait le 31 octobre 2026. Le badge est remplacé par un simple lien vers le résultat, et l'illustration est proposée en quatre largeurs : le navigateur charge de 12 à 42 Ko selon l'écran, 18 Ko sur un ordinateur courant.

### 6. Mode sombre

- **Conséquences directes**
  - Un petit script, chargé avec le thème.
- **Conséquences indirectes**
  - (+) Sur un écran OLED, un fond sombre consomme moins d'énergie.
- **Décision** : garder.

### 7. Hébergement et publication

- **Conséquences directes**
  - Site statique hébergé par GitHub Pages et servi par le CDN Fastly ; construction sur GitHub Actions à chaque publication.
- **Conséquences indirectes**
  - (+) Contrairement à un CMS, aucun serveur d'application ni aucune base de données ne tourne en permanence.
  - (−) L'hébergeur ne publie pas d'indicateurs environnementaux, et la durée de cache, fixée à 10 minutes, ne se règle pas.
- **Décision** : garder pour l'instant, et comparer avec un hébergeur qui publie ses indicateurs (action 5 du plan d'avancement).
