---
weight: 800
title: "5.8 - Archivage et suppression des contenus obsolètes"
description: "Critère 5.8 du RGESN : fixer une durée de vie à chaque type de contenu, purger automatiquement ce qui expire, prévoir une revue manuelle, respecter le RGPD et le droit des archives publiques, et suivre l'occupation du stockage."
icon: "auto_delete"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
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

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe et explicitement étiquetée « RGESN 5.8 » : la fiche [**RWEB 0114 — « Avoir une stratégie de fin de vie des contenus »**](https://rweb.greenit.fr/fr/fiches/RWEB_0114-avoir-une-strategie-de-fin-de-vie-des-contenus). Elle vise les contenus **dépubliés** : « continuer à les stocker n'a dans la plupart du temps pas d'intérêt d'un point de vue métier ». Sur un CMS, elle recommande de les supprimer des supports de stockage actifs, et de ne les conserver si besoin que « sur des supports de stockage froids : bande LTO (bande magnétique), disques durs capacitifs ». Son principe de validation : **aucun** contenu stocké et non accessible sur les pages web.

La fiche [**RWEB 0023 — « Réduire le volume de données stockées au strict nécessaire »**](https://rweb.greenit.fr/fr/fiches/RWEB_0023-reduire-le-volume-de-donnees-stockees-au-strict-necessaire), rattachée aux critères 5.8 et 7.2, donne un exemple de cycle complet : un rapport annuel est stocké sur un SSD à sa sortie, archivé sur un stockage classique un mois plus tard, puis supprimé au bout de dix ans. Elle affirme aussi qu'« on pourra cependant en supprimer au bout de 18 mois tout en respectant les contraintes RGPD ». Ce délai n'a pas de valeur générale : le RGPD ne fixe pas de durée unique, et chaque durée se déduit de la finalité du traitement (voir l'onglet « RGPD et archives publiques »).

Deux autres fiches complètent le dispositif :

- [**RWEB 0116 — « Entretenir son site régulièrement »**](https://rweb.greenit.fr/fr/fiches/RWEB_0116-entretenir-son-site-regulierement) apporte le volet **manuel** : son principe de validation compte les contenus dont la dernière mise à jour ou revue date de plus d'**un an**, avec un objectif de zéro.
- [**RWEB 0079 — « Mettre en place une politique d'expiration et suppression des données »**](https://rweb.greenit.fr/fr/fiches/RWEB_0079-mettre-en-place-une-politique-d-expiration-et-suppression-des-donnees), rattachée au critère 7.2, propose une durée de vie (« TTL ») et affirme que « de nombreux SGBDR » la gèrent nativement. Ce n'est pas le cas de PostgreSQL ni de MySQL, qui demandent un traitement planifié. Son exemple Java reprend d'ailleurs celui de la [documentation de Berkeley DB Java Edition](https://docs.oracle.com/cd/E17277_02/html/GettingStartedGuide/timetolive.html), une base clé-valeur, et non une base relationnelle.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Contributeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) aborde le sujet sous trois angles.

**Les contenus.** La recommandation [« Un planning d'archivage et une version allégée des contenus anciens consultables sont-ils mis en oeuvre ? »](https://gr491.isit-europe.org/crit.php?id=5-uxui-il-est-souvent-produit-une-quantite-non-e8402d), en priorité **Medium**, propose un indicateur que le RGESN ne donne pas : « Volume supprimé / Volume des contenus inactifs ». Elle ajoute une piste intermédiaire entre conserver et supprimer : garder consultable une **version allégée** des contenus anciens. Deux conseils de la [recommandation n°4 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=4) la précisent :

- [« Chaque contenu vidéo est-il associé à une durée de vie ? »](https://gr491.isit-europe.org/crit.php?id=4-contenus-les-videos-peuvent-etre-des-faits-dactualite-e65b59) : la date de fin est souvent connue « lors de la création » et doit servir « pour supprimer la vidéo après un délai défini » ;
- [« A t-on défini la proportion des contenus de type flux (contenus chauds de type actu...) et stock (contenus froid, longue traîne en SEO) ? »](https://gr491.isit-europe.org/crit.php?id=4-contenus-les-contenus-lies-a-un-evenement-ou-9d8fc1) : son test « Tous les contenus ont-ils une date d'expiration ? » résume le critère. Le conseil nuance toutefois : « Conserver les contenus anciens peut être utile pour conserver les référencement SEO acquis », à condition de les présenter comme des archives.

**Les données.** Dans la [recommandation n°1 de la famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=1), deux critères en priorité **High** demandent si [« Les données ont-elles une date d'expiration à laquelle elles sont supprimées ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-les-specifications-font-apparaitre-des-collections-de-811aa4) et si [« la suppression des données obsolètes est gérée ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-la-reglementation-impose-de-maitriser-le-cycle-46acee). Le second relève que, hors données personnelles, les données s'accumulent sans délai de péremption, avec « un accroissement permanent de la volumétrie de données, des volumes de sauvegardes ». Il propose aussi une étape avant la suppression : réduire la précision des données anciennes.

**Le stockage.** Le critère [« Est-ce que les données "vivantes" et "mortes" sont gérées de manière différentes ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-les-donnees-dhistoriques-doivent-etre-conservees-pour-8a647f) rejoint la fiche RWEB 0114 : les données inactives ne justifient pas un stockage haute performance, souvent le plus consommateur.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable de la sécurité informatique`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) contiennent un critère de succès qui correspond presque mot pour mot au 5.8, « Outdated content », dans la fiche [**« Promote responsible data practices »**](https://www.w3.org/TR/web-sustainability-guidelines/#promote-responsible-data-practices) :

> « Archive and delete outdated or otherwise expired product content and data via automated expiration dates and scheduled product audits. »

On y retrouve les deux mécanismes du RGESN : l'automatique (« automated expiration dates ») et le manuel (« scheduled product audits »).

La fiche [**« Store data according to the needs of your users »**](https://www.w3.org/TR/web-sustainability-guidelines/#store-data-according-to-the-needs-of-your-users) va plus loin côté infrastructure :

- **Remove unused data** : « Regularly remove unused or obsolete data ("dark data") to reduce storage and energy costs, and manage whether and how long data is stored. »
- **Lifecycle management** : « Use classification and tagging policies to define and manage data lifecycle rules, including retention, expiration, and archiving. »
- **Optimized logging** : « Manage logs with regular rotation, retention, compression, and backup practices ».

Le dernier point rappelle une catégorie souvent oubliée : les **journaux** (logs), qui ne sont pas des « contenus » au sens éditorial mais grossissent sans fin si personne ne fixe leur durée.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) des Designers Éthiques cite le critère 5.8 à deux étapes du projet.

Dès la phase de recherche : « Identifier les durées requises de conservation des contenus pour les utilisateurs : brouillons, posts, historique... »

Puis dans une rubrique « Définir des dates d'expiration des contenus », qui rappelle qu'il « vaut mieux fixer les règles de gestion en amont de la collecte des données ». Elle donne les moments où se poser la question (« si vous créez un espace de connexion, si vous permettez aux utilisateurs de créer des contenus, ou encore si vous migrez des articles de blog vers un nouveau site ») et les trois questions à trancher :

- « combien de temps garde-t-on ces données ? »
- « quel process mettre en place pour se rappeler de les supprimer à expiration (si manuelle) ? »
- « est-ce qu'on les archive ou est-ce qu'on les supprime à terme ? »

Le critère figure dans la liste des métiers du RGESN sans designer. La ressource explique pourquoi un designer peut pourtant le porter : « sur les petits projets (en tant qu'indépendant par exemple) ou encore si vous êtes la personne la plus experte en écoconception de votre équipe ». La décision se prend en concevant les parcours ; la purge se programme ensuite.

{{% /tab %}}

{{% tab tabName="RGPD et archives publiques" %}}

Profil(s) métier concerné(s) : `Responsable Juridique`, `Architecte Logiciel`

La présence du **responsable juridique** parmi les métiers concernés s'explique par deux régimes juridiques, que le [guide pratique de la CNIL sur les durées de conservation](https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees) (juillet 2020) articule.

**Le RGPD.** L'article 13 cité par le RGESN impose d'informer les personnes de la durée de conservation de leurs données. Le RGPD ne fixe pas cette durée : il appartient au responsable de traitement « de la déterminer en fonction de la finalité du traitement ». La CNIL distingue trois phases :

| Phase | Ce qu'elle recouvre |
|---|---|
| Base active | « Les données sont accessibles, dans l'environnement de travail immédiat » |
| Archivage intermédiaire | Données qui ne servent plus à l'objectif fixé, mais encore utiles (contentieux) ou imposées par la loi, consultées « de manière ponctuelle et motivée par des personnes spécifiquement habilitées » |
| Archivage définitif | Conservation sans limitation de durée, pour les seules archives d'intérêt public |

C'est le schéma du critère 5.8 : la base active est allégée, l'archivage intermédiaire se fait à part, et la suppression intervient à la fin. La CNIL rappelle qu'« en lieu et place de mesures d'effacement, les données peuvent faire l'objet d'un processus d'anonymisation ».

**Les archives publiques.** Pour un service public, les données produites sont des archives publiques : « l'ensemble des documents, y compris les données, quels que soient leur date, leur lieu de conservation, leur forme et leur support » (Code du patrimoine, article L. 211-1, cité par la CNIL). Leur élimination n'est pas libre. Le guide de la CNIL recommande de « prévoir une procédure de purge automatique et sélective des données (pour les archives publiques, cette purge est soumise à l'autorisation d'élimination du responsable du contrôle scientifique et technique) ».

Concrètement, un service public définit ses durées avec son service d'archives (archives ministérielles ou départementales). La purge automatique applique ensuite des règles déjà autorisées. Supprimer automatiquement des données publiques sans cette autorisation n'est pas une bonne pratique d'écoconception : c'est une élimination non autorisée.

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

Les durées ci-dessus sont des exemples. Pour les données personnelles, elles se déduisent de la finalité ; pour un service public, elles se fixent avec le service d'archives (voir l'onglet précédent).

**2. Fixer la date d'expiration à la création, et purger chaque nuit.** PostgreSQL et MySQL n'ont pas de durée de vie native : la purge est un traitement planifié.

```sql
ALTER TABLE brouillon ADD COLUMN expire_le timestamptz;

-- À chaque modification d'un brouillon : expire_le = now() + interval '6 months'

-- Purge quotidienne
DELETE FROM brouillon WHERE expire_le < now();
```

La purge se lance par une tâche planifiée : `cron`, minuteur systemd, ou fichier de tâches de l'hébergeur. DiaLog procède ainsi pour ses jetons (voir les retours d'expériences).

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

D'après la [documentation de PostgreSQL](https://www.postgresql.org/docs/current/ddl-partitioning.html), supprimer une partition « is far faster than a bulk operation » et évite entièrement le travail de `VACUUM` qu'entraîne un `DELETE` massif. Pour les journaux écrits dans des fichiers, `logrotate` fait le même travail :

```
/var/log/mon-service/*.log {
    weekly
    rotate 52
    compress
    missingok
    notifempty
}
```

52 fichiers hebdomadaires compressés sont conservés, soit un an ; les plus anciens sont supprimés automatiquement.

**4. Régler les CMS.** D'après sa [documentation](https://developer.wordpress.org/advanced-administration/wordpress/wp-config/), WordPress active par défaut les révisions des articles, sans limite de nombre, et vide la corbeille au bout de 30 jours (`EMPTY_TRASH_DAYS`). Une ligne dans `wp-config.php` limite les révisions :

```php
define( 'WP_POST_REVISIONS', 5 );
```

**5. Prévoir la revue manuelle**, pour les contenus dont l'obsolescence demande un jugement humain : une date de dernière revue sur chaque contenu, et une liste des contenus non revus depuis plus d'un an (le seuil de la fiche RWEB 0116), traitée chaque année. Un contenu ancien encore utile peut être allégé (images retirées ou réduites) et présenté comme une archive, comme le suggère le GR491.

**6. Suivre le taux d'occupation**, comme le propose le moyen de test :

```sql
SELECT pg_size_pretty(pg_database_size(current_database()));

SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) AS taille
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 10;
```

Une nuance pour lire l'indicateur : après un `DELETE`, PostgreSQL ne rend pas l'espace au système. Selon sa [documentation](https://www.postgresql.org/docs/current/routine-vacuuming.html), le `VACUUM` standard marque l'espace comme réutilisable mais « will not return the space to the operating system » ; seul `VACUUM FULL`, qui réécrit la table et la verrouille, le fait. Une purge réussie se voit donc d'abord par une taille qui **cesse de croître**, plutôt que par une baisse. Pour les fichiers (documents déposés, médias), `du -sh` sur les répertoires concernés, relevé chaque mois, joue le même rôle.

**7. Ne pas oublier les sauvegardes.** Une donnée supprimée subsiste dans les sauvegardes jusqu'à leur expiration. La durée de conservation des sauvegardes fait partie de la stratégie : c'est elle qui fixe le délai réel de disparition d'une donnée.

**8. Documenter** la stratégie dans la déclaration d'écoconception : le tableau de l'étape 1, les mécanismes automatiques (tâche, fréquence), le processus manuel (qui, quand) et la durée de conservation des sauvegardes.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Juridique`

Le critère 5.8 traite la fin de vie des contenus. Plusieurs critères déjà publiés sur ce site en traitent le début ou le contexte :

- le [critère 1.6](../../strategie/1-6_collecte-donnees/) (collecte de données) : la donnée la plus simple à supprimer est celle qu'on n'a pas collectée ;
- le [critère 2.7](../../specifications/2-7_maintenance-decommissionnement/) (maintenance et décommissionnement) : il traite la fin de vie du **service** entier, quand le 5.8 traite celle de ses contenus. La fiche RWEB 0115, présentée au 2.7, est rattachée aux deux critères ;
- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) (poids et formats des fichiers) : la limite de poids des fichiers déposés freine la croissance du stockage, la durée de vie l'arrête ;
- le [critère 5.7](../5-7_format-documents/) (format des documents) : un document compressé reste un document stocké tant qu'il n'est pas supprimé.

Le critère 7.2 du RGESN (durées de conservation des données et documents), dans la famille Backend, en est le pendant côté données : plusieurs fiches RWEB et la ressource des Designers Éthiques les traitent ensemble.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque le critère **« Non validé »**, avec une justification honnête : « Une règle d'archivage automatique des brouillons après 6 mois est prévue et sera mise en place prochainement. » Le [code source de DiaLog](https://github.com/MTES-MCT/dialog), consulté le 20 octobre 2026, montre où en est la démarche :

- les arrêtés n'ont toujours que deux statuts, `draft` et `published` : la règle d'archivage des brouillons n'apparaît pas encore ;
- en revanche, le mécanisme existe déjà pour un autre type de donnée. Le fichier `cron.json` lance chaque nuit à minuit la commande `app:user_tokens:purge`, qui supprime les jetons dont la date d'expiration est passée (`expirationDate < now`).

La règle annoncée pour les brouillons tient dans le même schéma : une date d'expiration, une requête de suppression et une ligne de plus dans `cron.json`.

[PeerTube](https://joinpeertube.org/) montre une stratégie réglable par type de donnée, d'après son [fichier de configuration](https://github.com/Chocobozzz/PeerTube/blob/develop/config/production.yaml.example) par défaut :

| Donnée | Durée par défaut |
|---|---|
| Statistiques de vues des vidéos des autres instances | 30 jours (`views.videos.remote.max_age`) |
| Archives d'export de compte | 2 jours (`export_expiration`) |
| Statistiques de vues des vidéos locales | Sans limite (`views.videos.local.max_age: -1`) |
| Historique de visionnage des utilisateurs | Sans limite (`history.videos.max_age: -1`) |

Le dernier réglage mérite attention : l'historique de visionnage est une donnée personnelle, et le RGPD impose d'en fixer la durée. Une instance qui laisse la valeur par défaut le conserve sans limite ; une ligne de configuration (par exemple `'6 months'`) suffit à le purger automatiquement.

{{% /tab %}}

{{< /tabs >}}
