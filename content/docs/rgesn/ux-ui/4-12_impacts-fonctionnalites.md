---
weight: 1200
title: "4.12 - Information sur les fonctionnalités à fort impact environnemental"
description: "Critère 4.12 du RGESN : comment identifier les fonctionnalités les plus coûteuses d'un service (vidéo haute qualité, export, gros téléchargement) et en informer l'utilisateur avant leur utilisation, avec des équivalences sourcées."
icon: "eco"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique indique-t-il à l'utilisateur que l'utilisation d'une fonctionnalité a des impacts environnementaux importants ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Expérience et Interface utilisateur (UX / UI)` |
| **Critère**  | `4.12` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'IHM` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.12/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Matérialiser pour l'utilisateur les impacts environnementaux des actions les plus coûteuses. Informer les utilisateurs en amont des impacts environnementaux avant l'utilisation d'une fonctionnalité, lorsque cette dernière est plus coûteuse par rapport au reste du service.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Pour chaque fonctionnalité du service qui est considérée comme ayant des impacts environnementaux importants, afficher une information préalable à l'utilisateur. Par exemple, pour chaque fichier téléchargeable, vidéo en « haute qualité » ou média consommateurs en ressources consulté, ou pour un traitement long, comme un export de données, une information relative au poids du fichier ou le temps requis pour l'opération est préalablement affichée à l'utilisateur. Proposer, si possible une fonctionnalité substituable avec un plus faible impact (par exemple : mode « écoute seule » au lieu du visionnage d'une vidéo « haute qualité », voir critère 5.5).

Dans l'éventualité où il est possible d'ajouter une information concernant des équivalences en impacts environnementaux, veiller à préciser la source et la méthodologie, et à favoriser une approche multicritère (pas uniquement en équivalent CO2). L'analyse d'impact décrite au critère 1.5 peut permettre d'identifier les fonctionnalités avec un poids environnemental significatif.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Contrôler la mise en œuvre en vérifiant que les fonctionnalités avec un impact environnemental significatif sont identifiées et signalées à l'utilisateur. Cet examen doit être documenté et pouvoir être audité par un tiers : en rendre compte, si possible, dans la déclaration d'écoconception.

Le critère est validé si le service ne comprend pas de fonctionnalités ayant un impact environnemental significatif ou si les informations relatives aux impacts environnementaux sont correctement affichées pour les fonctionnalités spécifiques identifiées comme ayant des conséquences significatives en termes de consommation de bande passante, énergétique ou de ressources informatiques. L'ajout d'une équivalence avec des indicateurs environnementaux dans l'affichage à l'utilisateur n'est pas obligatoire pour valider le critère.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Responsable RSE/Numérique soutenable`

