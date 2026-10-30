---
weight: 600
title: "1.6 - Collecte de données"
description: "Critère 1.6 du RGESN : comment collecter, stocker et conserver les données d'un service numérique de façon responsable et raisonnée, au-delà des seules obligations RGPD."
icon: "article"
date: "2025-12-21T13:29:09+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique collecte-t-il la donnée de façon responsable et raisonnée ?

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
| **Critère**  | `1.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** |  `Data Scientist` `Responsable Juridique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Cette pratique vise à encourager une collecte de données responsable et raisonnée en complément des obligations légales de minimisation prévues par le Règlement général sur la protection des données (RGPD) en ce qui concerne les données personnelles. 

Comme le souligne le rapport de la CNIL « [Données, Empreinte et Libertés](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.cnil.fr/sites/cnil/files/2023-07/cnil_cahier_ip9_0.pdf) » (2023), certains impératifs de respect de la vie privée et objectifs d'écoconception se rejoignent. 

Il s'agira donc d'œuvrer à **réduire la quantité de données collectées**, traitées et stockées par le service, y compris les **données non personnelles et métadonnées**, pour optimiser l'utilisation des ressources informatiques. Afin de limiter le profilage des utilisateurs, consommateur en ressources, le critère vise également à **restreindre la collecte et le traitement de métadonnées aux fins de tracking**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir clairement les **données nécessaires** au fonctionnement du service, en cohérence avec les **cibles utilisatrices** et leurs **attentes** telles que définies au [critère 1.2](../1-2_cibles-utilisatrices/) du présent référentiel. Si une **donnée ne contribue pas** directement à l'amélioration de l'expérience utilisateur ou au fonctionnement du service, mieux vaut envisager de **ne pas la collecter**. La **collecte de métadonnées** dans une perspective de profilage des utilisateurs devra être **évitée**.

Pour chaque type de donnée jugée essentielle au fonctionnement du service et aux besoins des utilisateurs, **définir les conditions de collecte** qui devront expressément respecter les dispositifs du **RGPD** concernant les données personnelles. Pour les **données non personnelles**, la **durée de conservation** devra également être **minimisée** afin d'éviter leur stockage excessif.

Systematiser la mise en place d'une information complète, le droit de s'opposer et/ou la demande de consentement explicite de l'utilisateur pour l'ensemble des données collectées, y compris pour les données non personnelles.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Contrôler le **type** et la **quantité de données** collectées, traitées et stockées par le service.

En ce qui concerne les données personnelles, indépendamment des enjeux d'écoconception, la minimisation de la collecte de ces données est un impératif du RGPD et doit être strictement suivie par le responsable de traitement.

De façon plus large, pour l'ensemble des données collectées (y compris non personnelles), **justifier dans la déclaration d'écoconception** du service le besoin de cette collecte au regard des cibles utilisatrices du service ([critère 1.2](../1-2_cibles-utilisatrices/)), la limitation de leur traitement et de la durée de conservation, et documenter les outils de recueil du consentement le cas échéant. En ce qui concerne les données personnelles, un renvoi pourra être fait au registre de traitements des données personnelles tel que prévu par le RGPD.

Ne pas collecter des métadonnées servant au profilage de l'utilisateur, sauf si cette collecte est essentielle aux besoins et cibles utilisatrices du service ([critère 1.2](../1-2_cibles-utilisatrices/)) ou au fonctionnement de ce dernier, et si l'utilisateur a donné son consentement explicite et éclairé et qu'il peut désactiver cette collecte à tout moment. Le cas échéant, ces éléments devront être documentés dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="RWEB" %}}

Trois fiches du référentiel RWEB (Collectif GreenIT) donnent des règles de validation concrètes et chiffrées pour ce critère :

