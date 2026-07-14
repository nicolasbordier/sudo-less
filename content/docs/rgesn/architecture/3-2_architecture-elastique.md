---
weight: 200
title: "3.2 - Architecture élastique et adaptation des ressources"
description: "Critère 3.2 du RGESN : pourquoi et comment adapter dynamiquement les ressources serveurs à la consommation réelle du service, plutôt que surdimensionner l'infrastructure."
icon: "auto_graph"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique fonctionne-t-il sur une architecture pouvant adapter la quantité de ressources utilisées à la consommation du service ?

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
| **Critère**  | `3.2` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service ne repose pas sur des ressources serveurs` |
| **Métiers concernés** | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est d'éviter une architecture surdimensionnée et de privilégier une architecture capable d'ajuster dynamiquement la quantité de ressources utilisées en fonction de la demande du service, et passer à l'échelle. Cela contribue à optimiser l'efficacité énergétique et à éviter le gaspillage de ressources inutiles.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Dans un premier temps, évaluer finement le besoin, le nombre d'utilisateurs pour adapter les ressources informatiques nécessaires. Dans un second temps, s'assurer que l'architecture peut s'adapter de manière optimale afin que soient allouées les ressources informatiques strictement nécessaires pour répondre à la demande fluctuante du service.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le service numérique fonctionne sur une architecture qui peut adapter les ressources allouées à la demande. Afin de s'en assurer, plusieurs moyens de test peuvent être envisagés, par exemple :

- **Suivi de l'évolution du ratio entre ressources allouées et consommées** : construire un comparatif entre les ressources allouées et celles consommées sur une période de temps et corriger les défauts existants en termes d'adaptation. Des outils de surveillance des ressources peuvent aussi être mis en place pour collecter des données sur l'utilisation du processeur, de la mémoire, de la bande passante, etc.
- **Simulation de montées en charge** : vérifier si l'architecture est capable de détecter automatiquement l'augmentation de la demande et d'allouer dynamiquement les ressources nécessaires pour maintenir les performances. Des tests de montée en charge réelle en situation réelle sont également utiles.
- **Mécanismes d'auto-ajustement** : ces mécanismes se déclenchent automatiquement en fonction des conditions de charge (par exemple : utilisation de mécanismes d'auto-scaling pour créer dynamiquement des instances du service en fonction de la demande).

Démontrer dans la déclaration d'écoconception l'adaptation de la consommation en ressources de l'architecture en fonction des besoins du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Responsable IT`