Le critère 4.12 rejoint la [recommandation n°2 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=2) du [GR491](https://gr491.isit-europe.org/) (INR), « Sensibiliser les parties prenantes internes et externes au Numérique Responsable ». Deux de ses critères, classés en « Conseil », portent sur l'information de l'utilisateur :

- [« Avez-vous mis en place un système de présentation du suivi d'impacts environnementaux, pour l'exploitation du service et pour chaque utilisateur ? »](https://gr491.isit-europe.org/crit.php?id=2-uxui-lengagement-des-utilisateurs-va-susciter-ladhesion-a-613160). L'un de ses tests reprend presque mot pour mot l'exemple du RGESN : « Le poids des fichiers à télécharger est-il systématiquement indiqué afin de sensibiliser à l'impact de la fonctionnalité ? »
- [« Pour permettre aux utilisateurs d'être acteurs dans la réduction de leurs impacts, ont-ils accès à des références qui les invitent à des pratiques NR ? »](https://gr491.isit-europe.org/crit.php?id=2-uxui-le-comportement-de-lutilisateur-reste-lun-des-8565f8). Ses tests demandent si « des solutions alternatives NR permettent-elles de prioriser les choix utilisateurs ? », l'équivalent de la « fonctionnalité substituable » du RGESN.

Les précisions de ce second critère expliquent pourquoi informer l'utilisateur compte : « la pratique de l'utilisateur peut soit démultiplier les effets positifs, soit les réduire dans des proportions importantes ».

Le GR491 propose aussi des dispositifs plus ambitieux que le RGESN : un « compteur écologique », un « compteur de la consommation électrique [...] par session ». Ils sont à manier avec précaution. Un compteur permanent est lui-même une fonctionnalité, qui consomme des ressources. Et une consommation électrique attribuée à une session repose forcément sur une estimation, dont la source et la méthodologie devront être précisées (voir l'onglet « Équivalences »). Le RGESN se limite volontairement aux fonctionnalités **significativement plus coûteuses** que le reste du service.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

La ressource des Designers Éthiques [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), déjà citée aux critères [4.9](../4-9_requetes-saisie-utilisateur/) à [4.11](../4-11_poids-formats-fichiers/), donne trois exemples concrets de fonctionnalités concernées dans sa rubrique **Interactions** : « Indiquer à l'utilisateur lorsqu'une fonctionnalité à des impacts environnementaux importants (ex : visionnage d'une vidéo en haute définition, export d'un grand volume de données, recherche sur une grande base…). Si des équivalences en impacts environnementaux sont citées par exemple, citer les sources et la méthodologie de calcul. »

Le troisième exemple, la recherche sur une grande base, n'est pas cité par le RGESN. Il rappelle qu'une fonctionnalité coûteuse ne transfère pas forcément beaucoup de données : son coût peut se situer côté serveur, dans le traitement, sans rien de visible dans le poids de la page.

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/), dans sa section [**7.9 Documents**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-9-documents-a-telecharger), cite **explicitement** le critère 4.12 à propos des exports : « si la puissance requise pour exporter est importante ou que le fichier qui en résultera aura un poids conséquent, indiquer à l'avance à l'utilisateur que l'usage de cette fonctionnalité va entraîner un impact environnemental relativement non négligeable ». Pour un document généré dont le poids n'est pas connu à l'avance, il propose d'« indiquer un poids approximatif (moyenne des exports par exemple) ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent le cas le plus courant, celui des médias, dans la fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use), déjà citée aux critères [4.6](../4-6_contenu-porteur-information/) et [4.7](../4-7_choix-sobre-format/). Son critère de succès « User-controlled media » demande :

- « Inform users about media length, format, and expected data use. »
- « Provide the option to disable data-intensive media or offer lower-bandwidth alternatives. »

Ces deux phrases correspondent aux deux volets de la « Mise en œuvre » du RGESN : informer avant l'usage (durée, format, volume de données), puis proposer une alternative plus sobre. Le W3C parle de volume de données (« expected data use ») plutôt que d'impact environnemental. C'est l'information la plus simple à calculer et à vérifier, et c'est aussi celle que le RGESN cite en premier (« une information relative au poids du fichier »).

{{% /tab %}}

{{% tab tabName="Équivalences : sources et méthodologie" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Concepteur UX / UI`

Afficher une équivalence environnementale (« ce visionnage équivaut à X km en voiture ») est **facultatif** pour valider le critère. Si on le fait, le RGESN pose deux exigences : préciser **la source et la méthodologie**, et privilégier une **approche multicritère**, pas seulement l'équivalent CO2.

**Pourquoi la source et la méthodologie comptent.** Le streaming vidéo en donne un exemple connu. En 2019, un chiffre tiré d'un rapport du Shift Project a été très repris dans les médias : 1,6 kg de CO2 pour une demi-heure de Netflix. Dans [une analyse publiée en décembre 2020](https://www.iea.org/commentaries/the-carbon-footprint-of-streaming-video-fact-checking-the-headlines), l'Agence internationale de l'énergie (AIE) estime l'heure de streaming à environ **36 g de CO2** en 2019, soit un chiffre initial **environ 90 fois trop élevé**. L'AIE relève aussi que le Shift Project avait lui-même corrigé en juin 2020 une erreur de conversion entre bits et octets, qui divisait son estimation par huit. Un chiffre sans source ni méthodologie ne permet pas de repérer ce genre d'écart.

**Une source publique française.** L'ADEME propose sur [Impact CO2](https://impactco2.fr/outils/usagenumerique) un calculateur d'impact des usages numériques (streaming, visioconférence, e-mails) qui cite sa source, la [Base Empreinte](https://base-empreinte.ademe.fr/) de l'ADEME. Il remplit donc la première exigence. Il ne remplit pas la seconde : il n'affiche qu'un seul indicateur, les émissions en CO2e.

**Une approche multicritère.** Le [critère 1.5](../../strategie/1-5_objectifs-environnementaux/) cite les indicateurs à considérer en priorité : la consommation d'énergie primaire, les émissions de gaz à effet de serre, la consommation d'eau bleue et l'épuisement des ressources abiotiques (métaux et minéraux). Pour le numérique, l'essentiel de l'impact vient souvent de la fabrication des terminaux. Un affichage limité au CO2 de l'usage peut donc donner une image très partielle.

En pratique, le **poids** d'un fichier et la **durée** d'un traitement restent les informations les plus fiables à afficher. Elles se mesurent directement, l'utilisateur peut les vérifier, et elles ne dépendent d'aucun facteur d'émission. Une équivalence n'a d'intérêt que si elle s'appuie sur une méthodologie publique et citée.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**1. Identifier les fonctionnalités concernées.** Le moyen de test exige que cet examen soit « documenté et [puisse] être audité par un tiers ». Un simple tableau suffit, publié si possible dans la déclaration d'écoconception. Par exemple, pour un service fictif :

| Fonctionnalité | Ordre de grandeur | Signalée ? | Alternative proposée |
|---|---|---|---|
| Consultation d'une page | ~1 Mo | Non (référence) | — |
| Vidéo de conférence en 1080p | de l'ordre du Go par heure | Oui | Version 480p, audio seul, transcription |
| Export complet des données | variable, jusqu'à 100 Mo | Oui | Export filtré par période |

Les fonctionnalités à signaler sont celles qui s'écartent nettement de l'usage courant du service. L'[analyse d'impact du critère 1.5](../../strategie/1-5_objectifs-environnementaux/) ou un simple relevé de l'onglet **Réseau** des outils de développement permet de les repérer.

**2. Informer avant l'action et proposer une alternative.** Pour une vidéo :

```html
<figure>
  <video controls preload="none" poster="conference.jpg">
    <source src="conference-480p.mp4" type="video/mp4">
  </video>
  <figcaption>
    Conférence d'ouverture (1 h 12) – vidéo 480p, environ 350 Mo.
    <a href="conference.mp3">Écouter seulement (MP3, environ 70 Mo)</a> ·
    <a href="conference-transcription.html">Lire la transcription</a>
  </figcaption>
</figure>
```

- **`preload="none"`** : rien n'est téléchargé avant que l'utilisateur lance la lecture, donc l'information affichée précède bien le transfert.
- **Poids estimé** : pour une vidéo ou un fichier audio, poids ≈ débit × durée. Une vidéo encodée à environ 650 kbit/s pèse environ 350 Mo pour 1 h 12 ; un MP3 à 128 kbit/s, environ 70 Mo.
- **Alternatives** : le mode « écoute seule » cité par le RGESN, et la transcription, qui est aussi une exigence d'accessibilité et dont le [critère 4.7](../4-7_choix-sobre-format/) rappelle l'écart de poids avec la vidéo.

Pour un export :

```html
<button type="button" aria-describedby="export-info">
  Exporter toutes les données (CSV)
</button>
<p id="export-info">
  Fichier d'environ 85 Mo, préparation estimée à 2 minutes.
  Pour un fichier plus léger, filtrez d'abord la période à exporter.
</p>
```

Le poids annoncé peut être calculé à partir du nombre de lignes à exporter, ou, comme le proposent les Designers Éthiques, à partir de la moyenne des exports précédents. L'attribut `aria-describedby` fait lire l'information par les lecteurs d'écran avant l'activation du bouton.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Ce critère généralise le [critère 4.11](../4-11_poids-formats-fichiers/) (poids et formats de fichier attendus), déjà publié sur ce site. Le 4.11 demande d'afficher le poids de **tous** les fichiers de plus de 10 Mo. Le 4.12 demande d'informer avant toute **fonctionnalité** significativement plus coûteuse que le reste du service, même quand elle ne produit pas de fichier : visionnage d'une vidéo, traitement long, recherche lourde. Pour un fichier téléchargeable volumineux, les deux critères demandent la même chose, et une seule information (le poids, affiché avant le téléchargement) répond aux deux.

Le RGESN rattache explicitement ce critère à deux autres :

- le [critère 1.5](../../strategie/1-5_objectifs-environnementaux/) (objectifs environnementaux), dont l'analyse d'impact « peut permettre d'identifier les fonctionnalités avec un poids environnemental significatif » ;
- le [critère 5.5](../../contenus/5-5_ecoute-seule/) (mode « écoute seule » pour les vidéos), qui fournit l'exemple type de « fonctionnalité substituable » à proposer.

Le [critère 4.15](../4-15_controle-usages/) prolonge ce critère à l'échelle du service entier : une information globale sur l'empreinte des usages, et un mode sobre qui s'applique partout plutôt qu'une alternative proposée au cas par cas.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »** par la première voie prévue par le moyen de test, l'absence de fonctionnalité concernée : « Le service ne contient pas de fonctionnalité avec un impact environnemental significatif, par rapport à d'autres : pas de vidéo ou autre média consommateur ni de téléchargements avec un poids élevé. » La justification nomme les catégories examinées (vidéo, médias, téléchargements) et raisonne par comparaison (« par rapport à d'autres »), comme le demande le critère. C'est ce qui la rend auditable par un tiers.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque lui aussi ce critère **« Validé »**, avec une nuance intéressante : « Aucune fonctionnalité ayant un impact environnemental significatif n'a été détectée, hormis les batchs qui [sont] exécutés sans lien avec l'utilisation du produit. » L'examen a donc bien identifié un poste coûteux, les traitements par lots, mais l'a écarté du critère parce qu'aucun utilisateur ne le déclenche. C'est cohérent avec le 4.12, qui porte sur l'information **avant l'utilisation** d'une fonctionnalité : l'impact des batchs relève plutôt des critères Backend et Hébergement du RGESN. Le fait de le mentionner rend néanmoins l'examen plus transparent pour un auditeur.

{{% /tab %}}

{{< /tabs >}}
