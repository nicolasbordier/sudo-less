---
weight: 500
title: "1.5 - Objectifs environnementaux"
description: "Critère 1.5 du RGESN : comment évaluer l'empreinte environnementale d'un service numérique et se fixer des objectifs de réduction chiffrés et suivis dans le temps."
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2026-07-03T00:00:00+01:00"
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
| **Applicabilité** | `Tous les services` |
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
### Comment appliquer concrètement cette recommandation ?

En fonction de chaque contexte :

{{< tabs tabTotal="3">}}
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
- La recommandation [ITU-T L.1470](https://www.itu.int/rec/T-REC-L.1470), développée avec le GeSI, la GSMA et la SBTi elle-même, décline cette approche **spécifiquement pour le secteur des TIC** (réseaux mobiles et fixes, data centers, réseaux d'entreprise, terminaux utilisateurs) : elle fixe une cible sectorielle de **réduction de 45 % des émissions de GES entre 2015 et 2030**, avec une ambition de long terme à horizon 2050. Ce sont les premiers objectifs sectoriels spécifiques aux TIC validés par la SBTi.

Ces deux référentiels sont surtout pertinents à l'échelle d'une organisation ou d'un grand programme ; pour un service unique, ils servent davantage de **point de repère** (un service numérique isolé peut difficilement obtenir une validation SBTi individuelle) que d'objectif directement applicable.

{{% /tab %}}
{{< /tabs >}}

---

### 
### Pour aller plus loin :

{{< tabs tabTotal="3">}}

{{% tab tabName="Retours d'expériences" %}}

En pratique, les déclarations d'écoconception publiées par les services publics numériques recourent plus souvent à des **budgets techniques proxy** (option 2 de l'onglet Designers Éthiques ci-dessus) qu'à une ACV multicritère complète — cohérent avec la préconisation du critère qui n'impose pas l'ACV en priorité :

- [DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr) fixe un **budget de performance chiffré** (40 requêtes serveur maximum par écran, 900 Ko de ressources maximum par écran) et un **objectif quantifié de progression** dans le temps : faire passer son taux de conformité RGESN de 71 % (mars 2025) à 80 % (juin 2026) — un exemple concret d'objectif suivi dans la durée, même sans indicateur d'ACV (énergie primaire, GES, eau, ressources abiotiques).
- [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) (Pôle ministériel Écologie) suit la même logique de budget technique (2 Mo de transfert réseau compressé par page, 120 requêtes et 5 noms de domaine maximum) et publie une page dédiée à l'évolution de son impact écologique dans le temps, mais sans objectif chiffré de réduction publié.

Ce contraste illustre une limite pratique du critère 1.5 : suivre un **budget technique proxy dans la durée** est aujourd'hui plus répandu et plus accessible que publier une trajectoire alignée sur des indicateurs d'ACV (SBTi, ITU-T L.1470) — une voie que le critère autorise explicitement, tant que des objectifs sont fixés, suivis et documentés publiquement.

{{% /tab %}}

{{% tab tabName="Déclaration d'écoconception" %}}
Pour réaliser votre déclaration d'écoconception :
- [Déclaration d'écoconception](https://www.arcep.fr/uploads/tx_gspublication/referentiel_general_ecoconception_des_services_numeriques_version_2024.pdf#page=7)
- [Calcul de score d'avancement](https://www.arcep.fr/uploads/tx_gspublication/referentiel_general_ecoconception_des_services_numeriques_version_2024.pdf#page=8)
{{% /tab %}}

{{< /tabs >}}
