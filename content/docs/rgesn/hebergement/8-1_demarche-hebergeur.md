---
weight: 100
title: "8.1 - Hébergeur engagé dans la réduction de son empreinte"
description: "Critère 8.1 du RGESN : choisir un hébergeur qui publie ses indicateurs environnementaux, s'appuie sur des cadres vérifiables comme le Code de conduite européen, et remonter toute la chaîne d'hébergement jusqu'au centre de données."
icon: "domain"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement ayant une démarche de réduction de son empreinte environnementale ?

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
| **Critère**  | `8.1` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service ne repose pas sur l'activité d'un centre de données` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` `Administrateur Système` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Les centres de données représentent environ 15 % de l'empreinte carbone du numérique en France et leur empreinte environnementale ne se limite pas aux émissions de GES (étude ADEME-Arcep). Il est donc important de prendre en compte dans le choix de la solution d'hébergement les pratiques du centre de données en matière environnementale. Il convient de favoriser un hébergement qui suit son empreinte environnementale et a engagé une démarche proactive pour la réduire.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Sélectionner un hébergeur transparent sur son empreinte environnementale et ayant des engagements environnementaux pour la réduire. Une ACV est recommandée, ou a minima, la publication des indicateurs suivants : émissions de GES (market-based et location-based), consommation énergétique, en eau, en ressources abiotiques (minérales/métalliques). Plus précisément, l'hébergeur devra avoir pris des engagements pour minimiser son empreinte environnementale, visant a minima les indicateurs suivants : émissions de GES (market-based et location-based), consommation énergétique, en eau, en ressources abiotiques (minérales/métalliques). Afin de vérifier les engagements environnementaux pris par l'hébergeur, ceux-ci devront se baser sur des cadres ou normes existantes, spécifiquement :

- Code de conduite européen sur les centres de données, établi par la Commission européenne ;
- Norme environnementale : ISO 14001... ;
- Certification environnementale : ISO 14001, LEED, BREEAM, HQE... ;
- Évaluation et communication des impacts via des référentiels reconnus (par exemple : Product Category Rules (PCR), Bilan Carbone/GHG Protocol, ISO14063, normes ITU, Carbon Disclosure Project (CDP), Science Based Targets (SBTi)...) mutualisation des ressources machines ;
- Type de refroidissement minimisant la consommation de l'environnement technique en fluides frigorigènes, en eau et en énergie ;
- Mécanisme de récupération de la chaleur fatale ;
- Mise en place d'efforts d'amélioration de la performance énergétique de l'hébergement via une certification ISO 50001 ;
- Analyse d'impact environnemental du « move to cloud » pour les acteurs ayant leurs serveurs on premise voire calculettes proposées par les fournisseurs en amont de la migration ;
- Politique de construction du centre de données et minimisation de l'artificialisation des sols ;
- Charte, politique RSE certifiée etc.

Il convient de rester vigilant au greenwashing lorsqu'il s'agit de communications sur la neutralité carbone, d'une charte, d'une politique ou d'une feuille de route interne, sans possibilité de vérifier la mise en œuvre ou sans un tiers indépendant qui certifie la mise en œuvre.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Sélectionner un hébergeur transparent sur son empreinte environnementale et ses engagements en faveur de l'environnement. Afin de vérifier la véracité des données communiquées par les centres de données, il est conseillé de demander à l'hébergeur les certificats relatifs aux performances environnementales ainsi que les méthodologies utilisées en se basant sur des normes et standards reconnus (ISO, etc.).

Vérifier ou demander des engagements à l'hébergeur pour diminuer son empreinte environnementale – a minima concernant les indicateurs suivants : émissions de GES (market-based et location-based), consommation en énergie, en eau, en ressources abiotiques (minérales/métalliques). S'assurer de la ratification du Code de conduite sur les centres de données par l'hébergeur (se référer, si possible, à la méthodologie de la Commission européenne dans le contexte de l'acte délégué sur la taxonomie climat qui permet d'évaluer le respect de ce Code de conduite par les centres de données) et des actions associées.

Documenter dans la déclaration d'écoconception du service l'empreinte environnementale de l'hébergement et la mise en place d'engagements environnementaux pour la minimiser.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable des achats`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) ne rattache aucune fiche au 8.1. Sa fiche générale sur l'hébergement, [**RWEB 0096 — « Choisir un hébergeur "éco-responsable" »**](https://rweb.greenit.fr/fr/fiches/RWEB_0096-choisir-un-hebergeur-eco-responsable), rattachée aux critères [8.2](../8-2_gestion-equipements/) à [8.4](../8-4_wue/), liste six points à examiner : déchets électroniques, PUE, CUE et WUE, achats, dimension sociale, électricité bas carbone et « compensation carbone ».

Ce dernier point va à l'encontre du RGESN, qui met en garde contre les communications « sur la neutralité carbone » qu'aucun tiers ne vérifie. La compensation ne réduit pas les émissions du centre de données.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

Dans la [famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=1) du [GR491](https://gr491.isit-europe.org/) (INR), deux critères en priorité **High** couvrent le 8.1 :

- [« L'hébergeur adhère-t-il aux meilleures pratiques de son secteur d'activité ? »](https://gr491.isit-europe.org/crit.php?id=1-hebergement-le-domaine-de-lhebergement-se-struture-pour-d84a04) pose la même question que le RGESN : le centre de données suit-il le Code de conduite européen ? Sa notation donne 50 points à une adhésion « en cours » ;
- [« Le fournisseur expose-t-il tous ses indicateurs ? »](https://gr491.isit-europe.org/crit.php?id=4-hebergement-le-niveau-de-maturite-nr-des-operateurs-935f7c), en recommandation incontournable, ajoute une réserve : « La communication d'indicateurs ne présume pas de la pertinence et de la fiabilité des indicateurs », dont la méthode doit aussi être publiée.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) traitent l'hébergement dans la fiche [**« Use sustainable hosting »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting). Deux de ses critères de succès correspondent au 8.1 :

- « Provider selection » demande de privilégier les fournisseurs qui publient « their environmental policies and related performance indicators » : PUE, WUE, CUE, part d'électricité renouvelable, engagements de réduction et pratiques de maintenance du matériel ;
- « Efficient operation » demande de suivre ces indicateurs dans la durée, que l'hébergement soit externe ou interne.

{{% /tab %}}

{{% tab tabName="Ce que la loi impose" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable RSE/Numérique soutenable`

