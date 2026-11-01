---
weight: 600
title: "8.6 - Localisation de l'hébergement"
description: "Critère 8.6 du RGESN : héberger le service dans un pays dont l'électricité émet moins de 100 gCO2eq/kWh, de préférence près des utilisateurs, vérifier où sont réellement les serveurs et citer la source de l'intensité carbone."
icon: "location_on"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un hébergement dont la localisation géographique est cohérente avec ses activités et qui minimise son empreinte environnementale ?

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
| **Critère**  | `8.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Responsable Logistique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est d'abord de privilégier un hébergement dans le pays où l'intensité carbone est peu élevée, et secondairement, dans une région où se situent la majorité des clients, afin de réduire la distance parcourue par les données et donc réduire l'infrastructure réseau mobilisée et son empreinte environnementale.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Privilégier un hébergeur dont les serveurs sont situés dans un pays avec une électricité bas carbone (source : [Electricity Maps](https://app.electricitymaps.com/map)). Dans la mesure du possible, il est également pertinent de privilégier un hébergeur qui soit proche des utilisateurs ou des activités identifiées (cela ne correspond pas à adopter les technologies Edge Computing mais à choisir un centre de données proche des utilisateurs).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Identifier la localisation des utilisateurs et celle des serveurs de l'hébergement.

Pour valider ce critère, il conviendra de vérifier que l'hébergeur du service numérique est situé dans un pays où l'intensité carbone de la consommation électrique est minimale. Pour cela, vérifier que cette intensité est en dessous du seuil annuel de 100 gCO₂eq/kWh, en lien avec la trajectoire de réduction des émissions de gaz à effet de serre telle que définie par l'initiative Science-Based Targets (SBTi) et conformément aux objectifs de l'Accord de Paris (à partir de 2030, le seuil à respecter est de 80 gCO₂eq/kWh puis 0 gCO₂eq/kWh à partir de 2050 – source : [Quick start guide for electric utilities](https://files.sciencebasedtargets.org/production/legacy/2020/06/SBTi-Power-Sector-15C-guide-FINAL.pdf) (PDF – 2 Mo)). De façon complémentaire (pas nécessaire pour la validation de ce critère), favoriser le choix d'un hébergement dans le pays où la majorité de ses utilisateurs sont localisés...

Documenter dans la déclaration d'écoconception, la localisation (pays, ville) de l'hébergement du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="GR491 et W3C" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Responsable Logistique`

Le [GR491](https://gr491.isit-europe.org/) (INR) ajoute un argument propre au **responsable logistique** : [« Le datacenter est-il situé à proximité de l'activité principale ? »](https://gr491.isit-europe.org/crit.php?id=2-hebergement-les-deplacements-physiques-sur-les-datacenters-sont-d74b7a). Les équipes techniques doivent parfois se rendre sur place, et la distance « doit être minimisée pour réduire les impacts de ces déplacements ». Un conseil voisin demande si les trajets sont possibles « en transport en commun ou mobilité douce ».

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) demandent, dans la fiche [**« Use sustainable hosting »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-hosting), de mesurer l'intensité carbone avec les données du réseau local (« Low-carbon electricity »). Pour un public local, la fiche sur les CDN conseille aussi un hébergement proche plutôt qu'une distribution mondiale (voir le [critère 6.7](../../frontend/6-7_domaine-unique/)).

{{% /tab %}}

