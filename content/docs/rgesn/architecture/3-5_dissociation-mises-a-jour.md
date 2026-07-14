---
weight: 500
title: "3.5 - Dissociation des mises à jour correctives et évolutives"
description: "Critère 3.5 du RGESN : pourquoi et comment dissocier les mises à jour correctives des mises à jour évolutives, avec changelog et politique de support à long terme."
icon: "manage_history"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il d'installer des mises à jour correctives indépendamment des mises à jour évolutives de façon transparente ?

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
| **Critère**  | `3.5` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne propose pas de mises à jour évolutives (non essentielles)` |
| **Métiers concernés** | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Depuis l'ordonnance n° 2021-1247 en date du 29 septembre 2021 relative à la garantie légale de conformité pour les biens, les contenus numériques et les services numériques, le Code de la consommation prévoit plusieurs obligations concernant les mises à jour logicielles afin de garantir la réception des mises à jour nécessaires à la conformité des biens pendant toute la durée de garantie légale de conformité (deux ans ou plus), ou toute la durée du contrat si la fourniture du bien est garantie au-delà de deux ans. Par ailleurs, plusieurs obligations sont définies pour les vendeurs concernant les mises à jour non nécessaires à la conformité du bien en termes d'information au consommateur et de possibilité de refus et de désinstallation de la mise à jour par ce dernier.

Dans la continuité de ces dispositions, l'objectif de ce critère est donc de limiter la contribution à l'obsolescence des équipements en permettant à l'utilisateur d'opter uniquement pour les mises à jour nécessaires au bon fonctionnement, à la sécurité et à la conformité du service ou de l'appareil. Cette dissociation peut aussi éviter l'ajout de fonctionnalités « de confort » pouvant être inutilisables sur son appareil ou exiger des ressources matérielles ou informatiques supplémentaires susceptibles de favoriser une obsolescence rapide des terminaux.

Ce critère vise également à promouvoir les politiques de support à long terme (« long-term support ») et le fonctionnement du service numérique sur des systèmes d'exploitation d'ancienne génération. Il s'agira également d'accroître la transparence de l'information sur le type de mises à jour installées et de prévenir les risques d'**obésiciel** (ce terme désigne la surallocation de ressources systèmes ou matérielles pour un service, en particulier avec l'inclusion de nouvelles versions ou de fonctionnalités qui ne sont pas indispensables).

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Ce critère est en particulier pertinent pour un service numérique de type API / composants / bibliothèque / framework / outils open source et plus rarement pour un service destiné à des utilisateurs finals.

Il est possible d'installer de façon dissociée les mises à jour correctives, ou toute autre mise à jour essentielle à la conformité et à la sécurité du service numérique ou du terminal de l'utilisateur, et les mises à jour évolutives qui ne sont pas nécessaires à la conformité du bien.

Par ailleurs, la fréquence des mises à jour évolutives non nécessaires doit être suivie. Si la nature du service le permet, il convient de laisser la possibilité d'installer les mises à jour correctives indépendamment des mises à jour évolutives, sur demande de l'utilisateur.

De façon générale, les mises à jour évolutives ne doivent pas empêcher le service numérique de fonctionner sur toute la durée de maintenance des systèmes d'exploitation supportés (sous réserve d'absence de contraintes techniques ou de sécurité). La transparence des changements effectués doit être garantie avec la mise à disposition d'un journal de modifications (ou changelog). De plus, une stratégie de gestion de versions optimale devrait être encouragée, avec par exemple la proposition de versions « long-term support ».

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère :

- Indiquer, dans la description des mises à jour d'une application (changelog ou journal des modifications), s'il s'agit d'une mise à jour de sécurité/maintenance (« corrective ») ou s'il s'agit d'une mise à jour évolutive ajoutant des fonctionnalités.
- S'assurer que les mises à jour évolutives non essentielles à la conformité du service n'empêchent pas le service de fonctionner pendant toute la durée de maintenance des systèmes d'exploitation supportés.
- Garantir, lorsque cela est possible, la possibilité d'installer de façon dissociée les mises à jour essentielles à la conformité et à la sécurité du service numérique ou du terminal de l'utilisateur aux mises à jour évolutives non nécessaires à la conformité du bien.
- Si possible, vérifier la présence d'une stratégie de gestion des versions du service visant à l'optimisation des mises à jour à effectuer, avec par exemple la fourniture de versions du service « Long-term support ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="3">}}
{{% tab tabName="Semantic Versioning" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Le critère précise lui-même être « en particulier pertinent pour un service numérique de type API / composants / bibliothèque / framework / outils open source » — c'est exactement le terrain du [Semantic Versioning](https://semver.org/lang/fr/) (SemVer), la convention de numérotation `MAJOR.MINOR.PATCH` devenue standard de facto dans l'écosystème open source (npm, la plupart des gestionnaires de paquets) :

- **PATCH** (ex. 2.1.3 → 2.1.4) : correction de bug rétrocompatible, sans nouvelle fonctionnalité — c'est la « mise à jour corrective » du critère.
- **MINOR** (ex. 2.1.4 → 2.2.0) : ajout de fonctionnalité rétrocompatible — une « mise à jour évolutive » qui ne casse rien d'existant.
- **MAJOR** (ex. 2.2.0 → 3.0.0) : changement non rétrocompatible.

Adopter SemVer donne mécaniquement à l'utilisateur (ou à l'outil de gestion de dépendances) le moyen de distinguer une mise à jour corrective d'une mise à jour évolutive **par le seul numéro de version**, sans avoir à lire une description — la condition de base pour permettre l'installation dissociée demandée par le critère.

{{% /tab %}}

{{% tab tabName="Changelog" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Porteur de projet`

