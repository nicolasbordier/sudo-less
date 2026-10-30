---
weight: 700
title: "1.7 - Niveau de chiffrement"
description: "Critère 1.7 du RGESN : comment choisir un niveau et des mécanismes de chiffrement adaptés aux besoins de sécurité réels, sans surdimensionner leur coût environnemental."
icon: "article"
date: "2026-07-03T00:00:00+01:00"
lastmod: "2026-07-03T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il recours à un niveau de chiffrement adapté à ses besoins ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Stratégie` |
| **Critère**  | `1.7` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service n'a pas recours à un mécanisme de chiffrement` |
| **Métiers concernés** | `Expert en sécurité informatique` `Responsable de la protection des données` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Dans la plupart des situations, le recours à des **mécanismes cryptographiques** est absolument essentiel pour protéger les systèmes informatiques ainsi que les données — notamment personnelles — collectées ou traitées. Ces mécanismes ont cependant une **empreinte environnementale à considérer** : le chiffrement augmente la consommation énergétique, d'abord par le calcul nécessaire à l'opération et au déchiffrement, mais aussi par le stockage et la charge des réseaux de communication qu'il génère.

Dans certains cas, le chiffrement peut au contraire **alléger** les systèmes informatiques (compression des archives en parallèle du chiffrement, évitement de la conservation ou de la circulation de certains fichiers). Ce critère vise donc à **minimiser le coût environnemental du chiffrement**, en tenant compte des contraintes de sécurité à respecter — le chiffrement contribuant par ailleurs à réduire le risque de faille et de fuite de données, dont les traitements ultérieurs ont eux aussi une empreinte énergétique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Chercher, pour un **niveau de sécurité donné**, les choix optimaux pour la préservation des ressources :

- En réalisant des **mesures comparatives** de différents algorithmes de chiffrement, afin de sélectionner celui qui introduit la plus faible quantité de ressources processeur pour une performance équivalente ;
- En évaluant la **pertinence du chiffrement** au regard de la nature des données et des risques associés — ne pas chiffrer par défaut ce qui ne le justifie pas ;
- Lorsque le chiffrement est retenu, mettre en œuvre, quand cela est possible, un **algorithme et une implémentation qui minimisent l'empreinte environnementale** du service, sans préjudice du niveau de sécurité requis.

Privilégier des mécanismes cryptographiques permettant de **générer des preuves sans nécessiter de conserver ou de divulguer le fichier à prouver** (ex. preuve de fourniture de pièce d'identité). Conserver des **archives chiffrées et compressées** plutôt que des fichiers chiffrés isolés (des outils gratuits comme 7-Zip ou Zed! fonctionnent sur ce principe).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Si le service repose sur des **mécanismes de chiffrement**, documenter dans la **déclaration d'écoconception** du service la **pertinence du choix de mise en œuvre** des mécanismes cryptographiques, au regard :

- des **risques de sécurité informatique** propres au service ;
- de la **minimisation de l'empreinte environnementale** associée à ce choix.

Le critère est **non applicable** si le service n'a pas recours à un mécanisme de chiffrement au-delà du chiffrement du transport standard (HTTPS).

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="ANSSI" %}}

Profil(s) métier concerné(s) : `Expert en sécurité informatique`

Pour dimensionner un chiffrement « adapté aux besoins » plutôt que systématiquement maximal, la référence française est le guide [« Règles et recommandations concernant le choix et le dimensionnement des mécanismes cryptographiques » (ANSSI-PG-083)](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf), publié par l'**ANSSI** (Agence nationale de la sécurité des systèmes d'information). Sa version en vigueur (3.00, 2026) intègre désormais la menace post-quantique.

Ce guide fixe, pour chaque famille de mécanisme (chiffrement symétrique, asymétrique, fonctions de hachage…), la **taille de clé minimale recommandée selon la durée de protection souhaitée des données** — c'est directement transposable à la logique du critère 1.7 : un chiffrement surdimensionné par rapport à la durée de vie réelle de la donnée consomme des ressources sans bénéfice de sécurité proportionné. Publié sous Licence Ouverte, il est librement réutilisable.

{{% /tab %}}

{{% tab tabName="Tableau comparatif" %}}

Profil(s) métier concerné(s) : `Expert en sécurité informatique`, `Architecte`

Trois familles d'algorithmes se combinent dans un service numérique, chacune avec un compromis sécurité/performance/poids différent. Le tableau ci-dessous synthétise les tailles de clé conformes au référentiel ANSSI-PG-083 et leur cas d'usage type :

