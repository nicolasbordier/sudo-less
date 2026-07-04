---
weight: 1000
title: "1.10 - API ouvertes pour le matériel"
description: "Critère 1.10 du RGESN : pourquoi documenter et ouvrir les API des objets connectés et périphériques pour éviter qu'un matériel fonctionnel devienne inutilisable en cas d'abandon logiciel."
icon: "article"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique repose-t-il sur des API documentées et ouvertes pour interagir avec le matériel ?

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
| **Critère**  | `1.10` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `Services reposant sur un objet connecté ou un périphérique matériel` |
| **Métiers concernés** | `Responsable IT` `Développeur` `Architecte Système` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.10/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Un objet connecté ou un périphérique interagit avec son environnement via des **API** (interfaces d'accès dédiées aux programmes), généralement appelées via un **pilote** (« driver ») ou une application sur smartphone.

- Lorsque ces API ne sont **pas ouvertes**, il est souvent impossible de prolonger la durée de vie de l'objet au-delà de celle de l'application ou du pilote initialement conçu pour lui : si ce logiciel est **abandonné**, un objet ou un périphérique parfaitement fonctionnel devient **inutilisable**.
- Lorsque les API sont **ouvertes** (documentées et d'usage libre), un développeur tiers peut développer une **application alternative** et prolonger la vie de l'objet ou du périphérique — y compris sur des systèmes d'exploitation non supportés par le concepteur initial du matériel.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Si le logiciel ou le pilote est associé à un équipement, un terminal ou un périphérique, le concepteur doit fournir des **API ouvertes et documentées**, afin que d'autres services numériques alternatifs puissent être utilisés sur l'appareil en cas de **défaut ou d'abandon du logiciel** d'origine — et ainsi **prolonger la vie** de l'objet ou du périphérique.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Si le service numérique repose sur l'utilisation d'un terminal, équipement ou appareil, le fournisseur doit rendre disponibles les **API nécessaires à l'exploitation** de l'objet connecté. Ces API doivent être **documentées et d'usage libre**, afin qu'un programme ou pilote alternatif puisse être créé pour prolonger la durée de vie de l'objet ou du périphérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="2">}}
{{% tab tabName="Data Act (UE)" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Système`, `Responsable Juridique`

Pour les objets connectés, ce critère rejoint désormais une **obligation légale européenne** plutôt qu'une simple bonne pratique. Le [règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act), entré en application le **12 septembre 2025**, impose aux fabricants et fournisseurs de services connectés que les données générées par un objet connecté soient rendues **directement accessibles** à l'utilisateur et aux tiers, dans un **format structuré, couramment utilisé et lisible par machine** (JSON, XML, CSV, Parquet, Apache Avro…), le plus souvent via une **API conforme à un standard reconnu** (REST par exemple).

Une échéance clé s'applique en **septembre 2026** pour la conception des nouveaux objets connectés et de leurs services associés — un calendrier qui concerne directement les fabricants d'objets connectés, éditeurs de logiciels et intégrateurs. Le format propriétaire reste toléré pour le fonctionnement interne du produit, mais **pas** pour les données mises à disposition des utilisateurs et des tiers.

{{% /tab %}}

{{% tab tabName="Outils & cas concrets" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Quand le fabricant ne propose pas d'API ouverte, l'écosystème du **firmware libre** permet parfois de reprendre la main : [**Tasmota**](https://tasmota.github.io/docs/) (créé par Theo Arends) est un firmware open source qui remplace le firmware propriétaire de milliers de prises et interrupteurs connectés Wi-Fi (souvent basés sur des puces Tuya), pour les faire communiquer en **local**, sans dépendre du cloud du fabricant. [**Home Assistant**](https://www.home-assistant.io/), hub domotique open source, agrège ensuite ces appareils (via Tasmota, [ESPHome](https://esphome.io/) ou des intégrations tierces) dans une interface unique et pérenne.

À nuancer cependant : depuis 2022, plusieurs fabricants ont **remplacé les puces reflashables** (ESP8266) par des alternatives verrouillées (Beken BK7231, Realtek RTL8720) précisément pour empêcher ce type de reprise en main — illustrant que le firmware libre reste un **contournement**, pas un substitut à une véritable obligation d'ouverture des API à la conception, celle que vise justement ce critère 1.10 et le Data Act.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Le secteur de la domotique grand public documente, malheureusement en abondance, le scénario que ce critère cherche à éviter — des objets **matériellement fonctionnels rendus inutilisables** par la fermeture d'une API ou d'un service cloud propriétaire ([source](https://www.howtogeek.com/smart-home-brands-that-bricked-products/)) :

- **Revolv** : racheté par Google/Nest en 2014, le hub domotique — vendu avec la promesse d'un usage « à vie » — voit ses serveurs fermés dès 2016, rendant tous les boîtiers inertes du jour au lendemain.
- **Insteon** : l'entreprise a fermé ses serveurs cloud sans préavis à ses clients, dont certains avaient investi plusieurs centaines, voire milliers de dollars dans leur installation.
- **Wink** : bascule en 2020 vers un abonnement mensuel payant pour conserver l'accès à des fonctionnalités (dont l'API) auparavant incluses gratuitement — sans fermer le service, mais en le rendant inaccessible à qui refuse de payer.

À l'inverse, l'écosystème **Tasmota**/**Home Assistant** cité plus haut illustre la parade côté communauté : « quand Tuya ou SmartLife ferment leurs serveurs, vos appareils continuent de fonctionner » — à condition d'avoir pu, en amont, reflasher un firmware libre sur un matériel qui le permettait encore.

Ce risque ne se limite pas à la domotique — deux exemples touchant d'autres catégories de matériel :

- **Casques de réalité virtuelle** : avec la mise à jour Windows 11 24H2 (2024), Microsoft a **retiré du système le portail Windows Mixed Reality**, rendant inopérants tous les casques reposant dessus — dont le **HP Reverb G2** — sauf à rester bloqué sur une version antérieure de Windows. Un pilote non officiel, [**Oasis**](https://www.heise.de/en/news/HP-Reverb-G2-Co-New-driver-makes-Windows-VR-glasses-usable-again-10511180.html), développé par un ancien membre de l'équipe Mixed Reality de Microsoft, s'appuie directement sur SteamVR (sans dépendre du portail supprimé) pour redonner vie à ces casques — mais uniquement sur cartes graphiques Nvidia, laissant les possesseurs de GPU AMD ou Intel sans solution.
- **Enceintes connectées** : en 2020, Sonos a présenté puis retiré en urgence, après un tollé public, un [« Recycle Mode »](https://www.digitalmusicnews.com/2020/03/06/sonos-scraps-recycle-mode/) qui aurait délibérément rendu inutilisables (compte à rebours de 21 jours) certaines enceintes fonctionnelles en échange d'une remise sur un nouveau modèle — un cas d'obsolescence programmée assumée, plutôt que subie, qui a valu des excuses publiques du PDG de l'entreprise.

{{% /tab %}}

{{< /tabs >}}
