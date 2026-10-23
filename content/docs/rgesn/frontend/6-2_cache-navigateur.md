---
weight: 200
title: "6.2 - Mise en cache côté utilisateur"
description: "Critère 6.2 du RGESN : régler les en-têtes de cache selon le type de ressource (fichiers versionnés, pages, données), vérifier le comportement au-delà de la visite immédiate et documenter sa stratégie de cache."
icon: "cached"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il des mécanismes de mise en cache pour la totalité des contenus transférés dont il a le contrôle ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Frontend` |
| **Critère**  | `6.2` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur l'utilisation d'un serveur` |
| **Métiers concernés** | `Administrateur Système` `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est de réduire le poids des données échangées. Une partie de l'empreinte énergétique des services numériques est liée à la volumétrie des données échangées sur les réseaux, en particulier lorsque les données sont transmises sur des réseaux radio (réseaux mobiles par exemple). La réduction de la volumétrie des données échangées sur les réseaux pour une application donnée est donc un axe important d'écoconception. Dans la plupart des cas, cette réduction pourra se faire sans dégradation de l'expérience utilisateur.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

La stratégie de cache doit être adaptée au contexte d'application, au type de contenus (images, fichiers CSS, JavaScript, etc.) qui sont transférés fréquemment depuis le serveur vers le client et au scénario d'usage. Mettre en place un mécanisme de cache côté utilisateur, en frontend (cache HTTP par exemple). La gestion du mode déconnecté (offline) est parfois très pertinente, parfois non.

Lorsqu'une même information est susceptible d'être requêtée plusieurs fois, privilégier un stockage temporaire local pour éviter un trafic réseau inutile. Par exemple, il est possible de stocker des données souvent utilisées dans le navigateur web, afin de limiter les échanges avec le serveur.

Vérifier qu'aucune des données destinées à être échangées n'est superflue et que les informations transmises ne sont pas redondantes.

Le critère 6.2 traite du cache côté client. Le cache côté serveur est, quant à lui, traité dans le critère 7.1.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, un mécanisme de cache côté utilisateur est mis en place, quand la solution est pertinente. En termes de moyens de test, accéder à plusieurs reprises au service et vérifier si les contenus sont récupérés à partir du cache plutôt que du serveur.

Expliciter dans la déclaration d'écoconception du service la stratégie de cache frontend, y compris son optimisation au regard du type de contenu, du contexte d'application et des scénarios d'usage.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache six fiches au critère 6.2. Les trois principales couvrent les trois niveaux du cache côté utilisateur.

**Les fichiers.** [**RWEB 0075 — « Ajouter des entêtes Expires ou Cache-Control »**](https://rweb.greenit.fr/fr/fiches/RWEB_0075-ajouter-des-entetes-expires-ou-cache-control) demande que la durée de vie des CSS, scripts et images soit « la plus longue possible, afin que le navigateur ne les redemande pas au serveur ». Son exemple Nginx applique `expires max` à une longue liste d'extensions. D'après la [documentation de Nginx](https://nginx.org/en/docs/http/ngx_http_headers_module.html), `max` fixe une expiration au 31 décembre 2037 et un `Cache-Control` de 10 ans. C'est sans risque pour un fichier dont le nom change à chaque modification, mais pas pour un fichier qui garde le même nom : `/css/style.css` modifié resterait servi dans son ancienne version pendant des années. Le principe de validation de la fiche, **aucun** en-tête `Expires` ou `Cache-Control` manquant, reste juste.

**Les réponses de l'API.** [**RWEB 0072 — « Mettre en cache les réponses AJAX »**](https://rweb.greenit.fr/fr/fiches/RWEB_0072-mettre-en-cache-les-reponses-ajax) vise les réponses « inchangées dans un futur proche », comme une liste de villes, avec un seuil de 10 % de réponses non mises en cache au plus. [**RWEB 0021 — « Limiter le nombre d'appels aux API HTTP »**](https://rweb.greenit.fr/fr/fiches/RWEB_0021-limiter-le-nombre-d-appels-aux-api-http), rattachée aux critères 6.2 et 7.1, donne des durées à adapter : un appel par jour pour des avis clients, un par heure pour un flux de réseau social affiché sur le site.

**Les données.** [**RWEB 0064 — « Stocker les données statiques localement »**](https://rweb.greenit.fr/fr/fiches/RWEB_0064-stocker-les-donnees-statiques-localement) cite les stockages du navigateur (IndexedDB, Web Storage, Cache Storage) pour éviter les allers-retours avec le serveur.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le [GR491](https://gr491.isit-europe.org/) (INR) traite le cache dans la [recommandation n°3 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=3), en priorité **High** : [« Utilisez vous les mécanismes de cache pour limiter les échanges ? »](https://gr491.isit-europe.org/crit.php?id=3-frontend-la-reduction-des-volumes-dechanges-des-operations-4f3639) Son test cite trois points de contrôle : « pas de directive no-cache, cache navigateur, cache API ». Il explique aussi où placer le cache : « Plus le cache est proche du demandeur qu'il doit servir, plus le volume de données en transit et la longueur du chemin emprunté par les données sont faibles. » Le cache du navigateur est le plus proche qui soit, c'est l'objet du 6.2.

Le test « pas de directive no-cache » demande une nuance. `no-cache` ne désactive pas le cache : la réponse est conservée, mais revalidée à chaque usage, et le serveur répond « 304 » sans renvoyer le contenu s'il n'a pas changé. C'est la bonne directive pour une page HTML (voir l'onglet « Ce que disent les en-têtes HTTP »). La directive à traquer est `no-store`, qui interdit tout stockage.

Le critère [« Est-ce que le framework ou la technologie utilisée ne bloque pas les caches navigateur ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-lutilisation-de-certains-framework-notamment-dans-les-56566f), lui aussi en priorité **High**, vise les applications monopages, qui « rendent difficiles la gestion du cache sur le périphérique utilisateur ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

La fiche [**« Optimize caching and support offline access »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-caching-and-support-offline-access) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) détaille le critère de succès « Client-side caching » plus précisément que le RGESN :

- « use cache-friendly approaches such as versioned filenames for resources that change over time » : des noms de fichiers **versionnés**, la condition d'un cache long sans risque ;
- « Verify caching behavior using both initial and repeat visits to ensure that resources are reused where intended without causing stale or inconsistent content or broken functionality » : le test du RGESN, complété du risque inverse, un contenu périmé ;
- « Ensure any content with authorization-based access restrictions does not remain accessible after logout » : une exigence de **sécurité** que le RGESN ne formule pas.

Son critère « Offline access » (« Keep essential content and functionality available during network interruptions ») rejoint la phrase du RGESN sur le mode déconnecté, « parfois très pertinente, parfois non ». Le mot important est **essential** : un mode hors ligne qui précharge tout le site au premier passage fait télécharger des pages que l'utilisateur ne visitera peut-être jamais.

La fiche [**« Use Content Delivery Networks (CDNs) when beneficial »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-content-delivery-networks-cdns-when-beneficial) rappelle une limite moins connue : le cache des navigateurs est désormais **cloisonné** par site (« cache partitioning »). Une bibliothèque chargée depuis un CDN public n'est plus partagée entre les sites qui l'utilisent ; elle est téléchargée une fois par site.

{{% /tab %}}

{{% tab tabName="Ce que disent les en-têtes HTTP" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Le cache du navigateur obéit aux en-têtes envoyés par le serveur, définis par la norme [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111) et documentés par [MDN](https://developer.mozilla.org/fr/docs/Web/HTTP/Guides/Caching). Quatre directives suffisent dans la plupart des cas :

| En-tête | Effet | Pour quoi |
|---|---|---|
| `Cache-Control: public, max-age=31536000, immutable` | Réutilisé un an sans contacter le serveur | Fichiers versionnés (`app.7a0495ae.css`) |
| `Cache-Control: max-age=3600` + `ETag` | Réutilisé une heure, puis revalidé | Fichiers non versionnés (`/css/style.css`) |
| `Cache-Control: no-cache` + `ETag` | Conservé, mais revalidé à chaque usage : 304 sans contenu s'il n'a pas changé | Pages HTML |
| `Cache-Control: private, no-store` | Jamais stocké | Pages et données personnelles |

**Sans en-tête, le navigateur devine.** En l'absence de durée explicite, la RFC 9111 autorise une durée « heuristique », calculée sur l'ancienneté du fichier (`Last-Modified`) : « A typical setting of this fraction might be 10% ». Le [code source de Chromium](https://chromium.googlesource.com/chromium/src/+/main/net/http/http_response_headers.cc) applique exactement cette règle. Un fichier modifié il y a 30 jours est gardé 3 jours ; un fichier sans `Last-Modified` n'est pas gardé du tout. Le cache fonctionne donc souvent sans en-tête, mais au hasard des dates de modification, ce qui n'est pas une stratégie.

**La revalidation coûte une requête, pas un téléchargement.** Grâce à l'`ETag` ou au `Last-Modified`, le navigateur demande « ce fichier a-t-il changé ? » et reçoit une réponse 304 de quelques centaines d'octets. C'est économe en volume, mais chaque revalidation reste un aller-retour, qui compte dans le budget de requêtes du [critère 6.1](../6-1_poids-requetes-ecran/).

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

**1. Versionner les fichiers statiques.** Les outils de build ajoutent une empreinte au nom des fichiers (Webpack, Vite, Hugo avec `fingerprint`, Symfony AssetMapper…). Le nom change quand le contenu change : le fichier peut alors être mis en cache pour un an, sans risque de version périmée.

**2. Régler les en-têtes par type de ressource.** Avec Nginx, si les fichiers versionnés sont rangés dans un répertoire dédié :

```nginx
# Fichiers versionnés par l'outil de build : un an, sans revalidation
location /build/ {
    add_header Cache-Control "public, max-age=31536000, immutable";
}

