---
weight: 800
title: "1.8 - Efforts d'open source"
description: "Critère 1.8 du RGESN : pourquoi et comment publier le code source d'un service numérique en licence libre pour allonger sa durée de vie et celle du matériel associé."
icon: "article"
date: "2026-07-03T00:00:00+01:00"
lastmod: "2026-07-03T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il mis en place des efforts d'open source ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Stratégie` |
| **Critère**  | `1.8` |
| **Phase** | `Toutes les phases` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Porteur de projet` `Responsable Développement` `Responsable Juridique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.8/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'**open source** permet la réutilisation du code pour d'autres projets, évitant ainsi un **gaspillage de ressources** dédiées. La publication du code source d'un service numérique en format libre permet d'**allonger la durée de vie du service** en s'appuyant sur la collaboration avec les communautés de développeurs et de chercheurs pour pallier d'éventuels défauts ou ajouter de nouvelles fonctionnalités. Elle renforce également son **auditabilité** et sa **transparence**, y compris d'un point de vue environnemental.

L'open source est aussi un levier pour **allonger la durée de vie du matériel** associé à l'utilisation d'un service numérique : par exemple, les applications ou pilotes ouverts associés à un objet connecté (enceinte, montre connectée…) ou à un périphérique (imprimante…) permettent de suppléer à la fin de vie de programmes propriétaires nécessaires à leur utilisation.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

**Publier le code source** du service numérique en licence libre pour les éléments qui ne sont **pas couverts par des obligations de confidentialité**, et dans la limite des **droits de propriété intellectuelle** applicables.

Lorsque cela est possible, l'**utilisation de code open source** existant est également à privilégier pour la conception et le développement du service, plutôt que de redévelopper des briques déjà disponibles.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le **code source** du service numérique est publié en open source lorsqu'il n'est soumis ni à des restrictions de confidentialité, ni aux droits de propriété intellectuelle de tiers.

Si certaines parties du code ne sont **pas publiées en open source**, les raisons de ce choix doivent être **justifiées dans la déclaration d'écoconception** du service, afin d'être auditables par un tiers. Le fournisseur devra le cas échéant faire état de ses **efforts pour ouvrir tout ou partie** de son code source. Lorsque cela est possible, le service numérique devrait également **utiliser du code open source** pour son propre fonctionnement.