Depuis la directive européenne 2023/1791 sur l'efficacité énergétique, une partie des indicateurs du 8.1 est obligatoire. La France l'a transposée par la loi n° 2025-391 du 30 avril 2025 et le décret n° 2025-1382 du 29 décembre 2025 (articles L. 236-1 et suivants du Code de l'énergie), d'après le [cabinet CMS](https://cms.law/en/fra/publication/performances-energetiques-des-data-centers-de-nouvelles-obligations) :

| Centre de données | Obligation |
|---|---|
| 500 kW de puissance installée ou plus | Transmettre et publier, au plus tard le 15 mai de chaque année, ses indicateurs annuels d'énergie et de durabilité, sur la plateforme du règlement délégué (UE) 2024/1364 |
| 1 MW ou plus | Récupérer sa chaleur fatale (voir le [critère 8.7](../8-7_chaleur-fatale/)) |

Pour un centre de données de cette taille, l'hébergeur n'a donc plus de raison de ne pas fournir son PUE, son WUE et sa part d'électricité renouvelable : il les déclare déjà.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

**1. Remonter la chaîne d'hébergement.** Un service sur une plateforme (PaaS) dépend souvent de trois acteurs : la plateforme, le fournisseur d'infrastructure (IaaS) et l'exploitant du bâtiment. Chez DiaLog : Scalingo, puis 3DS Outscale, puis les centres de données que loue Outscale. Les indicateurs du 8.1 viennent du dernier maillon, les engagements de chacun.

**2. Demander les éléments que le moyen de test exige**, avec la méthode et la période :

| Élément | Ce qu'il faut obtenir | Point de vigilance |
|---|---|---|
| Émissions de GES | Valeurs *location-based* et *market-based* | La seconde intègre les achats de certificats et peut être bien plus basse |
| Énergie, eau, ressources abiotiques | Valeurs annuelles, par site | Une moyenne de groupe masque les écarts entre sites |
| Code de conduite européen | Le nom du site dans la liste des participants du JRC | L'adhésion d'une maison mère ne couvre pas tous ses sites |
| ISO 14001, ISO 50001 | Le certificat et son périmètre | Le certificat doit couvrir le site qui héberge le service |
| « Neutralité carbone » | La part de réduction et la part de compensation | Sans vérification par un tiers, le RGESN y voit un risque d'écoblanchiment |

**3. Inscrire ces demandes dans le marché.** Pour un achat public, ces éléments peuvent figurer parmi les critères de sélection. L'obligation de publication rend ces valeurs disponibles pour les grands centres de données.

**4. Documenter** dans la déclaration d'écoconception : chaque acteur de la chaîne, ses engagements, les cadres qu'il suit et la date des données.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable des achats`

- le [critère 2.8](../../specifications/2-8_fournisseurs-impacts-environnementaux/) (fournisseurs) : la même démarche, appliquée à tous les fournisseurs ;
- les critères [8.3](../8-3_pue/) (PUE), [8.4](../8-4_wue/) (WUE) et [8.5](../8-5_electricite-renouvelable/) (électricité) : les indicateurs à obtenir, un par un ;
- le [critère 8.2](../8-2_gestion-equipements/) (équipements) : les ressources abiotiques viennent surtout de la fabrication du matériel ;
- le [critère 8.7](../8-7_chaleur-fatale/) (chaleur) : la récupération de chaleur fait partie des cadres listés par le RGESN.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration | Hébergeur |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | Scalingo, sur l'infrastructure de 3DS Outscale |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | Ecritel, dans des centres de données de ses fournisseurs |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | **Non validé** | Plateforme (PaaS) sur l'hébergement ECO4 |

**DiaLog** décrit la chaîne complète dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf) : Scalingo, Outscale, puis Telehouse, signataire du Code de conduite européen. Les autres fournisseurs d'Outscale ne le sont pas, mais ont signé le Climate Neutral Data Centre Pact, une initiative du secteur que le RGESN ne cite pas. Sa source, la [page RGESN de Scalingo](https://doc.scalingo.com/compliance/rgesn), date du 26 mai 2023, donne un PUE de 2021 et suit les questions de la version précédente du référentiel. Une page à jour, sur la version 2024, permettrait aux clients de Scalingo de documenter le 8.1 sans enquête.

**Le Musée d'arts de Nantes** l'écrit : « Ecritel n'est pas signataire du Code de Conduite sur les Datacenters. Ceux-ci ne leur appartiennent pas et sont gérés par leurs fournisseurs. » Ecritel a réalisé son bilan carbone en juin 2024 et finalise un plan de décarbonation. La chaîne compte donc deux maillons, et les indicateurs du 8.1 sont à demander au second.

**FACE** précise que l'hébergement ECO4 « n'est pas encore signataire du Code de Conduite européen », et que « le processus est en cours pour 2025 ». Le critère sera à réévaluer une fois l'adhésion obtenue.

{{% /tab %}}

{{< /tabs >}}