# Pages HTML : conservées, mais revalidées à chaque visite (304 si inchangées)
location / {
    add_header Cache-Control "no-cache";
}

# Espace connecté : rien en cache
location /compte/ {
    add_header Cache-Control "private, no-store";
}
```

Attention à une règle de Nginx : d'après sa [documentation](https://nginx.org/en/docs/http/ngx_http_headers_module.html), les directives `add_header` d'un niveau supérieur ne s'appliquent que « if and only if there are no add_header directives defined on the current level ». Un `add_header` dans un bloc `location` fait donc disparaître les en-têtes de sécurité définis au niveau `server`, sauf à les répéter (ou à utiliser `add_header_inherit`, depuis Nginx 1.29.3).

**3. Mettre en cache les réponses d'API stables** (fiches RWEB 0072 et 0021). Le plus simple est d'envoyer un `Cache-Control` depuis l'API elle-même : `fetch()` utilise le cache HTTP du navigateur, sans code supplémentaire.

```http
GET /api/communes?departement=44

HTTP/2 200
Cache-Control: public, max-age=86400
ETag: "communes-44-2026-10"
```

Le stockage local (`localStorage`, IndexedDB) ne se justifie que pour des données que le cache HTTP ne couvre pas, par exemple pour un fonctionnement hors ligne. Il ne doit pas contenir de données personnelles sur un poste partagé.

**4. Choisir le mode hors ligne au cas par cas.** Un service worker qui garde les écrans essentiels est très utile à un agent sur le terrain, en zone mal couverte (voir le [critère 2.3](../../specifications/2-3_connexion-bas-debit/)). Pour un site de contenus consulté ponctuellement, il fait souvent télécharger plus qu'il n'économise.

**5. Tester au-delà de la visite immédiate.** Le test du RGESN, revenir sur le service et vérifier que les contenus viennent du cache, est réussi par presque tous les sites quand on revient dans la minute : même un fichier sans en-tête reste en cache quelques minutes. Pour juger une stratégie :

- dans les outils de développement, onglet **Réseau**, ajouter la colonne `Cache-Control` (clic droit sur les en-têtes de colonnes, « En-têtes de réponse ») et vérifier la valeur de chaque type de ressource ;
- revenir sur le service le lendemain, ou après une mise en production : la colonne « Taille » signale un fichier réutilisé depuis le cache (« disk cache »), et le statut 304 une revalidation ;
- en ligne de commande, `curl -sI https://exemple.fr/build/app.css | grep -i cache-control`.