Le critère demande explicitement un « journal de modifications (changelog) ». [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) est la convention la plus largement adoptée pour structurer ce document : chaque version y liste ses changements sous des catégories fixes — `Ajouté`, `Modifié`, `Déprécié`, `Supprimé`, `Corrigé`, `Sécurité` — la catégorie `Corrigé`/`Sécurité` correspondant directement aux mises à jour correctives du critère, les autres aux mises à jour évolutives.

Un changelog structuré de cette façon permet à l'utilisateur (ou à un outil automatisé) de savoir immédiatement, pour chaque version publiée, si elle ne contient que des corrections — et donc si elle peut être installée sans risque de changement de comportement — sans avoir à lire le code source ou les tickets de développement associés.

{{% /tab %}}

{{% tab tabName="Support à long terme (LTS)" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Qualité`

Le critère encourage explicitement les « versions long-term support ». Cette politique se traduit très différemment d'un langage ou runtime à l'autre, à connaître avant de calquer une politique de version sur un seul exemple :

| Langage / Runtime | Politique de support | Détail |
|---|---|---|
| [Node.js](https://nodejs.org/en/about/previous-releases) | LTS explicite | Une nouvelle version majeure tous les 6 mois, mais une version sur deux est désignée **LTS** : elle ne reçoit plus de nouvelles fonctionnalités mais continue de recevoir des correctifs de sécurité et de bugs pendant **30 mois** après son passage en LTS — une cible stable sur laquelle ne recevoir que des mises à jour correctives, exactement la logique demandée par ce critère. |
| [Java](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) | LTS explicite | Une version LTS tous les 2 ans (8, 11, 17, 21, 25…) avec un support à paliers : 5 ans de correctifs (Premier Support), +3 ans supplémentaires (Extended Support), puis un support illimité mais sans correctif (Sustaining Support). |
| [Python](https://devguide.python.org/versions/) | Support équivalent, sans le nom « LTS » | Chaque version bénéficie d'un cycle de 5 ans normalisé par [PEP 602](https://peps.python.org/pep-0602/) : 2 ans de correctifs de bugs, puis 3 ans supplémentaires en corrections de sécurité uniquement. |
| C / C++ | Pas de LTS au niveau du langage | Une norme ISO (C++17, C++20, C++23…) n'est **jamais dépréciée ni mise en fin de vie** en tant que telle — la notion de support à long terme s'applique au **compilateur** (GCC, Clang…) ou à la distribution qui le fournit, pas au standard lui-même. Vérifier le [statut de support C++ de GCC](https://gcc.gnu.org/projects/cxx-status.html), pas une hypothétique « version LTS du C++ ». |
| [Rust](https://github.com/rust-lang/rfcs/pull/2483) | Aucun LTS | Modèle 100 % rolling release (nouvelle version stable toutes les 6 semaines, seule la dernière est officiellement supportée). Une RFC proposant un canal LTS a été discutée mais jamais adoptée. Les *editions* (2015, 2018, 2021, 2024) ne sont pas un mécanisme de support dans la durée : ce sont des épisodes de langage optionnels qui évitent de casser la compatibilité, et les éditions plus anciennes ne sont jamais mises en fin de vie — mais elles ne reçoivent pas non plus de correctifs qui leur seraient propres. |
| [Go](https://go.dev/doc/devel/release) | Aucun LTS | Politique différente de Rust pour un résultat similaire : **les deux dernières versions majeures** sont supportées en permanence (nouvelle version majeure tous les 6 mois, donc environ 1 an de support glissant par version), avec des correctifs de sécurité mineurs (1.6.1, 1.6.2…). Pas de branche LTS séparée : l'équipe Go encourage explicitement la mise à jour continue plutôt qu'un engagement de support long sur une version figée. |

Le même principe existe aussi au niveau des systèmes d'exploitation, avec là encore des politiques très variées :

| Système d'exploitation | Politique de support | Détail |
|---|---|---|
| [Ubuntu](https://ubuntu.com/about/release-cycle) | LTS explicite | Une version LTS tous les deux ans, avec **5 ans de mises à jour de sécurité** (extensible à 10 ans via Ubuntu Pro), contre 9 mois seulement pour une version standard. |
| [Debian](https://www.debian.org/releases/) | LTS explicite, à paliers | Une version stable tous les ~2 ans : **3 ans** de support standard par l'équipe sécurité Debian, puis **2 ans** supplémentaires de LTS assurés par une équipe de volontaires/entreprises distincte, et enfin une **Extended LTS (ELTS)** commerciale (via [Freexian](https://www.freexian.com/lts/extended/)) qui peut porter le total à 10 ans. |
| [RHEL](https://access.redhat.com/support/policy/updates/errata) | LTS le plus long du marché | Cycle de **10 ans** en 3 phases (Full Support, Maintenance Support, Extended Life Phase), extensible via l'add-on **Extended Life Cycle Support (ELS)** de 1 à 3 ans supplémentaires — jusqu'à 14 ans de couverture cumulée sur certaines versions mineures. |
| [Windows](https://learn.microsoft.com/en-us/windows/whats-new/ltsc/overview) | Deux canaux distincts | Le canal grand public (General Availability Channel) reçoit une mise à jour de fonctionnalités par an, supportée 2 à 3 ans. Le canal **LTSC** (Long-Term Servicing Channel), réservé aux systèmes spécialisés (matériel médical, caisses enregistreuses, guichets automatiques), ne reçoit aucune mise à jour de fonctionnalités mais un support figé de **5 ans** (10 ans pour la variante IoT). |
| macOS | Pas de politique LTS publiée | Apple ne publie **aucun engagement officiel de durée de support** — une nouvelle version majeure par an, avec des correctifs de sécurité généralement maintenus sur les **deux versions précédentes** en plus de la dernière (donc ~3 ans de facto), sans annonce publique de fin de support ni garantie contractuelle (suivi communautaire via [endoflife.date](https://endoflife.date/macos)). |

Le signal à retenir : une politique « LTS » n'est pas un standard universel — elle doit être définie et documentée pour le langage/framework/OS réellement utilisé, plutôt que supposée par analogie avec Node.js ou Ubuntu.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non applicable »**, sans autre justification que ce statut — cohérent avec la « Mise en œuvre » du critère elle-même, qui précise qu'il concerne « plus rarement » les services destinés aux utilisateurs finaux comme FACE, et davantage les API, bibliothèques et frameworks.

{{% /tab %}}

{{< /tabs >}}
