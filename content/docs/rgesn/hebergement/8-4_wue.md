---
weight: 400
title: "8.4 - WUE de l'hébergement"
description: "Critère 8.4 du RGESN : obtenir le WUE réel du site qui héberge le service, savoir le lire avec le PUE et le type de refroidissement, et tenir compte du stress hydrique local."
icon: "water_drop"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement dont son WUE (Water Usage Effectiveness) est minimisé ?

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
| **Critère**  | `8.4` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Connaître le WUE* de son hébergement, indicateur souvent peu pris en compte, et réduire ou limiter la consommation d'eau nécessaire au refroidissement des serveurs. Éviter le stress hydrique (c'est-à-dire de pénurie d'eau potable). Le stress hydrique local peut également être pris en compte : un WUE élevé dans une zone sans stress hydrique sera moins problématique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Sélectionner un hébergeur qui indique son WUE et la méthodologie utilisée pour le mesurer, basée sur des standards internationalement reconnus (par exemple ISO/IEC 30134). Cet indicateur est un ratio entre la quantité d'eau consommée et l'énergie totale utilisée par le centre de données. Il est mesuré en L/kWh. Pour les hébergements en activité depuis plus de deux ans, le WUE devra être mesuré – si possible – sur leur valeur dite « réelle » et non « by design » sur la base d'une méthodologie se référant à des normes et standards internationalement reconnus (par exemple normes ISO).

NB : Actuellement, il y a peu ou pas de données ouvertes sur le sujet du stress hydrique local. Comme pour le PUE, améliorer cet indicateur peut dégrader d'autres indicateurs, sans que cela ne réduise ni l'impact global, ni la consommation d'énergie, d'où l'intérêt de suivre plusieurs indicateurs (consommation d'énergie, consommation d'eau, politique de gestion du matériel, etc.).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si l'hébergeur du service numérique démontre une démarche de minimisation de sa consommation d'eau en suivant les indicateurs pertinents, en particulier son WUE. L'objectif d'un WUE inférieur ou égal à 0,4 L/kWh peut être visé (calculer en réel si possible et sinon, considérer le WUE by design, en particulier pour les centres de données qui sont en activité depuis moins de deux ans – le critère est donc à réévaluer passé ce délai de deux ans d'activité des installations).

La méthodologie de calcul et le type de WUE – réel ou by design – calculé sont précisés avec la valeur communiquée. Si possible, il faut fournir un lien ou justificatif incluant le WUE de l'hébergement dans la déclaration d'écoconception du service.

- La consommation en eau est encore relativement peu documentée au moment de la rédaction du présent référentiel. Il conviendra donc de prendre en compte les spécificités techniques et les possibles évolutions réglementaires en cours dans l'appréciation de ce critère, en particulier concernant l'objectif chiffré du WUE.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="GR491, RWEB et W3C" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

