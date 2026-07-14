---
weight: 700
title: "2.7 - Maintenance et décommissionnement"
description: "Critère 2.7 du RGESN : pourquoi et comment prévoir une stratégie de maintenance et de décommissionnement des environnements techniques inutilisés."
icon: "delete_sweep"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il prévu une stratégie de maintenance et de décommissionnement ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Spécifications` |
| **Critère**  | `2.7` |
| **Phase** | `Fin de vie` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable IT` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Mettre au rebut les **environnements techniques encore actifs mais qui ne sont plus utilisés** : production, QA (Quality Assurance), test, environnement de développement, sauvegarde, etc. Ces environnements peuvent occuper de la **ressource informatique inutilement**.

Il s'agit également de prévoir la **possible fin de vie** de tout ou partie du service.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir et mettre à jour régulièrement une **stratégie de maintenance et décommissionnement** des environnements et des dates de rappel.

Plus largement, en cas de non-utilisation ou de baisse importante d'utilisation, s'interroger sur l'**opportunité d'arrêter des parties du service** (ou tout le service) afin de diminuer les impacts de ce dernier, en prenant en compte les **équipements sous-jacents à réaffecter** pour prolonger leur durée de vie.

En cas de décommissionnement, il conviendra de :

- Donner une **nouvelle vie** au matériel et aux ressources libérées (réutilisation, reconditionnement, recyclage…) ;
- Anticiper l'avenir des **données non personnelles collectées**, pour prévoir par exemple leur suppression ou leur mise en **open data** ;
- Prévoir, en cas de fin de vie d'un service propriétaire, une **publication en open source** du code source du service.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Lister les **fonctionnalités, composants et environnements actifs**, en précisant leur état d'utilisation.

Le critère est **validé** si une stratégie de maintenance et de décommissionnement est définie pour le service, incluant :

- des **dates de rappel** pour les éléments non utilisés ;
- les **actions prévues** pour optimiser la seconde vie ou fin de vie des ressources libérées en cas de décommissionnement.

Les résultats doivent être documentés dans la **déclaration d'écoconception**. En cas de fin de vie de tout ou partie du service, la gestion des données non personnelles et des équipements utilisés devra être planifiée, de manière à diminuer les impacts environnementaux associés.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Logiciel`

Le critère 2.7 rejoint la [recommandation n°3 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Adapter l'utilisation des équipements techniques aux besoins » — déjà citée en page [Outils > Run](../../../outils/par-phase-projet/run/) : les serveurs et routeurs sont-ils éteints quand ils sont inutilisés ? Le provisionning et le déprovisionning sont-ils dynamiques en fonction de la charge ? La taille du parc physique reste-t-elle en adéquation avec le volume de machines virtuelles réellement utilisées ?

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Logiciel`, `Porteur de projet`

Depuis sa 5ème édition (2025), le [référentiel RWEB du Collectif GreenIT](https://rweb.greenit.fr/) publie une correspondance officielle avec les critères RGESN. La fiche [**RWEB 0115 — « Mettre en place un plan de fin de vie du site »**](https://rweb.greenit.fr/fr/fiches/RWEB_0115-mettre-en-place-un-plan-de-fin-de-vie-du-site) y est explicitement rattachée au critère **2.7** (et au 5.8).

Elle part du même constat que la fiche RGESN — « la plupart du temps, la fin de vie d'un service numérique n'est pas anticipée » — mais détaille une checklist plus opérationnelle des ressources à couvrir dans le plan de décommissionnement : serveurs, stockage, middlewares, configurations, **code source**, documentations, et surtout les éléments souvent oubliés de la vie de développement — canaux de messagerie, jobs d'intégration continue, environnements de test.

Elle illustre aussi la démarche par un exemple concret (fin de vie d'un site vitrine d'exposition : bases de données, serveurs d'applications, redirections d'URL, documentations, fichiers multimédias) et recommande d'assigner un **porteur d'action et une date** à chaque élément du plan, pour transformer la stratégie en tâches réellement suivies.

{{% /tab %}}

{{% tab tabName="Fin de vie du code et des données" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable IT`

Le texte du critère recommande explicitement, en cas de fin de vie d'un service propriétaire, une **publication en open source** du code source — rejoignant directement le [critère 1.8](../../strategie/1-8_efforts-open-source/) et le [guide des licences libres](https://code.gouv.fr/fr/doc/licences-libres-dinum/) de la DINUM déjà cité sur ce site : publier le code **avant** l'arrêt d'un service est la seule mesure qui donne une chance réelle à une communauté de le reprendre ([critère 1.8](../../strategie/1-8_efforts-open-source/), retours d'expérience Murena/ATF/Ordi3.0).

Pour les données non personnelles, la mise en **open data** rejoint la logique de collecte raisonnée du [critère 1.6](../../strategie/1-6_collecte-donnees/) : une donnée qui ne sert plus au service peut encore avoir de la valeur pour d'autres, à condition d'anticiper cette seconde vie avant la suppression pure et simple.

{{% /tab %}}

