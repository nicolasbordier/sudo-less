# sudo-less.dev

> `sudo less` — Faites moins, faites mieux, déployez sobre.

Guide pratique du [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) critère par critère : outils, retours d'expérience et méthodes pour écoconcevoir vos services numériques.

## À propos

Le numérique pèse 2,5 % de l'empreinte carbone en France — et entre 50 % et 80 % des fonctionnalités développées sont rarement ou jamais utilisées. Le Référentiel Général d'Écoconception de Services Numériques (RGESN) pose un cadre pour inverser cette tendance, mais il reste souvent perçu comme un document institutionnel difficile à mettre en pratique.

**sudo-less.dev** traduit chaque critère du RGESN en fiches actionnables : objectif, mise en œuvre pas à pas, outils gratuits, référentiels complémentaires (RWEB, AFNOR SPEC 2201, GR491, ISO 20125…) et retours d'expérience concrets d'organisations qui sont passées à l'acte.

L'ambition est simple : faire de l'écoconception un réflexe, pas une contrainte. Parce que la meilleure ligne de code est celle qu'on n'écrit pas.

## Pour qui ?

- **Porteurs de projet** — questionner l'utilité avant de lancer un développement
- **Produit (PO, PM)** — arbitrer le périmètre fonctionnel et prioriser sans surcharger
- **UX Designers** — concevoir sobre dès la phase d'exploration
- **Architectes** — concevoir des systèmes sobres, mutualisés et interopérables dès le cadrage technique
- **Développeurs** — implémenter les bonnes pratiques critère par critère
- **Ops** — dimensionner l'infrastructure au juste besoin et piloter les indicateurs d'impact en production
- **Responsables RSE / Numérique soutenable** — structurer et piloter la démarche

## Stack technique

Ce site est construit avec [Hugo](https://gohugo.io/) et le thème [Lotus Docs](https://lotusdocs.dev/).

## Contribuer

Les contributions sont les bienvenues ! Vous pouvez :

- Signaler une erreur ou un lien cassé via une [issue](../../issues)
- Proposer un retour d'expérience ou un outil manquant via une [pull request](../../pulls)
- Améliorer une fiche existante

Merci de respecter les licences décrites ci-dessous pour toute contribution.

## Licences

Ce projet utilise une double licence :

| Périmètre | Licence | Fichier |
|---|---|---|
| **Code source** (templates, configuration, assets techniques) | [MIT](https://opensource.org/licenses/MIT) | [LICENSE](./LICENSE) |
| **Contenu éditorial** (fiches, textes, analyses dans `content/`) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) | [LICENSE-CONTENT](./LICENSE-CONTENT) |

En résumé : vous pouvez librement réutiliser, modifier et redistribuer le code et le contenu, y compris à des fins commerciales, à condition de créditer sudo-less.dev et de partager vos modifications du contenu éditorial sous la même licence CC BY-SA 4.0.
