---
weight: 300
title: "6.3 - Compression des ressources transférées"
description: "Critère 6.3 du RGESN : compresser tous les fichiers texte (HTML, CSS, JavaScript, SVG, JSON), choisir entre gzip, Brotli et Zstandard selon le moment de la compression, minifier le code et vérifier le résultat type de fichier par type de fichier."
icon: "compress"
date: "2026-10-21T00:00:00+01:00"
lastmod: "2026-10-21T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il mis en place des techniques de compression pour les ressources transférées dont il a le contrôle ?

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
| **Critère**  | `6.3` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas de connexion réseau internet` |
| **Métiers concernés** | `Développeur` `Administrateur Système` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire la quantité de ressources transférées sur le réseau via la compression des données.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Mettre en place la compression, minification (réduction de la taille du code) des fichiers de scripts. Attention toutefois à ne pas générer de la consommation de ressources s'il y a besoin de puissance de calcul pour « décompresser » les fichiers : la compression systématique de type « .tgz » par exemple pour des petits fichiers peut être contreproductive. Ce critère s'applique uniquement aux fichiers texte (HTML, CSS, JavaScript par exemple).

Veiller à mettre en place une compression de bout en bout (exemple : [Documentation Mozilla sur la compression dans HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP/Guides/Compression)). Il faudra faire appel à des mécanismes de compression de flux pour minimiser le volume du trafic échangé. Favoriser, lorsque cela est possible, le mécanisme de compression le plus efficace.

Par exemple, pour HTTP plusieurs protocoles de compression existent, tels en particulier Brotli et GZIP.

Ne pas confondre avec le [critère 5.2](../../contenus/5-2_compression-images/) sur la compression des images (qui n'aborde pas la compression lors du transfert).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si les requêtes du service numérique utilisent un mécanisme de compression des données au niveau du frontend. Pour le protocole HTTP et la compression HTML, les mécanismes de compression Brotli ou GZIP sont conseillés.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache deux fiches au critère 6.3, avec le même principe de validation strict : **aucun** fichier non traité.

- [**RWEB 0076 — « Compresser les fichiers texte : CSS, JS, HTML et SVG »**](https://rweb.greenit.fr/fr/fiches/RWEB_0076-compresser-les-fichiers-css-javascript-html-et-svg) ajoute le **SVG** aux exemples du RGESN : c'est un fichier texte, qui se compresse comme une feuille de style. Son exemple Nginx demande deux précisions. Les modules Brotli ne font pas partie de Nginx : ils viennent du projet [ngx_brotli](https://github.com/google/ngx_brotli), packagé sous Debian. Et `brotli on` seul ne compresse que le HTML, car `brotli_types` vaut par défaut `text/html` ;
- [**RWEB 0077 — « Minifier les fichiers CSS, JavaScript, HTML et SVG »**](https://rweb.greenit.fr/fr/fiches/RWEB_0077-minifier-les-fichiers-css-javascript-html-et-svg) : deux des outils cités ne sont plus maintenus, HTMLMinifier, remplacé par son fork [html-minifier-terser](https://github.com/terser/html-minifier-terser), et Babel-minify. [Terser](https://terser.org/), [cssnano](https://cssnano.github.io/cssnano/), [htmlnano](https://github.com/maltsev/htmlnano) et [SVGO](https://svgo.dev/) le sont toujours.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

La [recommandation n°7 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=7) du [GR491](https://gr491.isit-europe.org/) (INR) demande, en priorité **High** : [« Les fichiers échangés sont-ils compressés ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-le-volume-de-donnees-transfere-augmente-lempreinte-c04347) Son test va plus loin que le RGESN : « La compression est-elle efficace ? » Un service peut compresser ses pages et oublier ses SVG (voir les retours d'expériences). Elle conseille aussi que les données soient « disponibles sous forme compressée » : compresser les fichiers statiques **une fois**, au déploiement, plutôt qu'à chaque requête.

La [recommandation n°6](https://gr491.isit-europe.org/?famille=frontend&num_reco=6) reprend la mise en garde du RGESN : la compression et la décompression « peuvent annuler le bénéfice de la compression des échanges ». Les mesures de l'onglet « Gzip, Brotli, Zstandard » situent ce risque : il porte sur la compression aux niveaux élevés, pas sur la décompression.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

La fiche [**« Reduce data transfer with compression »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-data-transfer-with-compression) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) demande de compresser les réponses du serveur « while balancing processing costs ». Son exemple Apache est utile à lire de près :

- il liste les types à compresser, dont `image/svg+xml` et `application/json`, et omet les formats déjà compressés (JPEG, PNG, WOFF2) ;
- il rétablit l'en-tête `Accept-Encoding` que certains proxys ou antivirus altèrent : un cas concret de la compression « de bout en bout » du RGESN ;
- il n'active que gzip. Brotli demande le module [`mod_brotli`](https://httpd.apache.org/docs/2.4/mod/mod_brotli.html).

La fiche [**« Minify and remove unused code »**](https://www.w3.org/TR/web-sustainability-guidelines/#minify-and-remove-unused-code) ajoute une condition à la minification : « Ensure that minification does not introduce any errors ».

{{% /tab %}}

{{% tab tabName="Gzip, Brotli, Zstandard" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Le RGESN met en garde contre la puissance de calcul nécessaire pour « décompresser ». Pour en juger, la feuille de style et le JavaScript minifiés du [Système de design de l'État](https://www.systeme-de-design.gouv.fr/) (DSFR 1.15.4) ont été compressés avec chaque algorithme :

| Algorithme et niveau | CSS (728 Ko) | JavaScript (115 Ko) | Compression du CSS | Décompression du CSS |
|---|---:|---:|---:|---:|
| gzip 1 (défaut de Nginx) | 125,3 Ko | 36,4 Ko | 3 ms | 1,2 ms |
| gzip 6 | 94,1 Ko | 30,0 Ko | 10 ms | 1,0 ms |
| gzip 9 | 93,6 Ko | 29,9 Ko | 21 ms | 1,0 ms |
| Brotli 5 | 79,2 Ko | 28,5 Ko | 6 ms | 0,6 ms |
| Brotli 11 | 62,2 Ko | 25,9 Ko | 774 ms | 0,6 ms |
| Zstandard 3 | 98,9 Ko | 32,0 Ko | 1 ms | 0,4 ms |

**La décompression ne coûte presque rien** : 1,2 ms au plus. Le transfert, lui, se compte en secondes : à 512 kbit/s (le débit du [critère 2.3](../../specifications/2-3_connexion-bas-debit/)), cette feuille de style demande 11,4 s sans compression, 1,5 s en gzip 6 et 1 s en Brotli 11.

**La compression coûte au serveur aux niveaux élevés** : 774 ms en Brotli 11. D'où deux réglages :

- pour un **fichier statique**, compresser une fois au niveau maximal (Brotli 11, gzip 9) et servir le fichier précompressé ;
- pour une **réponse générée à chaque requête**, un niveau intermédiaire : Brotli 5 est plus rapide et plus efficace que gzip 6. Gzip 1, le défaut de Nginx, laisse un fichier un tiers plus lourd.

**Zstandard compresse vite** : sept à huit fois plus vite que gzip 6, pour un fichier 5 à 7 % plus lourd. Il n'est compris que par 83 % des utilisateurs, contre 97 % pour Brotli ([Can I Use](https://caniuse.com/zstd)) : gzip reste nécessaire en repli.

**Les petits fichiers.** La mise en garde du RGESN se vérifie en dessous de quelques centaines d'octets :

| Fichier | Taille | gzip 9 | Brotli 11 |
|---|---:|---:|---:|
| Réponse JSON pour une commune ([API Découpage administratif](https://geo.api.gouv.fr/decoupage-administratif)) | 51 o | 68 o | 50 o |
| Icône SVG du DSFR (`arrow-right-line`) | 89 o | 97 o | 76 o |
| Icône SVG du DSFR (`account-pin-circle-line`) | 575 o | 340 o | 320 o |
| Liste des communes de Loire-Atlantique (JSON) | 8 039 o | 2 095 o | 1 734 o |

En dessous d'une centaine d'octets, gzip **alourdit** le fichier et Brotli ne gagne presque rien. Les serveurs fixent donc un seuil : 20 octets par défaut pour Nginx, 512 pour [Caddy](https://caddyserver.com/docs/caddyfile/directives/encode), 256 sur GitHub Pages.

{{% /tab %}}

{{% tab tabName="Minifier et compresser" %}}

Profil(s) métier concerné(s) : `Développeur`

Le RGESN demande la compression **et** la minification. Mesures du 21 octobre 2026, sur les versions publiées par les projets eux-mêmes :

| Fichier | Taille brute | gzip 6 | Brotli 11 |
|---|---:|---:|---:|
| jQuery 3.7.1, source | 285,3 Ko | 84,1 Ko | 69,5 Ko |
| jQuery 3.7.1, minifié | 87,5 Ko | 30,4 Ko | 27,4 Ko |
| DSFR 1.15.4, CSS source | 868,6 Ko | 102,8 Ko | 68,4 Ko |
| DSFR 1.15.4, CSS minifié | 728,0 Ko | 94,1 Ko | 62,2 Ko |

**La compression fait l'essentiel** : elle divise chaque fichier par 3 à 13. Une fois les fichiers compressés en gzip, la minification apporte encore 64 % sur jQuery, mais moins de 10 % sur la feuille de style du DSFR. Elle supprime ce que la compression ne peut pas : les commentaires et, pour le JavaScript, les noms de variables longs.

**En pratique**, minifier le JavaScript est indispensable ; minifier le CSS et le HTML est un complément peu coûteux. Une feuille de style compressée reste lourde si la page n'en utilise qu'une partie : c'est le sujet du [critère 6.5](../6-5_chargement-ressources/).

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

**1. Lister ce qui doit être compressé** : tous les fichiers texte (HTML, CSS, JavaScript, **SVG**, JSON, XML, WebAssembly), pas les formats déjà compressés (JPEG, PNG, WebP, AVIF, MP4, WOFF2).

**2. Minifier au build** avec [esbuild](https://esbuild.github.io/), [Terser](https://terser.org/), [Lightning CSS](https://lightningcss.dev/) ou [cssnano](https://cssnano.github.io/cssnano/) ; `hugo build --minify` pour le HTML d'un site Hugo ; [SVGO](https://svgo.dev/) pour les SVG. Vérifier ensuite que le service fonctionne toujours.

**3. Précompresser les fichiers statiques au déploiement**, au niveau maximal, en gardant l'original :

```sh
# Fichiers texte de 256 octets et plus : .gz (gzip 9) et .br (Brotli 11) à côté de l'original
find public -type f -size +255c \
  \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.svg' -o -name '*.json' -o -name '*.xml' \) \
  -exec gzip -k -n -9 {} \; -exec brotli -k -q 11 {} \;
