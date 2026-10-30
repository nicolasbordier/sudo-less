---
weight: 300
title: "8.3 - PUE de l'hébergement"
description: "Critère 8.3 du RGESN : obtenir le PUE réel du centre de données qui héberge le service, avec sa méthode, sa catégorie et sa période, et vérifier qu'il est inférieur à 1,5."
icon: "bolt"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement dont le PUE (Power Usage Effectiveness) est minimisé ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Hébergement` |
| **Critère**  | `8.3` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Il s'agit de connaître le PUE de son hébergement et favoriser la réduction de la consommation d'énergie nécessaire au bon fonctionnement et au refroidissement des serveurs nécessaires à l'hébergement.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Il est recommandé de prendre en compte le PUE du centre de données dans le choix de la solution d'hébergement. Pour les hébergements en activité depuis plus de deux ans, le PUE devra être mesuré sur leur valeur dite « réelle » et non « by design » sur la base d'une méthodologie se référant à des normes et standards internationalement reconnus (par exemple normes ISO).

Sélectionner un hébergeur qui indique son PUE et la stratégie mise en œuvre pour le réduire. La communication de cet indicateur s'accompagne de la communication de la méthodologie utilisée pour le mesurer, basée sur des standards internationalement reconnus (par exemple ISO/IEC 30134) et notamment sur le type de PUE qui est mesuré (type 1, 2 ou 3).

Le PUE est un indicateur d'efficacité énergétique qui consiste en un ratio entre l'énergie totale consommée par l'ensemble du centre d'exploitation (avec entre autres, le refroidissement, le traitement d'air, les onduleurs...) et la partie qui est effectivement consommée par les systèmes informatiques que ce centre exploite (serveurs, stockage, réseau). Un PUE proche de 1 indique une excellente performance énergétique du centre de données. Généralement, il est constaté un PUE à 1,1 pour les hyperscalers et de 2 pour les plus anciens centres de données. Cependant, améliorer cet indicateur peut dégrader d'autres indicateurs, sans que cela ne réduise ni l'impact global, ni la consommation d'énergie ; d'où l'intérêt de suivre plusieurs indicateurs (consommation d'énergie, consommation d'eau, politique de gestion du matériel, etc. Voir critère 8.1.).

À noter : Les centres de données les plus récents n'ont pas encore le taux de remplissage suffisant pour que le PUE réel soit l'indicateur approprié. Ainsi, en dessous de deux ans d'activité, le PUE by design est un meilleur indicateur auquel se référer, mais dans ce cas uniquement pour éviter les risques d'obsolescence.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Quel est le PUE de l'hébergeur du service numérique ? Vérifier la publication de cet indicateur de performance énergétique par l'hébergeur du service numérique. Pour valider le critère, il faut choisir un hébergeur avec un PUE inférieur à 1,5 en réel (ou un PUE by design inférieur ou égal à 1,3 si les installations de l'hébergeur sont entrées en activité depuis moins de deux ans – en conséquence, le critère devra être réévalué passé ce délai de deux ans d'activité des installations).

Si possible, fournir un lien ou justificatif incluant le PUE de l'hébergement dans la déclaration d'écoconception du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="RWEB, GR491 et W3C" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable des achats`

Les trois référentiels demandent le PUE, avec des seuils différents :

