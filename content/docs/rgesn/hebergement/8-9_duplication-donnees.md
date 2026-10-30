---
weight: 900
title: "8.9 - Duplication des données selon le besoin"
description: "Critère 8.9 du RGESN : fixer un niveau de service (SLA, RPO, RTO) par fonctionnalité, choisir la stratégie de reprise la plus légère qui le respecte, ne dupliquer que les données critiques et sauvegarder de façon incrémentale."
icon: "content_copy"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique duplique-t-il les données uniquement lorsque cela est nécessaire ?

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
| **Critère**  | `8.9` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'utilise pas d'hébergement` |
| **Métiers concernés** | `Responsable de l'hébergement` `Ingénieur en stockage de données` `Responsable de la sécurité informatique` `Architecte/Ingénieur Systèmes` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.9/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire les ressources informatiques et les ressources de stockage utilisées.

Il s'agit de se poser la question du bon niveau de service sélectionné par rapport au besoin. Plus le taux de disponibilité demandé est haut, plus cela mobilise une infrastructure financièrement et environnementalement coûteuse.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Ne pas systématiquement dupliquer toutes les données mais identifier les données nécessaires à être dupliquées (données critiques ou données très sollicitées par exemple). Un équilibre est à trouver entre sécurisation (pour éviter les pertes de données) et dissémination (en avoir trop partout).

Se questionner sur la pertinence de la redondance du service, pour en établir le bon dosage. Est-ce critique si l'une des fonctionnalités du service n'est pas disponible pendant un certain temps ?

- Le Backup & Restore est ce qu'il y a de moins cher, parfaitement adapté aux applications qui ont un RTO (Recovery Time Objective) ou RPO (Recovery Point Objective) de quelques heures.
- Le Pilot Light, à savoir par exemple une base de données « mirrorée » / dupliquée mais avec des machines virtuelles éteintes. Procédé un peu plus cher qu'un Backup & Restore, il fonctionne pour la plupart des applications qui n'ont pas d'exigences SLA (Service Level Agreement) extrêmes (inférieures à 1 heure).
- Le Warm Standby, lorsque les VMs tournent déjà mais dans une scalabilité limitée, presque en temps réel mais potentiellement en qualité légèrement dégradée s'il y a un incident.
- Le Hot Standby multisite : résilience totale pour des SLAs (Service Level Agreements) temps réel. Aucune perte de service n'est tolérée, mais cela a nécessairement un coût.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, vérifier la présence d'un SLA (Service Level Agreement) ajusté selon les besoins.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Architecte/Ingénieur Systèmes`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache au 8.9 la fiche [**RWEB 0091 — « Adapter la qualité de service et le niveau de disponibilité »**](https://rweb.greenit.fr/fr/fiches/RWEB_0091-adapter-la-qualite-de-service-et-le-niveau-de-disponibilite), également liée aux critères [3.1](../../architecture/3-1_architecture-composants/) et [3.2](../../architecture/3-2_architecture-elastique/). Elle juge inutile de « répliquer la base de données en continu sur plusieurs centres de données », surtout si les utilisateurs acceptent une disponibilité de 99 % ou moins pour un service non critique.

Elle rappelle pourquoi : plus un centre de données est disponible, plus son empreinte est élevée, car « tout est redondé et actif », alimentation comme refroidissement. Son principe de validation : **aucune** hausse du niveau de disponibilité quand le niveau actuel suffit.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Ingénieur en stockage de données`, `Responsable de la sécurité informatique`

La [recommandation n°3 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR) contient deux critères en priorité **High** :