{{% tab tabName="Quelle intensité carbone ?" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`

Le seuil de 100 gCO2eq/kWh s'applique à la moyenne annuelle du pays. Pour la France, les sources donnent des valeurs différentes, selon ce qu'elles comptent :

| Source | Année | Ce qui est compté | Intensité |
|---|---|---|---:|
| [Electricity Maps](https://www.electricitymaps.com/grid-in-review-2025/france) | 2024 | Électricité consommée, importations comprises | 33,5 g |
| Electricity Maps | 2025 | Électricité consommée, importations comprises | 32,0 g |
| [RTE](https://analysesetdonnees.rte-france.com/en/annual-review-2025/ghg-emissions) | 2025 | Électricité produite, émissions directes | 19,6 g |
| RTE | 2025 | Électricité produite, cycle de vie | 29,0 g |
| Base Empreinte de l'ADEME, [reprise par Nos Gestes Climat](https://nosgestesclimat.fr/documentation/commun/mix-%C3%A9lectrique/empreinte-carbone) | 2025 | Électricité consommée, amont des combustibles et construction des centrales compris | 46,1 g |

Toutes sont très en dessous du seuil de 100 g, et du seuil de 80 g qui s'appliquera à partir de 2030. L'écart entre elles compte quand on compare des pays : il faut comparer des valeurs de la même source, de la même année et de la même méthode.

Le lien du RGESN vers le guide du SBTi, à l'origine de ces seuils, commence par `chrome-extension://` : il ne s'ouvre que dans le navigateur de la personne qui l'a copié. L'adresse directe est donnée dans l'onglet « Moyen de test ou de contrôle » ci-dessus.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Administrateur Système`

**1. Situer les utilisateurs**, avec la mesure d'audience du service : pays et, si besoin, région.

**2. Situer les serveurs.** L'hébergeur indique la région choisie (par exemple `osc-fr1` chez Scalingo). Pour vérifier à qui appartient l'adresse d'un site et dans quel pays elle est enregistrée :

```sh
ip=$(dig +short exemple.fr | tail -n 1)
curl -s "https://rdap.db.ripe.net/ip/$ip" | jq -r '.name, .country'
```

La requête RDAP a été testée le 30 octobre 2026 sur les sites des retours d'expériences. Le pays affiché est celui de l'enregistrement de l'adresse, pas forcément celui du serveur. Derrière un CDN, l'adresse est celle du serveur de cache le plus proche du visiteur, et l'origine reste à demander à l'hébergeur.

**3. Recenser tout ce qui calcule pour le service** : tâches planifiées, intégration continue, services tiers de traitement. Une tâche qui tourne ailleurs que chez l'hébergeur déclaré a sa propre localisation (voir les retours d'expériences).

**4. Vérifier l'intensité carbone du pays** sur [Electricity Maps](https://app.electricitymaps.com/map) : moyenne annuelle, sous 100 gCO2eq/kWh.

**5. Documenter** dans la déclaration d'écoconception : pays et ville des serveurs, pays des utilisateurs, et intensité carbone avec sa source, son année et sa méthode.

{{% /tab %}}

{{% tab tabName="Proche des utilisateurs" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

La proximité est secondaire pour la validation, mais elle reste utile. Pour un public français, un hébergement en France réduit la distance parcourue par les données et le temps de réponse. Il évite aussi un CDN mondial, qui multiplie les copies des ressources sans bénéfice pour un public local.

La proximité ne doit pas l'emporter sur l'intensité carbone. Un centre de données voisin, dans un pays dont l'électricité émet 300 g/kWh, émet dix fois plus qu'un centre plus éloigné à 30 g, pour le même travail.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`

- le [critère 8.5](../8-5_electricite-renouvelable/) (électricité renouvelable) : une électricité bas carbone n'est pas forcément renouvelable ;
- le [critère 8.4](../8-4_wue/) (WUE) : le stress hydrique dépend aussi du lieu ;
- le [critère 6.7](../../frontend/6-7_domaine-unique/) (domaine unique) : un CDN n'est utile que s'il apporte un bénéfice clair ;
- le [critère 8.10](../8-10_decalage-asynchrone/) (traitements décalés) : au-delà du lieu, le moment du calcul fait aussi varier l'intensité carbone.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues et les adresses des sites vérifiées le 30 octobre 2026.

| Site | Déclaration | Réseau de l'adresse (RDAP) | Localisation déclarée | Intensité carbone déclarée |
|---|---|---|---|---:|
| [DiaLog](https://dialog.beta.gouv.fr/) | Validé | Outscale, France | Île-de-France | 33 g |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Validé | Ecritel, France | Clichy | 56 g, « en 2023 » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Validé | Non vérifiable (connexion requise) | Grenoble, trois centres de données | 53 g |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | Non détaillé | Ministère de la Transition écologique, France | — | — |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | — | GitHub, États-Unis | — | — |

**Les trois déclarations valident le critère, avec trois valeurs** pour le même pays : 33, 53 et 56 g. Elles datent d'années différentes et ne citent pas toutes leur méthode. Le critère est validé dans les trois cas, car toutes sont sous 100 g.

**DiaLog** a une partie de ses calculs ailleurs que chez Outscale. D'après son [code source](https://github.com/MTES-MCT/dialog), l'import des arrêtés depuis Litteralis tourne chaque jour ouvré sur un serveur de GitHub Actions (`runs-on: ubuntu-latest`), qui se connecte ensuite à la base de Scalingo. La localisation de ce serveur n'est ni choisie ni déclarée.

**Le site du RGESN** est servi par GitHub Pages. L'adresse est enregistrée aux États-Unis, mais la réponse vient d'un cache à Paris (`X-Served-By: cache-par-…`). Pour un site statique, c'est ce cache qui sert les visiteurs français ; l'origine n'est pas publiée.

{{% /tab %}}

{{< /tabs >}}
