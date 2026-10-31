---
weight: 800
title: "5.8 - Archivage et suppression des contenus obsolètes"
description: "Critère 5.8 du RGESN : fixer une durée de vie à chaque type de contenu, purger automatiquement ce qui expire, prévoir une revue manuelle, respecter le RGPD et le droit des archives publiques, et suivre l'occupation du stockage."
icon: "auto_delete"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il une stratégie d'archivage et de suppression, automatique ou manuelle, des contenus obsolètes ou périmés ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Contenus` |
| **Critère**  | `5.8` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service ne gère pas de contenu` |
| **Métiers concernés** | `Architecte Logiciel` `Data Scientist` `Responsable de la sécurité informatique` `Responsable Juridique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.8/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Alléger les bases de données et les serveurs physiques de données non utiles.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir une stratégie d'archivage et de suppression des contenus obsolètes, périmés, dépassés ou inutiles à conserver dans le service numérique. Cette stratégie peut être automatique en définissant une date d'expiration et un processus d'archivage et/ou de purge automatique.

De façon complémentaire à des mécanismes d'archivage automatique, prévoir également des mécanismes de suppression manuelle pour les contenus spécifiques qui nécessitent une évaluation humaine.

Cette stratégie est obligatoire pour le sous-ensemble des données personnelles collectées par les services, qui impose de définir et communiquer une durée de conservation des données personnelles (art. 13-2 du RGPD).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, vérifier l'existence d'une stratégie d'archivage et de suppression clairement définie, l'existence de mécanismes automatiques et de processus manuels pour les contenus dont le traitement requiert une intervention humaine. Le suivi de cette stratégie pourra être réalisé en évaluant régulièrement le taux d'occupation des bases de données et des serveurs physiques.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une fiche explicitement étiquetée « RGESN 5.8 » : [**RWEB 0114 — « Avoir une stratégie de fin de vie des contenus »**](https://rweb.greenit.fr/fr/fiches/RWEB_0114-avoir-une-strategie-de-fin-de-vie-des-contenus). Elle vise les contenus **dépubliés**, à supprimer des supports actifs, ou à conserver si besoin « sur des supports de stockage froids ». Son principe de validation : **aucun** contenu stocké et non accessible sur les pages web.

Trois autres fiches complètent le dispositif :

