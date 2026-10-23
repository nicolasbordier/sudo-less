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

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache deux fiches au critère 6.3, une par technique citée par le RGESN.

[**RWEB 0076 — « Compresser les fichiers texte : CSS, JS, HTML et SVG »**](https://rweb.greenit.fr/fr/fiches/RWEB_0076-compresser-les-fichiers-css-javascript-html-et-svg) ajoute le **SVG** aux exemples du RGESN : une image SVG est un fichier texte, qui se compresse comme une feuille de style. La fiche présente Brotli, « supporté par tous les navigateurs les plus répandus » (97 % des utilisateurs d'après [Can I Use](https://caniuse.com/brotli)), et donne un exemple Nginx qui charge deux modules, l'un pour compresser à la volée, l'autre pour servir des fichiers précompressés, puis active `brotli on`. Deux précisions avant de le recopier :

- ces modules ne font pas partie de Nginx : ils viennent du projet [ngx_brotli](https://github.com/google/ngx_brotli) de Google, à compiler ou à installer depuis sa distribution (paquets `libnginx-mod-http-brotli-filter` et `libnginx-mod-http-brotli-static` sous Debian). Nginx 1.31.7, la version du 14 octobre 2026, ne propose toujours que gzip ;
- d'après la documentation du module, `brotli_types` vaut par défaut `text/html` : `brotli on` seul ne compresse que les pages HTML, pas les CSS, JavaScript et SVG de la fiche. Il faut lister ces types, et ajouter `brotli_static on` pour que le second module serve réellement les fichiers précompressés.

Son principe de validation est strict : **aucun** fichier CSS, JavaScript, HTML ou SVG non compressé. Pour les tout petits fichiers, voir l'onglet « Gzip, Brotli, Zstandard ».

[**RWEB 0077 — « Minifier les fichiers CSS, JavaScript, HTML et SVG »**](https://rweb.greenit.fr/fr/fiches/RWEB_0077-minifier-les-fichiers-css-javascript-html-et-svg) couvre la minification, avec le même principe : aucun fichier non minifié. Parmi les outils cités, deux ne sont plus mis à jour : HTMLMinifier, dont la dernière version date d'avril 2019 et qui garde une faille de déni de service non corrigée ([CVE-2022-37620](https://nvd.nist.gov/vuln/detail/CVE-2022-37620)), remplacé par son fork [html-minifier-terser](https://github.com/terser/html-minifier-terser), et Babel-minify, resté à la version 0.5.2 de mai 2022. [Terser](https://terser.org/), [cssnano](https://cssnano.github.io/cssnano/), [htmlnano](https://github.com/maltsev/htmlnano) et [SVGO](https://svgo.dev/) restent maintenus.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Le [GR491](https://gr491.isit-europe.org/) (INR) pose la question directement dans la [recommandation n°7 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=7), en priorité **High** et en difficulté minimale : [« Les fichiers échangés sont-ils compressés ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-le-volume-de-donnees-transfere-augmente-lempreinte-c04347) Sa règle d'évaluation est un ratio, « Fichiers compressés / Fichiers échangés », à revoir à chaque mise à jour du service. Son test va plus loin que le RGESN : « La compression est-elle efficace ? » Un service peut compresser ses pages et oublier ses SVG, ou compresser au niveau le plus faible (voir les retours d'expériences).

La fiche donne aussi une indication de méthode : « l'opération de compression nécessitant des ressources de calcul et de stockage intermédiaire il est plus efficace que les données soient disponibles sous forme compressée ». Autrement dit, compresser les fichiers statiques **une fois**, au déploiement, plutôt qu'à chaque requête (voir l'onglet « Mise en œuvre technique »).

Le conseil [« Les volumétries d'échanges sont-elles évaluées et réduites avec les traitements techniques les plus pertinents (compression/minification) ? »](https://gr491.isit-europe.org/crit.php?id=6-frontend-les-echanges-indispensables-doivent-permettre-de-reduire-76e6aa), dans la [recommandation n°6](https://gr491.isit-europe.org/?famille=frontend&num_reco=6), reprend la mise en garde du RGESN : « les opérations de compression et décompression nécessitent des exécutions de traitements qui peuvent annuler le bénéfice de la compression des échanges ». Les mesures de l'onglet « Gzip, Brotli, Zstandard » permettent de situer ce risque : il porte sur la compression côté serveur aux niveaux élevés, pas sur la décompression.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) consacrent deux fiches au sujet.

La fiche [**« Reduce data transfer with compression »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-data-transfer-with-compression) demande de compresser les réponses du serveur « while balancing processing costs ». Son critère de succès « Server-side compression » ajoute « when appropriate » : comme le RGESN, le W3C ne demande pas de tout compresser à tout prix. Son exemple, une configuration Apache, est utile à lire de près :

- il liste explicitement les types à compresser, dont `image/svg+xml`, `application/json` et les polices TTF et OTF, et omet les formats déjà compressés (JPEG, PNG, WOFF2) ;
- il rétablit l'en-tête `Accept-Encoding` que certains proxys ou antivirus altèrent (`Accept-EncodXng`, `X-cept-Encoding`) : sans cette correction, le serveur croirait que le navigateur ne sait pas décompresser. C'est un cas concret de la compression « de bout en bout » du RGESN ;
- il n'active que gzip (module `mod_deflate`). Brotli demande le module [`mod_brotli`](https://httpd.apache.org/docs/2.4/mod/mod_brotli.html), disponible depuis Apache 2.4.26.

Le second critère de succès, « Media compression », concerne les images, vidéos et sons, traités par les critères [5.2](../../contenus/5-2_compression-images/), [5.4](../../contenus/5-4_compression-videos/) et [5.6](../../contenus/5-6_compression-audio/).

La fiche [**« Minify and remove unused code »**](https://www.w3.org/TR/web-sustainability-guidelines/#minify-and-remove-unused-code) couvre la minification, avec une condition : « Ensure that minification does not introduce any errors ». Son second critère, « Remove redundancy », vise le code inutilisé, le sujet du critère 6.5.

{{% /tab %}}

{{% tab tabName="Gzip, Brotli, Zstandard" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

Le RGESN conseille « Brotli ou GZIP » et met en garde contre la puissance de calcul nécessaire pour « décompresser ». Pour en juger, la feuille de style et le JavaScript minifiés du [Système de design de l'État](https://www.systeme-de-design.gouv.fr/) (DSFR 1.15.4), utilisés par trois des sites des retours d'expériences, ont été compressés avec chaque algorithme :

| Algorithme et niveau | CSS (728 Ko) | JavaScript (115 Ko) | Compression du CSS | Décompression du CSS |
|---|---:|---:|---:|---:|
| gzip 1 (défaut de Nginx) | 125,3 Ko | 36,4 Ko | 3 ms | 1,2 ms |
| gzip 6 | 94,1 Ko | 30,0 Ko | 10 ms | 1,0 ms |
| gzip 9 | 93,6 Ko | 29,9 Ko | 21 ms | 1,0 ms |
| Brotli 5 | 79,2 Ko | 28,5 Ko | 6 ms | 0,6 ms |
| Brotli 11 | 62,2 Ko | 25,9 Ko | 774 ms | 0,6 ms |
| Zstandard 3 | 98,9 Ko | 32,0 Ko | 1 ms | 0,4 ms |
| Zstandard 19 | 67,7 Ko | 27,5 Ko | 201 ms | 0,3 ms |

**La décompression ne coûte presque rien.** Elle prend 1,2 ms au plus pour 728 Ko, quel que soit l'algorithme. Même dix fois plus lente sur un smartphone d'entrée de gamme, elle resterait de l'ordre de 10 ms. Le transfert, lui, se compte en secondes : à 512 kbit/s (le débit du [critère 2.3](../../specifications/2-3_connexion-bas-debit/)), la feuille de style demande 11,4 s sans compression, 1,5 s en gzip 6 et 1 s en Brotli 11.

**La compression coûte au serveur, surtout aux niveaux élevés.** Brotli 11 met 774 ms pour cette feuille de style, plus de cent fois plus que Brotli 5. C'est acceptable une fois, au déploiement, pas à chaque requête. D'où deux réglages :

- pour un **fichier statique**, compresser une fois au niveau maximal (Brotli 11, gzip 9) et servir le fichier précompressé ;
- pour une **page ou une réponse d'API** générée à chaque requête, un niveau intermédiaire. Brotli 5 est à la fois plus rapide et plus efficace que gzip 6. Gzip 9 n'apporte presque rien sur gzip 6 pour un temps doublé ; à l'inverse, gzip 1, le niveau par défaut de Nginx, laisse un fichier un tiers plus lourd.

**Zstandard compresse vite, Brotli compresse mieux.** Zstandard 3 compresse sept à huit fois plus vite que gzip 6, pour un fichier à peine plus lourd (5 à 7 %). Il intéresse surtout les serveurs qui compressent beaucoup de réponses dynamiques. Pour les fichiers statiques, Brotli 11 reste le plus efficace.

**Le support des navigateurs.** D'après [Can I Use](https://caniuse.com/zstd), Brotli est compris par 97 % des utilisateurs, Zstandard par 83 % : Chrome et Edge depuis la version 123 (2024), Firefox depuis la 126, Safari depuis la 26.3 seulement, et pas Samsung Internet. Le navigateur annonce ce qu'il accepte (Chromium 155 envoie `Accept-Encoding: gzip, deflate, br, zstd`) et le serveur choisit : proposer Zstandard ou Brotli ne dispense pas de garder gzip. D'après le [Web Almanac 2025](https://almanac.httparchive.org/en/2025/cdn) de l'HTTP Archive, sur mobile, les CDN servent 46 % de leurs réponses compressées en Brotli, 42 % en gzip et 12 % en Zstandard ; les serveurs d'origine, 61 % en gzip et 39 % en Brotli.

**Les petits fichiers.** La mise en garde du RGESN se vérifie en dessous de quelques centaines d'octets :

| Fichier | Taille | gzip 9 | Brotli 11 |
|---|---:|---:|---:|
| Réponse JSON pour une commune ([API Découpage administratif](https://geo.api.gouv.fr/decoupage-administratif)) | 51 o | 68 o | 50 o |
| Icône SVG du DSFR (`arrow-right-line`) | 89 o | 97 o | 76 o |
| Icône SVG du DSFR (`close-line`) | 210 o | 167 o | 144 o |
| Icône SVG du DSFR (`account-pin-circle-line`) | 575 o | 340 o | 320 o |
| Liste des communes de Loire-Atlantique (JSON) | 8 039 o | 2 095 o | 1 734 o |

En dessous d'une centaine d'octets, gzip **alourdit** le fichier : son en-tête et sa fin de flux pèsent une vingtaine d'octets. Brotli s'en sort mieux, avec un en-tête plus léger et un dictionnaire de mots et de fragments de code courants intégré à son format ([RFC 7932](https://www.rfc-editor.org/rfc/rfc7932)). Au-delà de quelques centaines d'octets, la compression est nettement gagnante. Les serveurs fixent donc un seuil : 20 octets par défaut pour Nginx (`gzip_min_length`), 512 pour [Caddy](https://caddyserver.com/docs/caddyfile/directives/encode) (`minimum_length`), et 256 observés sur GitHub Pages (voir les retours d'expériences).

{{% /tab %}}

{{% tab tabName="Minifier et compresser" %}}

Profil(s) métier concerné(s) : `Développeur`

Le RGESN demande la compression **et** la minification. Les deux se cumulent, mais pas dans les mêmes proportions selon le type de fichier. Mesures du 21 octobre 2026, sur les versions source et minifiée publiées par les projets eux-mêmes :

| Fichier | Taille brute | gzip 6 | Brotli 11 |
|---|---:|---:|---:|
| jQuery 3.7.1, source | 285,3 Ko | 84,1 Ko | 69,5 Ko |
| jQuery 3.7.1, minifié | 87,5 Ko | 30,4 Ko | 27,4 Ko |
| DSFR 1.15.4, JavaScript source | 187,1 Ko | 39,8 Ko | 33,0 Ko |
| DSFR 1.15.4, JavaScript minifié | 115,3 Ko | 30,0 Ko | 25,9 Ko |
| DSFR 1.15.4, CSS source | 868,6 Ko | 102,8 Ko | 68,4 Ko |
| DSFR 1.15.4, CSS minifié | 728,0 Ko | 94,1 Ko | 62,2 Ko |

**La compression fait l'essentiel.** Elle divise chaque fichier par 3 à 13. Une fois les fichiers compressés en gzip, la minification apporte encore 64 % sur jQuery, 25 % sur le JavaScript du DSFR, et moins de 10 % sur sa feuille de style.

**Pourquoi un tel écart ?** La compression repère les répétitions : les espaces d'indentation et les retours à la ligne, très répétitifs, ne lui coûtent presque rien. Ce que la minification apporte en plus, ce sont les suppressions qu'aucun algorithme de compression ne peut faire : les commentaires (nombreux dans la source de jQuery) et, pour le JavaScript, le raccourcissement des noms de variables. Une feuille de style n'a pas de variables à renommer, d'où le faible gain.

**En pratique** : minifier le JavaScript est indispensable, minifier le CSS et le HTML est un complément peu coûteux, puisque les outils de build le font sans effort. Les deux ensemble ramènent jQuery de 285 Ko à 27 Ko, soit −90 %.

La minification a ses limites : une feuille de style minifiée et compressée de 62 Ko reste lourde si la page n'en utilise qu'une petite partie. Ne charger que les styles et scripts utiles relève du critère 6.5.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Administrateur Système`

**1. Lister ce qui doit être compressé.** Tous les fichiers texte : HTML, CSS, JavaScript, **SVG**, JSON, XML, texte brut, WebAssembly. Pas les formats déjà compressés (JPEG, PNG, WebP, AVIF, MP4, WOFF2) : les recompresser consomme du calcul sans rien gagner. Une police WOFF2 est déjà compressée en Brotli dans son format (voir le [critère 4.8](../../ux-ui/4-8_polices-caracteres/)).

**2. Minifier au build.** Les outils de build intègrent un minifieur pour le JavaScript et le CSS ([esbuild](https://esbuild.github.io/), [Terser](https://terser.org/), [Lightning CSS](https://lightningcss.dev/), [cssnano](https://cssnano.github.io/cssnano/)) ; Hugo minifie aussi le HTML avec `hugo build --minify` ; [SVGO](https://svgo.dev/) traite les SVG. Vérifier ensuite que le service fonctionne toujours, comme le demande le W3C.

**3. Précompresser les fichiers statiques au déploiement**, au niveau maximal, en gardant l'original :

```sh
# Fichiers texte de 256 octets et plus : .gz (gzip 9) et .br (Brotli 11) à côté de l'original
find public -type f -size +255c \
  \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.svg' -o -name '*.json' -o -name '*.xml' \) \
  -exec gzip -k -n -9 {} \; -exec brotli -k -q 11 {} \;
```

Certains outils le font eux-mêmes : [Symfony AssetMapper](https://symfony.com/doc/current/frontend/asset_mapper.html), par exemple, avec son option `precompress` (Brotli, Zstandard ou gzip).

**4. Configurer le serveur** pour servir les fichiers précompressés et compresser le reste à la volée, à un niveau intermédiaire. Avec Nginx :

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

D'après la [documentation de Nginx](https://nginx.org/en/docs/http/ngx_http_gzip_module.html), `gzip_types` vaut par défaut `text/html` : sans cette ligne, CSS, JavaScript et SVG partent non compressés. Avec `gzip_proxied off`, la valeur par défaut, Nginx ne compresse pas les réponses aux requêtes qui portent un en-tête `Via`, c'est-à-dire celles relayées par un proxy ou un CDN. Le module `gzip_static` n'est pas compilé par défaut dans Nginx, mais il est présent dans les paquets des principales distributions. Avec Apache, ce sont les modules `mod_deflate` et `mod_brotli` ; avec Caddy, `encode` compresse en Zstandard et gzip et `file_server` sert les fichiers précompressés (option `precompressed`). Le PDF du RGESN cite aussi l'extension IIS Brotli pour Microsoft IIS.

**5. Ne pas oublier `Vary: Accept-Encoding`.** Cet en-tête indique aux caches (navigateur, proxy, CDN) que la réponse dépend de ce que le client accepte. Sans lui, un cache partagé peut resservir une version Brotli à un client qui ne la comprend pas, ou une version non compressée à tous (voir le [critère 6.2](../6-2_cache-navigateur/)).

**6. Vérifier de bout en bout**, depuis l'extérieur, car un CDN ou un proxy peut changer le résultat :

- dans les outils de développement, onglet **Réseau**, ajouter la colonne `Content-Encoding` (clic droit sur les en-têtes de colonnes, « En-têtes de réponse ») et comparer, pour chaque type de fichier, la taille transférée à la taille de la ressource ;
- en ligne de commande, vérifier chaque type de fichier et chaque algorithme :

```sh
for f in / /build/app.css /build/app.js /images/logo.svg; do
  for ae in br gzip; do
    printf '%-20s %-5s ' "$f" "$ae"
    curl -s -o /dev/null -D - -H "Accept-Encoding: $ae" "https://exemple.fr$f" | grep -i '^content-encoding' || echo 'non compressé'
  done
done
```

Lighthouse ne suffit plus pour ce contrôle : depuis sa version 13 (octobre 2025), l'audit « Enable text compression » a été remplacé par l'indicateur « Document request latency », qui ne vérifie la compression que du **document HTML** principal, pas celle des CSS, scripts et SVG.

**7. Garder un œil sur la sécurité.** La documentation de Nginx le rappelle : en HTTPS, les réponses compressées « may be subject to BREACH attacks ». Le risque concerne les réponses qui contiennent à la fois un secret (un jeton CSRF, par exemple) et un texte saisi par l'utilisateur. Les frameworks courants s'en protègent en masquant leur jeton différemment à chaque réponse ([Django](https://docs.djangoproject.com/en/stable/ref/csrf/), par exemple). Ce n'est pas une raison de désactiver la compression des fichiers statiques.

**8. Documenter** dans la déclaration d'écoconception. Par exemple : « Fichiers statiques (CSS, JavaScript, SVG, JSON) minifiés et précompressés au déploiement en Brotli 11 et gzip 9. Pages HTML et réponses d'API compressées à la volée (Brotli 5, gzip 5). Seuil : 256 octets. Formats déjà compressés (images, vidéos, polices WOFF2) exclus. Contrôle par type de fichier à chaque mise en production. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La compression est le levier le moins coûteux du budget fixé par le [critère 6.1](../6-1_poids-requetes-ecran/) : elle divise le poids des fichiers texte par cinq à sept environ sur les sites mesurés, sans toucher au code. Le poids qui compte pour le budget est le poids **transféré**, après compression.

Critères déjà publiés sur ce site :

- le [critère 5.2](../../contenus/5-2_compression-images/) (compression des images), avec lequel le RGESN demande de ne pas confondre celui-ci : le 5.2 règle la qualité d'encodage d'une image, le 6.3 la compression des fichiers texte pendant le transfert. Une image JPEG ou WebP ne gagne rien à être compressée en gzip ;
- le [critère 5.1](../../contenus/5-1_format-images/) (format des images) : un SVG minifié reste un fichier texte, à compresser comme les autres ;
- le [critère 6.2](../6-2_cache-navigateur/) (cache) : un fichier précompressé et versionné se met en cache pour un an, et l'en-tête `Vary: Accept-Encoding` garantit que chaque client reçoit la version qu'il comprend ;
- le [critère 4.8](../../ux-ui/4-8_polices-caracteres/) (polices) : le format WOFF2 intègre déjà la compression Brotli ;
- le [critère 3.3](../../architecture/3-3_evolution-protocoles/) (évolution des protocoles) compare les formats binaires au JSON compressé en gzip : face à un JSON déjà compressé, les formats sans schéma (MessagePack, CBOR) ne gagnent plus qu'environ 8 %.

Le critère 6.5 (chargement des seules ressources utiles), pas encore publié sur ce site, prend le relais là où la compression s'arrête : ne pas envoyer le code inutile du tout.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Cinq sites ont été relevés le 21 octobre 2026 dans Chromium 155, qui annonce `Accept-Encoding: gzip, deflate, br, zstd` : page d'accueil, premier chargement. Chaque fichier texte hébergé par le site lui-même (HTML, CSS, JavaScript, SVG) a ensuite été redemandé avec curl en n'acceptant que gzip, que Brotli ou que Zstandard, puis compressé en Brotli (niveau 11 pour les fichiers statiques, 5 pour la page HTML) pour estimer le gain possible.

| Site | Compression proposée | Fichiers texte : brut → transféré | Fichiers non compressés | Estimation, tout en Brotli |
|---|---|---:|---|---:|
| [DiaLog](https://dialog.beta.gouv.fr/) | gzip | 2 638 Ko → 553 Ko | 11 icônes SVG (3,4 Ko) | 435 Ko (−21 %) |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | Brotli et gzip | 1 581 Ko → 309 Ko | 9 SVG (8,1 Ko) | 278 Ko (−10 %) |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | gzip | 2 253 Ko → 416 Ko | 24 SVG (61 Ko) | 287 Ko (−31 %) |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) (GitHub Pages) | gzip | 1 648 Ko → 247 Ko | 8 icônes SVG de moins de 256 octets (1,7 Ko) | 180 Ko (−27 %) |

**Tous valident le critère tel qu'il est rédigé** : leurs pages, feuilles de style et scripts arrivent compressés, et la compression divise leur poids par cinq à sept. Aucun ne propose Zstandard. Le test du GR491, « La compression est-elle efficace ? », fait apparaître trois marges de progrès.

**Les SVG oubliés.** DiaLog et SPOTE ne compressent aucun de leurs SVG. Chez DiaLog, ce sont de petites icônes (3,4 Ko en tout) ; chez SPOTE, 16 fichiers dépassent 256 octets, dont des pictogrammes de 3 à 15 Ko que gzip réduirait de moitié (`system.svg` : 15,3 Ko, 7,3 Ko en gzip). C'est le résultat attendu quand `image/svg+xml` manque à la liste des types compressés, qui ne contient par défaut que `text/html` dans Nginx.

**Brotli, peu utilisé.** Seul le Musée d'arts de Nantes l'emploie, pour la plupart de ses CSS et scripts. Sa page HTML, elle, est envoyée en gzip, alors que Chromium accepte Brotli. À l'inverse, la plupart de ses feuilles de style et scripts ne sont proposés qu'en Brotli : un client qui n'accepte que gzip reçoit la feuille de style principale non compressée (492 Ko). Pour les quatre autres sites, Brotli réduirait encore le poids des fichiers texte de 21 à 31 %. Le gros fichier JavaScript de DiaLog passerait de 393 Ko en gzip à 312 Ko.

**GitHub Pages ne se règle pas.** Le site du RGESN et celui-ci partagent la limite déjà relevée pour le cache au [critère 6.2](../6-2_cache-navigateur/) : GitHub Pages compresse en gzip seulement, sans option Brotli. Il ne compresse pas les fichiers de moins de **256 octets** : testé sur des icônes du site du RGESN, une icône de 255 octets part non compressée, une de 256 octets compressée, un seuil raisonnable au regard de l'onglet « Gzip, Brotli, Zstandard ». L'absence de Brotli rejoint le Web Almanac 2025, d'après lequel gzip reste majoritaire chez Fastly, le CDN de GitHub Pages.

**Ce que disent les déclarations.** [DiaLog](https://dialog.beta.gouv.fr/ecoconception) marque le critère « Validé » dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf) : « Mécanismes de compression mis en place côté front-end », avec pour évolution possible de « compresser davantage les logos d'organisation sans altérer la qualité ». Cette évolution relève du [critère 5.2](../../contenus/5-2_compression-images/), celui que le RGESN demande justement de ne pas confondre avec le 6.3. Pour le 6.3, le levier mesurable est Brotli. La [déclaration du Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) classe le critère « En cours de validation » : « Certains fichiers (notamment JS) ne sont pas compressés. » Le relevé ne le confirme pas pour le transfert : tous les scripts arrivent compressés. Il le confirme pour la **minification** : `tarteaucitron.services.js` (220 Ko) et `tarteaucitron.js` (112 Ko), le gestionnaire de consentement, sont servis dans leur version source.

**SPOTE**, enfin, montre une minification à moitié faite. Son fichier JavaScript principal (540 Ko : jQuery, jQuery UI et des modules de SPIP) est « compacté » par SPIP, qui retire commentaires et indentation, mais garde les noms de variables et les retours à la ligne. Le site charge aussi le noyau du DSFR 1.14.2 en version source (`core.module.js`, 95 Ko), en plus du DSFR 1.12.1 complet minifié. Ce doublon relève plutôt du critère 6.5.

{{% /tab %}}

{{< /tabs >}}
