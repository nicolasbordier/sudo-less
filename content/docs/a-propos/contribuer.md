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

## Durée de vie des contenus

Un contenu dépassé induit en erreur, et il alourdit le site : chaque page s'ajoute à l'index de recherche et au menu de toutes les autres. Chaque fiche indique la version et la date du critère RGESN qu'elle traite, et chaque page la date de sa dernière mise à jour. Entre deux relectures, les pages s'enrichissent au fil des nouveautés : outils, retours d'expérience, sources.

| Contenu | Conservé tant que… | Ensuite |
|---|---|---|
| Fiche RGESN | le critère existe dans la version en vigueur du RGESN | Quand le RGESN évolue, la fiche est mise à jour dans les 3 mois. Si le critère est supprimé, la fiche est retirée et redirige vers le critère le plus proche ; si des critères sont fusionnés, leurs fiches le sont aussi. |
| Toute page | sa dernière mise à jour date de moins de 12 mois | La page est relue : texte du critère, liens, outils et retours d'expérience. Elle est alors mise à jour, fusionnée avec une autre ou retirée. |
| Outil cité | son site répond et l'outil est maintenu | L'outil est retiré à la relecture si son site a disparu, si son dépôt est archivé ou s'il n'a publié aucune version depuis 2 ans. |
| Retour d'expérience | sa source est en ligne | La source est remplacée par sa copie sur le [Web Archive](https://web.archive.org/) si elle existe ; sinon, le retour est retiré. Il l'est aussi quand un retour plus récent de la même organisation le remplace. |
| Mesure datée | elle a moins de 2 ans | La mesure est refaite, ou retirée. |

- **Signalement automatique** : à chaque publication, la construction du site liste les pages dont la dernière mise à jour date de plus de 12 mois. Le mainteneur décide pour chacune : mise à jour, fusion ou retrait.
- **Archivage** : le site ne publie que la version en vigueur de chaque page. Les versions précédentes et les pages retirées restent dans l'[historique du dépôt](https://github.com/nicolasbordier/sudo-less/commits/main/), sans autre copie en ligne.
- **Données techniques** : le site ne stocke aucune donnée de visiteur. Chez GitHub, l'archive de chaque déploiement expire après 1 jour, le cache de construction est supprimé après 7 jours sans usage, et les journaux de construction après 30 jours.
- **Suivi** : à chaque mise à jour de la [déclaration d'écoconception](../declaration-ecoconception/), le poids du site construit et celui de l'index de recherche y sont relevés.

---

## Licences

Ce projet utilise une double licence :

| Périmètre | Licence | Fichier |
|---|---|---|
| **Code source** (templates, configuration, assets techniques) | [MIT](https://opensource.org/licenses/MIT) | [LICENSE](https://github.com/nicolasbordier/sudo-less/blob/main/LICENSE) |
| **Contenu éditorial** (fiches, textes, analyses dans `content/`) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) | [LICENSE-CONTENT](https://github.com/nicolasbordier/sudo-less/blob/main/LICENSE-CONTENT) |

En résumé : vous pouvez librement réutiliser, modifier et redistribuer le code et le contenu, y compris à des fins commerciales, à condition de créditer sudo-less.dev et de partager vos modifications du contenu éditorial sous la même licence CC BY-SA 4.0.
