---
weight: 100
title: "7.1 - Cache serveur pour les données les plus utilisées"
description: "Critère 7.1 du RGESN : repérer les réponses les plus coûteuses et les plus demandées, les mettre en cache côté serveur avec une durée adaptée à chaque type de contenu, prévoir leur rafraîchissement et vérifier que le cache sert vraiment."
icon: "memory"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il recours à un système de cache serveur pour les données les plus utilisées ?

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
| **Critère**  | `7.1` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service repose sur des requêtes ne pouvant être mises en cache ou s'il ne s'appuie pas sur la réponse d'un serveur` |
| **Métiers concernés** | `Administrateur Système` `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/7.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Limiter la consommation de ressources informatiques.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Identifier les données, entrées API, ressources les plus utilisées à mettre en cache afin d'éviter de les régénérer. Configurer une durée d'expiration pour les rafraîchir par exemple en invalidant automatiquement le cache après une durée déterminée ou en utilisant des mécanismes de purge du cache lorsqu'une mise à jour des données est effectuée.

Le critère 7.1 concerne le cache côté serveur, à ne pas confondre avec le critère 6.2 qui traite du cache côté client.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère :

- Vérifier la configuration des systèmes de cache serveurs utilisés et s'assurer que les ressources les plus utilisées sont mises en cache ;
- Examiner la présence et les règles d'expiration qui doivent être correctement paramétrées en fonction des caractéristiques de chaque fonctionnalité ;
- S'assurer de la présence d'un mécanisme de rafraîchissement du cache.

Expliquer la stratégie de gestion de cache côté serveur dans la déclaration d'écoconception du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache trois fiches au critère 7.1 :

- [**RWEB 0071 — « Utiliser tous les niveaux de cache du serveur d'application / CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0071-utiliser-tous-les-niveaux-de-cache-du-cms) cite les extensions de cache de WordPress (WP Super Cache, W3 Total Cache…). Elle conseille aussi d'« activer la mise en cache des requêtes SQL » : MySQL a [supprimé](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html) ce cache dans sa version 8.0. Le résultat d'une requête coûteuse se met désormais en cache dans l'application ;
- [**RWEB 0073 — « Mettre les caches entièrement en RAM »**](https://rweb.greenit.fr/fr/fiches/RWEB_0073-mettre-les-caches-entierement-en-ram-opcode-et-kvs) : Memcached, Varnish ou APCu évitent les lectures sur disque ;
- [**RWEB 0016 — « Mettre en cache les données calculées souvent utilisées »**](https://rweb.greenit.fr/fr/fiches/RWEB_0016-mettre-en-cache-les-donnees-calculees-souvent-utilisees), rattachée aux critères [6.2](../../frontend/6-2_cache-navigateur/) et 7.1, prend l'exemple du nombre de contenus d'une catégorie, recalculé à chaque affichage alors qu'il change rarement.

[**RWEB 0074 — « Utiliser un cache HTTP »**](https://rweb.greenit.fr/fr/fiches/RWEB_0074-utiliser-un-cache-http) n'est rattachée à aucun critère, mais relève du 7.1 : un proxy inverse (Varnish, Nginx) sert les pages déjà calculées sans solliciter l'application.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Dans la [recommandation n°2 de la famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=2) du [GR491](https://gr491.isit-europe.org/) (INR), le critère [« Les interactions entre les composants bénéficient-ils de systèmes de cache ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-la-reduction-des-volumes-dechanges-des-operations-dfb3ce), en priorité **High**, demande un dossier technique qui identifie « les caches et la stratégie de cache utilisée pour chaque type de flux ». Il en précise l'arbitrage : « Plus le cache est proche du demandeur […], plus le volume de données en transit » est faible ; plus il est proche de la source, « plus il peut être mutualisé ».

Dans la [recommandation n°1](https://gr491.isit-europe.org/?famille=backend&num_reco=1), le critère [« Est-ce que les données souvent accédées sont disponibles en RAM ? »](https://gr491.isit-europe.org/crit.php?id=1-backend-la-consommation-de-ressources-de-traitement-est-bc0308) (priorité **Medium**) propose un indicateur : le « taux d'accès physique aux données ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) ont un critère de succès « Server-side caching » dans la fiche [**« Optimize caching and support offline access »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-caching-and-support-offline-access). Il reprend le 7.1 (« Ensure cached content is invalidated and/or refreshed when the underlying content changes ») et ajoute deux réserves :

- n'appliquer le cache que là où il apporte « a clear benefit », car un cache se maintient ;
- quand une copie dépend des droits de l'utilisateur, la réserver aux personnes autorisées, et seulement tant qu'elles le restent.

Dans la fiche [**« Reduce the number and complexity of database queries »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-the-number-and-complexity-of-database-queries), le critère « Reuse of retrieved data » s'applique à l'échelle d'une seule requête : lire une donnée une fois et la réutiliser, au lieu de répéter la requête.

{{% /tab %}}

{{% tab tabName="Que mettre en cache ?" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Le moyen de test demande des règles d'expiration adaptées à chaque fonctionnalité. Un exemple, à adapter :

| Réponse | Cache | Durée | Rafraîchissement |
|---|---|---|---|
| Pages publiques (actualités, fiches) | Page entière, par le proxy inverse ou le CMS | 10 min à 24 h | Purge à la publication |
| Calculs partagés coûteux (comptages, tuiles de carte, exports) | Applicatif, en mémoire | Rythme de mise à jour des données | Régénération planifiée ou invalidation à la modification |
| Réponses d'une API tierce (géocodage, référentiels) | Applicatif | Selon son en-tête `Cache-Control` et ses conditions d'usage | Expiration |
| Données en temps réel | Aucun, ou une à quelques secondes | — | Expiration |
| Pages d'un utilisateur connecté | Aucun cache partagé | — | — |

**Les plus utilisées d'abord.** Une page servie mille fois par jour en 1 s coûte plus qu'une page servie dix fois en 5 s. On classe donc les réponses par temps total, c'est-à-dire leur coût multiplié par leur fréquence (étape 1 de l'onglet suivant).

**Un site statique** (Hugo, Jekyll, Eleventy) pousse ce cache à l'extrême : chaque page est calculée une seule fois, au déploiement. Le critère porte alors sur le reste, comme une recherche ou une API.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Développeur`

