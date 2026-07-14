---
weight: 400
title: "3.4 - Mises à jour correctives des équipements"
description: "Critère 3.4 du RGESN : pourquoi et comment garantir la disponibilité de mises à jour correctives pendant toute la durée de vie prévue des équipements liés au service (IoT, objets connectés)."
icon: "security_update_good"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique garantit-il la mise à disposition de mises à jour correctives pendant toute la durée de vie prévue des équipements et des logiciels liés au service ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Architecture` |
| **Critère**  | `3.4` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A pour les services numériques qui ne sont pas commercialisés avec un terminal associé` |
| **Métiers concernés** | `Porteur de projet` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'obsolescence du logiciel commercialisé avec un équipement lié à un service numérique (par exemple : système d'exploitation, logiciel d'objet connecté, assistants vocaux…) rend souvent l'équipement inutilisable, alors que sa durée de vie pourrait être prolongée si le logiciel était maintenu plus longtemps. Cela revêt une importance particulière dans le contexte du développement de l'internet des objets (IoT), caractérisé par des équipements connectés nécessitant une maintenance continue pour garantir leur fonctionnement optimal, leur sécurité et leur interopérabilité. L'objectif est donc de limiter la contribution à l'obsolescence des équipements liés au service en assurant la disponibilité de mises à jour correctives tout au long de leur durée de vie prévue.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Maintenir le service numérique pendant toute la durée prévue de l'équipement. Cela implique de prévoir une infrastructure de support appropriée, des ressources techniques et financières, ainsi qu'une planification de la maintenance à long terme – en cohérence avec la durée de vie estimée du matériel. Par exemple, sont visés ici des équipements spécifiques et les objets connectés (IoT).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, indiquer la durée de maintenance du service dans la déclaration d'écoconception et vérifier que les mises à jour sont effectivement disponibles tout au long de la durée de vie des équipements associés.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="2">}}
{{% tab tabName="Cadre réglementaire européen" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable RSE/Numérique soutenable`

Ce critère rejoint, sans le citer explicitement, deux réglementations européennes qui imposent désormais une obligation légale là où le RGESN formule une recommandation :

- Le [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) ([Règlement (UE) 2024/2847](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2847), entré en vigueur le 10 décembre 2024, pleinement applicable au 11 décembre 2027) impose aux fabricants de produits comportant des éléments numériques de fournir des **mises à jour de sécurité gratuites pendant une durée minimale de 5 ans** après la mise sur le marché — ou pendant la durée de vie prévue du produit si elle est plus courte.
- La [directive (UE) 2019/771](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32019L0771) « Vente de biens » impose, pour tout bien comportant des éléments numériques, de fournir les **mises à jour nécessaires au maintien de la conformité** pendant la durée que le consommateur peut raisonnablement attendre — une durée de référence de **5 ans pour un smartphone** est généralement retenue dans les analyses de cette directive.

Ces deux textes se complètent : le Cyber Resilience Act cible spécifiquement les mises à jour de **sécurité**, la directive Vente de biens vise plus largement le maintien de la **conformité** du produit. Documenter le respect de ces obligations légales dans la déclaration d'écoconception permet de valider ce critère par la même occasion.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Ce critère est le pendant logiciel du [critère 1.10](../../strategie/1-10_api-materiel/) (API ouvertes pour prolonger la durée de vie du matériel), déjà publié sur ce site : le 1.10 porte sur l'**ouverture des API matérielles** pour permettre à des tiers de prendre le relais après l'arrêt du support officiel, tandis que le 3.4 porte sur l'engagement du **fournisseur lui-même** à maintenir le logiciel à jour tout au long de la durée de vie annoncée de l'équipement. Le [règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act), déjà cité au critère 1.10, et le Cyber Resilience Act ci-contre relèvent tous deux de la même vague réglementaire européenne récente sur la durabilité des objets connectés, mais couvrent des aspects distincts et complémentaires (accès aux données vs sécurité des mises à jour).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non applicable »**, sans autre justification que ce statut. C'est un cas attendu et sans ambiguïté : FACE est un service web sans terminal associé commercialisé, exactement le cas d'exclusion prévu par la case « Applicabilité » du critère — contrairement aux critères voisins de cette même fiche (3.1, 3.2, 3.3), qui portaient eux sur l'architecture du service web lui-même et s'appliquaient donc pleinement.

Pour un cas concret côté matériel grand public, [Fairphone](https://www.fairphone.com/software-longevity) a systématiquement dépassé ses propres engagements de départ : le Fairphone 3 (2019), initialement promis pour 5 ans de mises à jour, en a finalement reçu 7 ; le Fairphone 4 (2021), annoncé pour 5 ans avec l'ambition d'atteindre 7, est aujourd'hui garanti jusqu'en 2028 ; le Fairphone 5 (2023) vise d'emblée 8 à 10 ans de mises à jour de sécurité. Quelques années plus tard, Google (Pixel 8, octobre 2023) et Samsung (Galaxy S24, janvier 2024) ont chacun porté leur propre engagement standard de 5 à **7 ans** de mises à jour. La chronologie suggère que Fairphone avait déjà normalisé ce niveau d'engagement avant que les deux plus gros acteurs du marché ne l'adoptent à leur tour — mais aucune source consultée n'établit de lien de cause à effet explicite entre les deux ; il s'agit d'une coïncidence de calendrier documentée, pas d'une influence directe confirmée.

{{% /tab %}}

{{< /tabs >}}
