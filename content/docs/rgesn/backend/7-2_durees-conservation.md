---
weight: 200
title: "7.2 - Durées de conservation des données"
description: "Critère 7.2 du RGESN : donner une date d'expiration à chaque donnée, archiver sur un support froid ce qui est rarement consulté, aider les utilisateurs à repérer leurs données obsolètes, purger automatiquement et suivre l'évolution du stockage."
icon: "inventory_2"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique met-il en place des durées de conservation sur les données et documents en vue de leur suppression ou archivage passé ce délai ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Backend` |
| **Critère**  | `7.2` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur l'utilisation d'un serveur` |
| **Métiers concernés** | `Administrateur Système` `Développeur` `Responsable Produit` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/7.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Le stockage des données n'est ni illimité, ni gratuit, il a un impact environnemental et doit être optimisé. Certains services traitent de grandes quantités de données qui ne sont jamais consultées, car l'utilisateur a cessé d'utiliser le produit (mais n'a, par exemple, pas supprimé le compte) ou parce que les données sont obsolètes depuis longtemps. La limitation des durées de conservation des données personnelles figure d'ailleurs dans les obligations du RGPD.

L'objectif est d'alléger les bases de données et les serveurs physiques de données non utiles.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir des dates d'expiration sur les données (fichiers, entrées en base de données...) permettant par la suite d'archiver et/ou de supprimer ces données. Implémenter des fonctionnalités qui aident les utilisateurs à identifier des données obsolètes grâce à des indicateurs et ou des suggestions de localisation où les données peuvent être supprimées.

Mettre en place un processus (de préférence automatique) d'archivage ou de suppression des données (fichiers, entrées en base de données...) dont la durée de conservation est dépassée.

Dans la mesure du possible, archiver les informations rarement consultées et intégrer une interface de « récupération à partir de l'archive » dans les interactions de l'utilisateur. Supprimer les archives inutilisées après une durée communiquée à l'utilisateur.

Déplacer le cas échéant les archives (données « froides ») sur un autre support que celui utilisé pour les données actives (données « chaudes »), voir critère 8.8.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, définir des dates d'expiration pour les informations obsolètes et mettre en place un mécanisme d'archivage ou de suppression des données dépassant la durée de conservation définie. Un suivi de l'évolution du poids des fichiers stockés et des bases de données.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Le [critère 5.8](../../contenus/5-8_archivage-suppression/) traite des **contenus** publiés : il détaille déjà l'inventaire des durées, le cadre du RGPD et des archives publiques, la purge en SQL, les partitions, la rotation des journaux et la mesure de la taille des bases. Le 7.2 étend la démarche à **toutes les données** du serveur, et ajoute trois exigences : l'archivage sur un support froid, une interface de récupération et des indicateurs pour l'utilisateur.

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache une fiche au critère 7.2 : [**RWEB 0079 — « Mettre en place une politique d'expiration et suppression des données »**](https://rweb.greenit.fr/fr/fiches/RWEB_0079-mettre-en-place-une-politique-d-expiration-et-suppression-des-donnees). Elle demande une durée de rétention pour « chaque donnée stockée ». Son principe de validation : **aucune** donnée stockée inutilisée.

Son exemple, présenté comme « une base Oracle en Java », utilise en fait Berkeley DB Java Edition, une base clé-valeur d'Oracle. La fiche affirme aussi que « de nombreux SGBDR » gèrent une durée de vie native, ce qui n'est le cas ni de PostgreSQL ni de MySQL (voir le 5.8).

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Administrateur Système`

Le [GR491](https://gr491.isit-europe.org/) (INR) rappelle les données que personne ne voit. Le critère [« Les données ont-elles une date d'expiration à laquelle elles sont supprimées ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-les-specifications-font-apparaitre-des-collections-de-811aa4), en priorité **High**, vise les données des « procédures asynchrones ou des tâches périodiques ». Elles sont « le plus souvent invisibles », donc : « Chacun de ces éléments doit porter sa propre information de fin de vie. »

Deux critères de la [recommandation n°2 de la famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=2) en donnent des exemples :

- [« Est-ce que les fichiers temporaires sont inclus dans les "logrotate" ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-dans-les-processus-dexecution-des-fichiers-temporaires-a8a74f), avec l'indicateur « Fichiers temporaires surveillés / fichiers temporaires » ;
- [« Le niveau des logs est-il adapté à l'environnement ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-la-mise-en-oeuvre-de-services-est-38e5ef) : les traces de débogage « collectées pour être ignorées » sont du gaspillage en production.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Administrateur Système`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) couvrent le 7.2 dans deux fiches :

