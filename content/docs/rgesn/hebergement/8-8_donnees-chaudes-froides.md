---
weight: 800
title: "8.8 - Données chaudes et froides hébergées séparément"
description: "Critère 8.8 du RGESN : au-delà de 10 To, séparer les données utilisées des archives et sauvegardes, et placer ces dernières sur un stockage froid adapté à leur fréquence de consultation."
icon: "ac_unit"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique héberge-t-il de façon distincte les données « chaudes » et « froides » ?

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
| **Critère**  | `8.8` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique repose sur l'hébergement de moins de l'équivalent de 10 To de données` |
| **Métiers concernés** | `Responsable de l'hébergement` `Responsable RSE/Numérique soutenable` `Architecte de bases de données` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.8/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Les données « chaudes » sont des données utilisées alors que les données « froides » sont des données archivées. Utiliser des hébergements différents permettrait de réduire les impacts environnementaux.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Séparer les données chaudes des données « froides » en utilisant des solutions techniques adaptées au contexte d'utilisation. Il convient d'avoir une réflexion sur le mode de stockage des données « froides » : il existe plusieurs technologies sur le marché, toutes n'ont pas nécessairement le même impact.

Par exemple, les archives et les sauvegardes à conserver dans la durée peuvent être mises dans un stockage « froid ».

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la séparation des données « chaudes » et « froides » dans l'architecture du service numérique, par exemple en examinant la configuration des systèmes, en s'assurant qu'ils sont distincts pour les deux types de données.

Pour valider ce critère, s'assurer que des stratégies de stockage appropriées sont mises en place pour les données « froides », en prenant en compte leur empreinte environnementale.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Le [critère 7.2](../../backend/7-2_durees-conservation/) fixe **quand** une donnée devient froide, puis quand elle est supprimée. Le 8.8 porte sur **où** elle est stockée entre les deux.

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="GR491 et W3C" %}}

Profil(s) métier concerné(s) : `Architecte de bases de données`, `Responsable de l'hébergement`

Le [GR491](https://gr491.isit-europe.org/) (INR) pose la question dans la famille Backend, [« Est-ce que les données "vivantes" et "mortes" sont gérées de manière différentes ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-les-donnees-dhistoriques-doivent-etre-conservees-pour-8a647f), avec l'exemple d'un « stockage lent pour les données "mortes" ». Dans la famille Hébergement, [« Est-ce que les solutions de stockage permettent de réduire le nombre de composants ? »](https://gr491.isit-europe.org/crit.php?id=3-hebergement-la-densite-des-espaces-de-stockage-conditionne-a76903) (priorité **Medium**) propose un indicateur : le « ratio entre l'espace consommé et le volume de données ».

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) demandent, dans la fiche [**« Store data according to the needs of your users »**](https://www.w3.org/TR/web-sustainability-guidelines/#store-data-according-to-the-needs-of-your-users), d'adapter le stockage à la fréquence d'accès, en déplaçant les données peu consultées « to energy-efficient storage ».

{{% /tab %}}

{{% tab tabName="Quel stockage froid ?" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Architecte de bases de données`

Le RGESN demande de réfléchir au support, car « toutes n'ont pas nécessairement le même impact ». Les principaux, des plus chauds aux plus froids :

| Support | Usage | Au repos | Délai d'accès |
|---|---|---|---|
| SSD | Données actives, bases | Faible consommation | Immédiat |
| Disque dur | Données tièdes, sauvegardes récentes | Consomme tant qu'il tourne | Immédiat |
| Classe d'archivage d'un stockage objet | Archives, sauvegardes anciennes | Selon la technologie de l'hébergeur | De quelques minutes à quelques heures |
| Bande magnétique | Archives de long terme | Aucune consommation hors lecture | Plusieurs minutes, souvent des heures |

**La bonne question est la fréquence de consultation.** Une archive lue une fois par an n'a pas besoin d'un support immédiat, et une restauration de quelques heures lui convient. À l'inverse, des données lues chaque jour placées en archive coûtent des restaurations répétées.

**Le volume compte aussi.** Moins de copies et des sauvegardes incrémentales réduisent le stockage froid lui-même (voir le [critère 8.9](../8-9_duplication-donnees/)).

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Architecte de bases de données`, `Administrateur Système`

**1. Mesurer le volume** pour savoir si le critère s'applique : bases, fichiers déposés, sauvegardes et archives. En dessous de 10 To, il est non applicable.

**2. Classer les données par fréquence d'accès**, à partir des journaux ou des dates de dernière lecture : actives, consultées occasionnellement, archivées.

**3. Placer les fichiers froids dans une classe d'archivage.** Sur un stockage objet compatible S3, une règle de cycle de vie déplace les fichiers au bout d'un délai, puis les supprime. Un exemple complet figure à l'étape 3 du [critère 7.2](../../backend/7-2_durees-conservation/).

**4. Séparer aussi dans la base de données.** Avec PostgreSQL, les partitions anciennes d'une table horodatée (voir le [critère 5.8](../../contenus/5-8_archivage-suppression/)) peuvent passer sur des disques plus lents :

```sql
CREATE TABLESPACE froid LOCATION '/srv/disques-lents/postgresql';
ALTER TABLE journal_acces_2025_10 SET TABLESPACE froid;
```

Le déplacement bloque la partition pendant la copie : à planifier en dehors des heures d'usage.

**5. Sortir les sauvegardes de la production.** Les sauvegardes de plus de quelques semaines vont sur le support froid, les plus récentes restent accessibles pour une restauration rapide.

**6. Tester une restauration** depuis le stockage froid, pour connaître son délai réel.

**7. Documenter** dans la déclaration d'écoconception : le volume total, les classes de stockage utilisées et la règle de passage de l'une à l'autre.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte de bases de données`

- le [critère 7.2](../../backend/7-2_durees-conservation/) (durées de conservation) : fixe la date de passage au froid, puis la suppression ;
- le [critère 5.8](../../contenus/5-8_archivage-suppression/) (archivage des contenus) : la même démarche pour les contenus publiés ;
- le [critère 8.9](../8-9_duplication-donnees/) (duplication) : chaque copie supplémentaire s'ajoute au stockage, chaud ou froid.

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
| [DiaLog](https://dialog.beta.gouv.fr/) | Non évalué | — |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Validé | Site sur des serveurs LXC, sauvegardes sur un serveur de sauvegarde |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Non applicable | « Le service numérique repose sur l'hébergement de moins de l'équivalent de 10 To de données. » |

**FACE** applique la règle d'applicabilité comme prévu : sous 10 To, le critère ne s'applique pas.

**Le Musée d'arts de Nantes** valide le critère en séparant le site de ses sauvegardes. La déclaration ne donne pas le volume hébergé. Pour le site d'un musée, il est sans doute sous 10 To, ce qui rendrait le critère non applicable. S'il s'applique, un serveur de sauvegarde distinct sépare bien les données, mais le moyen de test demande aussi un stockage adapté à leur empreinte : le type de support reste à préciser.

**DiaLog** n'évalue pas le critère dans sa déclaration. Il faudrait au moins indiquer le volume, pour le déclarer non applicable s'il est sous 10 To.

{{% /tab %}}

{{< /tabs >}}
