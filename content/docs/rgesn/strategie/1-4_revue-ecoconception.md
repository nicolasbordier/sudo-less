---
weight: 400
title: "1.4 - Revue d'écoconception"
description: "Critère 1.4 du RGESN : comment mettre en place des revues régulières et des outils de mesure pour vérifier dans la durée le respect de la démarche d'écoconception."
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
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
| **Applicabilité** | `Applicable à tous les services` |
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
### Complément pour appliquer concrètement cette recommandation ?

En fonction de chaque contexte :

{{< tabs tabTotal="6">}}
{{% tab tabName="Site Web" %}}

Le chapitre « **Evaluer l'impact du parcours utilisateur** » de la page [Evaluer et mesurer](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/3-evaluer-et-mesurer) du guide des **Designers Éthiques** explique comment évaluer périodiquement l'empreinte d'un site avec [`GreenIT-Analysis`](https://github.com/cnumr/GreenIT-Analysis) ([Chrome](https://chromewebstore.google.com/detail/greenit-analysis/mofbfhffeklkbebfclfaiifefjflcpad?pli=1), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/greenit-analysis/)), l'extension du [Collectif GreenIT](https://collectif.greenit.fr/).

Intégrée aux outils de développement, elle calcule le score **EcoIndex** de la page à partir de trois mesures : la **complexité du DOM**, le **poids transféré** et le **nombre de requêtes**. Elle donne une note sur 100, une lettre de A à G et une estimation de l'eau consommée et des gaz à effet de serre émis. Comme elle fonctionne dans le navigateur, elle mesure aussi un **parcours derrière une authentification**. Pour le détail de l'algorithme : [Sous le capot de la mesure (Pierrick Crepy, 2021)](https://blog.octo.com/sous-le-capot-de-la-mesure-ecoindex).

Pour automatiser la revue :

- [EcoSonar](https://github.com/green-code-initiative/EcoSonar), de la [Green Code Initiative](https://www.greencodeinitiative.org/), combine EcoIndex, Lighthouse et le validateur W3C avec une **analyse statique du code** dans SonarQube : une bonne option pour une équipe qui l'utilise déjà ;
- [Fruggr](https://www.fruggr.io/fr/), de [Digital4Better](https://digital4better.com/), solution **payante**, mesure l'empreinte par une **analyse du cycle de vie** de l'ensemble du système, plus large que l'EcoIndex ([Carenews](https://www.carenews.com/carenews-pro/news/fruggr-la-tech-au-service-de-la-reduction-de-l-impact-numerique)) ;
- [**Lighthouse CI**](https://github.com/GoogleChrome/lighthouse-ci) fait échouer un build qui dépasse un **budget de performance**. Lighthouse mesure l'expérience perçue, pas directement l'impact environnemental, mais les deux sont corrélés ;
- les [**Core Web Vitals**](https://web.dev/articles/vitals) (LCP, INP, CLS) se suivent en **données de terrain**, issues des vrais visiteurs, dans la [Search Console](https://support.google.com/webmasters/answer/9205520) : utile pour repérer une dérive progressive.

{{% /tab %}}

{{% tab tabName="Application mobile" %}}

Le poids d'une page ne suffit pas pour une application native : il faut mesurer la **consommation réelle sur le terminal** (processeur, batterie, réseau).

[GreenSpector](https://greenspector.com/en/consulting-and-services/), éditeur français, mesure les applications sur des smartphones et tablettes réels. Il range [14 critères du RGESN parmi ceux qui « reposent sur de la mesure »](https://greenspector.com/greenspector-studio-et-rgesn/), dont le 1.4. Son outil Greenspector Studio automatise des parcours représentatifs, suit un **budget de performance dans le temps** et s'intègre en CI/CD.

Sans banc de mesure, des outils gratuits mesurent une **unité fonctionnelle** rejouable à chaque sprint :

- [Maestro](https://maestro.dev/) ([open source](https://github.com/mobile-dev-inc/maestro)) automatise un parcours, par exemple « ajouter un article au panier », sur émulateur ou terminal réel ;
- [Proxyman](https://proxyman.com/) capture le trafic HTTP de ce parcours pour en chiffrer le volume ;
- [Flashlight](https://flashlight.dev/) ([open source](https://github.com/bamlab/flashlight)) mesure le processeur, la mémoire et la fluidité sur Android, en [rejouant les parcours Maestro](https://docs.flashlight.dev/test/maestro/) ;
- côté iOS, [py-ios-device](https://github.com/YueChen-C/py-ios-device) récupère ces métriques en ligne de commande, mais repose sur un protocole privé d'Apple rétro-ingénieré : à tester avant d'en dépendre.

Les profilers d'[Android Studio](https://developer.android.com/studio/profile/power-profiler) et d'[Xcode](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) servent à investiguer une régression, à la main.

Pour une application publiée :

- [Android Vitals](https://developer.android.com/topic/performance/vitals) (Play Console) remonte depuis les terminaux réels les **wake locks partiels excessifs** : [2 heures cumulées ou plus sur 24 heures](https://developer.android.com/google/play/vitals/excessive-wakelock), application en arrière-plan. Depuis le 1er mars 2026, une application dont 5 % des sessions dépassent ce seuil peut afficher un avertissement de consommation de batterie sur le Play Store ([BleepingComputer](https://www.bleepingcomputer.com/news/security/google-to-flag-android-apps-with-excessive-battery-use-on-the-play-store/)) ;
- le [rapport de pré-lancement](https://support.google.com/googleplay/android-developer/answer/9842757) teste chaque build sur des appareils réels avant la mise en production ;
- [MetricKit](https://developer.apple.com/documentation/MetricKit) remonte chaque jour, sur iOS, des métriques de processeur, mémoire, réseau et **impact énergétique**.

Pour la revue du code lui-même, les extensions SonarQube [creedengo](https://github.com/green-code-initiative/creedengo-rules-specifications/blob/main/RULES.md) signalent à chaque analyse une partie des défauts du référentiel [Best Practices Mobile](https://github.com/cnumr/best-practices-mobile) du CNUMR : verrous de veille durables (règle GCI508), capteurs ou localisation jamais arrêtés (voir le [critère 6.6](../../frontend/6-6_capteurs-terminaux/)).

{{% /tab %}}

{{% tab tabName="Application Backend (API, batch …)" %}}

Pour une API ou un traitement batch, il faut mesurer la consommation **au niveau du processus**, pas seulement de la machine.

[Scaphandre](https://github.com/hubblo-org/scaphandre), agent open source de [Hubblo](https://hubblo.org/), mesure en temps réel la puissance consommée par la machine et par **chaque processus**, sur serveur physique, VM ou Kubernetes. Exporté vers Prometheus et Grafana, il transforme la revue ponctuelle en **surveillance continue**.

[GreenFrame](https://greenframe.io/) ([CLI open source](https://github.com/marmelab/greenframe-cli), de [Marmelab](https://marmelab.com/)) mesure **avant la mise en production** : il démarre la stack dans des conteneurs Docker, rejoue un scénario et estime la consommation en Wh. En CI, il peut bloquer une pull request qui dépasse un **seuil d'émissions**.

{{% /tab %}}

{{% tab tabName="Infrastructure / Architecture" %}}

Pour une revue régulière de l'infrastructure :

- [Boavizta](https://boavizta.org/), groupe de travail ouvert, fournit une API ([Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur)) qui estime par **analyse de cycle de vie** l'empreinte de fabrication et d'usage d'un serveur ou d'une instance cloud. [Cloud Scanner](https://www.sfeir.dev/cloud/surveillez-limpact-environnemental-de-vos-instances-ec2-avec-cloud-scanner-de-boavizta/) l'applique aux instances AWS EC2, et [Datavizta](https://dataviz.boavizta.org/) compare des équipements avant de les choisir ;
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) (Thoughtworks, open source) estime les émissions à partir de la facturation, avec une vue **multi-cloud** (AWS, Azure, GCP) ;
- les tableaux de bord des fournisseurs cloud, [AWS](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Google Cloud](https://cloud.google.com/carbon-footprint) et [Azure](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard), sont pratiques pour une revue rapide, mais moins précis que Boavizta pour arbitrer entre deux choix techniques ;
- côté hébergeurs européens, [OVHcloud Impact Tracker](https://www.ovhcloud.com/en/about-us/environmental-impact-tracker/) (scopes 1 à 3) et le [calculateur de Scaleway](https://www.scaleway.com/en/environmental-footprint-calculator/) (carbone **et** eau, méthode ADEME) détaillent l'empreinte par produit. [Infomaniak](https://www.infomaniak.com/en/ecology) l'affiche sur la facture.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Développeur`

**1. Fixer le rythme.** Le critère ne fixe pas de fréquence. Un rythme courant : une auto-évaluation complète du RGESN chaque année et à chaque changement significatif (refonte, fonctionnalité majeure, changement d'hébergeur), et des mesures automatiques à chaque mise en production.

**2. Automatiser l'audit de performance** sur quelques parcours représentatifs, les plus consultés et les plus lourds. Les assertions Lighthouse CI du [critère 6.1](../../frontend/6-1_poids-requetes-ecran/) bloquent une version qui dépasse le budget. Pour repérer aussi la dérive due aux contenus ajoutés entre deux versions, lancer les mêmes mesures chaque semaine. Avec GitHub Actions :

```yaml
on:
  release:
    types: [published]   # à chaque mise en production
  schedule:
    - cron: "0 6 * * 1"  # et chaque lundi à 6 h UTC
```

**3. Ajouter un test de charge**, que demande aussi le critère. Avec [k6](https://grafana.com/docs/k6/latest/) (Grafana Labs, open source), le scénario s'écrit en JavaScript, avec des seuils qui font échouer le test :

```js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 50 },  // montée à 50 utilisateurs simultanés
    { duration: '3m', target: 50 },
    { duration: '1m', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95 % des réponses en moins de 500 ms
    http_req_failed: ['rate<0.01'],    // moins de 1 % d'erreurs
  },
};

export default function () {
  const res = http.get(`${__ENV.BASE_URL}/carte`);
  check(res, { 'statut 200': (r) => r.status === 200 });
  sleep(1);
}
```

```sh
K6_WEB_DASHBOARD=true K6_WEB_DASHBOARD_EXPORT=charge-2026-10.html \
  k6 run -e BASE_URL=https://recette.exemple.fr charge.js
```

Le rapport HTML exporté garde la trace de chaque revue. Le nombre d'utilisateurs simultanés se déduit du pic relevé par la mesure d'audience, pas d'un chiffre arbitraire. Le test se lance sur un environnement de recette ; sur la production, il se prévient auprès de l'hébergeur.

**4. Trouver le goulot d'étranglement.** Pendant le test, relever le processeur et la mémoire de chaque conteneur (`docker stats`) ou la puissance par processus avec Scaphandre (onglet « Application Backend (API, batch …) »). La ressource qui sature la première désigne la prochaine optimisation : requête SQL lente, cache serveur absent ([critère 7.1](../../backend/7-1_cache-serveur/)), traitement à décaler.

**5. Documenter** dans la déclaration d'écoconception : la date de la revue et le score RGESN, les parcours mesurés et leurs résultats, le scénario de charge et le goulot identifié, puis les actions envisagées, comme le demande la mise en œuvre.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Responsable IT`

- le [critère 1.3](../1-3_referent-ecoconception/) (référent écoconception) : la personne qui organise les revues ;
- le [critère 1.5](../1-5_objectifs-environnementaux/) (objectifs environnementaux) : chaque revue mesure l'écart aux objectifs ;
- le [critère 2.6](../../specifications/2-6_revue-conception-code/) (revue de conception et de code) : la revue technique, au fil des développements ;
- le [critère 6.1](../../frontend/6-1_poids-requetes-ecran/) (poids et requêtes par écran) : des indicateurs simples à relever à chaque revue.

{{% /tab %}}
{{< /tabs >}}

---


### 
### Pour aller plus loin :

{{< tabs tabTotal="2">}}

{{% tab tabName="Retours d'expériences" %}}

[Territoires en Transitions](https://beta.gouv.fr/startups/territoires-en-transitions.html) (beta.gouv.fr, ADEME) intègre la revue au rythme de développement : « **Toutes les pages sont testées à la fin de chaque sprint (toutes les 2 semaines) pour suivre l'évolution du produit** », avec le poids de page, le nombre de requêtes et d'éléments DOM et des indicateurs de vitesse ([Retours d'expérience RGESN](https://ecoresponsable.numerique.gouv.fr/ressources/documents-reference/referentiel-general-ecoconception/retour-experience/)).

[Les e-novateurs](https://les-enovateurs.com/eco-conception) déclenchent la revue à chaque mise en production : des tests [Playwright](https://playwright.dev/) vérifient les pages principales, puis un score **EcoIndex** supérieur à 50 est exigé sur la page d'accueil, un nouvel article et la liste des articles.

À l'inverse, l'[audit d'Extia pour Vamos](https://www.extia-group.com/fr-fr/blog/audit-d-ecoconception-d-un-service-numerique-existant-l-exemple-de-vamos-1) est un **audit ponctuel** : un bon point de départ pour prioriser les actions, mais qui ne valide pas le critère sans revue récurrente derrière.

{{% /tab %}}

{{% tab tabName="Déclaration d'écoconception" %}}

La déclaration d'écoconception sert de preuve pour ce critère (revue documentée) et pour le [critère 1.5](../1-5_objectifs-environnementaux/) (objectifs suivis dans le temps). L'Arcep et l'Arcom en proposent des **gabarits officiels** :

- **sans calcul de score** : [Word](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.docx), [OpenDocument](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.odt), [HTML](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.html) ou [texte brut](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.txt), ou les tableurs sans score ([xlsx](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_outil_declaration_ecoconception_sans_score.xlsx), [ods](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_outil_declaration_ecoconception_sans_score.ods)) ;
- **avec calcul automatique du score** : [tableur Excel](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.xlsx) ou [OpenDocument](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.ods).

Dans le tableur avec score, chaque critère se coche, famille par famille, comme conforme, non conforme ou non applicable. La feuille « Score d'avancement » calcule alors un score pondéré :

```
Score = [ (critères validés Prioritaire × 1,5) + (critères validés Recommandé × 1,25) + (critères validés Modéré × 1) ]
        ÷ [ (critères applicables Prioritaire × 1,5) + (critères applicables Recommandé × 1,25) + (critères applicables Modéré × 1) ]
        × 100
```

Un critère « Prioritaire », comme le 1.4, pèse donc plus qu'un critère « Modéré ». L'export PDF du tableur produit une déclaration de 14 pages prête à publier, avec l'historique des scores des évaluations précédentes : de quoi montrer la revue régulière d'une version à l'autre.

{{% /tab %}}

{{< /tabs >}}