| Famille | Algorithme | Taille recommandée | Cas d'usage type | Performance / empreinte | Résistance post-quantique |
|---|---|---|---|---|---|
| **Symétrique** | AES-128-GCM | 128 bits | Chiffrement de données en transit ou au repos, cas général | Rapide, quasi gratuit avec accélération matérielle AES-NI (serveurs et mobiles récents) | Présumée suffisante contre l'algorithme de Grover ; l'ANSSI recommande 192 bits ou plus si une sécurité post-quantique est visée |
| **Symétrique** | AES-256-GCM | 256 bits | Données sensibles, ou horizon de confidentialité long (>2030) | 14 tours de chiffrement au lieu de 10 pour AES-128, donc un peu plus de calcul | Oui *(au-delà des 192 bits recommandés par l'ANSSI en post-quantique)* |
| **Symétrique** | ChaCha20-Poly1305 | 256 bits | Terminaux sans accélération matérielle (mobiles bas/moyen de gamme, IoT) | Plus économe qu'AES en implémentation logicielle pure | Oui *(nécessite Poly1305 pour l'intégrité)* |
| **Asymétrique classique** | RSA-OAEP / RSA-PSS | ≥ 3072 bits *(2048 bits toléré jusqu'à fin 2030)* | Chiffrement/signature historique, compatibilité la plus large | Le plus coûteux des trois familles en calcul et en taille de clé | Non — vulnérable à l'algorithme de Shor |
| **Asymétrique classique** | ECDH / ECDSA (P-256, P-384, X25519) | 256-384 bits | Échange de clé TLS, signature, alternative légère à RSA (mobile, IoT) | Nettement plus léger que RSA à sécurité équivalente | Non — vulnérable à l'algorithme de Shor |
| **Post-quantique** | ML-KEM *(Kyber, FIPS 203)* | ML-KEM-768 recommandé | Encapsulation / échange de clé résistant à un ordinateur quantique | Clés et chiffrés plus volumineux que l'ECC classique (surcoût réseau) | Oui — retenu par le NIST et l'ANSSI |
| **Post-quantique** | ML-DSA *(Dilithium, FIPS 204)* | — | Signature numérique résistante au quantique | Signatures plus volumineuses que RSA/ECDSA | Oui |

**Comment arbitrer :** l'ANSSI fixe une règle de décision simple (`RecoSécuLongTerme`) plutôt qu'un choix binaire « classique ou post-quantique » — viser une sécurité post-quantique **si l'usage est prévu au-delà du 1ᵉʳ janvier 2030, ou s'il existe un risque d'attaque rétroactive** (dite *« store now, decrypt later »* : un adversaire enregistre aujourd'hui un échange de clé chiffré classiquement, pour le déchiffrer plus tard une fois un ordinateur quantique disponible). Pour un besoin de sécurité à court terme sans donnée à protéger durablement, un algorithme classique bien dimensionné (AES-128, ECDH) reste **suffisant et nettement plus sobre** qu'un algorithme post-quantique aux clés et signatures plus volumineuses. Durant la période de transition, l'**hybridation** (combiner un mécanisme classique et un mécanisme post-quantique, ex. X25519 + ML-KEM) reste conforme au référentiel — c'est l'approche actuellement déployée par défaut dans TLS 1.3 par les principaux navigateurs et CDN.

{{% /tab %}}

{{% tab tabName="Outils & benchmarks" %}}

Profil(s) métier concerné(s) : `Expert en sécurité informatique`, `Développeur`

Le choix de l'algorithme a un impact mesurable, mais **dépendant du matériel** : sur un CPU équipé d'accélération matérielle AES-NI (la majorité des serveurs et smartphones récents), **AES-256-GCM** est généralement plus rapide et moins gourmand que ChaCha20-Poly1305 — l'inverse étant vrai en l'absence d'accélération matérielle (anciens terminaux, certains environnements mobiles), où **ChaCha20-Poly1305** consomme moins d'énergie. Autre repère : **AES-256 effectue 14 tours de chiffrement, contre 10 pour AES-128**. Un niveau de sécurité supérieur à celui réellement requis a donc un coût.