| Référentiel | Exigence |
|---|---|
| RGESN 8.3 | Moins de 1,5 en réel, ou 1,3 au plus « by design » pour un site de moins de deux ans |
| [RWEB 0096](https://rweb.greenit.fr/fr/fiches/RWEB_0096-choisir-un-hebergeur-eco-responsable) | Principe de validation : PUE de l'hébergeur de 1,5 au plus |
| [GR491](https://gr491.isit-europe.org/crit.php?id=1-hebergement-la-puissance-totale-consommee-par-le-datacenter-dc3f58), priorité **High** | Test : « Le PUE est-il inférieur ou égal à 1,2 ? » La note passe de 100 à 1,2 ou moins, à 0 au-delà de 1,8 |
| [W3C](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting), « Provider selection » | Privilégier les fournisseurs qui publient leur PUE, sans seuil |

Le GR491 est le plus exigeant. Un hébergement à 1,4 valide le RGESN et RWEB, mais n'obtient que 75 points sur 100 au GR491.

{{% /tab %}}

{{% tab tabName="Lire un PUE" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

Un PUE de 1,5 signifie que pour 1 kWh consommé par les serveurs, le centre de données en consomme 0,5 de plus en refroidissement, onduleurs et éclairage. Avant de comparer deux valeurs, vérifier quatre points :

| Point | Pourquoi |
|---|---|
| **Réel ou « by design »** | La valeur de conception est un objectif. Le RGESN n'accepte qu'un PUE réel au-delà de deux ans d'activité |
| **Période** | Le PUE se calcule sur l'énergie d'une année entière : une valeur instantanée, mesurée un jour froid, est meilleure qu'elle ne sera en été |
| **Catégorie** | La norme ISO/IEC 30134-2 distingue trois catégories, selon l'endroit où l'énergie informatique est mesurée : en sortie d'onduleur (1), en sortie de distribution électrique (2) ou à l'entrée des équipements (3). Plus la catégorie est élevée, plus la mesure est précise |
| **Périmètre** | Une moyenne de groupe ou « pondérée » mélange des sites différents. Il faut le PUE du site qui héberge le service |

**Le PUE ne mesure pas tout.** Il ne dit rien de l'efficacité des serveurs eux-mêmes. Il peut aussi baisser au prix de plus d'eau consommée, par un refroidissement par évaporation ([critère 8.4](../8-4_wue/)), ou rendre la récupération de chaleur plus difficile ([critère 8.7](../8-7_chaleur-fatale/)).

**Un exemple de publication complète.** Les [indicateurs 2025 d'OVHcloud](https://www.ovhcloud.com/sites/default/files/external_files/kpis_fy25.pdf), sur l'exercice clos fin août 2025, donnent pour chaque site le PUE, sa catégorie, le WUE et la part d'électricité renouvelable, avec l'historique sur trois ans. En France : Roubaix 1,30, Gravelines 1,21, Strasbourg 1,19, tous en catégorie 2.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

**1. Identifier le centre de données** qui héberge le service, au bout de la chaîne d'hébergement ([critère 8.1](../8-1_demarche-hebergeur/)). Une plateforme peut s'appuyer sur plusieurs sites, avec un PUE chacun.

**2. Demander le PUE réel de ce site**, avec les quatre points de l'onglet précédent. Un centre de données de 500 kW ou plus le déclare chaque année avant le 15 mai, depuis la loi de 2025 (voir le [critère 8.1](../8-1_demarche-hebergeur/)).

**3. Comparer au seuil** : moins de 1,5 en réel. Pour un site récent, 1,3 au plus « by design », avec une date de réévaluation deux ans après la mise en service.

**4. Choisir l'offre ou la région.** Quand un hébergeur publie un PUE par site, la région du service peut se choisir en conséquence.

**5. Documenter** dans la déclaration d'écoconception : la valeur, le site, la période, la catégorie et le lien vers la publication de l'hébergeur.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

- le [critère 8.1](../8-1_demarche-hebergeur/) (démarche de l'hébergeur) : le PUE est l'un des indicateurs à publier ;
- le [critère 8.4](../8-4_wue/) (WUE) : à lire avec le PUE, car l'un peut baisser aux dépens de l'autre ;
- le [critère 8.7](../8-7_chaleur-fatale/) (chaleur) : un PUE réel inférieur à 1,3 permet aussi de valider le 8.7.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration | PUE déclaré | Méthode et période |
|---|---|---:|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | 1,64 | Moyenne pondérée des fournisseurs d'Outscale, 2021 |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | — | — |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Validé | 1,46 | Non précisées |

**DiaLog** est le plus précis sur la méthode, et c'est ce qui montre la limite de sa valeur. D'après la [page RGESN de Scalingo](https://doc.scalingo.com/compliance/rgesn), ce PUE pondéré est « une moyenne des PUE des fournisseurs de datacentre, proportionnellement au nombre de baies ». Il date de 2021 et dépasse le seuil de 1,5. Le PUE du site qui héberge réellement le service reste inconnu.

**Le Musée d'arts de Nantes** écrit que « Le PUE dépend des fournisseurs de Data Centers d'Ecritel ». C'est vrai, mais il suffit de le leur demander : c'est désormais un indicateur déclaré chaque année pour les grands sites.

**FACE** déclare un PUE de 1,46, sous le seuil, mais sans période ni catégorie. Sa déclaration justifie aussi le critère 8.7 par un PUE « inférieur ou égal à 1,2 », qui contredit cette valeur (voir le [critère 8.7](../8-7_chaleur-fatale/)).

{{% /tab %}}

{{< /tabs >}}