**6. Documenter** la stratégie dans la déclaration d'écoconception. Par exemple : « Fichiers statiques versionnés (CSS, JavaScript, polices, images d'interface) : un an (`immutable`). Pages HTML : revalidation à chaque visite (`no-cache`). Espace connecté : aucun cache (`no-store`). Liste des communes : un jour. Pas de mode hors ligne, le service étant consulté ponctuellement. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Ce critère est le premier levier du budget fixé par le [critère 6.1](../6-1_poids-requetes-ecran/) (poids et requêtes par écran) : à la deuxième visite, un cache bien réglé ramène le poids d'un écran de près de 1 Mo à quelques kilo-octets (voir les retours d'expériences).

Il croise aussi plusieurs critères déjà publiés sur ce site :

- le [critère 2.3](../../specifications/2-3_connexion-bas-debit/) (connexion bas débit ou hors connexion), pour la question du mode hors ligne ;
- le [critère 4.9](../../ux-ui/4-9_requetes-saisie-utilisateur/) (requêtes lors de la saisie) : une liste de suggestions mise en cache évite de redemander les mêmes résultats à chaque frappe ;
- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) : depuis le cloisonnement du cache par site, une ressource tierce n'est plus partagée entre sites, ce qui plaide pour héberger soi-même ses ressources ;
- le [critère 6.3](../6-3_compression-ressources/) (compression) : un fichier précompressé au déploiement se met en cache comme les autres, à condition d'envoyer l'en-tête `Vary: Accept-Encoding`.