Le critère 3.2 rejoint la [recommandation n°3 de la famille Hébergement](https://gr491.isit-europe.org/?famille=hebergement&num_reco=3) du [GR491](https://gr491.isit-europe.org/) (INR), « Adapter l'utilisation des équipements techniques aux besoins » — déjà citée aux pages [critère 2.7](../../specifications/2-7_maintenance-decommissionnement/) et [Outils > Run](../../../outils/par-phase-projet/run/). Ses critères sont directement transposables en tests pour ce critère : « Le provisionning/déprovisionning est-il dynamique en fonction de la charge ? », « Le nombre de cœurs attribués est-il fonction de l'usage réel ? », « Les cœurs inutilisés sont-ils désactivés ? », « La taille du parc physique est-elle en adéquation avec le volume de machines virtuelles à exécuter ? »

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Administrateur Systèmes`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a trois fiches qui couvrent chacune une facette différente du critère 3.2 :

- [**RWEB 0027 — « Mettre en place une architecture élastique »**](https://rweb.greenit.fr/fr/fiches/RWEB_0027-mettre-en-place-une-architecture-elastique) : correspond au critère quasiment à l'identique. La fiche prévient toutefois que l'élasticité a un coût de mise en œuvre (charge de travail, complexité accrue) et n'est pas indispensable pour une application à charge faible ou stable — exemple donné : redimensionner automatiquement selon une programmation horaire (extinction nocturne) ou selon le nombre de requêtes.
- [**RWEB 0091 — « Adapter la qualité de service et le niveau de disponibilité »**](https://rweb.greenit.fr/fr/fiches/RWEB_0091-adapter-la-qualite-de-service-et-le-niveau-de-disponibilite) : à efficience énergétique équivalente, un centre de données plus disponible a une empreinte environnementale plus élevée (redondance des chaînes d'alimentation et de froid). La fiche cite les géants du Web, qui n'utilisent pas de disponibilité Tier IV partout — un temps de bascule de quelques secondes en cas de panne serveur reste acceptable pour l'utilisateur final.
- [**RWEB 0092 — « Utiliser des serveurs virtualisés »**](https://rweb.greenit.fr/fr/fiches/RWEB_0092-utiliser-des-serveurs-virtualises) : la virtualisation ([VMware](https://www.vmware.com/), [Xen](https://xenproject.org/), [KVM](https://www.linux-kvm.org/)) et la conteneurisation ([Docker](https://www.docker.com/), [Kubernetes](https://kubernetes.io/)) permettent de mutualiser des ressources sous-utilisées — exemple donné : remplacer quatre serveurs dédiés chargés à 20 % chacun par un seul hyperviseur rendant le même service.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont une recommandation qui correspond littéralement au « Moyen de test » du critère, dans la fiche [**« Use automation wisely »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-automation-wisely) : « Use autoscaling to adjust server capacity based on demand. Implement buffering and throttling to manage load pressures. Scale resources up during high demand and scale down when demand drops to avoid overprovisioning. »

Une seconde recommandation, [**« Avoid maintaining unnecessary virtualized environments or containers »**](https://www.w3.org/TR/web-sustainability-guidelines/#avoid-maintaining-unnecessary-virtualized-environments-or-containers), recoupe la fiche RWEB 0092 ci-contre : désactiver ou retirer les environnements virtualisés (conteneurs, VM) redondants ou inutilisés, sans dégrader les garanties de sécurité, d'isolation ou de conformité requises.

{{% /tab %}}

{{% tab tabName="Outils" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Pour implémenter concrètement l'auto-scaling évoqué dans le « Moyen de test » du critère :

- Sur Kubernetes, le [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (natif) ajuste le nombre de pods selon des métriques comme le CPU ou la mémoire. [KEDA](https://keda.sh/) (CNCF, open source) va plus loin en permettant le **scale-to-zero** : un service sans trafic peut descendre à zéro replica et ne consommer aucune ressource, puis redémarrer automatiquement au premier événement — l'équivalent automatisé de « l'extinction nocturne » citée dans la fiche RWEB 0027.
- Les groupes d'auto-scaling natifs des fournisseurs cloud ([AWS Auto Scaling](https://aws.amazon.com/autoscaling/), équivalents chez GCP et Azure) permettent la même logique hors contexte Kubernetes.
- Le **serverless** (AWS Lambda, Google Cloud Functions, Cloudflare Workers…) pousse cette logique à son terme : aucune ressource n'est allouée entre deux invocations, la facturation se fait à l'exécution. C'est la forme la plus aboutie du « provisionning/déprovisionning dynamique » demandé par le GR491 ci-contre. Le principal bémol documenté par la recherche est le **cold start** : la création d'une nouvelle instance après une période d'inactivité ajoute de la latence et une consommation de ressources qui peut partiellement compenser le gain lié à l'absence de ressources allouées à vide — un point à vérifier avant de généraliser le serverless à tous les usages, en particulier ceux à fréquence d'appel faible mais régulière.
- Les **services managés** des fournisseurs cloud (bases de données managées type RDS, Kubernetes managé…) reposent en interne sur une mutualisation à grande échelle entre de nombreux clients — le même principe que la virtualisation de la fiche RWEB 0092 ci-contre, mais opéré par le fournisseur plutôt que par l'équipe projet. Un service managé est donc structurellement plus proche de la logique de ce critère qu'un déploiement entièrement custom sur des instances dédiées, à fonctionnalité équivalente.

Pour vérifier après coup que ces mécanismes fonctionnent réellement (plutôt que de les supposer actifs), voir les outils de suivi continu déjà cités en page [Outils > Run](../../../outils/par-phase-projet/run/) (Kepler, Scaphandre, tableaux de bord natifs cloud) : c'est la confrontation entre ressources allouées et ressources réellement consommées, dans la durée, qui objective le « Suivi de l'évolution du ratio » demandé par le critère.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, avec une justification concise mais révélatrice : « L'hébergement est assuré par le Ministère via l'offre ECO en mode Legacy à base de machine virtuelle, sans élasticité. »

Ce cas illustre une situation fréquente dans les organisations publiques : l'hébergement dépend d'une offre interne mutualisée (ici « ECO » côté ministériel), sur laquelle l'équipe projet n'a pas nécessairement la main pour activer un mécanisme d'élasticité — la non-conformité relève alors autant d'une décision d'infrastructure organisationnelle que d'un choix technique de l'équipe produit.

À l'inverse, un [audit d'écoconception mené par OCTO Technology sur l'outil C'Bilan (ICDC Informatique)](https://blog.octo.com/compte-rendu-comptoir-qu%27apporte-l%27analyse-de-cycle-de-vie-lors-d%27un-audit-d%27eco-conception-de-service-numerique), documenté via une analyse de cycle de vie (ACV) complète, chiffre précisément l'intérêt de la mutualisation. Trois scénarios cumulatifs ont été comparés : l'optimisation des conteneurs (suppression des réplicas superflus sur un service jugé non critique, vCPU 10,4 → 5,6, **-20 % d'impacts**), le passage en « Prod Only » (suppression des environnements de pré-production, vCPU 10,4 → 1,4, **-35 % d'impacts**), et enfin la **mutualisation de la base de données avec 4 autres services** (**-80 % d'impacts**) : le serveur de base de données dédié à C'Bilan restait allumé en permanence pour un usage ponctuel et peu de sollicitations. C'est ce dernier scénario — le plus proche de ce que demande le critère 3.2 — qui obtient de très loin le plus fort levier de réduction des trois.

[Alt Impact](https://altimpact.fr/ecoconception-du-site/) (site porté par l'ADEME, audit Conserto) documente un cas intermédiaire, entre l'absence totale d'élasticité de FACE et l'auto-scaling complet : « l'architecture du service numérique n'est pas en capacité de faire correspondre la quantité de ressources utilisée et la consommation effective de ces ressources de façon automatique, mais l'hébergeur [Datacampus] est en capacité de le faire de façon manuelle après validation », grâce à un monitoring de fréquentation qui permet de faire évoluer au jour le jour la configuration serveur. Ce n'est pas une élasticité automatique au sens strict du critère, mais un mécanisme d'ajustement manuel piloté par la donnée réelle plutôt qu'un dimensionnement figé à la conception.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent ce critère **« Non applicable »**, avec une justification assumée plutôt que subie : « nous n'utilisons pas de solution Docker ou Kubernetes, notre configuration serveur est suffisante pour gérer un flux moyen d'utilisateur [...] nous adaptons le service au fur et à mesure des années en fonction de la demande. » Pour un média associatif à trafic stable et croissance progressive, une architecture élastique serait une complexité disproportionnée par rapport au besoin réel — un rappel utile que ce critère n'impose pas l'élasticité en toute circonstance, seulement lorsque la variation de charge la justifie.

{{% /tab %}}

{{< /tabs >}}
