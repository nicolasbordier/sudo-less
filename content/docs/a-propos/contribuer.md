---
weight: 100
title: "Contribuer"
description: "Comment contribuer à sudo-less.dev : signaler une erreur, proposer un retour d'expérience ou un outil, améliorer une fiche."
icon: "handshake"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

**sudo-less.dev** est un projet open source — les contributions sont les bienvenues. Vous pouvez :

- **Signaler une erreur ou un lien cassé** via une [issue](https://github.com/nicolasbordier/sudo-less/issues).
- **Proposer un retour d'expérience ou un outil manquant** via une [pull request](https://github.com/nicolasbordier/sudo-less/pulls).
- **Améliorer une fiche existante** : préciser une mise en œuvre, corriger une source, ajouter un exemple réel.

---

## Relecture des contributions

Chaque contribution est relue par le mainteneur du projet avant d'être intégrée, comme chacun de ses propres commits. La relecture vérifie notamment :

- **le contenu** : les sources sont citées et datées ; chaque mesure indique sa date, son outil et ses conditions ; les exemples mesurés portent sur des services externes, pas sur ce site ; une fiche se lit en 10 minutes au plus ;
- **le code** : pas de nouveau service tiers, de nouvelle police ni de nouvelle bibliothèque sans justification ; le poids et le nombre de requêtes des pages concernées sont comparés avant et après la modification ; une ressource ne se charge que si elle sert.

Une nouvelle fonctionnalité passe aussi par la [revue de conception](../revue-conception/), qui en décrit les conséquences environnementales avant son développement.

---

## Licences

Ce projet utilise une double licence :

| Périmètre | Licence | Fichier |
|---|---|---|
| **Code source** (templates, configuration, assets techniques) | [MIT](https://opensource.org/licenses/MIT) | [LICENSE](https://github.com/nicolasbordier/sudo-less/blob/main/LICENSE) |
| **Contenu éditorial** (fiches, textes, analyses dans `content/`) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) | [LICENSE-CONTENT](https://github.com/nicolasbordier/sudo-less/blob/main/LICENSE-CONTENT) |

En résumé : vous pouvez librement réutiliser, modifier et redistribuer le code et le contenu, y compris à des fins commerciales, à condition de créditer sudo-less.dev et de partager vos modifications du contenu éditorial sous la même licence CC BY-SA 4.0.