- dans [**« Store data according to the needs of your users »**](https://www.w3.org/TR/web-sustainability-guidelines/#store-data-according-to-the-needs-of-your-users), déjà citée au [5.8](../../contenus/5-8_archivage-suppression/), le critère « Lifecycle management » demande de classer les données pour fixer leurs règles de « retention, expiration, and archiving », et de déplacer les moins consultées « to energy-efficient storage ». C'est le support froid du 7.2 ;
- dans [**« Reduce the number and complexity of database queries »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-the-number-and-complexity-of-database-queries), le critère « Data lifecycle controls » cite la durée de vie (« Time-to-Live (TTL) »), l'anonymisation et la minimisation des données stockées.

{{% /tab %}}

{{% tab tabName="Côté utilisateur" %}}

Profil(s) métier concerné(s) : `Responsable Produit`, `Développeur`

Le 7.2 demande aussi des fonctionnalités : les utilisateurs savent mieux que le serveur ce qui ne leur sert plus. Les Designers Éthiques, dans [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), rattachent ces choix aux critères [5.8](../../contenus/5-8_archivage-suppression/) et 7.2 et demandent de les faire dès la conception : « combien de temps garde-t-on ces données ? »

Trois éléments d'interface répondent au critère :

- **un indicateur**, dans l'espace de l'utilisateur. Par exemple : « 312 fichiers (1,2 Go) n'ont pas été ouverts depuis deux ans », avec un lien vers la liste triée par taille ;
- **une archive récupérable** : un dossier clos passe en archive, hors de la vue courante, avec un bouton « Restaurer ». Le délai avant la suppression est affiché sur la page, par exemple « Archive supprimée le 30 octobre 2027 » ;
- **une corbeille à durée annoncée**, par exemple « Les éléments supprimés depuis plus de 30 jours sont effacés définitivement ».

La durée annoncée doit être celle qui s'applique vraiment. Par défaut, Nextcloud garde les fichiers de la corbeille « for at least 30 days », puis ne les efface que « if space is needed » ([documentation](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/config_sample_php_parameters.html)). Sans quota, la limite est l'espace libre du disque : la corbeille peut grossir pendant des années. Le réglage `'trashbin_retention_obligation' => '30, 30'` efface les fichiers au bout de 30 jours.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Développeur`

**1. Compléter l'inventaire des durées** du [critère 5.8](../../contenus/5-8_archivage-suppression/) avec les données que le service produit sans les publier : comptes, fichiers déposés, files de tâches, fichiers temporaires, caches, exports générés, journaux et sauvegardes. Chacune reçoit une durée et une action à l'échéance : archiver ou supprimer.

**2. Porter la date d'expiration sur la donnée**, dès sa création, plutôt que de la recalculer lors de la purge :

```sql
ALTER TABLE dossier ADD COLUMN archive_le timestamptz,
                    ADD COLUMN supprimer_le timestamptz;

-- À la clôture d'un dossier : archivé, puis supprimé un an plus tard
UPDATE dossier SET archive_le = now(), supprimer_le = now() + interval '1 year' WHERE id = $1;

-- Purge quotidienne
DELETE FROM dossier WHERE supprimer_le < now();
```

La date `supprimer_le` est celle qu'affiche l'interface de l'onglet précédent. La purge se lance par une tâche planifiée, comme au 5.8.

**3. Déplacer les fichiers froids sur un autre support.** Sur un stockage objet compatible S3, une règle de cycle de vie fait le travail sans code. Par exemple, chez Scaleway, qui propose une classe d'archivage `GLACIER` :

```json
{
  "Rules": [{
    "ID": "pieces-jointes",
    "Filter": { "Prefix": "pieces-jointes/" },
    "Status": "Enabled",
    "Transitions": [{ "Days": 90, "StorageClass": "GLACIER" }],
    "Expiration": { "Days": 1095 }
  }]
}
```

```sh
aws s3api put-bucket-lifecycle-configuration --bucket mon-service \
  --lifecycle-configuration file://cycle-de-vie.json --endpoint-url https://s3.fr-par.scw.cloud
```

Les pièces jointes passent en archive au bout de 90 jours et sont supprimées au bout de trois ans. Les classes et les délais minimaux varient selon l'hébergeur ([Scaleway](https://www.scaleway.com/en/docs/object-storage/api-cli/lifecycle-rules-api/)). La restauration d'un fichier archivé prend du temps, ce qui convient aux données rarement consultées.

**4. Calculer l'indicateur de l'utilisateur** :

```sql
SELECT count(*), pg_size_pretty(sum(taille)) FROM fichier
WHERE proprietaire = $1 AND ouvert_le < now() - interval '2 years';
```

**5. Suivre l'évolution du poids**, comme le demande le moyen de test. Une ligne par mois suffit :

```sql
CREATE TABLE suivi_stockage (releve_le date PRIMARY KEY, base bigint, fichiers bigint);

-- Chaque mois, avec la taille des fichiers relevée par du -sb ou par le stockage objet :
INSERT INTO suivi_stockage VALUES (current_date, pg_database_size(current_database()), $1);
```

Une courbe qui cesse de monter montre que la purge fonctionne. PostgreSQL ne rend pas tout de suite l'espace libéré au disque (voir le 5.8).

**6. Documenter** dans la déclaration d'écoconception : le tableau des durées, les tâches de purge et d'archivage avec leur fréquence, le support des archives et la courbe de suivi.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Produit`

- le [critère 5.8](../../contenus/5-8_archivage-suppression/) (archivage et suppression des contenus) : le même travail pour les contenus publiés ;
- le [critère 1.6](../../strategie/1-6_collecte-donnees/) (collecte des données) : la donnée la plus simple à supprimer est celle qu'on n'a pas collectée ;
- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) (poids des fichiers) : la limite de poids freine la croissance, la durée de conservation l'arrête ;
- le [critère 7.4](../7-4_mecanisme-consensus/) (consensus) : une donnée inscrite dans une blockchain ne peut plus être supprimée ;
- le [critère 8.8](../../hebergement/8-8_donnees-chaudes-froides/) (données chaudes et froides), auquel renvoie le 7.2 pour le stockage des archives.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues et le code source de DiaLog consulté le 30 octobre 2026.

| Site | Déclaration | Justification |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | « A faire : Définir une politique de suppression de données » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | **Non validé** | « Les données sont horodatées mais aucune stratégie de suppression ou d'archivage identifiée. » |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | « A voir avec le client. » |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | Non détaillé | — |

**Aucun des services ne valide le critère.** Le 7.2 demande une décision sur la durée de chaque donnée, que l'équipe technique ne peut pas prendre seule. Le Musée renvoie la question au client, comme pour le [5.8](../../contenus/5-8_archivage-suppression/).

**DiaLog** a déjà le mécanisme : son fichier `cron.json` lance chaque nuit `app:user_tokens:purge`, qui supprime les jetons expirés. Les trois autres tâches planifiées actualisent un classement, envoient des relances ou régénèrent un export : aucune ne supprime de données. La règle d'archivage des brouillons au bout de six mois, annoncée pour le 5.8, n'est pas encore dans le code. Il reste aussi à fixer la durée des autres données, comme les comptes inactifs.

**FACE** a fait la première étape : ses données sont horodatées. Une date de création ne suffit pas à elle seule. Pour chaque type de donnée, il faut encore une durée, et une tâche qui compare cette date à la durée.

{{% /tab %}}

{{< /tabs >}}
