---
weight: 600
title: "3.6 - Mises à jour incrémentielles"
description: "Critère 3.6 du RGESN : pourquoi et comment proposer des mises à jour incrémentielles plutôt que de remplacer tout le code du service à chaque mise à jour."
icon: "difference"
date: "2026-07-15T00:00:00+01:00"
lastmod: "2026-07-15T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il les mises à jour incrémentielles, afin de ne pas remplacer tout le code à chaque mise à jour ?

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
| **Critère**  | `3.6` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne propose pas de mise à jour` |
| **Métiers concernés** | `Architecte Logiciel` `Porteur de projet` `Responsable Qualité` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/3.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

La mise à jour des applications peut consommer beaucoup de données si l'ensemble du code du service numérique est mis à jour. Ce critère vise à réduire drastiquement la quantité de données nécessaire pour une mise à jour. Cela implique de limiter les mises à jour aux ajouts incrémentaux.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Favoriser les mises à jour incrémentielles (seules les données modifiées sont transférées) ou la séparation du code binaire en petites entités qui ne sont téléchargées que si leur code a changé. L'objectif est de ne pas remplacer tout le code du programme à chaque fois qu'une mise à jour est livrée.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Il faut utiliser, lorsque cela est possible, un mécanisme de mise à jour qui ne nécessite pas de remplacer tout le code du programme à chaque mise à jour. Le cas échéant, il est possible de proposer une mise à jour complète du code du programme pour les fonctionnalités de « réinitialisation » ou « d'autoréparation ». Le critère est validé si les mises à jour incrémentielles sont favorisées pour le service numérique, en dehors des fonctionnalités de « réinitialisation » et « d'autoréparation ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C n'ont pas de fiche dédiée aux mécanismes de mise à jour, mais la recommandation [**« Modularize bandwidth-heavy components »**](https://www.w3.org/TR/web-sustainability-guidelines/#modularize-bandwidth-heavy-components) recoupe le principe de fond du critère : « Split large or bandwidth-heavy components into smaller modules that load only when needed. Avoid excessive splitting, as it can increase overhead, reduce caching efficiency, and make code harder to maintain. »

Le contexte visé par le W3C est le chargement initial (charger uniquement les modules nécessaires à l'usage courant), alors que le critère 3.6 porte spécifiquement sur les *mises à jour*. Le principe technique sous-jacent est néanmoins le même : un code découpé en modules indépendants permet de ne transférer, au chargement comme à la mise à jour, que les seules parties qui ont réellement changé — c'est exactement ce mécanisme de découpage qui rend possibles les mises à jour incrémentielles décrites ci-contre (Android App Bundle, iOS App Thinning). La mise en garde du W3C contre un découpage excessif s'applique aussi côté mise à jour : trop de petits modules multiplie les requêtes et les métadonnées de version à suivre, avec un gain marginal décroissant.

{{% /tab %}}

{{% tab tabName="Mises à jour applicatives (mobile)" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Porteur de projet`

Les deux principaux magasins d'applications mobiles ont chacun développé un mécanisme de découpage du binaire qui illustre concrètement la « séparation du code binaire en petites entités » demandée par le critère :