- [« La haute disponibilité est-elle conçue de manière modulaire ? »](https://gr491.isit-europe.org/crit.php?id=3-hebergement-les-besoins-de-securisation-sont-differents-en-dd75bb), avec le test : « Le besoin de sécurisation est-il défini pour chaque fonction ? » La même « règle générique d'excellence » n'est pas toujours nécessaire ;
- [« Le système de sauvegarde est-il incrémentiel ? »](https://gr491.isit-europe.org/crit.php?id=3-hebergement-la-securite-est-un-des-points-cle-ca3cd7), avec le test : « Quel est le volume des sauvegardes quotidiennes ? » Les données non modifiées « n'ont pas de raison d'encombrer inutilement des espaces de sauvegarde ».

Un conseil de la recommandation n°6 tire en sens inverse : disposer de [plusieurs centres de données distants de plus de 100 km](https://gr491.isit-europe.org/crit.php?id=6-hebergement-les-impacts-des-cataclysmes-naturels-ou-industriels-c39f4c). Le 8.9 demande de réserver ce niveau aux fonctions qui l'exigent.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Ingénieur en stockage de données`, `Responsable de la sécurité informatique`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) traitent les sauvegardes dans la fiche [**« Back up critical data at routine intervals »**](https://www.w3.org/TR/web-sustainability-guidelines/#back-up-critical-data-at-routine-intervals). Son critère « Data backups » demande des sauvegardes « secure and incremental », à l'accès limité, et des mécanismes qui évitent de conserver longtemps des informations permettant d'identifier les utilisateurs.

{{% /tab %}}

{{% tab tabName="Choisir le niveau de service" %}}

Profil(s) métier concerné(s) : `Responsable de l'hébergement`, `Architecte/Ingénieur Systèmes`

Trois grandeurs définissent le niveau de service :

- la **disponibilité** (SLA) : la part du temps où le service fonctionne ;
- le **RPO** (*Recovery Point Objective*) : la quantité de données qu'on accepte de perdre, exprimée en temps ;
- le **RTO** (*Recovery Time Objective*) : la durée d'interruption acceptable.

Chaque « 9 » de disponibilité divise par dix l'interruption admise :

| Disponibilité | Interruption admise par an |
|---|---:|
| 99 % | 3,65 jours |
| 99,9 % | 8,8 heures |
| 99,99 % | 53 minutes |

Les quatre stratégies du RGESN se rangent selon ces objectifs, et selon ce qu'elles font tourner en permanence :

| Stratégie | RTO typique | Ce qui tourne en permanence |
|---|---|---|
| Sauvegarde et restauration | Quelques heures | La production seule, plus le stockage des sauvegardes |
| Pilot Light | Moins d'une heure | Une copie de la base, sans serveurs d'application |
| Warm Standby | Quelques minutes | Une seconde production, réduite |
| Hot Standby multisite | Aucune interruption | Deux productions complètes |

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Architecte/Ingénieur Systèmes`, `Ingénieur en stockage de données`

**1. Fixer le niveau de service par fonctionnalité**, avec les métiers, comme le demande le GR491. Par exemple, à adapter :

| Fonctionnalité | Disponibilité | RPO | RTO | Stratégie |
|---|---|---|---|---|
| Consultation publique | 99,5 % | 24 h | 4 h | Sauvegarde et restauration |
| Saisie des dossiers | 99,9 % | 1 h | 1 h | Pilot Light |
| Paiement, urgence | 99,99 % | Aucune perte | Quelques minutes | Warm ou Hot Standby |

**2. Ne dupliquer que ce qui le justifie.** Les caches, les miniatures et les exports peuvent être recalculés : ils n'ont besoin ni de réplication ni de sauvegarde.

**3. Sauvegarder de façon incrémentale**, avec déduplication et une durée de conservation. Avec restic, par exemple :

```sh
restic backup /srv/donnees
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune
```

Seuls les blocs modifiés sont envoyés à chaque sauvegarde. La seconde commande garde 7 sauvegardes quotidiennes, 4 hebdomadaires et 12 mensuelles, et libère le reste.

**4. Tester la restauration** au moins une fois par an, et mesurer le RTO réel. Un objectif jamais testé n'est pas un niveau de service.

**5. Documenter le SLA** dans la déclaration d'écoconception, comme l'exige le moyen de test : le tableau de l'étape 1, la stratégie retenue et la date du dernier test de restauration.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte/Ingénieur Systèmes`

- le [critère 3.2](../../architecture/3-2_architecture-elastique/) (architecture élastique) : une seconde production réduite peut grandir au besoin ;
- le [critère 8.8](../8-8_donnees-chaudes-froides/) (données chaudes et froides) : les sauvegardes anciennes vont sur un stockage froid ;
- le [critère 7.2](../../backend/7-2_durees-conservation/) (durées de conservation) : une donnée supprimée subsiste dans les sauvegardes jusqu'à leur expiration ;
- le [critère 7.1](../../backend/7-1_cache-serveur/) (cache serveur) : un cache se reconstruit, il ne se sauvegarde pas.

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
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | Données dupliquées en temps réel sur deux serveurs physiques, bascule en 5 minutes |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | **Non validé** | « Les données sont redondées selon les critères de l'hébergeur, mais aucun ajustement n'a été identifié pour ce produit numérique. » |

**FACE** identifie précisément le manque : la redondance est celle que l'hébergeur applique à tous, pas un niveau choisi pour le service. Le critère est donc non validé.

**Le Musée d'arts de Nantes** décrit un niveau élevé : une duplication « en temps réel sur 2 serveurs physique », avec une bascule automatique en 5 minutes au plus : c'est proche d'un Warm Standby. Pour le site d'un musée, une interruption de quelques heures serait sans doute acceptable, et une sauvegarde avec restauration suffirait. Le moyen de test demande un SLA « ajusté selon les besoins » : il manque l'analyse qui justifie ce niveau.

**DiaLog** n'évalue pas le critère. Sa déclaration n'indique ni sa disponibilité visée ni sa stratégie de sauvegarde.

{{% /tab %}}

{{< /tabs >}}
