---
weight: 200
title: "8.2 - Gestion durable des équipements de l'hébergeur"
description: "Critère 8.2 du RGESN : choisir un hébergeur qui publie la durée de vie de ses équipements, vise plus de huit ans, répare et réemploie, et trace la fin de vie de son matériel."
icon: "recycling"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement qui fournit une politique de gestion durable des équipements ?

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
| **Critère**  | `8.2` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable des achats` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Favoriser un hébergement ayant des engagements en faveur de l'environnement concernant sa gestion des équipements : impacts environnementaux de l'achat de ces équipements, politique d'achat (achat durable, réparable), politique d'usage (upgrade, réparation par exemple) et politique de fin d'usage (réemploi et gestion des DEEE, les déchets d'équipements électriques et électroniques).

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Sélectionner un hébergeur ou de demander des engagements à un hébergeur ayant une politique transparente et écologique de sa gestion des équipements : communication sur la durée de vie de ces derniers (serveurs, commutateurs réseau, firewalls, routeurs...) et sur la gestion du cycle de vie de son parc. Par exemple, il serait intéressant que l'hébergeur indique une durée de vie totale de ses équipements de plus de huit ans (ou un objectif en ce sens, si les installations de l'hébergeur ont moins de huit ans).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la mise en place d'un plan de gestion durable des équipements informatiques par l'hébergeur. Le plan devra couvrir des informations sur la durée de vie des équipements, la politique d'achat durable et les actions mises en place pour minimiser l'empreinte environnementale du cycle de vie du matériel utilisé par l'hébergeur. Pour valider le critère, ce plan devra être référencé dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="RWEB (GreenIT) et W3C" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache au 8.2 la fiche [**RWEB 0096 — « Choisir un hébergeur "éco-responsable" »**](https://rweb.greenit.fr/fr/fiches/RWEB_0096-choisir-un-hebergeur-eco-responsable), dont deux points relèvent des équipements : la gestion des déchets électroniques (DEEE) et la « politique d'achat responsable ». Elle ne mentionne pas la durée de vie, au cœur du 8.2.

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) en font un critère de succès, « Equipment longevity », dans la fiche [**« Use sustainable hosting »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting) : « Extend the lifespan of hardware », et acheter le matériel neuf auprès de fournisseurs qui s'engagent sur la durée de vie, les mises à jour et la réparation.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable RSE/Numérique soutenable`

La [recommandation n°4 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR) suit le cycle de vie du matériel :

