---
weight: 600
title: "2.6 - Revue de conception et de code"
description: "Critère 2.6 du RGESN : pourquoi et comment intégrer la réduction des impacts environnementaux, par fonctionnalité, dans une revue de conception puis une revue de code."
icon: "rate_review"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il été conçu avec une revue de conception et une revue de code comprenant parmi ses objectifs la réduction des impacts environnementaux de chaque fonctionnalité ?

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
| **Critère**  | `2.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Architecte Logiciel` `Développeur` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Afin d'aboutir à une solution la plus sobre possible tout en répondant au besoin, il faut miser sur l'**intelligence collective** de toute l'équipe. Et pour cela, il ne suffit pas seulement de valider la conception par la revue de code, une bonne pratique maintenant assez répandue.

Il est nécessaire, et cela sera positif pour l'équipe et pour le projet, de **réfléchir en amont du développement** aux choix de conception et d'architecture, en ayant notamment pour objectif la **minimisation des impacts environnementaux**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

En impliquant l'ensemble de l'équipe, l'ensemble des métiers, une **revue de conception** en amont du développement est réalisée pour choisir la solution répondant au besoin tout en minimisant les impacts environnementaux.

Puis, si du code a été produit pour implémenter la solution, une **revue de code** est faite en aval du développement.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Quel est le processus de développement mis en place ? Le critère est **validé** si :

- Une **revue de conception** prenant en compte l'empreinte environnementale du service a été réalisée : dès sa conception, l'équipe projet devrait pouvoir définir un **arbre des conséquences** du service numérique en représentant, par fonctionnalité, les impacts directs et indirects du service numérique pour que toute l'équipe valide les fonctionnalités en connaissance des impacts environnementaux potentiels (voir la méthodologie **Empreinte Projet** de l'ADEME).
- Une **revue de code** visant à minimiser le coût environnemental du service a été produite en aval de la conception, pour les services reposant sur du code informatique.

Ces revues sont — le cas échéant — référencées dans la **déclaration d'écoconception** du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="3">}}
{{% tab tabName="Empreinte Projet (ADEME)" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Le texte officiel du critère renvoie explicitement à cette méthodologie pour construire l'**arbre des conséquences par fonctionnalité** attendu par le « Moyen de test ou de contrôle ». L'ADEME met à disposition :

- l'[outil web Empreinte Projet™ (niveau 1, gratuit et sans inscription)](https://base-empreinte.ademe.fr/empreinte-projet), qui guide pas à pas la comparaison entre un scénario « avec projet » et un scénario de référence « sans projet », fonctionnalité par fonctionnalité ;
- le [guide méthodologique complet « Empreinte projet : évaluer l'empreinte environnementale d'un projet » (PDF, 2021)](https://librairie.ademe.fr/industrie-et-production-durable/5040-empreinte-projet-evaluer-l-empreinte-environnementale-d-un-projet.html), qui détaille les 5 niveaux de la méthode.

Contrairement au [critère 1.1](../../strategie/1-1_evaluation-utilite/), qui questionne l'utilité du service dans son ensemble en amont du projet, ce critère applique la même logique d'arbre des conséquences à **chaque fonctionnalité individuellement**, lors de la revue de conception.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Le critère 2.6 rejoint la [recommandation n°1 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=1) du [GR491](https://gr491.isit-europe.org/) (INR), « Valider le périmètre et la couverture fonctionnelle du projet », qui pousse la question au-delà du seul arbre des conséquences : chaque fonction est-elle appréhendée en regard de son importance réelle ? 

Les fonctions secondaires ont-elles un impact moindre que les fonctions principales ? 

Les données d'analyse de cycle de vie sont-elles réutilisées en cas d'adaptation d'un service existant plutôt que recalculées à chaque fois ? 

Est-ce la fonctionnalité qui guide les choix techniques, plutôt que l'attrait d'une technologie à la mode ?

{{% /tab %}}

{{% tab tabName="Outils" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Cette revue en deux temps s'outille différemment selon la phase :

- **Revue de conception** : [EcoSimulateur](https://www.figma.com/community/plugin/1430170108116488365/ecosimulateur) (plugin Figma) donne un retour immédiat sur l'impact d'une maquette pendant que les choix sont encore modifiables — voir la page [Outils > UX Designer](../../../outils/par-metier/ux-designer/).
- **Revue de code** : [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis), [EcoSonar](https://github.com/green-code-initiative/EcoSonar) et les outils de mesure par processus (Scaphandre, GreenFrame) permettent d'objectiver le coût environnemental du code produit — voir le détail complet sur les pages [Outils > Dev Front](../../../outils/par-metier/dev-front/) et [Outils > Dev Back](../../../outils/par-metier/dev-back/).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, avec une justification en une seule phrase : « Aucune revue de conception identifiée à ce jour. »

Ce cas illustre une limite pratique très fréquente : la revue de code (critère plus proche du [1.4](../../strategie/1-4_revue-ecoconception/)) est une pratique déjà répandue dans beaucoup d'équipes, alors que la **revue de conception en amont**, spécifiquement centrée sur l'empreinte environnementale de chaque fonctionnalité, reste rarement formalisée — même sur un service par ailleurs plutôt avancé dans sa démarche RGESN.

{{% /tab %}}

{{< /tabs >}}