La [recommandation n°1 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=1) du [GR491](https://gr491.isit-europe.org/) (INR) regarde l'eau sous plusieurs angles :

- [« Est-ce que le WUE (Water Usage Effectivness) est disponible ? »](https://gr491.isit-europe.org/crit.php?id=1-hebergement-la-quantite-deau-consommee-par-le-datacenter-f915ce), en priorité **High**, avec un seuil de **1 L/kWh**, deux fois et demie moins exigeant que les 0,4 L/kWh du RGESN ;
- [« L'eau utilisée ne provient-elle pas du réseau d'eau potable ? »](https://gr491.isit-europe.org/crit.php?id=1-hebergement-il-ny-a-pas-de-traitement-superflu-92d198) : refroidir avec de l'eau potable, c'est la traiter pour rien ;
- deux conseils sur les nappes phréatiques et la qualité de l'eau rejetée.

[RWEB 0096](https://rweb.greenit.fr/fr/fiches/RWEB_0096-choisir-un-hebergeur-eco-responsable), rattachée au 8.4, et le critère « Provider selection » des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting) du W3C demandent de privilégier les hébergeurs qui publient leur WUE, sans fixer de seuil.

{{% /tab %}}

{{% tab tabName="Lire un WUE" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

**Le dénominateur est l'énergie informatique.** Le RGESN décrit le WUE comme un ratio avec « l'énergie totale utilisée par le centre de données ». La norme ISO/IEC 30134-9 le définit avec l'énergie des **équipements informatiques**, comme le PUE : OVHcloud publie d'ailleurs le sien en « L/kWh IT ». Pour un même site, le WUE est donc plus élevé avec la norme, dans le rapport du PUE.

**Le WUE dépend du refroidissement.** Un refroidissement par évaporation (adiabatique) consomme de l'eau pour moins d'électricité : il améliore le PUE et dégrade le WUE. Un refroidissement à air sec ou en circuit fermé consomme peu d'eau, mais plus d'électricité. Les deux indicateurs se lisent donc ensemble.

**Le même hébergeur peut avoir des sites très différents.** Les [indicateurs 2025 d'OVHcloud](https://www.ovhcloud.com/sites/default/files/external_files/kpis_fy25.pdf) donnent un WUE de groupe de 0,34 L/kWh, sous l'objectif du RGESN, mais de 0,18 (Erith, Royaume-Uni) à 1,31 L/kWh selon les sites :

| Site | WUE (L/kWh IT) |
|---|---:|
| Gravelines | 0,20 |
| Roubaix | 0,29 |
| Strasbourg | 0,39 |
| Beauharnois (Canada) | 0,86 |
| Hillsboro (États-Unis) | 1,31 |

**Le lieu compte.** Un même WUE pèse plus là où l'eau manque. Le RGESN note qu'il existe « peu ou pas de données ouvertes » sur le stress hydrique local : l'atlas Aqueduct du World Resources Institute en donne une estimation par bassin versant, à demander à l'hébergeur de confirmer pour son site.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

**1. Demander le WUE réel du site** qui héberge le service, avec sa méthode, sa période et son dénominateur (énergie informatique ou totale). Comme le PUE, il fait partie des indicateurs que les centres de données de 500 kW ou plus déclarent chaque année (voir le [critère 8.1](../8-1_demarche-hebergeur/)).

**2. Demander le type de refroidissement** et l'origine de l'eau : réseau d'eau potable, forage, eau de pluie ou eau industrielle.

**3. Comparer à l'objectif de 0,4 L/kWh**, en tenant compte du PUE du même site ([critère 8.3](../8-3_pue/)) et du stress hydrique local.

**4. Documenter** dans la déclaration d'écoconception : la valeur, réelle ou « by design », la méthode, la période et le lien vers la publication de l'hébergeur. Si le WUE n'est pas suivi, l'écrire, avec la date à laquelle l'hébergeur prévoit de le publier.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

- le [critère 8.3](../8-3_pue/) (PUE) : à lire avec le WUE, car le refroidissement les fait varier en sens inverse ;
- le [critère 8.1](../8-1_demarche-hebergeur/) (démarche de l'hébergeur) : la consommation d'eau est l'un des quatre indicateurs que l'hébergeur doit suivre ;
- le [critère 8.6](../8-6_localisation/) (localisation) : le stress hydrique dépend du lieu du centre de données.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration | WUE déclaré |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | « Inconnu » |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | « Le WUE dépend des fournisseurs de Data Centers d'Ecritel » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | **Non validé** | « Des études sont en cours pour évaluer le WUE et le minimiser. » |

**Aucun des trois services ne connaît le WUE de son hébergement.** C'est le critère le moins documenté de la famille, comme le RGESN l'annonçait.

**DiaLog** s'appuie sur la [page RGESN de Scalingo](https://doc.scalingo.com/compliance/rgesn), où le WUE « n'est pas suivi » et « pourra constituer néanmoins une piste d'amélioration pour l'année 2023 ». La page n'a pas été mise à jour depuis le 26 mai 2023.

Pour ces trois services, la loi de 2025 change la donne : si leurs centres de données atteignent 500 kW, le WUE est désormais déclaré chaque année, et il suffit de le demander.

{{% /tab %}}

{{< /tabs >}}
