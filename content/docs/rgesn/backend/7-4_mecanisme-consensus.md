---
weight: 400
title: "7.4 - Mécanisme de consensus sobre"
description: "Critère 7.4 du RGESN : se demander d'abord si une blockchain est nécessaire, écarter la preuve de travail, choisir la preuve d'enjeu ou d'autorité, régler la fréquence des blocs et mesurer la consommation des nœuds."
icon: "token"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique s'appuie-t-il sur un mécanisme de consensus qui minimise sa consommation de ressources ?

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
| **Critère**  | `7.4` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service ne repose pas sur un mécanisme de consensus` |
| **Métiers concernés** | `Développeur` `Administrateur Système` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/7.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'empreinte énergétique des services numériques reposant sur une technologie blockchain publique dépendra essentiellement du mécanisme de consensus choisi. Contrairement aux blockchains privées et de consortium, les blockchains publiques sont ouvertes à tout participant et doivent donc s'appuyer sur un mécanisme de consensus particulièrement sécurisé. La preuve de travail est le mécanisme de consensus utilisé qui consomme le plus d'énergie, car s'appuyant sur le minage. L'objectif est donc de réduire l'impact environnemental de la blockchain en évitant tout algorithme de consensus reposant sur le minage et en choisissant un mécanisme de consensus moins énergivore et, plus généralement, moins consommateur en ressources.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Prendre en compte les critères de performance environnementale dans le choix de la blockchain.

En particulier, choisir un mécanisme de consensus alternatif à la preuve de travail ne reposant pas sur le minage, en s'assurant que l'algorithme de consensus a une consommation énergétique réduite. Par exemple :

- Preuve d'enjeu ;
- Preuve d'enjeu déléguée ;
- Preuve d'autorité.

Si possible, définir les paramètres de la blockchain de manière à minimiser sa consommation en énergie et en ressources matérielles (par exemple : la fréquence des validations ou la gestion de la taille des blocs).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la consommation d'énergie et en ressources matérielles du mécanisme de consensus utilisé par le service numérique : l'algorithme doit être testé ou reconnu comme pauvre en consommation d'énergie et de ressources. Selon les fonctionnalités du service, choisir l'algorithme de consensus de la blockchain permettant de minimiser la consommation énergétique requise. Il faudra s'assurer que les paramètres de la blockchain minimisent son impact environnemental.

Si le service repose sur une blockchain ayant recours à la preuve de travail ou à un algorithme de consensus reposant sur le minage et, de façon générale, associée à une consommation énergétique et en ressources élevée, le critère n'est pas validé.

Le choix de la blockchain et la pertinence de l'algorithme de consensus choisi au regard des enjeux environnementaux devront être documentés dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Aucune fiche de RWEB, aucune recommandation du GR491 ni des Web Sustainability Guidelines du W3C ne porte sur la blockchain. Les sources ci-dessous viennent de la CNIL, du droit européen et des projets eux-mêmes.

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="Faut-il une blockchain ?" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Développeur`