```

Certains outils le font eux-mêmes, comme [Symfony AssetMapper](https://symfony.com/doc/current/frontend/asset_mapper.html) avec son option `precompress`.

**4. Configurer le serveur** pour servir les fichiers précompressés et compresser le reste à la volée. Avec Nginx :

```nginx
# Fichiers précompressés au déploiement (.gz, .br), servis sans recalcul
gzip_static on;
brotli_static on;        # module ngx_brotli

# Pages et réponses d'API générées à chaque requête
gzip on;
gzip_comp_level 5;       # 1 par défaut
brotli on;               # module ngx_brotli
brotli_comp_level 5;     # 6 par défaut

# text/html est toujours compressé ; les autres types doivent être listés
gzip_types   text/css application/javascript text/javascript application/json image/svg+xml text/xml text/plain application/wasm;
brotli_types text/css application/javascript text/javascript application/json image/svg+xml text/xml text/plain application/wasm;

gzip_min_length 256;     # 20 octets par défaut
brotli_min_length 256;
gzip_vary on;            # ajoute Vary: Accept-Encoding
gzip_proxied any;        # compresse aussi les requêtes relayées par un proxy ou un CDN
```

Sans `gzip_types`, seul le HTML est compressé ([documentation de Nginx](https://nginx.org/en/docs/http/ngx_http_gzip_module.html)). Avec Apache, ce sont les modules `mod_deflate` et `mod_brotli` ; avec Caddy, `encode` et l'option `precompressed` de `file_server`. L'en-tête `Vary: Accept-Encoding` indique aux caches que la réponse dépend de ce que le client accepte (voir le [critère 6.2](../6-2_cache-navigateur/)).

**5. Vérifier de bout en bout**, depuis l'extérieur, car un CDN ou un proxy peut changer le résultat. Dans l'onglet **Réseau**, ajouter la colonne `Content-Encoding` et comparer, pour chaque type de fichier, la taille transférée à la taille de la ressource. En ligne de commande :

```sh
for f in / /build/app.css /build/app.js /images/logo.svg; do
  for ae in br gzip; do
    printf '%-20s %-5s ' "$f" "$ae"
    curl -s -o /dev/null -D - -H "Accept-Encoding: $ae" "https://exemple.fr$f" | grep -i '^content-encoding' || echo 'non compressé'
  done
