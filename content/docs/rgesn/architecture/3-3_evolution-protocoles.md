---
weight: 300
title: "3.3 - Évolution technique des protocoles"
description: "Critère 3.3 du RGESN : pourquoi et comment garantir la pérennité du service face à l'évolution des protocoles réseau (IPv6, HTTPS/TLS, protocoles d'échange de données)."
icon: "network_check"
date: "2026-07-14T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique est-il en mesure de supporter l'évolution technique des protocoles ?

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
| **Critère**  | `3.3` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas de connexion réseau internet` |
| **Métiers concernés** | `Architecte Système` `Développeur` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Le choix des protocoles sous-jacents aux échanges réseaux associés au service numérique développé a un impact sur la sollicitation des infrastructures, mais aussi sur la durée de vie du service numérique. En effet, les évolutions techniques des protocoles non supportées par le service numérique peuvent conduire à des dysfonctionnements de certains modules ou fonctionnalités de celui-ci. Prendre en compte ces risques d'obsolescence pour faire les meilleurs choix en matière de protocole permettra de limiter les mises à jour/modernisations nécessaires, et rendra ainsi le service numérique plus durable et pérenne. L'objectif est donc de limiter l'obsolescence du service induite par l'obsolescence des protocoles utilisés, en tenant compte particulièrement des éléments suivants :

- **Protocole d'adressage** : face à la pénurie d'IPv4 et la généralisation d'IPv6 (à moyen terme, certains accès à internet ne proposeront plus de connectivité IPv4), un service disponible en IPv6 assure sa pérennité. Ce choix permet aussi de limiter le nombre de plateformes nécessaires et la consommation d'énergie associée chez les opérateurs ayant recours à du partage d'IPv4 entre clients. L'IPv6 n'a pas besoin de passer par la plateforme CG-NAT, coûteuse en matériel et en énergie.
- **Protocole de chiffrement/d'authentification** : les navigateurs tendent vers le blocage du protocole HTTP et l'obligation d'utiliser HTTPS, qui devient donc le choix le plus pérenne. En outre, la couche de chiffrement TLS doit être adaptée à l'évolution de ce protocole puisque les anciennes versions de TLS (TLS v1.0 et TLS v1.1) ne sont plus prises en charge par les navigateurs web.
- **Protocole d'échanges de données** : s'assurer de l'adéquation entre le choix du protocole et le type des contenus échangés.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Vérifier que le choix des protocoles sous-jacents au service — protocole d'adressage, d'authentification et chiffrement et d'échanges de données — favorise la pérennité du service. Considérer en particulier les actions suivantes selon les fonctionnalités du service :

- Vérifier que le service est accessible en IPv6 et définir une stratégie de test IPv6 incluant des tests depuis un équipement où la connectivité IPv4 est désactivée. Objectif : déceler du code ou des fonctions qui ne fonctionnent qu'en IPv4-only, qui seront inutilisables à moyen terme, avec le retrait d'IPv4.
- Utiliser le protocole d'authentification et de chiffrement HTTPS. Dans un contexte où l'utilisateur accède au service numérique par son navigateur, il est le plus souvent obligatoire d'utiliser HTTPS au lieu de HTTP (l'utilisation d'un moyen sécurisé pour le transfert de données personnelles est une obligation de l'article 32 du RGPD).
- Pour le protocole de sécurité, la version de TLS utilisée doit prendre en charge la version la plus récente (au moment de la rédaction de ce référentiel : TLS v1.3). Par exemple, avec Apache la ligne de configuration recommandée est « `SSLProtocol al -SSLv3 -TLSv1 -TLSv1.1` », ce qui permet d'activer les nouvelles versions de TLS quand elles sont disponibles et de désactiver les versions de TLS problématiques d'un point de vue sécurité.
- Pour les protocoles d'échanges de données, il est recommandé de comparer les protocoles disponibles en fonction des types de contenu et des fonctionnalités recherchées. Cette évaluation devrait prendre en considération des critères tels que l'efficacité de transfert des données, la latence, la compatibilité avec les technologies utilisées, ainsi que l'impact environnemental de chaque protocole. Par exemple :
  - Pour la vidéo : Multicast, HTTP Live Streaming (HLS), Real-Time Messaging Protocol (RTMP), Web Real-Time Communications (WebRTC)…
  - Pour les API : REST, SOAP, GraphQL, Protocol Buffers…

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la mise en œuvre en s'assurant :

- Que les différents composants du service numérique fonctionnent bien :
  - En IPv6 et ne font appel à aucun service tiers IPv4-only.
  - En HTTPS et non en HTTP.
- Que la dernière version de TLS (au moment de la rédaction de ce référentiel : TLS v1.3) est bien supportée.
- De l'adéquation du protocole utilisé par rapport au contenu transféré en tenant compte de son empreinte environnementale, ce qui peut être réalisé en :
  - Analysant les caractéristiques techniques du protocole dans le contexte des besoins du service, voire en réalisant des scénarios-tests ou des comparaisons de performances ;
  - Prenant en compte l'impact environnemental du protocole utilisé, notamment la consommation d'énergie et les ressources informatiques sous-jacentes à son usage.

Le critère est validé si le choix des protocoles nécessaires au fonctionnement du service en assure sa pérennité, en respectant, selon ses fonctionnalités, les conditions susmentionnées. Documenter les protocoles utilisés dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C recoupent directement ce critère dans la fiche [**« Assess the impact and requirements of data processing »**](https://www.w3.org/TR/web-sustainability-guidelines/#assess-the-impact-and-requirements-of-data-processing) : « Choose communication protocols that balance user needs, security, and sustainability... Prioritize secure options like HTTPS and SFTP/SSH, avoid insecure legacy protocols such as HTTP and FTP, and adopt modern standards like HTTP/2 or HTTP/3 for better performance and lower network overhead. »

La même fiche propose une architecture événementielle plutôt que des API synchrones, quand elle réduit la charge du serveur : c'est la question du protocole d'échange de données que pose le RGESN.

{{% /tab %}}

{{% tab tabName="Protocoles d'échange de données" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Le critère cite REST, SOAP, GraphQL et Protocol Buffers sans trancher : le choix dépend du contexte.

- [**REST**](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) : le plus simple à mettre en œuvre et à déboguer, et le seul des trois à profiter pleinement du cache HTTP (navigateur, CDN) grâce à des adresses stables ;
- [**GraphQL**](https://graphql.org/) : le client ne demande que les champs dont il a besoin, au prix d'un traitement supplémentaire côté serveur à chaque requête ;
- [**gRPC**](https://grpc.io/) et [**Protocol Buffers**](https://protobuf.dev/) : un encodage binaire sur HTTP/2, adapté aux échanges internes à fort volume, de service à service.

**Le format d'encodage pèse moins qu'on ne le dit.** Les gains de 20 à 50 % souvent annoncés pour les formats binaires sont mesurés face à du JSON non compressé. L'étude [« A Benchmark of JSON-compatible Binary Serialization Specifications »](https://arxiv.org/abs/2201.03051) (Viotti et Kinderkhedia, université d'Oxford, 2022) les compare à du JSON **compressé en gzip**, sur 480 documents réels :

| Format (compressé) | Schéma | Gain médian face au JSON compressé | Usage typique |
|---|---|---:|---|
| [Apache Avro](https://avro.apache.org/) | Oui | 52,2 % | Flux d'événements (Kafka), pipelines de données |
| [Protocol Buffers](https://protobuf.dev/) | Oui | 46,4 % | gRPC, échanges entre services, API mobiles |
| [CBOR](https://cbor.io/) ([RFC 8949](https://www.rfc-editor.org/rfc/rfc8949)) | Non | 8,8 % | Objets connectés (CoAP), WebAuthn |
| [MessagePack](https://msgpack.org/) | Non | 7,5 % | Temps réel sur WebSocket |

Une fois la compression HTTP en place ([critère 6.3](../../frontend/6-3_compression-ressources/)), un format binaire **sans schéma** n'apporte presque rien. Le gain vient des formats **avec schéma**, qui n'envoient pas le nom des champs à chaque message.

Un format compact réduit la taille de la réponse, mais une réponse servie depuis un cache évite la requête elle-même, ce qui est souvent le gain le plus important. Le critère demande de documenter le choix, pas d'imposer un protocole.

{{% /tab %}}

{{% tab tabName="Activer HTTP/2 et HTTP/3" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

**Nginx** :

- HTTP/2 : depuis Nginx 1.25.1, la directive dédiée `http2 on;` remplace l'ancien paramètre `listen ... http2` :
  ```nginx
  server {
      listen 443 ssl;
      http2 on;
      ssl_certificate     server.crt;
      ssl_certificate_key server.key;
  }
  ```
- HTTP/3 : nécessite un binaire Nginx compilé avec `--with-http_v3_module` (pas présent par défaut dans tous les paquets pré-compilés) et repose sur QUIC (UDP) en plus de TLS :
  ```nginx
  server {
      listen 443 quic reuseport;
      listen 443 ssl;
      http3 on;
      ssl_certificate     server.crt;
      ssl_certificate_key server.key;
      add_header Alt-Svc 'h3=":443"; ma=86400';
  }
  ```
  Le port 443 est volontairement partagé entre HTTP/3 (QUIC/UDP) et HTTPS (TCP) ; l'en-tête `Alt-Svc` annonce aux clients compatibles que HTTP/3 est disponible sur ce port.

**Apache httpd** :

- HTTP/2 : activer `mod_http2`, puis déclarer les protocoles supportés via la directive `Protocols` :
  ```apache
  LoadModule http2_module modules/mod_http2.so
  Protocols h2 http/1.1
  ```
  L'ordre compte : le protocole le plus à gauche est le plus préféré par le serveur.
- HTTP/3 : **Apache httpd ne le prend pas en charge**. Il n'existe pas de module `mod_http3` dans ses sources, contrairement à ce que laissent entendre certains articles : HTTP/3 repose sur QUIC, un protocole UDP, alors qu'Apache est conçu autour de connexions TCP. Pour proposer HTTP/3, il faut placer devant Apache un proxy inverse ou un CDN qui le gère (Nginx, Caddy…), Apache continuant de servir HTTP/1.1 ou HTTP/2 en interne.

{{% /tab %}}

{{% tab tabName="Outils de test" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

Pour vérifier concrètement les trois volets du critère plutôt que de les présumer respectés :

- [test-ipv6.com](https://test-ipv6.com/) diagnostique l'accessibilité IPv6 d'un service et détecte les composants qui ne fonctionnent qu'en IPv4.
- [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) audite la configuration TLS d'un serveur public (versions supportées, suites de chiffrement, note de A à F) ; [testssl.sh](https://testssl.sh/) fait de même en ligne de commande, utile pour l'intégrer en CI/CD ou tester un serveur non accessible publiquement.
- Le [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) génère une configuration TLS prête à l'emploi (Apache, Nginx, etc.) selon le niveau de compatibilité souhaité, sans les versions de TLS obsolètes : c'est l'équivalent, pour tous les serveurs, de la ligne de configuration Apache citée dans la « Mise en œuvre » du critère.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Système`, `Développeur`