Le mécanisme le plus sobre reste de ne pas en avoir. La CNIL, dans [« Blockchain et RGPD : quelles solutions pour un usage responsable en présence de données personnelles ? »](https://www.cnil.fr/fr/technologies/blockchain-et-rgpd-quelles-solutions-pour-un-usage-responsable-en-presence-de-donnees-personnelles) (20 septembre 2018), demande de justifier, dès la conception, le recours « à la technologie Blockchain plutôt qu'à une technologie alternative ».

Elle rappelle aussi qu'une donnée inscrite dans la chaîne « ne peut pas être modifiée ou supprimée », et recommande de ne pas y stocker de donnée personnelle en clair. Cela heurte directement les durées de conservation du [critère 7.2](../7-2_durees-conservation/) : ce qui est écrit dans une blockchain y reste.

Pour les besoins les plus courants, d'autres solutions existent :

| Besoin | Alternative sans consensus |
|---|---|
| Partager des données entre quelques organisations | Une base de données commune, avec des droits par organisation et un journal des modifications |
| Prouver qu'un document existait à une date | Un horodatage par une autorité ([RFC 3161](https://www.rfc-editor.org/rfc/rfc3161)) |
| Prouver qu'un document n'a pas été modifié | Une signature électronique |

{{% /tab %}}

{{% tab tabName="Les mécanismes de consensus" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`

| Mécanisme | Qui valide les blocs | Ce qui consomme | Critère 7.4 |
|---|---|---|---|
| Preuve de travail | Le premier mineur qui résout un calcul | Le calcul lui-même, dont la difficulté augmente avec le nombre de mineurs | **Non validé** |
| Preuve d'enjeu | Un validateur tiré au sort parmi ceux qui ont immobilisé des jetons | Les nœuds du réseau | Compatible |
| Preuve d'enjeu déléguée | Des délégués élus par les détenteurs de jetons | Les nœuds des délégués | Compatible |
| Preuve d'autorité | Des validateurs identifiés et autorisés | Les nœuds des validateurs | Compatible, pour un réseau privé ou de consortium |

**En preuve de travail, la dépense est le mécanisme de sécurité.** Un attaquant devrait dépenser plus que les autres mineurs réunis. Optimiser le logiciel n'y change rien, car la difficulté s'ajuste pour garder le même rythme de blocs.

**Sans minage, la consommation dépend du nombre de nœuds et de leur matériel.** C'est ce qui se mesure et se règle, avec la fréquence des blocs.

{{% /tab %}}

{{% tab tabName="Ordres de grandeur" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Administrateur Système`

**Ethereum** est passé de la preuve de travail à la preuve d'enjeu le 15 septembre 2022, lors de la « Merge ». D'après l'étude du Crypto Carbon Ratings Institute (CCRI) citée par [ethereum.org](https://ethereum.org/en/energy-consumption/), ce changement a réduit la consommation électrique annuelle du réseau de « more than 99.988% ».

La même page compare des consommations annuelles, dont les périmètres diffèrent :

| Réseau | Consommation annuelle |
|---|---:|
| Bitcoin (preuve de travail) | 149 TWh |
| Ethereum avant la Merge (preuve de travail) | 21 TWh |
| Ethereum après la Merge (preuve d'enjeu) | 0,0026 TWh, soit 2 601 MWh |

Le même réseau, aux mêmes usages, consomme environ 8 000 fois moins sans minage. Le critère 7.4 est classé **Prioritaire** pour cette raison.

{{% /tab %}}

{{% tab tabName="Réglementation MiCA" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable Juridique`

Le règlement européen sur les marchés de crypto-actifs (MiCA, règlement (UE) 2023/1114) oblige les prestataires de services sur crypto-actifs à publier, sur leur site, les principales incidences négatives sur le climat et l'environnement du mécanisme de consensus de chaque crypto-actif proposé (article 66, paragraphe 5). Les émetteurs le font dans leur livre blanc.

Le règlement délégué (UE) 2025/422, publié le 31 mars 2025, en fixe le contenu ([texte adopté](https://data.consilium.europa.eu/doc/document/ST-17034-2024-INIT/en/pdf)) :

- un indicateur obligatoire, la **consommation d'énergie annuelle**, en kWh ;
- au-delà de **500 000 kWh** par an, des indicateurs supplémentaires sur l'énergie et les émissions de gaz à effet de serre.

MiCA ne concerne que les crypto-actifs. Un service public qui utilise une blockchain peut cependant reprendre ces indicateurs pour documenter le critère 7.4 avec une méthode reconnue.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Administrateur Système`, `Développeur`

**1. Justifier le recours à une blockchain**, en comparant avec les alternatives de l'onglet « Faut-il une blockchain ? ». Le [critère 1.1](../../strategie/1-1_evaluation-utilite/) (utilité du service) s'applique aussi à ce choix technique.

**2. Sur une blockchain publique, écarter la preuve de travail**, et y écrire le moins possible. Pour prouver l'existence de documents, regrouper leurs empreintes (`SHA-256`) dans un arbre de Merkle et n'inscrire que sa racine, une fois par jour par exemple : une transaction au lieu d'une par document. Aucune donnée personnelle ne va dans la chaîne.

**3. Sur un réseau privé ou de consortium, choisir la preuve d'autorité.** Hyperledger Besu, un client Ethereum qui sert aussi aux réseaux privés, recommande QBFT, « the recommended enterprise-grade consensus protocol for private networks ». Il ne prend plus en charge Ethash, sa preuve de travail ([documentation](https://docs.besu-eth.org/private-networks/how-to/configure/consensus)).

**4. Régler la fréquence des blocs**, comme le demande le RGESN. Par défaut, QBFT produit un bloc chaque seconde, même vide, soit 86 400 blocs par jour. Dans le fichier `genesis.json` :

```json
{
  "config": {
    "qbft": {
      "blockperiodseconds": 5,
      "emptyblockperiodseconds": 60,
      "requesttimeoutseconds": 10
    }
  }
}
```

Un bloc toutes les cinq secondes au plus quand il y a des transactions, et un bloc vide par minute au plus quand il n'y en a pas, soit au plus 1 440 blocs vides par jour ([documentation QBFT](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft)). Le nombre de validateurs se règle aussi : QBFT en demande quatre pour tolérer une panne, et chacun de plus ajoute un serveur.

**5. Mesurer la consommation des nœuds** que le service opère : relevé de l'hébergeur ou wattmètre, multiplié par le nombre de nœuds, en kWh par an, l'indicateur de MiCA.

**6. Documenter** dans la déclaration d'écoconception, comme l'exige le moyen de test. Par exemple : « Réseau de consortium Hyperledger Besu, consensus QBFT, quatre validateurs. Un bloc vide par minute au plus. Consommation estimée : 1 200 kWh par an. Seules les racines d'arbres de Merkle sont inscrites, une fois par jour. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`

- le [critère 1.1](../../strategie/1-1_evaluation-utilite/) (utilité) : une blockchain doit répondre à un besoin qu'une base de données ne couvre pas ;
- le [critère 7.2](../7-2_durees-conservation/) (durées de conservation) : une donnée inscrite dans la chaîne ne peut pas être supprimée ;
- le [critère 2.8](../../specifications/2-8_fournisseurs-impacts-environnementaux/) (impacts des fournisseurs) : une blockchain fournie en service relève aussi de l'évaluation des fournisseurs.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

| Site | Déclaration | Justification |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | Non applicable | — |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Non applicable | « Pas de mécanisme de consensus. » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Non applicable | « Le service ne repose pas sur un mécanisme de consensus. » |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | Non détaillé | — |

**Aucun des services relevés n'utilise de blockchain.** Le critère est pourtant classé **Prioritaire** : pour un service qui en utilise une, le choix du mécanisme décide à lui seul de l'essentiel de l'impact.

**Ethereum** montre qu'un changement de mécanisme est possible, mais coûteux : sa chaîne en preuve d'enjeu a fonctionné près de deux ans en parallèle avant la Merge de 2022. Pour un nouveau service, le choix se fait dès la conception.

{{% /tab %}}

{{< /tabs >}}