- [**RWEB 0023 — « Réduire le volume de données stockées au strict nécessaire »**](https://rweb.greenit.fr/fr/fiches/RWEB_0023-reduire-le-volume-de-donnees-stockees-au-strict-necessaire) donne un cycle complet : un rapport annuel sur SSD à sa sortie, archivé un mois plus tard, supprimé au bout de dix ans. Son délai de « 18 mois » pour respecter le RGPD n'a pas de valeur générale : chaque durée se déduit de la finalité du traitement ;
- [**RWEB 0116 — « Entretenir son site régulièrement »**](https://rweb.greenit.fr/fr/fiches/RWEB_0116-entretenir-son-site-regulierement) apporte le volet **manuel** : zéro contenu non revu depuis plus d'**un an** ;
- [**RWEB 0079 — « Mettre en place une politique d'expiration et suppression des données »**](https://rweb.greenit.fr/fr/fiches/RWEB_0079-mettre-en-place-une-politique-d-expiration-et-suppression-des-donnees) affirme que « de nombreux SGBDR » gèrent une durée de vie nativement. Ce n'est pas le cas de PostgreSQL ni de MySQL, qui demandent un traitement planifié.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Contributeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) aborde le sujet sous trois angles.

**Les contenus.** [« Un planning d'archivage et une version allégée des contenus anciens consultables sont-ils mis en oeuvre ? »](https://gr491.isit-europe.org/crit.php?id=5-uxui-il-est-souvent-produit-une-quantite-non-e8402d) propose un indicateur, « Volume supprimé / Volume des contenus inactifs », et une piste entre conserver et supprimer : une **version allégée** des contenus anciens. Le conseil [« Chaque contenu vidéo est-il associé à une durée de vie ? »](https://gr491.isit-europe.org/crit.php?id=4-contenus-les-videos-peuvent-etre-des-faits-dactualite-e65b59) rappelle que la date de fin est souvent connue « lors de la création ».

**Les données.** Dans la [famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=1), deux critères en priorité **High** demandent si [les données ont une date d'expiration](https://gr491.isit-europe.org/crit.php?id=1-backend-les-specifications-font-apparaitre-des-collections-de-811aa4) et si [la suppression des données obsolètes est gérée](https://gr491.isit-europe.org/crit.php?id=1-backend-la-reglementation-impose-de-maitriser-le-cycle-46acee). Avant la suppression, le GR491 propose aussi de réduire la précision des données anciennes.

**Le stockage.** [« Est-ce que les données "vivantes" et "mortes" sont gérées de manière différentes ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-les-donnees-dhistoriques-doivent-etre-conservees-pour-8a647f) : les données inactives ne justifient pas un stockage haute performance.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable de la sécurité informatique`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) ont un critère de succès qui correspond presque mot pour mot au 5.8, « Outdated content », dans la fiche [**« Promote responsible data practices »**](https://www.w3.org/TR/web-sustainability-guidelines/#promote-responsible-data-practices) :

> « Archive and delete outdated or otherwise expired product content and data via automated expiration dates and scheduled product audits. »

La fiche [**« Store data according to the needs of your users »**](https://www.w3.org/TR/web-sustainability-guidelines/#store-data-according-to-the-needs-of-your-users) ajoute la suppression des données inutilisées (« dark data »), des règles de cycle de vie par type de donnée, et la rotation des **journaux** (logs), une catégorie souvent oubliée qui grossit sans fin si personne ne fixe sa durée.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) des Designers Éthiques demande d'« identifier les durées requises de conservation des contenus pour les utilisateurs : brouillons, posts, historique... » dès la phase de recherche, car il « vaut mieux fixer les règles de gestion en amont de la collecte des données ». Trois questions à trancher :

- « combien de temps garde-t-on ces données ? »
- « quel process mettre en place pour se rappeler de les supprimer à expiration (si manuelle) ? »
- « est-ce qu'on les archive ou est-ce qu'on les supprime à terme ? »

La décision se prend en concevant les parcours ; la purge se programme ensuite.

{{% /tab %}}

{{% tab tabName="RGPD et archives publiques" %}}

Profil(s) métier concerné(s) : `Responsable Juridique`, `Architecte Logiciel`

Le **responsable juridique** est concerné par deux régimes, que le [guide de la CNIL sur les durées de conservation](https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees) articule.

**Le RGPD** ne fixe pas de durée : le responsable de traitement doit la déterminer « en fonction de la finalité du traitement ». La CNIL distingue trois phases :

| Phase | Ce qu'elle recouvre |
|---|---|
| Base active | « Les données sont accessibles, dans l'environnement de travail immédiat » |
| Archivage intermédiaire | Données qui ne servent plus à l'objectif fixé, mais encore utiles (contentieux) ou imposées par la loi, consultées « de manière ponctuelle et motivée par des personnes spécifiquement habilitées » |
| Archivage définitif | Conservation sans limitation de durée, pour les seules archives d'intérêt public |

C'est le schéma du critère 5.8. L'anonymisation peut remplacer l'effacement.

**Les archives publiques.** Pour un service public, les données produites sont des archives publiques (Code du patrimoine, article L. 211-1), dont l'élimination est soumise à « l'autorisation d'élimination du responsable du contrôle scientifique et technique ». Un service public fixe donc ses durées avec son service d'archives ; la purge automatique applique ensuite des règles autorisées. Sans cette autorisation, c'est une élimination non autorisée.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Data Scientist`

**1. Dresser l'inventaire des contenus et de leur durée de vie.** C'est la « stratégie clairement définie » du moyen de test. Par exemple, à adapter :

| Type de contenu | Durée en base active | À l'échéance | Mécanisme |
|---|---|---|---|
| Brouillons abandonnés | 6 mois sans modification | Suppression | Automatique |
| Jetons et liens de connexion | Leur date d'expiration | Suppression | Automatique |
| Comptes inactifs | 2 ans sans connexion | Relance, puis suppression | Automatique |
| Journaux techniques (logs) | 12 mois | Suppression | Automatique (rotation) |
| Actualités, événements | Revue annuelle | Archive allégée ou suppression | Manuel |
| Fichiers déposés | Durée du dossier auquel ils sont liés | Suppression avec le dossier | Automatique |

Ces durées sont des exemples, à fixer selon la finalité et, pour un service public, avec le service d'archives.

**2. Fixer la date d'expiration à la création, et purger chaque nuit.** PostgreSQL et MySQL n'ont pas de durée de vie native : la purge est un traitement planifié.

```sql
ALTER TABLE brouillon ADD COLUMN expire_le timestamptz;

-- À chaque modification d'un brouillon : expire_le = now() + interval '6 months'

-- Purge quotidienne
DELETE FROM brouillon WHERE expire_le < now();
```

La purge se lance par une tâche planifiée (`cron`, minuteur systemd, tâches de l'hébergeur), comme chez DiaLog pour ses jetons.

**3. Pour les données horodatées volumineuses**, comme les journaux d'accès ou les mesures, partitionner la table par mois et supprimer les partitions entières :

```sql
CREATE TABLE journal_acces (
  cree_le timestamptz NOT NULL,
  chemin  text
) PARTITION BY RANGE (cree_le);

CREATE TABLE journal_acces_2026_10 PARTITION OF journal_acces
  FOR VALUES FROM ('2026-10-01') TO ('2026-11-01');

-- Un an plus tard
DROP TABLE journal_acces_2025_10;
```

Supprimer une partition « is far faster than a bulk operation » ([PostgreSQL](https://www.postgresql.org/docs/current/ddl-partitioning.html)) et évite le `VACUUM` d'un `DELETE` massif. Pour les journaux en fichiers, `logrotate` fait le même travail :

```
/var/log/mon-service/*.log {
    weekly
    rotate 52
    compress
    missingok
    notifempty
}
```

52 fichiers hebdomadaires sont conservés, soit un an.

**4. Régler les CMS.** WordPress garde par défaut toutes les révisions des articles ([documentation](https://developer.wordpress.org/advanced-administration/wordpress/wp-config/)). Une ligne dans `wp-config.php` les limite :

```php
define( 'WP_POST_REVISIONS', 5 );
```

C'est la fiche [RWP 4.03](https://rwp.greenit.fr/fr/fiches/RWP_4.03-limiter-le-nombre-de-revisions) du [RWP](https://rwp.greenit.fr/), la déclinaison WordPress de RWEB. Sa fiche [RWP 8.01](https://rwp.greenit.fr/fr/fiches/RWP_8.01-entretenir-son-site-regulierement), version WordPress de RWEB 0116, ajoute trois nettoyages : les médias inutilisés de la bibliothèque, les résidus en base (commentaires indésirables, brouillons, données d'extensions supprimées) et les anciennes sauvegardes.

**5. Prévoir la revue manuelle** des contenus dont l'obsolescence demande un jugement : une date de dernière revue sur chaque contenu, et chaque année, la liste des contenus non revus depuis plus d'un an. Un contenu ancien encore utile peut être allégé et présenté comme une archive.

**6. Suivre le taux d'occupation**, comme le propose le moyen de test :

```sql
SELECT pg_size_pretty(pg_database_size(current_database()));

SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) AS taille
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 10;
```

Après un `DELETE`, PostgreSQL ne rend pas l'espace au système : le `VACUUM` standard « will not return the space to the operating system » ([documentation](https://www.postgresql.org/docs/current/routine-vacuuming.html)). Une purge réussie se voit donc d'abord par une taille qui **cesse de croître**. Pour les fichiers déposés, `du -sh` relevé chaque mois joue le même rôle.

**7. Ne pas oublier les sauvegardes.** Une donnée supprimée subsiste dans les sauvegardes jusqu'à leur expiration : leur durée fixe le délai réel de disparition.

**8. Documenter** la stratégie dans la déclaration d'écoconception : le tableau de l'étape 1, les mécanismes automatiques (tâche, fréquence), le processus manuel (qui, quand) et la durée de conservation des sauvegardes.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Juridique`

Le 5.8 traite la fin de vie des contenus. D'autres critères en traitent le début ou le contexte :

- le [critère 1.6](../../strategie/1-6_collecte-donnees/) : la donnée la plus simple à supprimer est celle qu'on n'a pas collectée ;
- le [critère 2.7](../../specifications/2-7_maintenance-decommissionnement/) : la fin de vie du **service** entier ;
- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) : la limite de poids freine la croissance du stockage, la durée de vie l'arrête ;
- le [critère 5.7](../5-7_format-documents/) : un document compressé reste stocké tant qu'il n'est pas supprimé.

Le [critère 7.2](../../backend/7-2_durees-conservation/) du RGESN (durées de conservation), dans la famille Backend, en est le pendant côté données.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) ([déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque le critère **« Non validé »** : « Une règle d'archivage automatique des brouillons après 6 mois est prévue et sera mise en place prochainement. » Son [code source](https://github.com/MTES-MCT/dialog), consulté le 20 octobre 2026, ne la contient pas encore. Le mécanisme existe pourtant pour un autre type de donnée : `cron.json` lance chaque nuit `app:user_tokens:purge`, qui supprime les jetons expirés. La règle des brouillons tient dans le même schéma.

[PeerTube](https://joinpeertube.org/) montre une stratégie réglable par type de donnée, d'après son [fichier de configuration](https://github.com/Chocobozzz/PeerTube/blob/develop/config/production.yaml.example) par défaut :

| Donnée | Durée par défaut |
|---|---|
| Statistiques de vues des vidéos des autres instances | 30 jours (`views.videos.remote.max_age`) |
| Archives d'export de compte | 2 jours (`export_expiration`) |
| Statistiques de vues des vidéos locales | Sans limite (`views.videos.local.max_age: -1`) |
| Historique de visionnage des utilisateurs | Sans limite (`history.videos.max_age: -1`) |

L'historique de visionnage est une donnée personnelle, dont le RGPD impose de fixer la durée : une ligne de configuration (par exemple `'6 months'`) suffit à le purger.

{{% /tab %}}

{{< /tabs >}}