Le critère est **validé** si le code du service est publié en licence libre, **ou** si les choix et efforts effectués en la matière sont justifiés dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="2">}}
{{% tab tabName="code.gouv.fr / DINUM" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable Juridique`

Pour un acteur public français, l'ouverture du code source n'est pas qu'une bonne pratique d'écoconception : c'est une **obligation légale**. Depuis la loi pour une République numérique, le code source produit par une administration est un **document administratif communicable**, soumis aux mêmes obligations d'ouverture que les bases de données publiques.

Le [Pôle open source et communs numériques de la DINUM](https://code.gouv.fr/fr/), qui pilote cette politique depuis la circulaire du Premier ministre du 27 avril 2021, propose plusieurs ressources directement actionnables :

- [code.gouv.fr](https://code.gouv.fr/fr/) recense les codes sources et bibliothèques publiés par les administrations, pour favoriser leur **réutilisation** plutôt qu'un redéveloppement (cf. mise en œuvre du critère) ;
- son [guide des licences libres](https://code.gouv.fr/fr/doc/licences-libres-dinum/) recommande, pour un code source public, des licences reconnues par la FSF et l'OSI : permissives (**MIT**, **Apache 2.0**, **BSD**), copyleft (**GPL**, **AGPL**, **LGPL v3**) ou la famille française **CeCILL** (CEA/CNRS/Inria, compatible GPL et conçue pour le droit français) ;
- le [Socle Interministériel des Logiciels Libres (SILL)](https://code.gouv.fr/sill/) référence les logiciels libres recommandés pour l'administration, à privilégier lors du choix de composants tiers.

{{% /tab %}}

{{% tab tabName="beta.gouv.fr" %}}

Profil(s) métier concerné(s) : `Porteur de projet`

Le [Manifeste beta.gouv.fr](https://beta.gouv.fr/manifeste) fait de l'open source un principe fondateur plutôt qu'une option : « en échange de cette autonomie, les équipes assurent la plus grande transparence possible sur leur travail : **code open source**, mesure d'impact public, budget ouvert, démonstrations fréquentes, documentation facilement accessible ». Toutes les startups d'État publient ainsi par défaut leur code sur l'organisation [github.com/betagouv](https://github.com/betagouv), qui héberge plusieurs centaines de dépôts.

Cette politique de « open source par défaut » illustre concrètement l'esprit du critère 1.8 : l'ouverture du code n'est pas traitée comme un effort ponctuel à justifier a posteriori, mais comme une contrainte de conception dès le départ du projet.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Le contraste entre deux déclarations d'écoconception publiques illustre bien les deux issues possibles de ce critère :

- [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 30 janvier 2025) marque ce critère **« Non validé »**, avec la justification suivante : « Le service numérique ne publie pas son code source sous licence open-source à ce jour. » — un exemple concret de la situation « non conforme mais honnêtement documentée » que le critère anticipe explicitement.
- À l'inverse, l'ensemble des startups d'État de [beta.gouv.fr](https://github.com/betagouv) valident ce critère par construction : le code de services déjà cités dans ce guide (DiaLog, Territoires en Transitions…) est public dès le premier commit, sans qu'un effort de mise en conformité a posteriori soit nécessaire.

Ce contraste rappelle que ce critère, noté « Fort » en difficulté, se traite bien plus facilement **en amont** (choisir une licence et un dépôt public dès l'initialisation du projet) qu'**a posteriori** sur un code déjà écrit sans cette contrainte — où subsistent alors des questions de propriété intellectuelle, de secrets métier mêlés au code, ou de dépendances propriétaires à isoler avant publication.

Côté secteur privé, le rapport [« Apports du logiciel libre à la durabilité des équipements »](https://code.gouv.fr/docs/2023_01_RapportIndiceDurabilite.pdf) (Pierre-Yves Gibello/OW2 pour la DINUM, janvier 2023) documente, avec des témoignages nommés, le lien direct entre ce critère et l'**allongement de la durée de vie du matériel** évoqué dans l'objectif de la fiche RGESN :

- [**Murena**](https://murena.com/) (entreprise française, éditrice de l'OS mobile open source **/e/OS**) en a fait un modèle économique entier : le Fairphone 2 (2015) a reçu des mises à jour Android 9 des années après la fin de support habituelle, uniquement parce qu'Android est open source et que Fairphone a pu recompiler lui-même les versions récentes. Murena a promis deux années de mises à jour supplémentaires sur le Fairphone 3.
- **ATF** (entreprise de l'économie sociale et solidaire, 350 000 ordinateurs reconditionnés par an) : son ex-directeur du développement témoigne — « sur un vieux Core 2 Duo, Windows ne passe plus, et ça fonctionne très bien sous Linux » — imputant le problème à une stratégie conjointe d'obsolescence programmée entre constructeurs et éditeurs d'OS propriétaires.
- **Fréco / Electrocycle** chiffre que 100 % des ordinateurs populaires de 2004 à 2015 restent exploitables et à jour avec un système libre, contre 0 % avec Windows 10.
- Le réseau **Ordi3.0** (200 structures labellisées, 300 000 ordinateurs reconditionnés/an) cite un de ses labellisés faisant durer des postes jusqu'à **18 ans** grâce à un système d'exploitation et une suite logicielle open source.

Ces exemples illustrent, en creux, pourquoi ce critère va au-delà de la seule transparence du code : l'open source y est un **levier concret de sobriété matérielle**, en évitant le remplacement d'un équipement encore fonctionnel faute de support logiciel.

{{% /tab %}}

{{< /tabs >}}