**1. Repérer les réponses qui coûtent le plus.** Ajouter la durée de chaque requête au journal de Nginx :

```nginx
log_format temps '$request_time $upstream_response_time "$request"';
access_log /var/log/nginx/temps.log temps;
```

Après quelques jours, classer les adresses par temps de calcul cumulé :

```sh
awk '{split($4, u, "?"); t[u[1]] += $1; n[u[1]]++} END {for (k in t) printf "%8.1f s %6d %s\n", t[k], n[k], k}' /var/log/nginx/temps.log | sort -rn | head -20
```

**2. Mettre les pages publiques en cache devant l'application**, ici avec Nginx :

```nginx
# Bloc http
proxy_cache_path /var/cache/nginx/pages levels=1:2 keys_zone=pages:10m max_size=1g inactive=1h;

# Bloc server
location / {
    proxy_pass http://application;
    proxy_cache pages;
    proxy_cache_valid 200 10m;
    proxy_cache_use_stale error timeout updating;
    proxy_cache_background_update on;
    proxy_cache_lock on;
    proxy_cache_bypass $cookie_PHPSESSID;
    proxy_no_cache $cookie_PHPSESSID;
    add_header X-Cache-Status $upstream_cache_status always;
}
```

Les directives `proxy_cache_bypass` et `proxy_no_cache` écartent les visiteurs connectés. L'en-tête `Cache-Control` de l'application prime sur `proxy_cache_valid`, et une réponse qui pose un cookie n'est pas gardée ([documentation](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_valid)). L'application doit donc envoyer `Cache-Control: public, s-maxage=…`, sans cookie, sur les pages partageables. Sur un CMS, l'extension de cache fait le même travail.

**3. Mettre en cache les calculs coûteux dans l'application**, avec une expiration et une invalidation à la modification. Avec Symfony :

```php
public function __construct(private TagAwareCacheInterface $cache) {}

public function nombreDeContenus(int $categorie): int
{
    return $this->cache->get("categorie_{$categorie}_nombre", function (ItemInterface $item) use ($categorie) {
        $item->expiresAfter(3600);
        $item->tag("categorie_{$categorie}");
        return $this->repository->compterParCategorie($categorie);
    });
}

// À chaque modification d'un contenu de la catégorie :
$this->cache->invalidateTags(["categorie_{$categorie}"]);
```

Pour un résultat utilisé par tous, comme un export complet, une tâche planifiée peut le régénérer chaque nuit.

**4. Garder le cache en mémoire** (Redis, Memcached, APCu), comme le propose RWEB 0073, et activer le cache d'opcodes du langage (OPcache pour PHP).