- [« Les équipements sont-ils réparés plutôt que remplacés ? »](https://gr491.isit-europe.org/crit.php?id=4-hebergement-la-reparabilite-des-materiels-et-le-taux-5bc85c) (priorité **Medium**), avec un test : « Le taux de réparation est-il communiqué ? » ;
- [« Les équipements en fin de vie sont-ils revalorisés ( vente / don / recyclage ... ) ? »](https://gr491.isit-europe.org/crit.php?id=4-hebergement-le-renouvellement-du-parc-technique-est-incontournable-f80f16), avec le test « La chaîne est-elle traçable ? ».

Un troisième conseil semble aller dans l'autre sens : [« Est-ce que les serveurs et routeurs sont renouvelés lorsque les technologies permettent une meilleure efficacité énergétique ? »](https://gr491.isit-europe.org/crit.php?id=4-hebergement-les-avancees-technologiques-et-lefficacite-des-composants-a0aa09). En France, où l'électricité est peu carbonée, un serveur plus efficace compense rarement la fabrication de son remplaçant (onglet suivant).

{{% /tab %}}

{{% tab tabName="Pourquoi huit ans" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`

L'[API de Boavizta](https://api.boavizta.org/) (version 2.5.0, interrogée le 30 octobre 2026) estime, pour un serveur type Dell PowerEdge R740 :

- la fabrication à **900 kgCO2e**, hors fin de vie ;
- une consommation moyenne de **536 W**, soit environ 4 700 kWh par an.

Boavizta compte l'électricité française à 98 gCO2e/kWh, une valeur publiée en 2021. Avec 32 g, la valeur 2025 d'[Electricity Maps](https://www.electricitymaps.com/grid-in-review-2025/france), l'usage émet environ 150 kgCO2e par an, hors refroidissement :

| Durée de vie | Fabrication | Usage | Total par an |
|---|---:|---:|---:|
| 4 ans | 900 kg | 600 kg | 375 kg |
| 8 ans | 900 kg | 1 200 kg | 262 kg |

Sur 4 ans, la fabrication représente 60 % de l'empreinte du serveur. Le garder 8 ans réduit son empreinte annuelle d'environ 30 %. Un serveur neuf qui consommerait 20 % de moins ne ferait gagner que 30 kg par an, soit trente ans pour amortir sa fabrication.

Le calcul ne porte que sur le climat. La fabrication pèse plus encore sur l'épuisement des ressources abiotiques, que le [8.1](../8-1_demarche-hebergeur/) demande aussi de suivre.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Responsable des achats`, `Responsable de l'hébergement`

**1. Demander le plan de gestion des équipements**, que le moyen de test exige de référencer. Il doit répondre à cinq questions :

| Question | Ce qu'il faut obtenir |
|---|---|
| Combien de temps les équipements restent-ils en service ? | La durée de vie moyenne par type (serveurs, stockage, réseau), et l'objectif |
| Comment sont-ils achetés ? | Les critères d'achat : garantie, disponibilité des pièces, réparabilité |
| Sont-ils réparés ? | Le taux de réparation, comme le demande le GR491 |
| Que deviennent leurs composants ? | La part réemployée. OVHcloud, par exemple, [annonce](https://corporate.ovhcloud.com/en/newsroom/press-kit/sustainability/) 20 à 30 % de composants de serveurs réemployés chaque année |
| Où finissent-ils ? | La filière de reconditionnement ou de recyclage, avec ses justificatifs |

**2. Comparer avec l'objectif de huit ans** du RGESN. Une durée moyenne qui n'est pas publiée, ou qui est inférieure à huit ans sans objectif, ne permet pas de valider le critère.

**3. Agir sur sa propre part.** Le service ne choisit pas les serveurs de l'hébergeur, mais il choisit combien il en occupe. Dimensionner les instances au besoin réel ([critère 3.2](../../architecture/3-2_architecture-elastique/)) et éteindre les environnements inutilisés ([critère 3.7](../../architecture/3-7_environnements-developpement-test/)) réduisent la part de matériel mobilisée.

**4. Documenter** dans la déclaration d'écoconception le lien vers le plan de l'hébergeur, la durée de vie annoncée et sa date.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable des achats`

- le [critère 8.1](../8-1_demarche-hebergeur/) (démarche de l'hébergeur) : le plan de gestion des équipements en est une pièce ;
- le [critère 2.8](../../specifications/2-8_fournisseurs-impacts-environnementaux/) (fournisseurs) : les mêmes questions, posées à tous les fournisseurs ;
- le [critère 2.2](../../specifications/2-2_anciens-terminaux/) (anciens terminaux) : la même logique de durée de vie, côté utilisateur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration | Durée de vie publiée |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | Non |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | Non |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Validé | Non |

**DiaLog** reprend la réponse de Scalingo : « Outscale n'a pas de politique des gestion durable des équipements ». La réparation est prioritaire, puis le matériel du cloud est « revendu à un prestataire ». Le critère est logiquement non validé.

**Le Musée d'arts de Nantes** décrit le plan d'Ecritel : il couvre la « durée de vie moyenne du parc d'équipements », l'impact de l'achat et la fin de vie. La politique d'achat durable est « en cours de rédaction ». Le plan existe, mais la déclaration n'en donne ni le lien ni la durée : il faudrait les ajouter pour valider le critère.

**FACE** valide le critère avec trois engagements de son hébergement, dont « l'allongement de la durée de vie des matériels » sur une infrastructure « de plus de 5 ans ». Le moyen de test demande pourtant que le plan soit référencé dans la déclaration, ce qui n'est pas le cas.

{{% /tab %}}

{{< /tabs >}}