- [Limiter les outils d'analytics et les données collectées](https://rweb.greenit.fr/fr/fiches/RWEB_0111-limiter-les-outils-d-analytics-et-les-donnees-collectees) *(impact 4/5, priorité 4/5)* : ne pas utiliser plus d'**un seul outil d'analytics**. La fiche illustre un anti-pattern fréquent : Google Analytics, Matomo et ContentSquare qui coexistent sur un même service, pour satisfaire « les habitudes de chaque membre de l'équipe » marketing, chacun ajoutant requêtes, fichiers JavaScript et cookies.
- [Réduire le volume de données stockées au strict nécessaire](https://rweb.greenit.fr/fr/fiches/RWEB_0023-reduire-le-volume-de-donnees-stockees-au-strict-necessaire) *(impact 4/5, difficulté 4/5)* : ne stocker que ce qui est indispensable ou légalement requis, via un archivage à froid après une première période d'accès puis une suppression après le délai de conservation, et une suppression régulière des doublons et enregistrements obsolètes. Son délai de « 18 mois » n'a pas de valeur générale : le RGPD ne fixe pas de durée, elle se déduit de la finalité du traitement (voir le [critère 5.8](../../contenus/5-8_archivage-suppression/)). Critère de validation : une donnée stockée sans utilité pour le service doit être ramenée à zéro.
- [Optimiser la taille des cookies](https://rweb.greenit.fr/fr/fiches/RWEB_0062-optimiser-la-taille-des-cookies) : ne stocker dans les cookies que les données strictement nécessaires au fonctionnement (identifiant de session par exemple), pas des objets métier complets.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Responsable Juridique`

Le critère 1.6 du RGESN fait écho à la [recommandation n°1 de la famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=1) du [GR491](https://gr491.isit-europe.org/) (INR) : « Réduire l'impact des données de leur stockage et accès ». Elle pousse le questionnement plus loin que le seul volume stocké, notamment :

- **Utilité réelle** : les jeux de données collectés sont-ils réellement nécessaires ?
- **Données sensibles** : les données sensibles collectées sont-elles indispensables ?
- **Cycle de vie** : les données ont-elles une date de suppression prévue ? Les données obsolètes sont-elles effectivement supprimées ?
- **Gestion différenciée** : les données « actives » et « inactives » sont-elles gérées différemment (ex. mise en cache mémoire des données actives, archivage à froid des inactives) ?
- **Réplication** : la réplication des bases de données est-elle dimensionnée selon la sensibilité et le besoin réel de disponibilité, plutôt que par défaut ?

{{% /tab %}}

{{% tab tabName="CNIL" %}}

Profil(s) métier concerné(s) : `Responsable Juridique`, `Responsable RSE/Numérique soutenable`

Le [Cahier IP n°9 « Données, empreinte et libertés »](https://linc.cnil.fr/cahier-ip9-donnees-empreinte-et-libertes) (LINC - CNIL, 2023), déjà cité dans la fiche RGESN de ce critère, documente en détail où convergent — et où **s'opposent** — protection des données et sobriété numérique :

- **Convergences** : la minimisation des données, la limitation de la durée de conservation et la limitation des finalités (déjà imposées par le RGPD) rejoignent directement les objectifs de sobriété numérique — c'est une forme d'« hygiène numérique » commune aux deux enjeux.
- **Tensions** : à l'inverse, certaines obligations de protection des données **augmentent** l'empreinte environnementale des traitements — le recours à la cryptographie pour sécuriser des données personnelles étant l'exemple le plus documenté par le cahier. Protection des données et écoconception ne sont donc pas toujours alignées, et un arbitrage explicite peut être nécessaire.

Le guide pratique de la CNIL [Minimiser les données collectées](https://www.cnil.fr/fr/minimiser-les-donnees-collectees) complète ce cadrage avec des questions opérationnelles directement transposables à ce critère : cette donnée est-elle nécessaire à *toutes* les catégories d'utilisateurs ou seulement certaines ? Peut-on réduire sa granularité (ex. année de naissance plutôt que date complète) sans nuire à la fonctionnalité ? Un système de suppression automatique existe-t-il à l'échéance de la durée de conservation ?

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Juridique`

**1. Tenir l'inventaire des données collectées**, versionné avec le code : une ligne par donnée, personnelle ou non, métadonnées comprises.

| Donnée | Finalité | Durée |
|---|---|---|
| Adresse e-mail | Lettre d'information, avec consentement | Jusqu'au désabonnement |
| Journaux d'accès (IP, URL, date) | Sécurité | 6 mois à 1 an ([CNIL](https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation)) |
| Mesure d'audience | Statistiques de fréquentation | 13 mois pour le traceur, 25 mois pour les données |

Une donnée sans ligne n'a pas à être collectée. Les durées s'appliquent avec les mécanismes du [critère 7.2](../../backend/7-2_durees-conservation/).

**2. Réduire la granularité dès le formulaire**, comme le suggère la CNIL (onglet CNIL) : l'année de naissance plutôt que la date complète.

```html
<label for="annee">Année de naissance</label>
<input id="annee" name="annee_naissance" type="number" inputmode="numeric" autocomplete="bday-year">
```

**3. Un seul outil de mesure d'audience** (fiche RWEB 0111), si possible sans cookie. Avec Matomo, une ligne placée avant `trackPageView` désactive les cookies ([Matomo](https://matomo.org/faq/general/faq_157/)) :

```js
var _paq = window._paq = window._paq || [];
_paq.push(['disableCookies']);
_paq.push(['trackPageView']);
```

Avec un cookie, l'outil peut être exempté de consentement s'il respecte les conditions de la [CNIL](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience) (page du 4 juillet 2025) : finalité limitée à la mesure d'audience, pour le compte exclusif de l'éditeur, données statistiques anonymes, pas de suivi d'un site à l'autre. La CNIL cite une durée de vie de 13 mois pour le traceur, et 25 mois au plus pour conserver les données.

**4. Vérifier ce que le service dépose sur le terminal**, sans rien accepter dans le bandeau, dans une fenêtre de navigation privée. Après le chargement, coller dans la console :

```js
({
  cookies: document.cookie ? document.cookie.split('; ').map((c) => c.split('=')[0]) : [],
  localStorage: Object.keys(localStorage),
  sessionStorage: Object.keys(sessionStorage),
  indexedDB: (await indexedDB.databases()).map((b) => b.name),
})
```

Les cookies `HttpOnly` n'y figurent pas : l'onglet **Application** de Chromium ou **Stockage** de Firefox les montre tous. Les domaines tiers contactés se relèvent avec le script du [critère 6.7](../../frontend/6-7_domaine-unique/).

Testé le 30 octobre 2026 dans Chromium 155, avant tout choix dans les bandeaux :

- **DiaLog** ne dépose rien ;
- **les e-novateurs** déposent un cookie de langue et celui de Wysistat, leur mesure d'audience ;
- **le Musée d'arts de Nantes** dépose, outre celui de son bandeau, trois cookies de Piano Analytics valables 13 mois, dont un identifiant de navigateur. L'un d'eux enregistre le mode « essential », celui que [Piano](https://docs.piano.io/en/analytics/consent-management) prévoit pour une mesure exemptée de consentement ;
- **SPOTE** dépose un cookie `SRV` sur son domaine et sur `audience-sites.din.developpement-durable.gouv.fr`.

**5. Documenter** dans la déclaration d'écoconception : l'inventaire, ou un renvoi au registre des traitements pour les données personnelles, comme l'autorise le moyen de test ; l'outil de mesure d'audience et ses réglages ; les cookies déposés sans consentement et leur justification.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Responsable Juridique`

- le [critère 7.2](../../backend/7-2_durees-conservation/) (durées de conservation) : une donnée collectée doit aussi avoir une date de fin ;
- le [critère 5.8](../../contenus/5-8_archivage-suppression/) (archivage et suppression des contenus) : la même logique pour les contenus publiés ;
- le [critère 1.7](../1-7_niveau-chiffrement/) (niveau de chiffrement) : moins de données sensibles, moins de données à protéger ;
- le [critère 6.6](../../frontend/6-6_capteurs-terminaux/) (capteurs des terminaux) : une donnée de capteur est une collecte comme une autre ;
- le [critère 9.4](../../algorithmie/9-4_donnees-apprentissage/) (données d'apprentissage) : la même minimisation pour l'entraînement des modèles.

{{% /tab %}}
{{< /tabs >}}


---

### 
### Pour aller plus loin :


{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Contrairement aux autres critères de la famille Stratégie, les déclarations d'écoconception consultées détaillent peu leur politique de collecte. [DiaLog](https://dialog.beta.gouv.fr/ecoconception) et [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) valident le critère en deux phrases : pas de « collecte de métadonnées à des fins publicitaires », et des données personnelles traitées selon le RGPD. Aucune ne parle du nombre d'outils de mesure ni de la durée de conservation des données. Ce silence documentaire est en soi une indication : la minimisation des données reste, en pratique, plus documentée sous l'angle RGPD (registre de traitement, PIA) que sous l'angle écoconception.

L'anti-pattern décrit par la fiche [RWEB 0111](https://rweb.greenit.fr/fr/fiches/RWEB_0111-limiter-les-outils-d-analytics-et-les-donnees-collectees) reste néanmoins l'illustration la plus concrète et la plus fréquemment observée en audit : plusieurs outils d'analytics concurrents (Google Analytics, Matomo, ContentSquare...) coexistant sur un même service, chacun ajouté par une équipe différente sans concertation ni suppression des outils devenus redondants — un cas qui justifie à lui seul de vérifier ce critère lors de toute revue d'écoconception ([critère 1.4](../1-4_revue-ecoconception/)).

Une exception à ce silence documentaire : la [déclaration d'écoconception de « Les entreprises s'engagent »](https://lesentreprises-sengagent.gouv.fr/eco-conception) (communauté lancée par la Présidence de la République, dernière mise à jour le 25 novembre 2022) affirme n'utiliser « aucun tracking non nécessaire », et donc aucun cookie soumis au consentement des utilisateurs. Cette déclaration s'appuie toutefois sur la **version 1** du RGESN (79 critères, dont 53 validés en octobre 2022, soit 67,09 %) et non sur la v2 utilisée dans ce guide — elle ne peut donc pas être citée critère par critère avec la même précision que FACE, mais elle reste un exemple positif rare et concret sur ce point précis.

La [déclaration d'écoconception du Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) (Nantes Métropole, sur la v2 du RGESN) illustre une nuance plus honnête encore : critère marqué « En cours de validation », avec une auto-critique explicite plutôt qu'une déclaration de conformité totale — « La collecte de données personnelles se fait dans le respect du RGPD. […] L'intégration de Youtube nécessite la collecte de données supplémentaires qui sont soumises au consentement des utilisateurs. Dans cette optique, l'utilisation de Youtube devrait être remise en question. » Le service identifie donc lui-même son point faible plutôt que de le passer sous silence — un exemple rare de transparence sur un compromis non résolu.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent ce critère « Validé » dans leur déclaration mise à jour le 21 septembre 2026. Leur mesure d'audience passe par Wysistat, « dans les conditions d'exemption de consentement fixées par la CNIL » : statistiques anonymes, sans suivi d'un site à l'autre. L'adresse e-mail n'est collectée qu'avec consentement, pour la newsletter, et les comptes lecteurs se limitent au « strict nécessaire », sans mot de passe stocké grâce à une connexion par lien à usage unique.

{{% /tab %}}

{{< /tabs >}}
