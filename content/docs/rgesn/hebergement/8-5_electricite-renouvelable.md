---
weight: 500
title: "8.5 - Électricité d'origine renouvelable"
description: "Critère 8.5 du RGESN : distinguer électricité bas carbone et renouvelable, préférer les contrats d'achat direct (PPA) aux garanties d'origine, et demander à l'hébergeur la quantité contractée par mode d'approvisionnement."
icon: "solar_power"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement dont l'origine de consommation d'électricité est documentée et majoritairement d'origine renouvelable ?

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
| **Critère**  | `8.5` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif de ce critère est de promouvoir la transparence sur l'origine de la consommation électrique des centres de données et d'œuvrer à la transition énergétique, en particulier au développement des énergies renouvelables.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Demander à l'hébergeur sa politique en termes d'achat d'électricité. Les PPA (Power Purchase Agreements) des contrats d'énergie renouvelable de long terme sont considérés comme de meilleure qualité que les certificats d'origine de l'électricité.

Voir à ce sujet le rapport [Development of the EU Green Public Procurement (GPP) criteria for data centres, server rooms and cloud services](https://publications.jrc.ec.europa.eu/repository/handle/JRC118558). Ainsi, la quantité annuelle d'énergie contractualisée devra être renseignée, en précisant les modalités de fourniture d'énergie renouvelable : via PPA sur le réseau français mais hors site, via autoconsommation donc sur site (potentiellement par PPA ou support complet des coûts de capital et autres) et via des garanties d'origine. Pour les garanties d'origine renouvelable, l'additionnalité doit être prouvée.

Secondairement, un indicateur de performance normé peut être suivi : le REF, Renewable Energy Factor. La part en électricité bas carbone est également une donnée pertinente pour appréhender l'empreinte environnementale du mix énergétique de l'hébergement.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

S'assurer de la transparence de l'hébergeur en matière d'énergies renouvelables.

Demander des justificatifs sur la provenance de l'électricité consommée par l'hébergeur (PPA en priorité, sinon certificat d'origine de l'électricité).

Le critère est validé si l'hébergeur du service numérique est transparent sur son mix énergétique et documente une politique de recours majoritaire aux énergies renouvelables, ayant un impact effectif sur la réduction de la demande en énergie fossile. Au-delà de l'indicateur REF, l'hébergeur devra renseigner la quantité annuelle d'énergie contractualisée telle que décrite dans la section « Mise en œuvre » pour documenter sa politique de recours aux énergies renouvelables.

La provenance de l'électricité consommée par l'hébergement sera documentée dans la déclaration d'écoconception du service, par exemple en renvoyant vers la documentation détaillée pertinente du fournisseur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="RWEB (GreenIT) et GR491" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable RSE/Numérique soutenable`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache au 8.5 la fiche [**RWEB 0095 — « Privilégier un fournisseur d'électricité écoresponsable »**](https://rweb.greenit.fr/fr/fiches/RWEB_0095-privilegier-un-fournisseur-d-electricite-ecoresponsable). Elle reconnaît qu'« il n'existe pas de mécanisme solide » pour garantir l'origine de l'électricité consommée. Son principe de validation se contente pourtant de la preuve d'achat de garanties d'origine. Le RGESN va plus loin : il place les PPA avant les garanties d'origine, et demande, pour ces dernières, de prouver l'additionnalité.

Le [GR491](https://gr491.isit-europe.org/) (INR) pose la question dans sa [recommandation n°4 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=4) : « L'électricité provient-elle d'énergies renouvelables ? »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`

Dans la fiche [**« Use sustainable hosting »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026), deux critères de succès encadrent le 8.5 :

- « Low-carbon electricity » demande de mesurer l'intensité carbone avec les données du réseau local (*location-based*), avant tout achat de certificats ;
- « Remaining emissions » accepte les certificats pour les émissions restantes, à condition qu'ils correspondent « the time and location of the electricity used », et qu'ils ne soient pas comptés deux fois.

Une garantie d'origine annuelle, achetée dans un autre pays, ne respecte pas cette correspondance de lieu et de moment.

{{% /tab %}}

{{% tab tabName="Bas carbone n'est pas renouvelable" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Responsable de l'hébergement`

En France, la distinction décide du critère. D'après [Electricity Maps](https://www.electricitymaps.com/grid-in-review-2025/france), l'électricité consommée en 2025 était :

| Part de l'électricité consommée en France | 2024 | 2025 |
|---|---:|---:|
| Bas carbone (renouvelable et nucléaire) | 95,9 % | 96,3 % |
| Renouvelable | 28,6 % | 27,9 % |

Un centre de données français alimenté par le réseau, sans contrat particulier, consomme donc une électricité très peu carbonée, mais **pas majoritairement renouvelable**. Il valide le [critère 8.6](../8-6_localisation/) (localisation), pas le 8.5.

Pour atteindre une part majoritaire, l'hébergeur dispose de trois moyens, du plus au moins solide selon le RGESN :

| Moyen | Ce que c'est | Ce qu'il faut demander |
|---|---|---|
| PPA hors site | Un contrat d'achat de long terme avec un parc éolien ou solaire précis, qui finance sa construction | La quantité annuelle et le site de production |
| Autoconsommation | Une production sur le site du centre de données | La quantité produite et consommée sur place |
| Garanties d'origine | Un certificat par MWh renouvelable produit, acheté séparément de l'électricité | La quantité, l'origine, et la preuve d'additionnalité |

L'indicateur REF de la norme ISO/IEC 30134-3 donne la part renouvelable, mais pas le moyen employé : un REF de 100 % obtenu par des garanties d'origine ne finance pas forcément de nouvelle production.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

**1. Demander à l'hébergeur la quantité annuelle d'électricité contractée**, répartie entre les trois moyens de l'onglet précédent, comme l'exige le moyen de test. Une mention « contrat énergie verte » ne suffit pas : c'est généralement un contrat adossé à des garanties d'origine.

**2. Demander les justificatifs** : contrat de PPA, ou certificats de garanties d'origine avec leur pays et leur année de production.

**3. Vérifier la part majoritaire** sur l'électricité du site qui héberge le service, pas sur les bureaux de l'hébergeur.

**4. Documenter** dans la déclaration d'écoconception : la part renouvelable, sa répartition par moyen et le lien vers la documentation de l'hébergeur. Si la part n'est pas majoritaire, le dire, comme FACE (voir les retours d'expériences).

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

- le [critère 8.6](../8-6_localisation/) (localisation) : l'intensité carbone du pays, à ne pas confondre avec la part renouvelable ;
- le [critère 8.1](../8-1_demarche-hebergeur/) (démarche de l'hébergeur) : les émissions *market-based* tiennent compte des certificats, les *location-based* non ;
- le [critère 8.10](../8-10_decalage-asynchrone/) (traitements décalés) : déplacer un calcul vers les heures où le réseau est le moins carboné agit sur l'électricité réellement produite.

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
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | Un « contrat énergie verte » pour les fournisseurs d'Outscale, non détaillé |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Validé | Centres de données « 100% fournis en énergies renouvelables » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | **Non validé** | Électricité du réseau français, bas carbone mais minoritairement renouvelable |

**FACE** fait le raisonnement attendu : la France produit une électricité « très majoritairement bas carbone (93% sur une année) », mais elle reste « minoritairement d'origine renouvelable (28 % sur une année) ». Le critère n'est donc pas validé, et la déclaration l'explique.

**DiaLog** l'écrit aussi : le contrat n'étant pas détaillé, « il n'est pas possible de savoir s'il s'agit d'une part majoritaire ». C'est exactement ce qu'il faut demander à Outscale : la quantité et le moyen.

**Le Musée d'arts de Nantes** valide le critère sur la parole de ses centres de données, « 100% fournis en énergies renouvelables », sans en préciser le moyen ni la quantité contractée. Le moyen de test demande ces deux éléments. Sans précision, cette alimentation peut reposer sur des garanties d'origine, dont il faudrait alors prouver l'additionnalité.

{{% /tab %}}

{{< /tabs >}}