- **Android** — le format [Android App Bundle](https://developer.android.com/guide/app-bundle) (recommandé par Google Play depuis 2021, remplaçant l'APK monolithique) permet à Google Play de générer et servir des **APK optimisés par appareil** (architecture processeur, densité d'écran, langue), puis d'utiliser le [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery) pour ne télécharger certains modules qu'à la demande (installation conditionnelle ou différée). Lors d'une mise à jour, Google Play calcule en plus un **patch delta** entre la version installée et la nouvelle version : seules les portions binaires modifiées sont retransmises, au lieu de l'APK complet. Des retours d'expérience documentés par [Google](https://android-developers.googleblog.com/2021/06/the-future-of-android-app-bundles.html) citent une réduction de taille de **23 % pour LinkedIn** et **35 % pour Twitter** après migration vers ce format.
- **iOS** — le mécanisme d'[« App Thinning »](https://help.apple.com/xcode/mac/current/en.lproj/devbbdc5ce4f.html) d'Apple combine deux techniques pertinentes pour ce critère : le **Slicing**, qui ne délivre à chaque appareil que les ressources correspondant à sa configuration (résolution d'écran, architecture) plutôt qu'un binaire universel contenant toutes les variantes, et les **On-Demand Resources**, qui permettent de ne télécharger certains contenus (niveaux de jeu, assets volumineux) qu'au moment où l'utilisateur en a effectivement besoin, sans attendre une mise à jour complète de l'application.

Dans les deux cas, le principe est le même que celui demandé par le critère : plus le binaire est découpé finement en amont, plus une mise à jour ultérieure peut se limiter aux seules entités réellement modifiées.

{{% /tab %}}

{{% tab tabName="Mises à jour logicielles (navigateurs, desktop)" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable RSE/Numérique soutenable`

Pour les logiciels installés sur poste de travail, le cas le plus documenté est celui du **différentiel binaire** (binary diffing), qui calcule un patch ne contenant que les octets qui ont changé entre deux versions d'un même exécutable, plutôt que de retélécharger le binaire complet à chaque mise à jour :

- [**Courgette**](https://www.chromium.org/developers/design-documents/software-updates-courgette/), l'algorithme développé par Google pour les mises à jour de Chrome, améliore l'algorithme générique [bsdiff](https://www.daemonology.net/bsdiff/) en désassemblant d'abord le code exécutable pour normaliser les adresses relatives avant de calculer le différentiel — ce qui rend le diff binaire beaucoup plus compact. Sur l'exemple documenté par [le blog Chromium](https://blog.chromium.org/2009/07/smaller-is-faster-and-safer-too.html), le patch d'une mise à jour est ainsi passé de **6,7 % de la taille du binaire complet (avec bsdiff seul) à 0,76 % (avec Courgette)**, soit un patch environ 9 fois plus petit qu'avec bsdiff seul.
- L'algorithme [**bsdiff**](https://www.daemonology.net/bsdiff/) lui-même, sans le prétraitement de Courgette, reste largement utilisé tel quel — notamment par **macOS** pour ses propres mises à jour système, comme détaillé dans [cette analyse de son fonctionnement](https://jonready.com/blog/posts/visualizing-bsdiff.html).

Ce mécanisme correspond directement à la première option citée dans la « Mise en œuvre » du critère : des « mises à jour incrémentielles » où « seules les données modifiées sont transférées », par opposition à la séparation du binaire en modules indépendants (approche plutôt illustrée par les exemples mobiles ci-contre).

{{% /tab %}}

{{% tab tabName="Conteneurs et infrastructure" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`

Côté déploiement serveur, l'image de conteneur ([Docker](https://docs.docker.com/build/cache/), OCI) illustre le même principe à l'échelle de l'infrastructure plutôt que du poste client : une image est construite comme un empilement de **couches (layers)** immuables, chacune associée à une somme de contrôle. Lors d'une nouvelle mise à jour de l'application, seules les couches dont le contenu a changé sont reconstruites, poussées vers le registre et retéléchargées par les serveurs qui exécutent déjà une version antérieure de l'image — les couches inchangées (dépendances système, runtime de base…) sont réutilisées telles quelles, sans retransfert.

C'est une application directe, côté infrastructure, de la même logique que la « Mise en œuvre » du critère décrit pour le poste utilisateur : ne remplacer que les entités dont le code a réellement changé, pas l'ensemble du programme.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Qualité`

Ce critère est complémentaire du [critère 3.5](../3-5_dissociation-mises-a-jour/) (dissociation des mises à jour correctives et évolutives), déjà publié sur ce site : le 3.5 porte sur la **nature** de la mise à jour (corrective ou évolutive, et la possibilité de les installer indépendamment l'une de l'autre), tandis que le 3.6 porte sur le **volume de données transféré** pour livrer cette mise à jour, quelle que soit sa nature. Une même stratégie de gestion de versions (SemVer, changelog) peut documenter les deux à la fois : la nature du changement (3.5) et, si le mécanisme de livraison le permet, le fait qu'il ne transfère que les parties modifiées (3.6).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 17 janvier 2025) marque ce critère **« Non applicable »**, sans autre justification que ce statut — le même niveau d'information minimal que pour les critères voisins 3.4 et 3.5 sur cette même déclaration. FACE étant un service web sans mécanisme de mise à jour binaire distribuée (contrairement à une application mobile ou un logiciel installé), l'absence de justification détaillée est cohérente avec la nature même du service.

{{% /tab %}}

{{< /tabs >}}