**5. Vérifier que le cache sert vraiment.** Appeler deux fois la même page et comparer le temps jusqu'au premier octet :

```sh
for i in 1 2 3; do curl -s -o /dev/null -w '%{time_starttransfer}\n' https://exemple.fr/; done
```

L'en-tête `X-Cache-Status: HIT` de l'étape 2 confirme une réponse servie depuis le cache.

**6. Documenter** la stratégie dans la déclaration d'écoconception. Par exemple : « Pages publiques en cache Nginx 10 minutes, purgé à la publication. Tuiles de carte en cache 5 minutes. Export complet régénéré chaque nuit. Aucun cache partagé pour les pages des utilisateurs connectés. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

- le [critère 6.2](../../frontend/6-2_cache-navigateur/) (cache navigateur) : l'en-tête `Cache-Control` règle les deux caches à la fois, `max-age` pour le navigateur, `s-maxage` pour les caches partagés ;
- le [critère 3.2](../../architecture/3-2_architecture-elastique/) (architecture élastique) : un cache absorbe les pics de visites sans ajouter de serveur ;
- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) : garder en cache les réponses d'une API tierce lui évite des appels répétés ;
- le [critère 7.3](../7-3_traitement-arriere-plan/) (traitement en arrière-plan) : un calcul trop long pour un cache relève souvent d'une tâche asynchrone.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les pages ont été appelées le 30 octobre 2026 avec curl, plusieurs fois de suite. Le temps indiqué va jusqu'au premier octet de la réponse, hors ouverture de la connexion.

| Site | Déclaration | Cache serveur relevé | Premier appel | Appels suivants |
|---|---|---|---:|---:|
| [DiaLog](https://dialog.beta.gouv.fr/), accueil | Validé | Aucun sur la page | 0,11 s | 0,07 à 0,08 s |
| [DiaLog](https://dialog.beta.gouv.fr/carte), tuile de carte | Validé | Aucun | 0,75 s | 0,24 à 0,28 s |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | En cours de validation | WP Super Cache | 0,06 s | 0,06 à 0,08 s |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | Non détaillé | Cache de SPIP, 24 h | 0,93 s | 0,14 à 0,17 s |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | — | Site statique et CDN de GitHub Pages | 0,16 s | 0,04 s |

**Le Musée d'arts de Nantes** classe le critère **« En cours de validation »** dans sa [déclaration d'écoconception](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/), avec pour justification : « A voir avec le client. » Le site a pourtant un cache serveur, que sa page d'accueil signale en commentaire : « Dynamic page generated in 1.040 seconds », puis « Cached page generated by WP-Super-Cache ». WordPress calcule la page en une seconde environ, et le cache la sert en 60 à 80 ms. Il manque donc la vérification et la stratégie écrite, pas le cache.

**DiaLog** marque le critère **« Validé »** dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf), avec un « Cache côté serveur pour limiter le nb de requêtes ». Son [code source](https://github.com/MTES-MCT/dialog), consulté le 30 octobre 2026, en contient trois :

- le cache de requêtes de Doctrine, qui garde la traduction des requêtes DQL en SQL, mais pas leurs résultats. Le cache de résultats est configuré, mais aucune requête ne l'utilise ;
- la liste des gestionnaires de voirie, gardée une journée ;
- l'export CSV complet de la base, régénéré chaque nuit à 3 h. L'export filtré est calculé à chaque demande.

Les tuiles de la carte sont recalculées à chaque appel. Leur en-tête `Cache-Control: max-age=300, public, s-maxage=300, stale-while-revalidate=300` les autorise dans un cache partagé, mais aucun n'est placé devant l'application : les réponses ne portent ni en-tête `Age` ni `X-Cache`. Un cache Nginx, comme à l'étape 2, servirait la même tuile à tous les visiteurs pendant cinq minutes.

**SPOTE**, construit avec SPIP, annonce son cache par l'en-tête `X-Spip-Cache: 86400`, soit 24 heures. D'après la [documentation de SPIP](https://programmer.spip.net/Configuring-the-cache), le cache est invalidé « when changes have been made to any content ». La déclaration de SPOTE ne détaille pas les critères.

**Le site du RGESN** est généré à l'avance et servi par le CDN de GitHub Pages (`X-Cache: HIT`). [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) marque le critère « Non validé » : « Aucune stratégie de mise en cache côté serveur implémentée. »

{{% /tab %}}

{{< /tabs >}}
