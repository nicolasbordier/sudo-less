---
weight: 100
title: "9.1 - Nécessité d'une phase d'entraînement"
description: "Critère 9.1 du RGESN : avant d'entraîner un modèle, vérifier que le besoin est avéré, essayer une solution sans apprentissage ou un modèle existant, et fixer un niveau de satisfaction suffisant."
icon: "quiz"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il interrogé la nécessité d'une phase d'entraînement pour éviter un usage non justifié et déraisonné ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Algorithmie` |
| **Critère**  | `9.1` |
| **Phase** | `Exploration` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Porteur de projet` `Responsable R&D` `Responsable RSE/Numérique soutenable` `Data Scientist` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

La phase d'apprentissage ou d'entraînement repose sur une infrastructure numérique qui, dans certains cas, peut nécessiter l'utilisation d'un important volume de données et de calculs. Largement répandue dans le domaine de l'intelligence artificielle, la phase d'entraînement peut engendrer une grande consommation d'énergie et de ressources. L'objectif est donc de réduire l'empreinte environnementale de la phase d'apprentissage en évitant de recourir à ces techniques si le besoin n'est pas avéré ou en choisissant une méthode adaptée et proportionnée aux besoins et caractéristiques du service numérique.

Il s'agira donc de s'interroger sur la nécessité d'inclure une phase d'entraînement dans le service numérique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Ne pas intégrer de phase d'entraînement dans le service tant que le besoin n'est pas avéré. Pour établir ce besoin, identifier les cibles utilisatrices et leurs besoins (voir « Mise en œuvre » du critère 1.2) vis-à-vis du service numérique. Lister les fonctionnalités du service essentielles à ces besoins et se poser la question de la nécessité ou non de l'inclusion d'une phase d'entraînement.

Il conviendra de s'interroger régulièrement sur la valeur ajoutée espérée par la phase d'entraînement : l'ajout d'une phase d'entraînement améliore-t-il significativement le service numérique dans l'atteinte des besoins de ses cibles ? L'amélioration est-elle effectivement perceptible et utile pour l'utilisateur ?

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Ne pas inclure une phase d'entraînement tant que le besoin n'est pas démontré et le cas échéant, préférer les méthodes de recherches classiques, ou des solutions existantes déjà entraînées.

Pour démontrer le besoin d'une phase d'entraînement, il s'agira de cibler des publics, les besoins associés et de rendre accessible des documents de référence faisant état des études, entretiens, recherches, personas ayant permis de définir les cibles utilisatrices et leur besoin.

Justifier dans la déclaration d'écoconception le lien avec les fonctionnalités du service et les raisons expliquant la nécessité (si pertinent) de l'inclusion d'une phase d'entraînement dans le service numérique, en particulier en termes de valeur ajoutée pour l'utilisateur. Si les besoins sont clairement établis, il conviendra de définir un niveau de satisfaction suffisant et de choisir une quantité d'entraînement proportionnée.

Le critère est validé si le service n'intègre pas d'apprentissage non justifié. Dans l'éventualité de la mise en place d'une phase d'apprentissage, les critères de documentation susmentionnés démontrant l'utilité de la phase d'entraînement et son caractère proportionnel au regard de ses cibles ainsi que des fonctionnalités concernées devront également être suivis pour valider le critère.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

RWEB ne rattache aucune fiche à la famille Algorithmie, et le GR491 n'a pas de famille consacrée à l'apprentissage automatique. Les sources de la famille Algorithmie sont donc surtout le référentiel de l'AFNOR sur l'IA frugale et les Web Sustainability Guidelines du W3C.

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="AFNOR et W3C" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable RSE/Numérique soutenable`

L'[**AFNOR Spec 2314 « Référentiel général pour l'IA frugale »**](https://www.boutique.afnor.org/en-gb/standard/afnor-spec-2314/fa208976/421140) (juin 2024, 100 pages, consultation gratuite) est né d'une initiative du ministère de la Transition écologique, dans la continuité du RGESN. Il propose une méthode d'évaluation des impacts sur tout le cycle de vie et des fiches de bonnes pratiques. Il distingue la **frugalité** d'un service d'IA, qui interroge le besoin et l'usage, de l'**efficience** du système technique. Le 9.1 relève de la première.

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) le formulent dans le critère de succès « Environmental responsibilities » de la fiche [**« Establish responsible practices around AI and emerging or disruptive technologies »**](https://www.w3.org/TR/web-sustainability-guidelines/#establish-responsible-practices-around-ai-and-emerging-or-disruptive-technologies) : « Evaluate the need for AI and emerging or disruptive technologies before implementation to avoid unnecessary resource use. »

{{% /tab %}}

{{% tab tabName="Avant d'entraîner" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Data Scientist`

