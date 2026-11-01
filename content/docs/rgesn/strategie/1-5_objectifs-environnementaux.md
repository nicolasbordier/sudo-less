---
weight: 500
title: "1.5 - Objectifs environnementaux"
description: "Critère 1.5 du RGESN : comment évaluer l'empreinte environnementale d'un service numérique et se fixer des objectifs de réduction chiffrés et suivis dans le temps."
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique s’est-il fixé des objectifs en matière de réduction ou de limitation de ses propres impacts environnementaux ?

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
| **Critère**  | `1.5` |
| **Phase** | `Exploration` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** |  `Responsable RSE/Numérique soutenable` `Porteur de projet` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.5/ |
{{< /table >}}

---

### 
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Connaître et réduire l’empreinte environnementale du service numérique. Cela implique d’avoir une vision globale des conséquences du service numérique, à **chaque phase** (début, usage, fin) et en intégrant les impacts environnementaux des **équipements matériels utilisés**, dans la **production** mais aussi dans **l’usage de ce service numérique**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir les indicateurs environnementaux à suivre, si possible suite à un diagnostic basé sur une méthodologie d’**analyse de cycle de vie** (ACV) multicritère afin d’identifier les indicateurs permettant de documenter la majorité de l’empreinte environnementale du service ou de l’organisation (se référer aux [méthodologies](https://eplca.jrc.ec.europa.eu/EnvironmentalFootprint.html) « Product Environmental Footprint » and « Organisation Environmental Footprint » de la Commission européenne, ou aux normes [ISO 14040](https://www.iso.org/fr/standard/37456.html) et [ISO 14044](https://www.iso.org/fr/standard/38498.html)). Les indicateurs d’impacts environnementaux à considérer prioritairement – en fonction des données disponibles – sont la consommation d’énergie primaire, les émissions de gaz à effet de serre (GES), la consommation d’eau bleue (c’est-à-dire la consommation directe des eaux de surface ou des eaux souterraines) et l’épuisement des ressources abiotiques (au moins métaux et minéraux). Le périmètre de l’analyse de cycle de vie peut être élargi par exemple en tenant compte des moyens de production : impacts environnementaux des équipements de conception, services en ligne mobilisés (environnement de test, de Quality Assurance (QA)...), déplacements des équipes, etc.

Fixer les objectifs de réduction de l’empreinte environnementale du service numérique (à court, moyen ou long terme) au regard du nombre d’utilisateurs escompté. 
Les indicateurs suivis doivent concerner prioritairement :
- la consommation d’énergie primaire
- les émissions de GES
- la consommation d’eau bleue
- l’épuisement des ressources abiotiques.

 Selon le contexte, il convient de préciser s’il s’agit d’indicateurs en valeur absolue (kg CO2e) ou relative (kg CO2e / utilisateur).


{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Des **indicateurs** ont été identifiés pour renseigner l’empreinte environnementale du service numérique. Si la disponibilité des données le permet, ces indicateurs devront s’appuyer sur la méthodologie ACV. Lors de la revue du document, les questions suivantes requièrent une attention particulière :

- Quels sont les indicateurs définis ? Les indicateurs prioritaires mentionnés dans la partie mise en œuvre devront a minima être intégrés.
- Comment sont suivis ces indicateurs ?
- Sont-ils publiés/ouverts et si oui, où ?
- La méthodologie d’évaluation des indicateurs suivis est-elle accessible publiquement ?

Quel est le rythme d’évaluation ? De plus, des **objectifs de réduction d’impacts environnementaux** sont fixés pour le service dans le cadre des indicateurs environnementaux suivis. Ceux-ci concernent au moins la consommation d’énergie primaire, les émissions de GES, la consommation en eau et ressources abiotiques (métal/minéral). Ces objectifs peuvent s’inscrire dans une trajectoire fixée au niveau du système ou de l’organisation. Pour certains enjeux environnementaux comme le climat, les trajectoires devraient être alignées avec l’Accord de Paris (en se basant par exemple sur les référentiels de l’initiative Science Based Targets (SBTi) ; ou la recommandation ITU-T L.1470).

Le **critère est validé** si l’empreinte environnementale du service a été **évaluée** – avec une méthodologie reconnue, si possible une ACV (multicritère) évaluant les impacts du service sur tout son cycle de vie – et si le service s’est **fixé des objectifs** de réduction d’impact. Ces éléments doivent faire l’objet d’un **suivi régulier** et être renseignés dans un document public et auditable, par exemple la **déclaration d’écoconception** du service.

{{% /tab %}}
{{< /tabs >}}

---

### 
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="Designers Éthiques" %}}

Dans le cas où la réalisation d'une ACV n'est pas envisagée en priorité, voici 2 alternatives :

- **1 - Évaluation**

Réaliser une évaluation de l'empreinte environnementale via un outil de mesure (cf : [critère 1.4](../1-4_revue-ecoconception/))

- **2 - Objectiver**

Définir un écobudget afin de s'objectiver via des mesures "proxy" technique (souvent plus simple à évaluer que les indicateurs environnementaux) : 
  - poids de page
  - nombre de requêtes par page
  - temps de chargement
  - débit réseau minimum de fonctionnement
  - version d'OS minimum
  - indicateur des [core web vitals](https://developers.google.com/search/docs/appearance/core-web-vitals?hl=fr)

Dans un contexte de type "**site web**", pour définir vos indicateurs, vous pouvez vous aider de cet outil [PerformanceBudget](https://www.performancebudget.io/)

Nous vous conseillons de consulter en détail le chapitre "**Etablir un budget environnemental**" de la page [Evaluer et mesurer](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/3-evaluer-et-mesurer)

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Porteur de projet`

Le critère 1.5 du RGESN fait écho à la [recommandation n°3](https://gr491.isit-europe.org/?famille=strategie&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR) : « Déterminer et planifier la capacité de suivre et capitaliser sur les composantes Numérique Responsable des projets ». Elle interroge, entre autres :

- **Identification** : les indicateurs pour mesurer l'efficacité de la démarche NR sont-ils identifiés et suivis ?
- **Outillage** : les outils pour mesurer cette efficacité sont-ils identifiés et communiqués aux équipes ?
- **Couverture** : les indicateurs couvrent-ils la mesure, l'évaluation, le pilotage, l'amélioration et le contrôle du niveau de maturité NR ?
- **Horizon temporel** : la durée de vie du projet est-elle définie ? (une donnée nécessaire pour borner une analyse de cycle de vie ou une trajectoire de réduction)

{{% /tab %}}

{{% tab tabName="SBTi & ITU-T L.1470" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`

Pour aligner des objectifs de réduction sur une trajectoire climatique reconnue plutôt que sur un pourcentage arbitraire, deux référentiels complémentaires, déjà cités dans la fiche RGESN de ce critère, méritent d'être détaillés :

- La [Science Based Targets initiative (SBTi)](https://sciencebasedtargets.org/) traduit les conclusions du GIEC en objectifs mesurables adaptés à chaque secteur, sur la base du GHG Protocol. Une organisation soumet sa trajectoire de réduction (scopes 1, 2 et 3), évaluée par des experts SBTi selon des critères scientifiques stricts, pour vérifier sa compatibilité avec une limitation du réchauffement à 1,5°C.
- La recommandation [ITU-T L.1470](https://www.itu.int/rec/T-REC-L.1470), développée avec le GeSI, la GSMA et la SBTi elle-même, décline cette approche **spécifiquement pour le secteur des TIC**, avec des trajectoires pour les opérateurs de réseaux mobiles, de réseaux fixes et de centres de données : elle fixe une cible sectorielle de **réduction de 45 % des émissions de GES entre 2020 et 2030** ([ITU, 2020](https://www.itu.int/en/mediacentre/Pages/PR04-2020-ICT-industry-to-reduce-greenhouse-gas-emissions-by-45-percent-by-2030.aspx)). Ce sont les premiers objectifs sectoriels spécifiques aux TIC validés par la SBTi. Une révision, avec des objectifs pour 2035, est en cours.

Ces deux référentiels sont surtout pertinents à l'échelle d'une organisation ou d'un grand programme ; pour un service unique, ils servent davantage de **point de repère** (un service numérique isolé peut difficilement obtenir une validation SBTi individuelle) que d'objectif directement applicable.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Développeur`

**1. Choisir l'unité et le périmètre.** Chaque indicateur se suit en valeur absolue (par an) et en valeur relative (par utilisateur ou par visite), comme le précise la mise en œuvre. Le périmètre couvre la fabrication et l'usage de l'hébergement, du réseau et des terminaux.

**2. Estimer l'hébergement** avec l'[API de Boavizta](https://api.boavizta.org/), qui calcule par analyse de cycle de vie trois des quatre indicateurs prioritaires. Pour une instance Scaleway située en France, utilisée à 30 %, sur un an (8 760 heures) :

```sh
curl -s -X POST 'https://api.boavizta.org/v1/cloud/instance?verbose=false&duration=8760&criteria=gwp&criteria=pe&criteria=adpe' \
  -H 'Content-Type: application/json' \
  -d '{"provider": "scaleway", "instance_type": "pop2-2c-8g", "usage": {"usage_location": "FRA", "time_workload": 30}}'
```

| Indicateur | Fabrication | Usage |
|---|---:|---:|
| Émissions de GES (`gwp`) | 3,4 kg CO2e | 2,8 kg CO2e |
| Énergie primaire (`pe`) | 44 MJ | 690 MJ |
| Ressources minérales et métalliques (`adpe`) | 9,8 × 10⁻⁵ kg Sb éq. | 3 × 10⁻⁶ kg Sb éq. |

Testé le 1er novembre 2026 (API version 2.5.0). L'API compte l'électricité française à 98 gCO2e/kWh, une valeur de 2021. L'usage est recalculé ici avec 46 g, la valeur 2025 de la Base Empreinte de l'ADEME pour le mix moyen consommé, amont compris ([reprise par Nos Gestes Climat](https://nosgestesclimat.fr/documentation/commun/mix-%C3%A9lectrique/empreinte-carbone)) : l'instance consomme 61 kWh par an (champ `avg_power` avec `verbose=true`). Pour une instance cloud, l'API ignore le facteur passé dans `usage.elec_factors` ; pour un serveur ou un terminal, `"elec_factors": {"gwp": 0.0461}` suffit. L'eau n'est pas couverte : l'indicateur `wu` n'est pas calculé pour l'usage, et sa valeur de fabrication, tirée de données génériques, est négative. Le calculateur de Scaleway, cité dans l'onglet « Infrastructure / Architecture » du [critère 1.4](../1-4_revue-ecoconception/), donne l'eau.

**3. Compléter avec les terminaux et le réseau.** L'API couvre aussi les terminaux (`/v1/terminal/laptop`, `/v1/terminal/smartphone`…), avec les données génériques de la Base IMPACTS de l'ADEME, mais sans l'énergie primaire de fabrication. Elle ne couvre pas le réseau : l'[étude ADEME-Arcep](https://www.arcep.fr/uploads/tx_gspublication/etude-numerique-environnement-ademe-arcep-volet02-synthese_janv2022.pdf) de 2022 donne sa consommation par Go. Le [RCP d'un service numérique](https://librairie.ademe.fr/societe-et-politiques-publiques/9418-methodologie-d-evaluation-environnementale-basee-sur-l-analyse-du-cycle-de-vie-acv-pour-un-service-numerique.html) de l'ADEME décrit comment attribuer au service une part de leur empreinte. Par défaut, le [référentiel de l'ADEME pour les services numériques](https://codde.fr/wp-content/uploads/2023/01/Referentiel-services-numeriques_v1.0_FR.pdf) l'attribue au temps d'utilisation pour un terminal et au volume de données pour le réseau.

**4. Fixer une trajectoire chiffrée.** Pour chaque indicateur : la valeur de départ et sa date, l'objectif, l'échéance et la méthode. S'aligner sur l'ITU-T L.1470, soit −45 % entre 2020 et 2030 (onglet « SBTi & ITU-T L.1470 »), revient à environ 6 % de baisse par an :

```
réduction annuelle = 1 − (1 − 0,45)^(1/10) ≈ 5,8 %
```

Les budgets techniques du [critère 6.1](../../frontend/6-1_poids-requetes-ecran/) servent alors de jalons, vérifiés à chaque mise en production, entre deux évaluations complètes.

**5. Documenter** dans la déclaration d'écoconception : les valeurs, la trajectoire et la méthode, avec l'outil, sa version et les hypothèses (durée de vie, taux d'utilisation, localisation). Le moyen de test pose la question : « La méthodologie d'évaluation des indicateurs suivis est-elle accessible publiquement ? »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Porteur de projet`

- le [critère 1.1](../1-1_evaluation-utilite/) (évaluation de l'utilité) : la situation de départ des objectifs ;
- le [critère 1.4](../1-4_revue-ecoconception/) (revue d'écoconception) : le suivi des objectifs dans le temps ;
- le [critère 6.1](../../frontend/6-1_poids-requetes-ecran/) (poids et requêtes par écran) : un objectif chiffré, vérifiable sur chaque écran ;
- le [critère 2.8](../../specifications/2-8_fournisseurs-impacts-environnementaux/) (fournisseurs) : les objectifs du service s'étendent aux fournisseurs.

{{% /tab %}}
{{< /tabs >}}

---

### 
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

En pratique, les déclarations d'écoconception publiées par les services publics numériques recourent plus souvent à des **budgets techniques proxy** (option 2 de l'onglet Designers Éthiques ci-dessus) qu'à une ACV multicritère complète — cohérent avec la préconisation du critère qui n'impose pas l'ACV en priorité :

- Le [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) (Nantes Métropole) fixe un budget technique proxy précis, critère marqué « Validé » : pas plus de 3 secondes de chargement d'une page (mesuré sur Samsung Galaxy S10, WiFi), pas plus de 750 Ko de données transférées au premier chargement, pas plus de 30 requêtes par page. Au [critère 6.1](../../frontend/6-1_poids-requetes-ecran/), il ajoute des seuils de régression plus larges (1 Mo, 50 requêtes) pour détecter une dérive avant qu'elle ne devienne critique.
- [Alt Impact](https://altimpact.fr/ecoconception-du-site/) (site porté par l'ADEME) combine budget technique et outils de mesure nommés avec objectif chiffré : [Fruggr](https://fruggr.io/) (Digital4Better) évalué à chaque fin de sprint avec un objectif de 80/100, Lighthouse (Google) avec un objectif de 90 % sur chaque page, et un budget de 5 Mo / 50 requêtes maximum par page — un exemple rare qui documente à la fois l'outil de mesure utilisé et sa fréquence d'évaluation (à chaque sprint, pas seulement au lancement).
- [DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr) marque le critère **« Non validé »** : il a estimé son empreinte avec GreenIT-Analysis, sans objectif de réduction. Il fixe en revanche un **budget par écran** au critère 6.1 (900 Ko et 40 requêtes au plus) et un **objectif de score RGESN** : de 71 % en mars 2025 à 80 % en juin 2026. Ces objectifs de moyens ne remplacent pas un objectif de réduction des impacts eux-mêmes.
- [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) (Pôle ministériel Écologie) suit la même logique de budget technique (2 Mo de transfert réseau compressé par page, 120 requêtes et 5 noms de domaine maximum) et publie une page dédiée à l'évolution de son impact écologique dans le temps, mais sans objectif chiffré de réduction publié.

Ce contraste illustre une limite pratique du critère 1.5 : suivre un **budget technique proxy dans la durée** est aujourd'hui plus répandu et plus accessible que publier une trajectoire alignée sur des indicateurs d'ACV (SBTi, ITU-T L.1470) — une voie que le critère autorise explicitement, tant que des objectifs sont fixés, suivis et documentés publiquement.

{{% /tab %}}

{{< /tabs >}}