Le critère 7.1 (cache côté serveur), dans la famille Backend, et le critère 6.7 (ressources hébergées sur un même domaine), complètent celui-ci.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) valide les critères 6.2 et 7.1 ensemble, avec côté terminal la « mise en cache des fichiers statiques par le navigateur ».

Cinq sites ont été analysés le 20 octobre 2026 dans Chromium 155 : une première visite, puis une seconde dans un nouvel onglet. À la seconde visite, tous servent plus de 90 % de leurs ressources depuis le cache. Le test du RGESN, appliqué tel quel, les valide donc tous. Pour aller plus loin, les en-têtes de chaque ressource ont été relevés et la règle de Chromium appliquée, pour estimer ce qui resterait en cache **un jour plus tard**, sans mise en production entre-temps :

| Site | Stratégie observée | Au bout d'un jour |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | Fichiers versionnés (`/build/app.7a0495ae.css`) gardés un an ; page HTML revalidée | 32 ressources sur 36 en cache |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | La plupart des fichiers sans `Cache-Control` : durée devinée par le navigateur | 47 sur 52 en cache, 4 à revalider |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | La plupart des fichiers sans `Cache-Control` ; page HTML `no-store` | 28 sur 45 en cache, 16 à revalider |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) (GitHub Pages) | Tous les fichiers à 10 minutes (`max-age=600`) | 0 sur 29 en cache, 28 à revalider |

**DiaLog** applique la stratégie de l'onglet « Mise en œuvre technique » : sa page d'accueil passe de 1 042 Ko à la première visite à 7 Ko à la seconde. Les sites sans `Cache-Control` fonctionnent correctement, mais au hasard de l'ancienneté de leurs fichiers.

{{% /tab %}}

{{< /tabs >}}