Pour l'archivage chiffré évoqué dans la fiche RGESN, deux outils gratuits illustrent le principe « compresser et chiffrer ensemble » : [7-Zip](https://www.7-zip.org/) (logiciel libre) et [Zed!](https://www.primx.eu/en/encryption-software/zed-en/) (édité par la société française Prim'X, dont une version de découverte gratuite chiffre des fichiers jusqu'à 200 Mo). La CNIL les cite, avec [PeaZip](https://peazip.github.io/) et [VeraCrypt](https://veracrypt.io/) (chiffrement de répertoires), dans sa fiche [« Comment chiffrer ses documents et ses répertoires »](https://www.cnil.fr/fr/comment-chiffrer-ses-documents-et-ses-repertoires).

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Expert en sécurité informatique`, `Développeur`

**1. Lister les mécanismes au-delà du HTTPS** : fichiers ou colonnes chiffrés en base, sauvegardes chiffrées, signatures, archives. S'il n'y en a aucun, le critère est non applicable (voir les retours d'expériences). La configuration de TLS relève du [critère 3.3](../../architecture/3-3_evolution-protocoles/).

**2. Mesurer avant de choisir**, comme le demande la mise en œuvre. OpenSSL compare les algorithmes sur la machine qui les exécutera :

```sh
openssl speed -seconds 2 -bytes 16384 -evp aes-128-gcm
openssl speed -seconds 2 -bytes 16384 -evp aes-256-gcm
openssl speed -seconds 2 -bytes 16384 -evp chacha20-poly1305
```

| Débit sur un cœur | Avec AES-NI | Sans AES-NI |
|---|---:|---:|
| AES-128-GCM | 5,9 Go/s | 0,42 Go/s |
| AES-256-GCM | 5,4 Go/s | 0,36 Go/s |
| ChaCha20-Poly1305 | 3,2 Go/s | 1,8 Go/s |

Mesuré le 30 octobre 2026 avec OpenSSL 3.5.7 sur un processeur AMD Ryzen 7 7735HS, par blocs de 16 Ko. La colonne « Sans AES-NI » désactive l'accélération avec la variable `OPENSSL_ia32cap="~0x200000200000000"`. Avec l'accélération, AES-256 ne perd que 9 % de débit face à AES-128. Sans elle, ChaCha20-Poly1305 va quatre à cinq fois plus vite qu'AES. Le bon choix dépend donc du matériel qui chiffre, serveur ou terminal ancien : la mesure se refait sur ce matériel.

**3. Mesurer le surcoût du post-quantique.** D'après la règle de l'ANSSI (onglet « Tableau comparatif »), l'échange de clé hybride se justifie pour des données à protéger au-delà de 2030. Son coût réseau se mesure avec OpenSSL 3.5 ou plus récent :

```sh
openssl s_client -connect exemple.fr:443 -tls1_3 -groups X25519 </dev/null 2>&1 | grep 'handshake has read'
openssl s_client -connect exemple.fr:443 -tls1_3 -groups X25519MLKEM768 </dev/null 2>&1 | grep 'handshake has read'
```

Mesuré le 30 octobre 2026 : le site du RGESN et DiaLog acceptent déjà l'échange hybride `X25519MLKEM768`. Il ajoute environ 1,2 Ko envoyés et 1,1 Ko reçus à chaque poignée de main, soit la taille de la clé publique ML-KEM-768 (1 184 octets) et de son chiffré (1 088 octets). Ce surcoût se paie à chaque connexion, pas à chaque requête : une raison de plus de réutiliser les connexions (voir le [critère 6.7](../../frontend/6-7_domaine-unique/)).

**4. Compresser, puis chiffrer**, comme le recommande la fiche RGESN : une donnée chiffrée ne se compresse plus. 7-Zip fait les deux en une commande, et `-mhe=on` chiffre aussi les noms de fichiers :

```sh
7z a -t7z -mhe=on -p archive.7z dossiers/
```

Testé le 30 octobre 2026 avec 7-Zip 26.04 sur les fiches de ce site : 1,07 Mo de texte donnent une archive de 233 Ko, compressée en LZMA2 et chiffrée en AES-256. Sans le mot de passe, demandé au lancement, la liste des fichiers ne s'affiche pas.

**5. Prouver sans conserver.** Pour une pièce justificative vérifiée une fois, garder le résultat du contrôle et une empreinte plutôt que le fichier :

```sh
sha256sum justificatif.pdf
```

L'empreinte de 64 caractères permet de vérifier plus tard qu'un document présenté à nouveau est bien celui qui a été contrôlé, sans stocker ni chiffrer le document.

**6. Documenter**, pour chaque mécanisme : la donnée protégée et sa durée de protection, l'algorithme et la taille de clé retenus au regard du guide de l'ANSSI, et la mesure qui justifie ce choix.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Expert en sécurité informatique`, `Responsable de la protection des données`

- le [critère 1.6](../1-6_collecte-donnees/) (collecte de données) : ne pas collecter une donnée évite de devoir la chiffrer ;
- le [critère 3.3](../../architecture/3-3_evolution-protocoles/) (évolution des protocoles) : les versions de TLS et les protocoles chiffrés à prendre en charge ;
- le [critère 3.5](../../architecture/3-5_dissociation-mises-a-jour/) (dissociation des mises à jour) : les correctifs de sécurité doivent pouvoir être installés seuls.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, évaluation du 30 janvier 2025, score global 48 %) illustre le cas le plus fréquent en pratique : le critère est marqué **« Non applicable »**, avec la justification suivante consignée dans la déclaration — « Aucun mécanisme de chiffrement, hormis l'accès HTTPS n'a été identifié. » Pour un service qui ne va pas au-delà du chiffrement de transport standard, ce critère n'appelle donc ni sur-ingénierie ni justification complexe : il suffit de documenter honnêtement ce constat de non-applicabilité dans la déclaration d'écoconception.

Ce critère prend tout son sens dès qu'un service va plus loin (chiffrement de données au repos, signature électronique, preuve documentaire, partitions chiffrées…) — voir aussi le [critère 1.6](../1-6_collecte-donnees/), dont l'onglet CNIL détaille précisément la tension entre obligations de chiffrement et sobriété numérique.

{{% /tab %}}

{{< /tabs >}}
