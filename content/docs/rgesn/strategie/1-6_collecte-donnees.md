---
weight: 600
title: "1.6 - Collecte de données"
description: ""
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2025-12-21T13:29:09+01:00"
draft: true
toc: true
---

---

## Le service numérique collecte-t-il la donnée de façon responsable et raisonnée ?

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
| **Critère**  | `1.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** |  `Data Scientist` `Responsable Juridique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Cette pratique vise à encourager une collecte de données responsable et raisonnée en complément des obligations légales de minimisation prévues par le Règlement général sur la protection des données (RGPD) en ce qui concerne les données personnelles. 

Comme le souligne le rapport de la CNIL « [Données, Empreinte et Libertés](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.cnil.fr/sites/cnil/files/2023-07/cnil_cahier_ip9_0.pdf) » (2023), certains impératifs de respect de la vie privée et objectifs d'écoconception se rejoignent. 

Il s'agira donc d'œuvrer à **réduire la quantité de données collectées**, traitées et stockées par le service, y compris les **données non personnelles et métadonnées**, pour optimiser l'utilisation des ressources informatiques. Afin de limiter le profilage des utilisateurs, consommateur en ressources, le critère vise également à **restreindre la collecte et le traitement de métadonnées aux fins de tracking**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir clairement les **données nécessaires** au fonctionnement du service, en cohérence avec les **cibles utilisatrices** et leurs **attentes** telles que définies au [critère 1.2](../1-2_cibles-utilisatrices/) du présent référentiel. Si une **donnée ne contribue pas** directement à l'amélioration de l'expérience utilisateur ou au fonctionnement du service, mieux vaut envisager de **ne pas la collecter**. La **collecte de métadonnées** dans une perspective de profilage des utilisateurs devra être **évitée**.

Pour chaque type de donnée jugée essentielle au fonctionnement du service et aux besoins des utilisateurs, **définir les conditions de collecte** qui devront expressément respecter les dispositifs du **RGPD** concernant les données personnelles. Pour les **données non personnelles**, la **durée de conservation** devra également être **minimisée** afin d'éviter leur stockage excessif.

Systematiser la mise en place d'une information complète, le droit de s'opposer et/ou la demande de consentement explicite de l'utilisateur pour l'ensemble des données collectées, y compris pour les données non personnelles.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Contrôler le **type** et la **quantité de données** collectées, traitées et stockées par le service.

En ce qui concerne les données personnelles, indépendamment des enjeux d'écoconception, la minimisation de la collecte de ces données est un impératif du RGPD et doit être strictement suivie par le responsable de traitement.

De façon plus large, pour l'ensemble des données collectées (y compris non personnelles), **justifier dans la déclaration d'écoconception** du service le besoin de cette collecte au regard des cibles utilisatrices du service ([critère 1.2](../1-2_cibles-utilisatrices/)), la limitation de leur traitement et de la durée de conservation, et documenter les outils de recueil du consentement le cas échéant. En ce qui concerne les données personnelles, un renvoi pourra être fait au registre de traitements des données personnelles tel que prévu par le RGPD.

Ne pas collecter des métadonnées servant au profilage de l'utilisateur, sauf si cette collecte est essentielle aux besoins et cibles utilisatrices du service ([critère 1.2](../1-2_cibles-utilisatrices/)) ou au fonctionnement de ce dernier, et si l'utilisateur a donné son consentement explicite et éclairé et qu'il peut désactiver cette collecte à tout moment. Le cas échéant, ces éléments devront être documentés dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via d'autre(s) référentiel(s) :

{{< tabs tabTotal="1">}}
{{% tab tabName="RWEB" %}}


{{% /tab %}}
{{< /tabs >}}


---

### 
### Pour aller plus loin :


{{< tabs tabTotal="3">}}

{{% tab tabName="Retours d'expériences" %}}
`TODO`
{{% /tab %}}

{{% tab tabName="Déclaration d'écoconception" %}}
Pour réaliser votre déclaration d'écoconception :
- [Déclaration d'écoconception](https://www.arcep.fr/uploads/tx_gspublication/referentiel_general_ecoconception_des_services_numeriques_version_2024.pdf#page=7)
- [Calcul de score d'avancement](https://www.arcep.fr/uploads/tx_gspublication/referentiel_general_ecoconception_des_services_numeriques_version_2024.pdf#page=8)
{{% /tab %}}

{{< /tabs >}}
