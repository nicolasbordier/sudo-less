---
weight: 350
title: "Revue de conception"
description: "Revue de conception de sudo-less.dev : l'arbre des conséquences de chaque fonctionnalité, selon le niveau 1 de la méthode Empreinte Projet de l'ADEME (critère RGESN 2.6), et la comparaison de son architecture avec les autres options possibles (critère 3.1)."
icon: "account_tree"
date: "2026-10-31T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

Cette page est la revue de conception de **sudo-less.dev**, demandée par le critère [2.6](../../rgesn/specifications/2-6_revue-conception-code/) du RGESN. Pour chaque fonctionnalité, elle décrit les conséquences environnementales du site par rapport à un scénario sans le site, puis la décision prise. Elle suit le niveau 1, qualitatif, de la méthode [Empreinte Projet](https://base-empreinte.ademe.fr/empreinte-projet) de l'ADEME. Elle compare enfin l'architecture et les composants du site aux autres options possibles, comme le demande le critère [3.1](../../rgesn/architecture/3-1_architecture-composants/).

| | |
|---|---|
| **Date** | 31 octobre 2026 ; comparaison d'architecture le 1er novembre 2026 |
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
  - La première saisie télécharge la bibliothèque de recherche, FlexSearch, et l'index : 344 Ko compressés ; tout se passe ensuite dans le navigateur, sans requête au serveur.
  - Ouvrir la recherche ne télécharge rien : son poids est annoncé avant la première saisie.
- **Conséquences indirectes**
  - (+) Trouver directement la bonne fiche évite d'en ouvrir plusieurs.
  - (−) Pour une seule recherche, l'index pèse plus de quatre fois le poids d'une page.
- **Décision** : garder, avec la bibliothèque et l'index chargés seulement à la première saisie, et leur poids annoncé dès l'ouverture de la recherche, ce qui est fait depuis le 31 octobre 2026.

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
- **Décision** : garder pour l'instant, et comparer avec un hébergeur qui publie ses indicateurs (action 3 du [plan d'avancement](../declaration-ecoconception/#plan-davancement)).

---

## Comparaison d'architecture

Écrite le 1er novembre 2026, après la mise en ligne du site en juillet 2026 : elle confronte les choix en place aux autres options possibles. Chaque option est jugée sur ce qui s'exécute à chaque consultation, sur le serveur et dans le navigateur, puis sur ce que demandent la publication et la maintenance.

### Type de site

| Option | À chaque consultation | Publication et maintenance | Décision |
|---|---|---|---|
| **Site statique généré par Hugo** | Le serveur renvoie des fichiers déjà construits, sans calcul. Le navigateur n'exécute que 24 Ko de JavaScript : onglets, menu et mode sombre. | Une construction par publication : 0,8 s pour Hugo sur le poste du mainteneur. Hugo est un seul exécutable ; Go sert à récupérer le thème. | Retenu. |
| Autre générateur statique sans framework côté client : Jekyll, Eleventy, MkDocs | Identique. | Seule la construction diffère, et elle prend déjà moins d'une seconde avec Hugo. | Équivalent : aucun gain à changer. |
| Générateur statique qui hydrate un framework JavaScript : Docusaurus (React), VitePress (Vue) | Les pages sont construites à l'avance, mais le navigateur télécharge et exécute le framework pour les rendre interactives. | Node.js et des paquets npm à installer à chaque construction. | Écarté : le framework alourdirait chaque page, sans rien apporter à une documentation. |
| CMS dynamique : WordPress, Drupal | Le serveur exécute PHP et interroge la base de données pour chaque page absente du cache. | Un serveur d'application et une base de données tournent en permanence ; mises à jour de sécurité du CMS et de ses extensions. | Écarté. |
| Plateforme hébergée : GitBook, Notion, wiki | Une application JavaScript de l'éditeur, dont le poids et les scripts tiers ne se règlent pas (critères 1.6, 2.10 et 6.1). | Aucune construction, mais le contenu et sa présentation dépendent de l'éditeur. | Écarté. |

### Composants

| Composant | Options comparées | Choix et raison |
|---|---|---|
| Thème Lotus Docs 0.3.0, avec Bootstrap 5.3 : mise en page, menu, onglets | Thème écrit sur mesure ; autre thème Hugo de documentation | Gardé, et allégé à la construction (critère [2.9](../../rgesn/specifications/2-9_composants-interface/)) : CSS réduit aux règles utilisées, 14 Ko compressés sur une fiche ; 19 Ko de JavaScript Bootstrap pour cinq composants. Un thème sur mesure serait plus léger, mais le mainteneur devrait l'entretenir seul. Sa dernière version date d'avril 2026 : voir [Maintenance et fin de vie](../declaration-ecoconception/#maintenance-et-fin-de-vie). |
| Recherche FlexSearch, fournie par le thème | Service tiers, comme Algolia DocSearch ; [Pagefind](https://pagefind.app/) ; pas de recherche | Gardée, chargée à la première saisie : 344 Ko avec l'index. Un service tiers recevrait chaque requête (critère 1.6). Pagefind découpe son index et ne télécharge que les morceaux utiles à la requête ; son site annonce environ 100 Ko pour la plupart des sites. Il pourrait donc réduire ce poids : à mesurer à la prochaine revue. |
| Police d'icônes Material Symbols | Icônes SVG intégrées dans chaque page | Gardée, réduite aux icônes utilisées : 11,3 Ko, mis en cache par le navigateur. Des SVG intégrés ajouteraient des éléments au DOM de chaque page, le point du site le plus proche de son budget. |
| Polices du texte | Police web | Polices du système : aucune police de texte n'est téléchargée. |
| Hébergement GitHub Pages, avec le CDN Fastly ; construction sur GitHub Actions | Hébergeur qui publie ses indicateurs environnementaux ; serveur hébergé par le mainteneur | Gardés pour l'instant, mais choisis sans critère environnemental documenté (critères [2.8](../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) et [2.10](../../rgesn/specifications/2-10_services-tiers/) non validés) : à comparer (action 3 du [plan d'avancement](../declaration-ecoconception/#plan-davancement)). |
| Contrôles à la construction : Dart Sass, scripts Python, Chromium pour vérifier le budget de chaque page | Ne pas vérifier le budget | Gardés. La vérification du budget est l'étape la plus longue de la publication, 199 s sur 244 : la réduire est l'objectif fixé par publication dans la page [Empreinte environnementale](../empreinte-environnementale/). |

Le site ne repose sur aucune brique particulièrement énergivore : ni apprentissage automatique, ni chaîne de blocs, ni réalité virtuelle ou augmentée.

**Limite.** Seul le site lui-même a été mesuré. Les autres options sont comparées d'après leur fonctionnement : elles n'ont pas été construites pour être mesurées.
