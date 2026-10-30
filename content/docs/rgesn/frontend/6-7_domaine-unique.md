---
weight: 700
title: "6.7 - Ressources statiques sur un même domaine"
description: "Critère 6.7 du RGESN : servir toutes les ressources en HTTP/2 ou HTTP/3, regrouper les ressources statiques sur un seul nom de domaine et vérifier le protocole et les domaines de chaque page."
icon: "dns"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique héberge-t-il toutes les ressources statiques transférées dont il est l'émetteur sur un même domaine ?

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
| **Critère**  | `6.7` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas le protocole HTTP` |
| **Métiers concernés** | `Administrateur Système` `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Permettre de diminuer la taille des échanges et de requêtes en utilisant HTTP/2 ou HTTP/3 à la place de HTTP/1.1 et en limitant le nombre de domaines différents pour les ressources utilisées. Il s'agit ainsi d'optimiser la sollicitation des serveurs.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Activer HTTP/2 ou HTTP/3 et limiter le nombre de domaines différents pour les ressources utilisées afin notamment de profiter du multiplexage proposé par HTTP/2 ou HTTP/3.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si (conditions cumulatives) :

- L'ensemble de ses ressources prennent en charge HTTP/2 ou HTTP/3 ;
- Les ressources statiques, hors services tiers, sont transférées via un seul nom de domaine à un instant « t ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache trois fiches au critère 6.7 :

