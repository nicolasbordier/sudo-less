---
weight: 700
title: "8.7 - Traitement de la chaleur produite par les serveurs"
description: "Critère 8.7 du RGESN : choisir un hébergeur qui récupère la chaleur fatale de ses serveurs, ou à défaut dont le PUE réel est inférieur à 1,3, et demander son facteur de réutilisation de l'énergie (ERF), désormais encadré par la loi."
icon: "heat_pump"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement qui traite efficacement la chaleur produite par les serveurs ?

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
| **Critère**  | `8.7` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Encourager les initiatives permettant de diminuer ou de récupérer l'énergie produite, par exemple pour chauffer des bâtiments en hiver. Se reporter à la [définition de la chaleur fatale de l'ADEME](https://fondschaleur.ademe.fr/chaleur-fatale-2/).

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Sélectionner un hébergeur ayant pris des engagements de récupération ou réutilisation de la chaleur fatale générée (par exemple, pour chauffer directement les bureaux ou d'autres installations à proximité) ou mettant en place des mécanismes alternatifs permettant de gérer la température des serveurs et de minimiser l'empreinte environnementale de l'hébergement.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si l'hébergeur a mis en place des initiatives assurant la récupération et la réutilisation de la chaleur fatale générée par son installation, et que celles-ci sont documentées dans la déclaration d'écoconception du service numérique. Il est nécessaire que le bilan environnemental global de la réutilisation de la chaleur produite soit positif, en tenant compte de l'investissement initial pour la construction ou de l'adaptation des installations pour la validation du critère.

De façon alternative, le critère peut être validé si le centre de données utilisé pour le service a un PUE inférieur à 1,3 en réel (ou un PUE by design inférieur ou égal à 1,2 si les installations de l'hébergeur sont entrées en activité depuis moins de deux ans – le critère est donc à réévaluer passé ce délai de deux ans d'activité des installations). Un centre de données avec un PUE faible – bien qu'efficient énergétiquement – peut rendre impossible ou compliquée cette réutilisation de la chaleur fatale.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="GR491" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

Ni RWEB ni les Web Sustainability Guidelines du W3C ne traitent de la chaleur des serveurs. La [recommandation n°1 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=1) du [GR491](https://gr491.isit-europe.org/) (INR) pose la question : « Est-ce que de l'énergie indirecte produite (chaleur) est réutilisée ? » Le 30 octobre 2026, la page de ce conseil ne s'affichait pas ; son titre figure dans la liste de la recommandation.

Trois critères voisins portent sur l'efficacité du refroidissement : un refroidissement réglé sur « une analyse de température précise », une organisation des salles qui facilite le refroidissement, et des alimentations de serveurs efficaces.

{{% /tab %}}

{{% tab tabName="Ce que la loi impose" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

Depuis le 1er janvier 2026, la récupération de chaleur est une obligation pour les grands centres de données. D'après le [cabinet CMS](https://cms.law/en/fra/publication/performances-energetiques-des-data-centers-de-nouvelles-obligations), le décret n° 2025-1382 du 29 décembre 2025 l'applique aux centres « dont la puissance installée est supérieure ou égale à un (1) mégawatt » :

- un centre est réputé récupérer sa chaleur si son facteur de réutilisation de l'énergie (ERF) est d'au moins **0,20**. Ce seuil pourra être relevé jusqu'à 0,40 ;
- une dérogation reste possible si le projet n'est pas viable ;
- les centres dont le permis a été déposé avant 2026 ont jusqu'au 1er octobre 2027 pour analyser leurs possibilités.

L'ERF, défini par la norme ISO/IEC 30134-6, rapporte l'énergie réutilisée hors du centre de données à l'énergie totale qu'il consomme. Un ERF de 0,20 signifie qu'un cinquième de l'énergie consommée sert ensuite, par exemple, à chauffer des bâtiments.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

**1. Demander à l'hébergeur s'il récupère la chaleur**, et sous quelle forme : ERF, quantité annuelle de chaleur livrée, destination (réseau de chaleur, bâtiments voisins, serres) et date de mise en service.

**2. Vérifier le bilan global**, comme l'exige le moyen de test. La chaleur des serveurs est à basse température : elle doit souvent être remontée par une pompe à chaleur, qui consomme elle-même de l'électricité. Le projet est positif s'il remplace un chauffage plus émetteur, gaz ou fioul.

Un exemple : Equinix a raccordé son centre de données PA10, à Saint-Denis, au réseau de chaleur urbain pour chauffer une piscine ([Next, 19 janvier 2022](https://next.ink/brief-article/pa10-equinix-ouvre-un-dixieme-datacenter-a-saint-denis-avec-recuperation-de-la-chaleur/)).

**3. À défaut, vérifier le PUE réel** du site : moins de 1,3, ou 1,2 au plus « by design » pour un site de moins de deux ans (voir le [critère 8.3](../8-3_pue/)). Le RGESN reconnaît qu'un PUE très bas peut rendre la récupération « impossible ou compliquée ».

**4. Documenter** dans la déclaration d'écoconception : l'existence de la récupération, sa destination et son ERF, ou, à défaut, le PUE réel avec sa période.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

- le [critère 8.3](../8-3_pue/) (PUE) : la voie alternative du 8.7 en dépend ;
- le [critère 8.1](../8-1_demarche-hebergeur/) (démarche de l'hébergeur) : le RGESN y liste la récupération de la chaleur fatale parmi les engagements attendus ;
- le [critère 8.4](../8-4_wue/) (WUE) : le mode de refroidissement fixe à la fois la chaleur récupérable et l'eau consommée.

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
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | Pas de récupération ; PUE de 1,64 |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | Couloirs froids pour optimiser la climatisation |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Validé | « Non nécessaire car le PUE de l'hébergeur est inférieur ou égal à 1,2 » |

**FACE** valide le critère par la voie du PUE, mais sa propre déclaration donne un PUE de **1,46** au [critère 8.3](../8-3_pue/). Cette valeur ne permet pas la voie alternative, qui demande moins de 1,3. Pourtant, au [critère 8.2](../8-2_gestion-equipements/), FACE cite « la récupération de la chaleur fatale » parmi les engagements de son hébergement. C'est cette récupération, avec sa destination et son ampleur, qui devrait justifier le 8.7.

**Le Musée d'arts de Nantes** décrit des couloirs froids, qui réduisent la consommation de la climatisation « de 15 à 20 % ». C'est une mesure d'efficacité du refroidissement, qui joue sur le PUE, pas une récupération de la chaleur.

**DiaLog** reprend la réponse de Scalingo : la récupération « se fait au niveau des datacentres et relève donc de la responsabilité du fournisseur de datacentre ». C'est vrai, et c'est donc à ce fournisseur qu'il faut poser la question.

{{% /tab %}}

{{< /tabs >}}