- le [critère 6.7](../../frontend/6-7_domaine-unique/) (domaine unique) : HTTP/2 et HTTP/3 sur tous les domaines du service ;
- le [critère 6.3](../../frontend/6-3_compression-ressources/) (compression des ressources) : HTTP/2 compresse les en-têtes, le 6.3 le contenu ;
- le [critère 1.7](../../strategie/1-7_niveau-chiffrement/) (niveau de chiffrement) : les versions de TLS à prendre en charge.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non validé »**, mais leur justification montre une conformité partielle plutôt qu'un rejet global : « Le service numérique repose sur le protocole HTTPS. La version de TLS utilisée prend en charge la version la plus récente (...) : TLS v1.3. Cependant, à ce jour, le service numérique n'est pas accessible en IPv6. »

Ce cas illustre bien la structure du critère : les trois volets (adressage, chiffrement, échange de données) sont évalués indépendamment, et il suffit qu'un seul ne soit pas respecté — ici l'IPv6 — pour que le critère dans son ensemble soit marqué « Non validé », même si les deux autres volets (HTTPS, TLS 1.3) sont pleinement conformes.

[Alt Impact](https://altimpact.fr/ecoconception-du-site/) (site porté par l'ADEME, audit Conserto) valide les trois volets à la fois, en une phrase : « l'hébergeur Datacampus est accessible en IPv6 / HTTPS / TLS 1.3. » Pour un service public comme pour FACE, l'IPv6 dépend d'abord du choix de l'hébergeur.

{{% /tab %}}

{{< /tabs >}}
