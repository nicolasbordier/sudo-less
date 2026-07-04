---
weight: 400
title: "1.4 - Revue d'écoconception"
description: "Critère 1.4 du RGESN : comment mettre en place des revues régulières et des outils de mesure pour vérifier dans la durée le respect de la démarche d'écoconception."
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2026-07-03T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique réalise-t-il régulièrement des revues pour s’assurer du respect de sa démarche d’écoconception ?

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
| **Critère**  | `1.4` |
| **Phase** | `Toutes les phases` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable RSE/Numérique soutenable` `Responsable IT` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.4/ |
{{< /table >}}

---

### 
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Selon le contexte, un **service numérique peut évoluer** : équipe qui change, ajout de contenu par les utilisateurs, traitements de plus en plus gourmands, etc. 

Pour veiller à ce que la démarche d’écoconception dure dans le temps, il est important de **réaliser régulièrement une revue**. 

Par ailleurs, la **publication d’une déclaration d’écoconception** œuvre à davantage de transparence sur la performance environnementale des services numériques à destination des utilisateurs et parties prenantes.


{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

**Réaliser une revue, auto-évaluation ou audit régulier, appliquant ce référentiel**. De plus, réaliser des **audits de performances** et **tests de charge** au sein de l’application / composant / micro service avec identification des bottlenecks (goulots d’étranglement), des ressources utilisées, etc. La fréquence de ces procédés devra être adaptée à la taille et à la nature du service numérique.

Il s’agit ensuite de rendre compte de cette (auto)évaluation dans une déclaration d’écoconception, qui devra être mise à jour régulièrement, au moins à chaque changement significatif du service. La **déclaration d’écoconception** devra également **indiquer les actions envisagées pour améliorer la performance environnementale** du service.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider ce critère, il convient de **mettre en œuvre une revue ou autoévaluation régulière appliquant ce référentiel** et d’en **rendre compte dans la déclaration d’écoconception** du service. Des **audits de performance** et des **tests de charge** réguliers devront également être effectués.


{{% /tab %}}
{{< /tabs >}}

---

### 
### Comment appliquer concrètement cette recommandation ?

En fonction de chaque contexte :

{{< tabs tabTotal="4">}}
{{% tab tabName="Site Web" %}}

Nous vous conseillons de consulter en détail le chapitre "**Evaluer l’impact du parcours utilisateur**" de la page [Evaluer et mesurer](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/3-evaluer-et-mesurer) du guide des **Designer Ethiques**.

Vous allez y apprendre comment évaluer périodiquement l'empreinte environnementale de votre site web via l'outil [`GreenIT-Analysis`](https://github.com/cnumr/GreenIT-Analysis) ([Chrome](https://chromewebstore.google.com/detail/greenit-analysis/mofbfhffeklkbebfclfaiifefjflcpad?pli=1), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/greenit-analysis/)), l'extension de référence maintenue par le [Collectif GreenIT](https://collectif.greenit.fr/). Intégrée aux DevTools du navigateur, elle calcule en direct le score **EcoIndex** de la page affichée à partir de trois mesures observables : la **complexité du DOM** (nombre de nœuds HTML après chargement complet), le **poids transféré** (somme en kilooctets de toutes les ressources téléchargées) et le **nombre de requêtes HTTP**. Ces trois critères produisent une note sur 100 et une lettre de A à G, ainsi qu'une estimation de la consommation d'eau et des émissions de GES pour l'affichage de la page. Fonctionnant côté client, elle permet de mesurer un **parcours utilisateur complet, y compris derrière une authentification ou un firewall** (contrairement à un outil en ligne qui ne teste qu'une URL publique).

Pour plus de détails sur le fonctionnement des outils **GreenIT-Analysis** et **EcoIndex** (l'algorithme est identique) :
- [Article - Sous le capot de la mesure (Pierrick Crepy - 2021)](https://blog.octo.com/sous-le-capot-de-la-mesure-ecoindex)

Pour automatiser cette mesure en continu plutôt que de la lancer manuellement page par page, [EcoSonar](https://github.com/green-code-initiative/EcoSonar), maintenu par la [Green Code Initiative](https://www.greencodeinitiative.org/) (association derrière le plugin `EcoCode`), combine une **analyse dynamique** (GreenIT-Analysis/EcoIndex, Google Lighthouse et le validateur W3C) avec une **analyse statique du code** via un plugin SonarQube. Intégré à une pipeline SonarQube existante, il permet d'auditer automatiquement l'ensemble d'un site à chaque analyse plutôt qu'une page à la fois manuellement — une bonne option pour une équipe qui utilise déjà SonarQube dans sa chaîne de revue de code.

En alternative **payante** (essai limité, tarifs sur devis selon des paliers Starter/Basic/Business/Professional), [Fruggr](https://www.fruggr.io/fr/), édité par [Digital4Better](https://digital4better.com/) (déjà cité en retour d'expérience du critère 1.1), propose une plateforme SaaS reposant sur une méthodologie d'**ACV numérique** plus large que le seul EcoIndex (épuisement des ressources, particules fines…), avec un score sur 100 étalonné sur l'analyse d'un million de pages d'accueil (httparchive). Fruggr recommande explicitement de réserver l'analyse exhaustive page par page aux mises en production majeures, et de n'intégrer en CI/CD qu'une **analyse par unité fonctionnelle**, plus légère — la même logique de budget par fonctionnalité déjà évoquée plus haut, mais packagée en solution clé en main avec tableau de bord de pilotage dans la durée plutôt qu'en outils à assembler soi-même.

Ces outils dédiés à l'écoconception peuvent être complétés par deux outils de performance web plus généralistes, gratuits et maintenus par Google — à condition de garder à l'esprit qu'ils mesurent l'**expérience utilisateur perçue**, pas directement un impact environnemental (même si les deux sont corrélés : une page plus légère et plus rapide consomme aussi moins de ressources) :

- [**Lighthouse**](https://developer.chrome.com/docs/lighthouse) (open source, intégré aux DevTools Chrome, en CLI ou via [PageSpeed Insights](https://pagespeed.web.dev/)) audite une page sur 5 axes : Performance, Accessibilité, Bonnes pratiques, SEO et PWA. Décliné en [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci), il s'intègre en pipeline (action GitHub officielle disponible) pour faire échouer une build en cas de dépassement d'un **budget de performance** défini par `budget.json` — la même logique de porte CI/CD que GreenFrame ou Fruggr, appliquée cette fois à la performance web générale plutôt qu'à une mesure d'émissions.
- Les [**Core Web Vitals**](https://web.dev/articles/vitals) sont les trois métriques que Google a isolées comme les plus représentatives du ressenti utilisateur : LCP (vitesse de chargement, bon score sous 2 s depuis le durcissement 2026 du seuil), INP (réactivité aux interactions, sous 200 ms) et CLS (stabilité visuelle, sous 0.1). Contrairement au score Lighthouse (mesuré en laboratoire sur une session simulée), les Core Web Vitals peuvent aussi être consultées en **données de terrain** issues des vrais visiteurs via le rapport dédié de la [Search Console](https://support.google.com/webmasters/answer/9205520) — utile pour objectiver une dérive progressive de performance dans le temps plutôt qu'un seul relevé ponctuel.

{{% /tab %}}

{{% tab tabName="Application mobile" %}}

Contrairement au web, le poids d'une page ne suffit pas à estimer l'impact d'une application mobile native : il faut mesurer la **consommation réelle sur terminal** (CPU, batterie, réseau).

[GreenSpector](https://greenspector.com/en/consulting-and-services/), éditeur français spécialisé, combine un **audit statique** (détection des mauvaises pratiques dans le code) et une **sonde de mesure dynamique** exécutée sur un banc de plus de 100 smartphones et tablettes réels (haut, moyen et bas de gamme, Android et iOS). Leurs études de cas font état de gains de **25 à 70 % de consommation énergétique** après écoconception d'une application mobile native.

Leur outil [Greenspector Studio couvre directement une quinzaine de critères du RGESN mesurables](https://greenspector.com/greenspector-studio-et-rgesn/), dont le 1.4 : il permet d'automatiser des parcours utilisateurs représentatifs, de suivre un **budget de performance dans le temps** (pour détecter les régressions d'un sprint à l'autre) et de s'intégrer en CI/CD pour en faire une revue continue plutôt qu'un audit ponctuel.

Sans budget pour un banc de mesure dédié, une alternative gratuite consiste à combiner des outils génériques (pas spécifiques à l'écoconception, mais détournables pour mesurer le **poids réseau et la charge machine d'une unité fonctionnelle**) : [Maestro](https://maestro.dev/) ([CLI open source](https://github.com/mobile-dev-inc/maestro), flows YAML) automatise un parcours reproductible (ex. « ajouter un article au panier ») sur émulateur ou terminal réel, pendant que [Proxyman](https://proxyman.com/) (gratuit pour un usage basique, licence unique payante pour les fonctionnalités avancées) capture en proxy le trafic HTTP/HTTPS généré et permet de chiffrer le volume de données transféré par ce parcours. Cette combinaison ne mesure que le **réseau**, mais [Flashlight](https://flashlight.dev/) ([open source, BAM.tech](https://github.com/bamlab/flashlight)) comble le manque côté **CPU/RAM/FPS** : il [supporte nativement les flows Maestro](https://docs.flashlight.dev/test/maestro/) (une version forkée de Maestro est même fournie pour fiabiliser la mesure du temps d'exécution) et calcule un score de performance agrégé, sans instrumentation à ajouter dans l'app, y compris en production. L'ensemble Maestro + Proxyman + Flashlight reste cohérent avec la méthodologie déjà utilisée côté web (poids de page, nombre de requêtes) et permet d'objectiver un budget de performance **par fonctionnalité**, rejouable à chaque sprint et intégrable en CI.

Pour un diagnostic ponctuel en cours de développement, les IDE natifs embarquent leurs propres profilers gratuits : le [Profiler d'Android Studio](https://developer.android.com/studio/profile/power-profiler) (CPU, mémoire, réseau, et un onglet Power/Energy dédié) et le [Power Profiler d'Xcode Instruments](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) (qui a remplacé l'ancien template « Energy Log » depuis Xcode 13). Utiles pour investiguer une régression détectée, ils restent des outils d'**inspection manuelle et locale**, à la différence des outils ci-dessus qui s'automatisent nativement dans une chaîne de revue régulière.

Pour scripter ce type de mesure côté iOS sans passer par l'interface d'Instruments, [py-ios-device](https://github.com/YueChen-C/py-ios-device) expose en Python le protocole `instruments` d'Apple et permet de récupérer CPU, GPU, mémoire et autres métriques depuis un terminal réel en ligne de commande — l'équivalent, côté iOS, de ce que Flashlight apporte côté Android pour automatiser une mesure en CI. À noter : il s'agit d'un projet communautaire qui repose sur un protocole privé rétro-ingénieré (non maintenu par Apple), à tester avant d'en dépendre dans un pipeline critique.

Pour une application déjà publiée, Google et Apple fournissent également des outils natifs de suivi en production, sans instrumentation à ajouter :

- [Android Vitals](https://developer.android.com/topic/performance/vitals) (Play Console) remonte des métriques de qualité technique agrégées depuis les terminaux des utilisateurs réels, dont plusieurs indicateurs directement liés à la consommation : **réveils excessifs** (`excessive wakeups`, plus de 10 réveils/heure hors charge) et, depuis fin 2025/2026, les **wake locks partiels excessifs** (plus de 3h cumulées sur 24h). Ce n'est plus seulement un indicateur passif : depuis mars 2026, une application au-delà de ces seuils peut être signalée comme énergivore sur le Play Store et exclue des surfaces de découverte (recommandations), ce qui en fait un signal de revue à surveiller au même titre qu'un budget de performance.
- Le [rapport de pré-lancement](https://support.google.com/googleplay/android-developer/answer/9842757) (Firebase Test Lab) teste automatiquement chaque build importé sur un panel d'appareils réels et remonte, entre autres, des problèmes de performance et de stabilité **avant la mise en production** — un équivalent natif et gratuit à la logique de porte CI/CD décrite plus haut (Flashlight, GreenSpector Studio), bien que moins spécifiquement orienté énergie/carbone.
- Côté iOS, [MetricKit](https://developer.apple.com/documentation/MetricKit) remonte quotidiennement, depuis les terminaux réels des utilisateurs, des métriques agrégées de CPU, mémoire, réseau et **impact énergétique**, consultables notamment dans l'Organizer d'Xcode.

{{% /tab %}}

{{% tab tabName="Application Backend (API, batch …)" %}}

Pour une API ou un traitement batch, l'enjeu est de mesurer la consommation électrique **au niveau du processus**, pas seulement de la machine.

[Scaphandre](https://github.com/hubblo-org/scaphandre), agent de métrologie open source maintenu par [Hubblo](https://hubblo.org/), expose en temps réel la puissance consommée par la machine hôte (`scaph_host_power_microwatts`) et par **chaque processus** (`scaph_process_power_consumption_microwatts`). Il tourne sur bare metal, VM ou Kubernetes, et exporte ses métriques vers Prometheus/Grafana pour un suivi dans la durée, ou directement en console pour identifier rapidement les 20 processus les plus énergivores lors d'un traitement batch.

Intégré à une chaîne de CI/CD ou à un tableau de bord de supervision existant, il permet de transformer une revue ponctuelle en **surveillance continue de la consommation** des services back-end.

En complément, [GreenFrame](https://greenframe.io/) ([CLI open source](https://github.com/marmelab/greenframe-cli), maintenu par l'agence [Marmelab](https://marmelab.com/)) déplace la mesure **avant la mise en production** : il démarre toute la stack dans des conteneurs Docker (API, base de données, dépendances), rejoue un scénario utilisateur ou une séquence d'appels API, et collecte les métriques `docker stats` (CPU, mémoire, réseau, disque) de chaque conteneur pour estimer une consommation en Wh. Intégré en CI, il permet de bloquer une pull request en cas de dépassement d'un **seuil d'émissions maximal**, ce qui en fait un bon complément à Scaphandre pour une revue systématique à chaque changement plutôt qu'une simple surveillance en production.

{{% /tab %}}

{{% tab tabName="Infrastructure / Architecture" %}}

À l'échelle de l'infrastructure, plusieurs approches complémentaires permettent d'outiller une revue régulière :

- [Boavizta](https://boavizta.org/), groupe de travail ouvert, fournit une base de données et une API ([Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur)) appliquant une méthodologie d'**analyse de cycle de vie** pour estimer l'empreinte fabrication *et* usage d'un serveur ou d'une instance cloud (GWP, énergie primaire, épuisement des ressources abiotiques). Leur outil [Cloud Scanner](https://www.sfeir.dev/cloud/surveillez-limpact-environnemental-de-vos-instances-ec2-avec-cloud-scanner-de-boavizta/) applique cette méthode aux instances AWS EC2, avec un export par région et type d'instance, réutilisable pour objectiver un choix d'architecture ou une migration. Leur tableau de bord [Datavizta](https://dataviz.boavizta.org/) permet, lui, d'explorer la base de données brute (impacts déclarés par les fabricants) pour comparer plusieurs équipements et visualiser la répartition fabrication/usage/fin de vie — utile en amont, pour objectiver un choix de matériel avant même de le déployer.
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) (Thoughtworks, open source) calcule une estimation d'émissions à partir des données de facturation, avec une vue **unifiée multi-cloud** (AWS, Azure, GCP) là où les outils propriétaires ci-dessous restent chacun cantonnés à leur fournisseur. Il propose aussi des recommandations d'optimisation chiffrées (économies de coût et de carbone estimées).
- Les principaux fournisseurs cloud proposent des tableaux de bord natifs : [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) (scopes 1, 2 et 3), [Google Cloud Carbon Footprint](https://cloud.google.com/carbon-footprint) (avec un outil de sélection de région par arbitrage carbone/coût/latence) et [Microsoft Emissions Impact Dashboard](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) pour Azure (rapport Power BI, principalement scope 3). Pratiques pour une revue périodique rapide, mais moins précis qu'une mesure de type Boavizta pour arbitrer entre plusieurs choix techniques.
- Côté hébergeurs souverains/européens, l'offre progresse : [OVHcloud Impact Tracker](https://www.ovhcloud.com/en/about-us/environmental-impact-tracker/) (scopes 1 à 3, méthode validée par un organisme indépendant selon le GHG Protocol et l'ISO 14067, disponible sur Baremetal/Hosted Private Cloud/Public Cloud Compute) et le [calculateur d'empreinte environnementale de Scaleway](https://www.scaleway.com/en/environmental-footprint-calculator/) (données quotidiennes carbone **et** eau, par produit/région/projet, méthodologie PCR ADEME) offrent un niveau de détail comparable aux hyperscalers. Plus sobre, [Infomaniak](https://www.infomaniak.com/en/ecology) affiche depuis 2024 l'empreinte carbone de ses principaux services d'hébergement directement sur la facture client, sans tableau de bord dédié.

{{% /tab %}}
{{< /tabs >}}

---


### 
### Pour aller plus loin :

{{< tabs tabTotal="3">}}

{{% tab tabName="Retours d'expériences" %}}

[Territoires en Transitions](https://beta.gouv.fr/startups/territoires-en-transitions.html) (beta.gouv.fr, porté par l'ADEME) illustre une revue d'écoconception intégrée au rythme de développement plutôt qu'un audit ponctuel isolé : « **Toutes les pages sont testées à la fin de chaque sprint (toutes les 2 semaines) pour suivre l'évolution du produit** », avec un suivi du poids de page, du nombre de requêtes, du nombre d'éléments DOM, du *First Meaningful Paint* et du *Time to Interactive* (source : [Retours d'expérience RGESN - Numérique écoresponsable](https://ecoresponsable.numerique.gouv.fr/ressources/documents-reference/referentiel-general-ecoconception/retour-experience/)).

À l'inverse, [Extia / Vamos](https://www.extia-group.com/fr-fr/blog/audit-d-ecoconception-d-un-service-numerique-existant-l-exemple-de-vamos-1) illustre un **audit d'écoconception ponctuel** d'un service existant : utile en point de départ (constituer un état des lieux, prioriser les actions), mais qui ne suffit pas à lui seul à valider ce critère sans mise en place d'une cadence de revue récurrente derrière.

Ces deux retours d'expérience montrent la distinction attendue par le critère 1.4 : une **revue régulière suivie dans le temps** (budget de performance, alerte de régression) apporte plus de garanties qu'un audit isolé, aussi complet soit-il.

{{% /tab %}}

{{% tab tabName="Déclaration d'écoconception" %}}

La déclaration d'écoconception est le document par lequel un service rend compte publiquement de sa démarche RGESN — c'est elle qui sert de preuve pour ce critère 1.4 (revue documentée) et pour le critère 1.5 (objectifs suivis dans le temps). L'Arcep et l'Arcom mettent à disposition des **gabarits officiels prêts à l'emploi**, à compléter directement plutôt qu'à rédiger de zéro :

- **Sans calcul de score** (si seule la rédaction textuelle vous intéresse) : [Word (.docx)](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.docx), [OpenDocument (.odt)](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.odt), [HTML](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.html) ou [texte brut](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.txt).
- **Avec calcul automatique du score d'avancement** : [tableur Excel (.xlsx)](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.xlsx) (Excel, OnlyOffice, Google Sheets, Apple Numbers) ou [tableur OpenDocument (.ods)](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.ods) (LibreOffice Calc, Apache OpenOffice Calc). Une variante « sans score » de ces mêmes tableurs existe aussi, pour qui veut juste la trame sans faire l'exercice de notation ([xlsx](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_outil_declaration_ecoconception_sans_score.xlsx), [ods](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_outil_declaration_ecoconception_sans_score.ods)).

**Comment fonctionne le tableur avec score :** une feuille par famille RGESN (Stratégie, Spécifications, Architecture, UX/UI, Contenus, Frontend, Backend, Hébergement, Algorithmie), où chaque critère se coche comme conforme, non conforme ou non applicable. Une feuille de synthèse « Score d'avancement » calcule alors automatiquement un score pondéré, publié en page 2 de la déclaration :

```
Score = [ (critères validés Prioritaire × 1,5) + (critères validés Recommandé × 1,25) + (critères validés Modéré × 1) ]
        ÷ [ (critères applicables Prioritaire × 1,5) + (critères applicables Recommandé × 1,25) + (critères applicables Modéré × 1) ]
        × 100
```

La pondération valorise donc davantage un critère « Prioritaire » (×1,5, comme le 1.4) qu'un critère « Modéré » (×1) — un même nombre de critères validés ne produit pas le même score selon leur priorité. Une fois les feuilles complétées, un export PDF intégré (menu Fichier → Exporter → Créer PDF, avec les options « classeur entier », « balises de structure pour l'accessibilité » et « compatible PDF/A ») génère directement un **document de 14 pages prêt à publier**, incluant un historique des scores des évaluations précédentes — pratique pour matérialiser la revue régulière demandée par ce critère 1.4 d'une version à l'autre.

{{% /tab %}}

{{< /tabs >}}