done
```

Lighthouse ne suffit plus : depuis sa version 13, il ne vérifie la compression que du document HTML principal.

**6. Garder un œil sur la sécurité.** En HTTPS, une réponse compressée qui contient à la fois un secret (un jeton CSRF) et un texte saisi par l'utilisateur peut être exposée à l'attaque BREACH. Les frameworks courants s'en protègent, comme [Django](https://docs.djangoproject.com/en/stable/ref/csrf/) : ce n'est pas une raison de désactiver la compression des fichiers statiques.

**7. Documenter** dans la déclaration d'écoconception. Par exemple : « Fichiers statiques minifiés et précompressés au déploiement en Brotli 11 et gzip 9. Pages HTML et réponses d'API compressées à la volée (Brotli 5, gzip 5), à partir de 256 octets. Contrôle par type de fichier à chaque mise en production. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La compression est le levier le moins coûteux du budget fixé par le [critère 6.1](../6-1_poids-requetes-ecran/) : elle divise le poids des fichiers texte par cinq à sept sur les sites mesurés, sans toucher au code.

- le [critère 5.2](../../contenus/5-2_compression-images/) (compression des images), à ne pas confondre avec celui-ci : une image JPEG ou WebP ne gagne rien à être compressée en gzip ;
- le [critère 6.2](../6-2_cache-navigateur/) (cache) : un fichier précompressé et versionné se met en cache pour un an ;
- le [critère 4.8](../../ux-ui/4-8_polices-caracteres/) (polices) : le format WOFF2 intègre déjà la compression Brotli ;
- le [critère 3.3](../../architecture/3-3_evolution-protocoles/) (évolution des protocoles) : face à un JSON compressé, les formats binaires sans schéma ne gagnent plus qu'environ 8 % ;
- le [critère 6.5](../6-5_chargement-ressources/) prend le relais : ne pas envoyer du tout le code inutile.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Quatre pages d'accueil ont été relevées le 21 octobre 2026 dans Chromium 155. Chaque fichier texte hébergé par le site a ensuite été redemandé avec curl en n'acceptant que gzip, que Brotli ou que Zstandard, puis compressé en Brotli pour estimer le gain possible.

| Site | Compression proposée | Fichiers texte : brut → transféré | Fichiers non compressés | Estimation, tout en Brotli |
|---|---|---:|---|---:|
| [DiaLog](https://dialog.beta.gouv.fr/) | gzip | 2 638 Ko → 553 Ko | 11 icônes SVG (3,4 Ko) | 435 Ko (−21 %) |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | Brotli et gzip | 1 581 Ko → 309 Ko | 9 SVG (8,1 Ko) | 278 Ko (−10 %) |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | gzip | 2 253 Ko → 416 Ko | 24 SVG (61 Ko) | 287 Ko (−31 %) |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) (GitHub Pages) | gzip | 1 648 Ko → 247 Ko | 8 icônes SVG de moins de 256 octets (1,7 Ko) | 180 Ko (−27 %) |

**Tous valident le critère tel qu'il est rédigé** : leurs pages, feuilles de style et scripts arrivent compressés. Aucun ne propose Zstandard. Le test du GR491, « La compression est-elle efficace ? », fait apparaître trois marges de progrès :

- **les SVG oubliés** : DiaLog et SPOTE n'en compressent aucun. Chez SPOTE, des pictogrammes de 3 à 15 Ko que gzip réduirait de moitié. C'est ce qui arrive quand `image/svg+xml` manque à la liste des types compressés ;
- **Brotli, peu utilisé** : seul le Musée d'arts de Nantes l'emploie, mais pas pour sa page HTML. Et sa feuille de style principale n'est proposée qu'en Brotli : un client qui n'accepte que gzip la reçoit non compressée (492 Ko). Ailleurs, Brotli réduirait encore les fichiers texte de 21 à 31 % ;
- **GitHub Pages ne se règle pas** : le site du RGESN, comme celui-ci, n'a que gzip, et les fichiers de moins de 256 octets n'y sont pas compressés, un seuil raisonnable.

**Ce que disent les déclarations.** DiaLog marque le critère « Validé » dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf). L'évolution qu'elle prévoit, « compresser davantage les logos d'organisation », relève en fait du [critère 5.2](../../contenus/5-2_compression-images/). Le [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) classe le critère « En cours de validation » : « Certains fichiers (notamment JS) ne sont pas compressés. » Tous ses scripts arrivent pourtant compressés. Ce qui manque, c'est la **minification** de son gestionnaire de consentement : `tarteaucitron.services.js` (220 Ko) et `tarteaucitron.js` (112 Ko) sont servis dans leur version source. SPOTE, de son côté, se contente de « compacter » son JavaScript principal (540 Ko) avec SPIP, qui garde les noms de variables.

{{% /tab %}}

{{< /tabs >}}