- [**RWEB 0083 — « Privilégier HTTP/2 à HTTP/1 »**](https://rweb.greenit.fr/fr/fiches/RWEB_0083-privilegier-http2-a-http1) (priorité 5/5) présente le multiplexage, la priorisation et la compression des en-têtes. Son principe de validation : **aucune** requête en HTTP/1. Elle cite aussi le « push serveur », à ne plus utiliser : Chrome l'a [désactivé](https://developer.chrome.com/blog/removing-push) en 2022, dans sa version 106, au profit de la réponse `103 Early Hints` ;
- [**RWEB 0082 — « Limiter le nombre de domaines servant les ressources »**](https://rweb.greenit.fr/fr/fiches/RWEB_0082-limiter-le-nombre-de-domaines-servant-les-ressources) : chaque domaine demande une connexion de plus. Son seuil de **cinq** domaines est celui du GR491 ; le RGESN est plus strict pour les ressources statiques, avec **un seul** domaine, hors services tiers ;
- [**RWEB 0081 — « Héberger les ressources statiques sur un domaine sans cookie »**](https://rweb.greenit.fr/fr/fiches/RWEB_0081-heberger-les-ressources-cssjs-sur-un-domaine-sans-cookie) propose un domaine séparé, `media.domain.tld`, pour ne pas envoyer les cookies avec chaque image. C'est une pratique pensée pour HTTP/1.1 : HTTP/2 compresse les en-têtes répétés ([HPACK, RFC 7541](https://www.rfc-editor.org/rfc/rfc7541)), alors qu'un domaine de plus coûte toujours une connexion de plus.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Dans la [recommandation n°6 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=6) du [GR491](https://gr491.isit-europe.org/) (INR), le critère [« Combien de domaines différents sont utilisés ? »](https://gr491.isit-europe.org/crit.php?id=6-frontend-les-mecanismes-de-cache-et-la-mise-2613c3), en priorité **Low**, demande : « Utilisez-vous plus de 5 domaines différents ? Est-ce vraiment justifié ? » Ses précisions : « L'utilisation de nombreux domaines est inefficace à la fois d'un point de vue performance et NR », alors que le cache et l'accès aux ressources sont facilités « lorsque le nombre de sources sont réduites ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Architecte Logiciel`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) couvrent les deux conditions du critère :

- le critère de succès « Protocol efficiency » de la fiche [**« Assess the impact and requirements of data processing »**](https://www.w3.org/TR/web-sustainability-guidelines/#assess-the-impact-and-requirements-of-data-processing), déjà cité au [critère 3.3](../../architecture/3-3_evolution-protocoles/), demande d'« adopt modern standards like HTTP/2 or HTTP/3 for better performance and lower network overhead » ;
- la fiche [**« Use Content Delivery Networks (CDNs) when beneficial »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-content-delivery-networks-cdns-when-beneficial) touche la seconde, car un CDN sert souvent les ressources statiques depuis un domaine à part. Le W3C ne le recommande « only where it provides clear benefits », et pour un public uniquement local, conseille de « prefer geographically close hosting instead ».

{{% /tab %}}

{{% tab tabName="Pourquoi un seul domaine" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Développeur`

**Chaque domaine coûte une connexion.** Avant le premier octet, le navigateur résout le nom (DNS), ouvre une connexion TCP et négocie le chiffrement TLS. Relevé le 30 octobre 2026 dans Chromium 155, sur une connexion fibre, sur les sites des retours d'expériences : de 17 à 84 ms pour la connexion et le chiffrement, plus jusqu'à 38 ms de DNS, pour chaque nouveau domaine. Sur un réseau mobile, chaque échange avec le serveur est plus long.

**HTTP/1.1 multiplie les connexions.** En HTTP/1.1, une connexion ne transporte qu'une requête à la fois : le navigateur en ouvre plusieurs par domaine, six dans le relevé du Musée d'arts de Nantes. En HTTP/2, une seule connexion transporte toutes les requêtes en parallèle (le multiplexage) et compresse les en-têtes.

**Le « domain sharding » est devenu nuisible.** Répartir les ressources sur plusieurs domaines contournait la limite de HTTP/1.1. D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x), en HTTP/2, « domain sharding is no longer useful » et « is even detrimental to performance ».

**HTTP/3 n'est pas obligatoire.** Le RGESN accepte HTTP/2 ou HTTP/3. Le navigateur n'utilise HTTP/3 qu'une fois annoncé, le plus souvent par l'en-tête `Alt-Svc` d'une première réponse en HTTP/2. D'après le [Web Almanac 2024](https://almanac.httparchive.org/en/2024/http), 21 à 22 % des pages d'accueil sont encore servies en HTTP/1.1, et jusqu'à 29 % des requêtes qui ne passent pas par un CDN.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Administrateur Système`, `Développeur`

**1. Relever le protocole et les domaines de chaque type de page.** Dans l'onglet **Réseau** des outils de développement, afficher les colonnes **Protocol** (`h2`, `h3` ou `http/1.1`) et **Domain**. Ou coller ce script dans la console, après le chargement :

```js
const hotes = {};
for (const r of [...performance.getEntriesByType('navigation'), ...performance.getEntriesByType('resource')]) {
  const { host } = new URL(r.name);
  if (!host) continue;
  const h = (hotes[host] ??= { requêtes: 0, protocoles: new Set() });
  h.requêtes++;
  h.protocoles.add(r.nextHopProtocol || 'inconnu');
}
console.table(Object.fromEntries(Object.entries(hotes).map(([hote, h]) => [hote, { requêtes: h.requêtes, protocoles: [...h.protocoles].join(', ') }])));
```

Testé le 30 octobre 2026 dans Chromium 155. Le protocole d'un domaine tiers s'affiche `inconnu` : le navigateur ne le communique qu'avec un en-tête `Timing-Allow-Origin` ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/nextHopProtocol)). Pour un domaine précis, curl répond directement :

```sh
curl -sI --http2 -o /dev/null -w 'HTTP/%{http_version}\n' https://exemple.fr/
```

**2. Activer HTTP/2 partout** : sur le domaine principal, mais aussi sur ceux de l'API, des médias ou du CDN. Avec Nginx 1.25.1 et plus, une ligne `http2 on;` dans le bloc `server` suffit. Les configurations de Nginx et d'Apache, HTTP/3 compris, sont détaillées au [critère 3.3](../../architecture/3-3_evolution-protocoles/).

**3. Regrouper les ressources statiques sur un seul domaine**, de préférence celui des pages : la connexion déjà ouverte pour le HTML sert aussi aux styles, scripts, images et polices.

- Héberger soi-même les bibliothèques et les polices plutôt que de les charger depuis un CDN public (voir le [critère 4.8](../../ux-ui/4-8_polices-caracteres/)).
- Pour une carte, servir les icônes et les polices du style depuis le domaine du service ; les tuiles d'un fournisseur restent un service tiers.
- Le moyen de test n'exige pas que ce domaine soit celui des pages. Un domaine statique distinct, comme `static.exemple.fr`, reste conforme s'il est le seul, mais il coûte une connexion de plus.

**4. Retirer les `preconnect` et `dns-prefetch`** vers les domaines abandonnés (voir le [critère 6.5](../6-5_chargement-ressources/)).

**5. Documenter** dans la déclaration d'écoconception. Par exemple : « Toutes les ressources servies en HTTP/2. Styles, scripts, images et polices hébergés sur exemple.fr. Services tiers : mesure d'audience. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

- le [critère 3.3](../../architecture/3-3_evolution-protocoles/) (évolution des protocoles) : la configuration de HTTP/2 et HTTP/3 ;
- le [critère 6.1](../6-1_poids-requetes-ecran/) (poids et requêtes) : HTTP/2 réduit le coût de chaque requête, pas leur nombre ;
- le [critère 6.3](../6-3_compression-ressources/) (compression) : HTTP/2 compresse les en-têtes, le 6.3 le contenu ;
- le [critère 4.8](../../ux-ui/4-8_polices-caracteres/) (polices) : des polices hébergées sur le domaine du service ;
- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) : exclus de la seconde condition, ils ajoutent pourtant chacun un domaine.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les pages d'accueil ont été relevées le 30 octobre 2026 dans Chromium 155, au premier chargement puis après défilement complet. Le protocole du site a été vérifié avec curl.

| Site | Protocole du site | Domaines des ressources statiques du site | Domaines tiers | Connexions ouvertes |
|---|---|---:|---:|---:|
| [DiaLog](https://dialog.beta.gouv.fr/), accueil | HTTP/2 | 1 | 1 | 2 |
| [DiaLog](https://dialog.beta.gouv.fr/carte), carte | HTTP/2 | 1 | 4 | 6 |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | **HTTP/1.1** | 1 | 3 | 9, dont 6 vers le site |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | HTTP/2 | 1 | 1 | 2 |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | HTTP/2 | 1 | 1 | 2 |

**Tous regroupent leurs ressources statiques sur leur propre domaine.** Aucun n'annonce HTTP/3 pour ce domaine, ce qui n'est pas exigé.

**Le Musée d'arts de Nantes** marque le critère **« Validé »** dans sa [déclaration d'écoconception](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) : « Les ressources statiques sont bien regroupées sur un même domaine (mais les cookies ne devraient pas être utilisés pour ceux-ci). » Le regroupement est confirmé, mais le site répond en **HTTP/1.1**, au navigateur comme à curl : la première condition n'est pas remplie. Le navigateur ouvre six connexions chiffrées vers le site, et chaque requête porte ses en-têtes en entier, dont 455 octets de cookies sur onze ressources statiques. Le serveur étant Nginx, activer HTTP/2 tient en une ligne et réglerait aussi la question des cookies.

**DiaLog** marque le critère **« Validé »** dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf) : les ressources hébergées sont « distribuées via du HTTP2 depuis notre propre domaine ». C'est exact pour la page d'accueil, dont la mesure d'audience vient d'un service tiers, stats.beta.gouv.fr. La page de la carte charge en plus les icônes et les polices du style de carte depuis openmaptiles.github.io et openmaptiles.geo.data.gouv.fr, ce dernier en HTTP/1.1. Hébergées sur dialog.beta.gouv.fr, elles passeraient par la connexion déjà ouverte. Les tuiles de l'IGN (data.geopf.fr) restent un service tiers.

**SPOTE** envoie un cookie d'une cinquantaine d'octets avec chacune de ses 34 ressources statiques : moins de 2 Ko en tout, en HTTP/2. Un domaine sans cookie, comme le propose RWEB 0081, n'apporterait presque rien.

**Le site du RGESN**, hébergé sur GitHub Pages comme celui-ci, sert tout en HTTP/2 depuis son propre domaine ; seule sa mesure d'audience vient de stats.data.gouv.fr. [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) marque le critère « Validé » : « Toutes les ressources sont hébergées sur face.din.developpement-durable.gouv.fr », et son serveur répond lui aussi en HTTP/2.

{{% /tab %}}

{{< /tabs >}}