{{% tab tabName="FinOps / GreenOps" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Logiciel`

Côté suivi des environnements eux-mêmes, les outils de supervision continue déjà cités en page [Outils > Run](../../../outils/par-phase-projet/run/) (Kepler, Cloud Carbon Footprint, tableaux de bord natifs des fournisseurs cloud) permettent d'identifier concrètement les environnements à faible taux d'utilisation, candidats à un décommissionnement — une logique **GreenOps**, centrée sur le suivi continu de l'empreinte carbone plutôt que sur le coût.

Une démarche **FinOps** aide aussi à repérer ces ressources dormantes, à la source : sur AWS, [Trusted Advisor](https://aws.amazon.com/trustedadvisor/) et [Compute Optimizer](https://aws.amazon.com/compute-optimizer/) identifient les ressources sous-utilisées ou surdimensionnées (ex. instance EC2 dont la charge reste faible depuis plusieurs semaines) et peuvent déclencher une notification — une manière concrète de faire remonter des candidats au décommissionnement sans attendre une revue manuelle. La [FinOps Foundation](https://www.finops.org/) documente cette pratique plus largement, au-delà du seul fournisseur AWS.

FinOps (signal coût) et GreenOps (signal carbone) convergent souvent sur les mêmes ressources : une instance surdimensionnée coûte cher **et** consomme plus qu'il ne faudrait — deux raisons indépendantes d'en faire un candidat au décommissionnement.

{{% /tab %}}

{{% tab tabName="Cartographie des dépendances" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable IT`

Pour identifier un service candidat à la fin de vie — et surtout décommissionner sans casser un autre service qui en dépend encore — la question clé est de savoir **qui appelle quoi**. Trois approches, avec un ordre de préférence :

- **Excel ou Draw.io** : suffisant pour un inventaire ponctuel ou une petite organisation, mais ce sont des documents **statiques** qui se maintiennent manuellement — ils se périment dès la première dépendance non documentée ou le premier changement non reporté, ce qui est risqué au moment précis où l'on s'appuie dessus pour décommissionner.
- **CMDB** (Configuration Management Database) : solution plus robuste pour cartographier les dépendances entre services dans la durée. [GLPI](https://www.glpi-project.org/) ou [iTop](https://www.itophub.io/) (tous deux open source) permettent de déclarer les composants et leurs relations — à condition que l'inventaire soit tenu à jour, ce qui reste une démarche déclarative.
- **Cartographie automatique par la donnée réelle** : plutôt que de documenter les dépendances a priori, un outil de traçage distribué comme [OpenTelemetry](https://opentelemetry.io/) couplé à [Grafana Tempo](https://grafana.com/oss/tempo/) (ou Jaeger) observe les appels **réellement effectués** entre services en production. Cette approche détecte aussi les dépendances non documentées — souvent la vraie cause d'un décommissionnement qui casse un service tiers oublié.

Un [service catalog](https://backstage.io/) comme Backstage (CNCF, open source) combine les deux logiques : registre déclaratif des services et de leurs propriétaires, enrichi par les données de traçage réelles quand elles sont disponibles.

Ce signal de dépendance se combine avec le suivi FinOps / GreenOps (voir onglet précédent) : une ressource sous-utilisée **et** sans appelant entrant identifié sont deux indices indépendants qui, ensemble, renforcent la confiance dans un candidat au décommissionnement.

{{% /tab %}}

{{% tab tabName="Seconde vie" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Logiciel`

Pour la seconde vie du **matériel** libéré par un décommissionnement (réutilisation, reconditionnement, recyclage), voir la page [Outils > Fin de vie](../../../outils/par-phase-projet/fin-de-vie/) — réseau [Ordi3.0](http://www.ordi3-0.fr/), OS mobile open source, guide des licences libres.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, avec une justification là aussi réduite à une phrase : « Aucune stratégie identifiée à ce jour. » — un constat qui, mis bout à bout avec le [critère 2.6](../2-6_revue-conception-code/) également non validé sur ce même service, illustre que les efforts d'écoconception se concentrent souvent sur la conception et le développement, plus rarement sur l'anticipation de la fin de vie.

À l'inverse, [SNE — Système national d'enregistrement des demandes de logement social](https://ecoresponsable.numerique.gouv.fr/ressources/documents-reference/referentiel-general-ecoconception/retour-experience/), déjà cité au [critère 1.1](../../strategie/1-1_evaluation-utilite/), documente un cas concret de décommissionnement réussi : dans le cadre d'une expérimentation du RGESN accompagnée par l'INR, un **module dont l'usage avait été détourné** de sa finalité initiale a été purement et simplement décommissionné plutôt que maintenu par défaut.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent ce critère « Validé » avec un plan de décommissionnement volontairement simple, proportionné à la taille du service : « il suffit de passer le projet sur GitHub en Open Source, et d'arrêter le seul serveur de production. » Côté maintenance courante, le service dispose d'un système de redémarrage automatique et de signalement en cas d'indisponibilité, complété par l'hébergeur [Ikoula](https://www.ikoula.com/), qui assure une surveillance régulière des VPS via des agents [Zabbix](https://www.zabbix.com/).

{{% /tab %}}

{{< /tabs >}}