Pour chaque fonctionnalité qui semble demander de l'apprentissage, poser les questions dans l'ordre, et s'arrêter à la première réponse positive :

| Question | Si oui |
|---|---|
| Le besoin est-il absent des recherches utilisateurs ([critère 1.2](../../strategie/1-2_cibles-utilisatrices/)) ? | Ne pas développer la fonctionnalité |
| Une règle, un formulaire ou une recherche classique répondent-ils au besoin ? | Les utiliser |
| Un modèle déjà entraîné, ou un service existant, y répond-il ? | L'utiliser ([critère 9.3](../9-3_quantite-entrainement/)) |
| Sinon | Entraîner, avec la méthode la plus simple qui suffit ([critère 9.2](../9-2_methode-apprentissage/)) |

Quelques exemples d'alternatives sans apprentissage :

| Besoin | Sans apprentissage |
|---|---|
| Trouver un document | Une recherche plein texte (celle de PostgreSQL, ou un moteur comme Meilisearch) |
| Orienter une demande vers le bon service | Un formulaire qui demande la catégorie, ou des règles sur des mots-clés |
| Répondre aux questions fréquentes | Une FAQ structurée et sa recherche |
| Repérer des données incohérentes | Des contrôles de saisie et des règles métier |

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable R&D`

**1. Partir des besoins documentés** : les études, entretiens et personas du [critère 1.2](../../strategie/1-2_cibles-utilisatrices/). Le moyen de test demande de les rendre accessibles.

**2. Écrire l'hypothèse de valeur** de chaque fonctionnalité d'apprentissage : ce qu'elle améliore pour l'utilisateur, et comment on le mesurera.

**3. Tester d'abord l'alternative sans apprentissage**, de l'onglet précédent, et mesurer ce qu'il lui manque.

**4. Fixer un niveau de satisfaction suffisant** avant de commencer : par exemple, « 90 % des demandes orientées vers le bon service ». Il bornera ensuite la méthode ([critère 9.2](../9-2_methode-apprentissage/)) et la quantité d'entraînement ([critère 9.3](../9-3_quantite-entrainement/)).

**5. Réinterroger le besoin** à chaque revue d'écoconception ([critère 1.4](../../strategie/1-4_revue-ecoconception/)) : la fonctionnalité est-elle utilisée ? L'amélioration est-elle perçue ?

**6. Documenter** dans la déclaration d'écoconception. Sans apprentissage : « Le service n'utilise pas d'apprentissage automatique. » Avec : le lien vers les besoins, l'alternative testée et le niveau de satisfaction visé.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`

- le [critère 1.1](../../strategie/1-1_evaluation-utilite/) (utilité) : la même question, posée au service entier ;
- le [critère 1.2](../../strategie/1-2_cibles-utilisatrices/) (cibles) : les besoins qui justifient, ou non, l'apprentissage ;
- le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) (impacts des fonctionnalités) : informer l'utilisateur quand une fonctionnalité est coûteuse ;
- les critères [9.2](../9-2_methode-apprentissage/) et [9.3](../9-3_quantite-entrainement/) : la suite, une fois le besoin établi.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration | Justification |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | Non applicable | « pas d'utilisation de l'IA à l'heure actuelle », pour toute la famille |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Validé | « Le site n'intègre pas de mécanisme d'apprentissage automatique. » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Validé | — |
| [compar:IA](https://arene.comparia.beta.gouv.fr/eco-design) | Famille « Apprentissage automatique » à 100 % | Le service compare des modèles existants, sans en entraîner |

**Le Musée d'arts de Nantes** applique le critère comme prévu : un service sans apprentissage le valide, en le disant.

**DiaLog** déclare toute la famille non applicable. C'est juste pour les critères [9.2](../9-2_methode-apprentissage/) à [9.7](../9-7_strategie-inference/), qui supposent un entraînement ou une inférence. Le 9.1, lui, s'applique « à tous les services » : il est validé dès lors que le service n'utilise pas d'apprentissage injustifié.

**compar:IA**, service du ministère de la Culture, fait comparer deux modèles conversationnels existants et recueille les votes des utilisateurs. Il n'entraîne aucun modèle lui-même. Ses votes, publiés en jeux de données, peuvent servir à d'autres pour affiner leurs modèles (voir le [critère 9.4](../9-4_donnees-apprentissage/)).

{{% /tab %}}

{{< /tabs >}}
