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
| **Applicabilité** | `N/A si le service numérique ne repose pas sur un objet connecté ou un périphérique matériel` |
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
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="Data Act (UE)" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Architecte Système`, `Responsable Juridique`

Pour les objets connectés, ce critère rejoint désormais une **obligation légale européenne** plutôt qu'une simple bonne pratique. Le [règlement européen sur les données (Data Act)](https://digital-strategy.ec.europa.eu/en/policies/data-act), entré en application le **12 septembre 2025**, impose aux fabricants et fournisseurs de services connectés que les données générées par un objet connecté soient rendues **directement accessibles** à l'utilisateur et aux tiers, dans un **format structuré, couramment utilisé et lisible par machine** (JSON, XML ou CSV, par exemple), ce qui passe souvent par une **API documentée**.

Une échéance clé s'applique en **septembre 2026** pour la conception des nouveaux objets connectés et de leurs services associés — un calendrier qui concerne directement les fabricants d'objets connectés, éditeurs de logiciels et intégrateurs. L'obligation porte sur les données mises à disposition des utilisateurs et des tiers, **pas** sur les formats internes du produit.

{{% /tab %}}

{{% tab tabName="Outils & cas concrets" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

Quand le fabricant ne propose pas d'API ouverte, l'écosystème du **firmware libre** permet parfois de reprendre la main : [**Tasmota**](https://tasmota.github.io/docs/) (créé par Theo Arends) est un firmware open source qui remplace le firmware propriétaire de milliers de prises et interrupteurs connectés Wi-Fi (souvent basés sur des puces Tuya), pour les faire communiquer en **local**, sans dépendre du cloud du fabricant. [**Home Assistant**](https://www.home-assistant.io/), hub domotique open source, agrège ensuite ces appareils (via Tasmota, [ESPHome](https://esphome.io/) ou des intégrations tierces) dans une interface unique et pérenne.

À nuancer cependant : depuis 2022, plusieurs fabricants ont **remplacé l'ESP8266** par d'autres puces (Beken BK7231, Realtek RTL8720), que Tasmota ne prend pas en charge. Des firmwares libres comme OpenBeken les gèrent, mais la manipulation est plus délicate. Le firmware libre reste donc un **contournement**, pas un substitut à une véritable ouverture des API dès la conception, celle que visent ce critère 1.10 et le Data Act.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Système`

**1. Exposer une API locale**, sur le réseau de l'utilisateur, en plus du cloud du fabricant : l'objet reste utilisable si les serveurs ferment. Les enceintes SoundTouch de Bose en sont l'exemple : elles répondent à des commandes HTTP sur le port 8090, et l'application les pilote en local depuis la fin du cloud, le 6 mai 2026 ([Bose](https://www.bose.com/soundtouch-end-of-life)).

**2. Annoncer l'objet sur le réseau** avec un protocole de découverte standard, mDNS et DNS-SD, plutôt qu'un mécanisme propre au fabricant. Un logiciel tiers le trouve alors sans configuration ; sous Linux, pour vérifier :

```sh
avahi-browse -rt _http._tcp
```

La première documentation de l'API de Bose, publiée le 7 janvier 2026, ne décrivait pas la découverte des enceintes. La version 1.1 du 1er avril l'a ajoutée ([SoundTouch Web API](https://assets.bosecreative.com/m/496577402d128874/original/SoundTouch-Web-API.pdf)).

**3. Décrire l'API dans un format standard.** Un fichier [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0.html), lisible par les humains et par les outils, suffit à générer documentation et clients. Exemple pour un thermostat :

```yaml
openapi: 3.1.0
info:
  title: API locale du thermostat
  version: 1.0.0
  license: { name: Licence Ouverte 2.0, identifier: etalab-2.0 }
servers:
  - url: http://thermostat.local:8080/api/v1
paths:
  /consigne:
    get:
      summary: Lire la température de consigne
      responses:
        "200":
          description: Consigne en degrés Celsius
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Consigne" }
    put:
      summary: Modifier la consigne
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Consigne" }
      responses:
        "204": { description: Consigne enregistrée }
  /mesures:
    get:
      summary: Exporter l'historique des relevés
      responses:
        "200":
          description: Une ligne par relevé
          content:
            text/csv:
              schema: { type: string }
components:
  schemas:
    Consigne:
      type: object
      required: [celsius]
      properties:
        celsius: { type: number, minimum: 5, maximum: 30 }
```

Avec une licence ouverte, cette description se reprend librement, par exemple pour générer un client. L'export en CSV répond à l'exigence du Data Act d'un format structuré, couramment utilisé et lisible par machine (onglet « Data Act (UE) »).

**4. Prévoir la fin du support** dès la conception (voir le [critère 3.4](../../architecture/3-4_mises-a-jour-correctives/)) : une dernière version du logiciel qui active le mode local et, si possible, autorise l'installation d'un firmware libre. Bose a publié son API et mis à jour son application avant la fermeture, mais ses enceintes ne reçoivent plus de mise à jour de sécurité.

**5. Documenter** dans la déclaration d'écoconception : l'adresse de la documentation de l'API, sa licence, ce qui fonctionne sans le cloud du fabricant, et le plan de fin de support.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Développeur`

- le [critère 1.9](../1-9_technologies-standard/) (technologies standard) : des interfaces standard, utilisables par d'autres logiciels ;
- le [critère 3.4](../../architecture/3-4_mises-a-jour-correctives/) (mises à jour correctives des équipements) : un matériel documenté peut continuer d'être mis à jour ;
- le [critère 2.2](../../specifications/2-2_anciens-terminaux/) (anciens terminaux) : la même volonté de prolonger la vie du matériel ;
- le [critère 1.8](../1-8_efforts-open-source/) (open source) : le code qui pilote le matériel peut être publié.

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

À l'inverse, l'écosystème **Tasmota**/**Home Assistant** cité plus haut illustre la parade côté communauté : avec un firmware local, les appareils continuent de fonctionner même si le cloud du fabricant tombe en panne ou ferme, à condition d'avoir pu, en amont, installer ce firmware sur un matériel qui le permettait.

Ce risque ne se limite pas à la domotique — deux exemples touchant d'autres catégories de matériel :

- **Casques de réalité virtuelle** : avec la mise à jour Windows 11 24H2 (2024), Microsoft a **retiré du système le portail Windows Mixed Reality**, rendant inopérants tous les casques reposant dessus — dont le **HP Reverb G2** — sauf à rester bloqué sur une version antérieure de Windows. Un pilote non officiel, [**Oasis**](https://www.heise.de/en/news/HP-Reverb-G2-Co-New-driver-makes-Windows-VR-glasses-usable-again-10511180.html), développé par un ancien membre de l'équipe Mixed Reality de Microsoft, s'appuie directement sur SteamVR (sans dépendre du portail supprimé) pour redonner vie à ces casques — mais uniquement sur cartes graphiques Nvidia, laissant les possesseurs de GPU AMD ou Intel sans solution.
- **Enceintes connectées** : jusqu'en mars 2020, Sonos offrait 30 % de remise sur un nouveau modèle à qui activait, sur son ancienne enceinte, un [« Recycle Mode »](https://www.digitalmusicnews.com/2020/03/06/sonos-scraps-recycle-mode/) qui la rendait inutilisable au bout de 30 jours. La marque l'a supprimé après la polémique : un cas d'obsolescence organisée par le fabricant lui-même, plutôt que subie.

{{% /tab %}}

{{< /tabs >}}
