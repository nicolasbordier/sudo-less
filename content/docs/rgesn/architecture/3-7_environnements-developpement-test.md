---
weight: 700
title: "3.7 - Optimisation des environnements de développement, préproduction et test"
description: "Critère 3.7 du RGESN : pourquoi et comment optimiser la sollicitation des environnements de développement, de préproduction ou de test en fonction des besoins réels (mutualisation, extinction automatique)."
icon: "bedtime"
date: "2026-07-15T00:00:00+01:00"
lastmod: "2026-07-15T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique optimise-t-il la sollicitation des environnements de développement, de préproduction ou de test en fonction de ses besoins ?

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
| **Critère**  | `3.7` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur l'utilisation de serveur` |
| **Métiers concernés** | `Architecte Système` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Faire fonctionner des serveurs ou machines virtuelles inutilisés consomme des ressources. Ce critère vise à limiter cette perte en optimisant l'utilisation des environnements de développement, de préproduction ou de test grâce à la mutualisation ou l'extinction de leur fonctionnement sur les plages horaires où ils sont inutilisés.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

S'appuyer sur des environnements de développement, de préproduction ou de test mutualisés (par exemple : une machine virtuelle).
Si cela n'est pas possible, désactivez-ces environnements sur les plages horaires où ils sont inutilisés (par exemple la nuit). La remise en service de ces environnements peut se faire automatiquement à une heure donnée, via un signal permettant de savoir qu'ils pourraient être prochainement utilisés, ou manuellement.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service s'appuie sur des environnements de développement / préproduction / tests mutualisés, ou bien si ces environnements sont désactivés sur les plages horaires où ils sont inutilisés. Indiquer dans la déclaration d'écoconception du service numérique les choix réalisés pour limiter les ressources utilisées par les environnements de développement, de préproduction ou de test.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Contrairement aux critères précédents de cette même fiche, celui-ci trouve une correspondance directe et explicite dans le [GR491](https://gr491.isit-europe.org/) de l'Institut du Numérique Responsable : la [recommandation n°2](https://gr491.isit-europe.org/crit.php?id=2-6008-architecture-en-dehors-de-la-production-qui-peut) (famille Architecture), classée **« recommandation incontournable »**, pose exactement la même question : « Est-ce que les environnements autres que production (DEV, QA, ...) sont éteints ou décommissionnés en dehors des plages d'usage ? ». Sa justification rejoint mot pour mot celle du RGESN : « Lorsque les environnements ne sont pas utilisés, ils ne doivent pas être actifs afin de réduire les consommations énergétiques. »

Le GR491 appuie cette recommandation sur un chiffre concret : une étude de 2015 menée par [Anthesis Group et le chercheur Jonathan Koomey (Stanford)](https://www.anthesisgroup.com/report-zombie-and-comatose-servers-redux-jon-taylor-and-jonathan-koomey/) a établi qu'environ **30 % des serveurs physiques dans le monde étaient « comateux »** — c'est-à-dire qu'ils n'avaient fourni aucun service informatique depuis six mois ou plus — soit environ 10 millions de serveurs, représentant plus de 30 milliards de dollars de capital immobilisé pour rien. Si l'étude porte sur des serveurs de production oubliés plutôt que sur des environnements de test au sens strict, l'ordre de grandeur illustre bien l'ampleur du gaspillage que ce critère cherche à éviter.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Architecte Logiciel`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) recoupent elles aussi directement ce critère, à travers deux fiches distinctes :

- [**« Avoid maintaining unnecessary virtualized environments or containers »**](https://www.w3.org/TR/web-sustainability-guidelines/#avoid-maintaining-unnecessary-virtualized-environments-or-containers) : « Reduce the number of active environments by deactivating, offlining, or removing unused or redundant virtual and physical environments (e.g., containers and virtual machines) wherever this can be done without reducing required security, isolation, or compliance guarantees. […] Similarly, codebases and setups for unused branches, environments, and services, and remove what is no longer needed. »
- [**« Use automation wisely »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-automation-wisely), qui recommande notamment : « Use autoscaling to adjust server capacity based on demand. […] Scale resources up during high demand and scale down when demand drops to avoid overprovisioning. »

La première fiche correspond au volet « extinction » du critère RGESN (y compris son extension naturelle aux branches et environnements applicatifs abandonnés, pas seulement aux machines), la seconde à l'automatisation de la remise en service évoquée dans la « Mise en œuvre ».

{{% /tab %}}

{{% tab tabName="Extinction planifiée : outillage cloud et virtualisation" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Architecte Logiciel`

Pour la partie « désactivez ces environnements sur les plages horaires où ils sont inutilisés » et sa remise en service automatique, chaque plateforme propose un outillage prêt à l'emploi plutôt que de scripter un mécanisme sur mesure :

- **AWS** — [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html) est une solution officielle (basée sur EventBridge, Lambda et des tags de ressources) qui arrête et redémarre automatiquement des instances EC2 et RDS selon un planning défini par équipe ou par environnement. Limiter des environnements non-production à des horaires de bureau (passer de 168 h à environ 50 h par semaine) permet, selon la documentation, jusqu'à **70 % d'économie** sur ces instances.
- **Azure** — [DevTest Labs](https://learn.microsoft.com/en-us/azure/devtest-labs/devtest-lab-auto-shutdown) intègre nativement des politiques d'[**auto-shutdown**](https://learn.microsoft.com/en-us/azure/devtest-labs/devtest-lab-auto-shutdown) et d'[**auto-start**](https://learn.microsoft.com/en-us/azure/devtest-labs/devtest-lab-auto-startup-vm) appliquées à l'ensemble des VM d'un labo, avec la possibilité de personnaliser l'horaire par machine.
- **Kubernetes** — pour des environnements de test conteneurisés, [KEDA](https://keda.sh/) permet de définir un `ScaledObject` avec un déclencheur `cron` et `minReplicaCount: 0`, ramenant à zéro réplique un déploiement en dehors des horaires ouvrés puis le remontant automatiquement au moment défini — l'équivalent, pour des workloads Kubernetes, du signal de remise en service mentionné par la « Mise en œuvre » du critère. Dans le même esprit mais bâti spécifiquement pour cet usage plutôt que détourné d'un mécanisme d'autoscaling générique, [**DailyClean**](https://github.com/AxaFrance/dailyclean) (AXA France, licence MIT) éteint et rallume des pods, Deployments ou StatefulSets Kubernetes selon une planification par CronJob, avec une interface dédiée permettant aussi une remise en service manuelle — le projet revendique explicitement sa vocation environnementale (« Save the planet by auto turn off your pods on kubernetes »).
- **Datacenter privé / virtualisation VMware** — pour les environnements hébergés sur un vSphere on-premises (fréquent dans les grandes organisations françaises soumises à des contraintes de résidence des données), [**VMware Aria Operations**](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations.html) (anciennement vRealize Operations Manager, vROPS) propose un tableau de bord prédéfini dédié, [**« Environmental Impact of Idle VMs »**](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations/8-16/vmware-aria-operations-configuration-guide-8-16/predefined-dashboards-in-vrealize-operations-manager/sustainability-dashboards/environmental-impact-of-idle-vms-dashboard.html), qui traduit directement les VM inactives détectées en impact environnemental chiffré (énergie gaspillée en Wh, émissions de CO2 en kg, nombre d'arbres nécessaires pour compenser) et recommande de les éteindre ou de les supprimer. Contrairement aux outils précédents, il ne s'agit pas d'un ordonnanceur qui coupe automatiquement à heure fixe, mais d'un outil de détection qui identifie les environnements de dev/préproduction/test laissés actifs sans usage réel, à charge ensuite pour l'équipe de les éteindre (manuellement ou via un script d'automatisation vSphere).

{{% /tab %}}

{{% tab tabName="Mutualisation : environnements à la demande" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Le critère cite aussi la mutualisation comme alternative à l'extinction programmée. Une déclinaison moderne de cette mutualisation consiste à ne plus maintenir des environnements de préproduction permanents du tout, mais à en générer un **à la demande**, pour la durée exacte du besoin : les [Review Apps de GitLab](https://docs.gitlab.com/ci/review_apps/) déploient automatiquement un environnement éphémère pour chaque merge request, puis l'arrêtent dès que la branche est fusionnée ou supprimée — ou après un délai défini via `auto_stop_in` (par exemple une semaine), afin d'éviter l'accumulation d'environnements de revue oubliés. Le même principe existe chez la plupart des plateformes de déploiement continu (Vercel, Netlify, Heroku Review Apps…) sous le nom d'« environnements de prévisualisation » ou « preview deployments ».

Cette approche répond aux deux volets du critère à la fois : elle mutualise l'infrastructure sous-jacente (un seul mécanisme de déploiement pour tous les environnements de revue) tout en garantissant qu'aucun environnement ne reste actif au-delà de son besoin réel, sans nécessiter de planning d'extinction manuel.

{{% /tab %}}

{{% tab tabName="Infrastructure as Code : environnements sur mesure" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Architecte Logiciel`

Les Review Apps ci-contre couvrent bien le cas d'un environnement de prévisualisation applicative lié à une PR, mais pas celui d'un environnement à la forme libre — un nombre de machines arbitraire, une topologie réseau spécifique — nécessaire ponctuellement, par exemple pour valider un correctif urgent en conditions proches de la production ou pour mener une campagne de test d'endurance. Décrire l'infrastructure en code avec [**Terraform**](https://www.hashicorp.com/en/products/terraform) ou [**Ansible**](https://docs.ansible.com/) rend justement cette infrastructure reproductible et jetable : `terraform apply` provisionne l'environnement exact requis pour le besoin, `terraform destroy` le supprime intégralement une fois l'objectif atteint — sans laisser de machines éteintes mais toujours allouées (stockage, IP, etc.), contrairement à une simple extinction planifiée.

- **Terraform** — HashiCorp a industrialisé ce principe sous forme de fonctionnalité managée avec les [**Ephemeral Workspaces**](https://www.infoq.com/news/2023/09/terraform-ephemeral-workspaces/) de Terraform Cloud (bêta publique depuis septembre 2023) : une date de désapprovisionnement est définie à la création du workspace, et Terraform exécute automatiquement un plan de destruction une fois cette date atteinte — sans intervention manuelle de nettoyage.
- **Ansible** — son approche agentless et push-based en fait un outil adapté à l'orchestration ponctuelle de bancs de test complets : [TestRail décrit ainsi](https://www.testrail.com/blog/ansible-ephemeral-testing/) le provisionnement, via Ansible, de « centaines de VM ou conteneurs représentant des milliers de microservices interdépendants » pour une campagne de test de performance, l'environnement étant simplement détruit une fois les objectifs de test atteints — évitant au passage d'avoir à restaurer manuellement des bases de données ou systèmes de fichiers, puisqu'il suffit de reprovisionner l'environnement à l'identique pour rejouer un test.

Les deux cas cités en exemple — validation d'un hotfix de production et campagne de test d'endurance — correspondent typiquement à des besoins ponctuels et non récurrents selon un horaire fixe, ce qui rend l'extinction planifiée (onglet précédent) moins adaptée que la création/destruction à la demande décrite ici.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Responsable RSE/Numérique soutenable`

Ce critère est le pendant, côté environnements non-production, du [critère 3.2](../3-2_architecture-elastique/) (architecture élastique et adaptation des ressources), déjà publié sur ce site : le 3.2 porte sur l'adaptation dynamique des ressources de **production** à la charge réelle du service, tandis que le 3.7 porte sur les environnements de **développement, préproduction et test**, dont l'usage est généralement discontinu (horaires de bureau, périodes de campagne de tests) et non corrélé à une charge utilisateur. Les deux critères partagent le même principe de fond — ne pas maintenir des ressources actives au-delà du besoin réel — mais s'appliquent à des couches différentes de l'infrastructure et avec des mécanismes techniques distincts (autoscaling piloté par la charge pour le 3.2, planification horaire ou événementielle pour le 3.7).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, avec une justification franche et sans ambiguïté : « Le service numérique utilise des environnements de développement, préproduction, et/ou tests, qui fonctionnent actuellement de manière continue. » Contrairement aux critères voisins 3.4, 3.5 et 3.6 de cette même déclaration — marqués « Non applicable » faute de mécanisme concerné — celui-ci s'applique pleinement à FACE et documente un axe d'amélioration identifié mais non encore traité : les environnements non-production tournent en continu, sans extinction ni mutualisation.

À l'opposé de ce constat, l'épisode 12 du talk-show [Instant Coding](https://www.youtube.com/watch?v=uEp7hPIRBC0), partage le retour d'expérience d'un site public (consultation de données pour des professionnels, sans transaction ni authentification) resté **8 mois sans aucun environnement de préproduction** entre les postes de développement et la production. L'argumentation détaillée mérite d'être citée : la détection d'erreur en quelques minutes (via un outil de suivi d'erreurs type Sentry) combinée à une correction systématique en moins d'une heure a été présentée au client comme garde-fou de substitution à un environnement de recette classique — un point du critère explicitement couvert par le « Moyen de test » ci-dessus, qui admet l'absence de mutualisation ou d'extinction dès lors que le besoin réel est démontré. Le consultant souligne aussi un effet secondaire recherché : sans environnement tampon, la responsabilité de la qualité (tests, relecture de code) retombe directement sur le développeur, chaque mise en production étant immédiatement visible plutôt que filtrée par une étape de recette. Ce choix n'excluait toutefois pas ponctuellement un environnement temporaire : les [Review Apps de Scalingo](https://doc.scalingo.com/platform/app/review-apps) étaient mobilisées quelques minutes ou heures pour sécuriser une opération jugée risquée (migration de base de données), avant d'être détruites — une illustration concrète de la mutualisation « à la demande » déjà décrite plus haut, plutôt qu'un environnement de test permanent.

{{% /tab %}}

{{< /tabs >}}
