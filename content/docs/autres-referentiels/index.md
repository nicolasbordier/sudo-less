---
weight: 200
title: "Autres référentiels"
description: "Panorama des référentiels, guides et cadres réglementaires cités sur ce site en complément du RGESN : GR491, RWEB, guide des Designers Éthiques, ANSSI, CNIL, DINUM, ARCEP..."
icon: "library_books"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

Le [RGESN](../rgesn/) sert de fil conducteur à ce site, mais chaque fiche s'appuie aussi sur d'autres référentiels — techniques, juridiques ou méthodologiques — pour préciser, illustrer ou compléter une recommandation. Ils sont classés ci-dessous par domaine.

{{< tabs tabTotal="10">}}

{{% tab tabName="Web" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [GR491](https://gr491.isit-europe.org/) (Institut du Numérique Responsable) | Référentiel de conception responsable | 8 familles de recommandations (Stratégie, Spécifications, Architecture, Frontend, Backend, UX-UI, Hébergement, Contenu) ; sert de grille de questionnement complémentaire à la quasi-totalité des critères du RGESN | La plupart des fiches Stratégie et Spécifications |
| [Guide d'écoconception](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception) (Designers Éthiques) | Guide méthodologique | 8 chapitres orientés conception/UX (définir le besoin, évaluer et mesurer, tester...), en complément d'une approche plus technique | [1.1](../rgesn/strategie/1-1_evaluation-utilite/), [1.2](../rgesn/strategie/1-2_cibles-utilisatrices/), [1.3](../rgesn/strategie/1-3_referent-ecoconception/), [1.4](../rgesn/strategie/1-4_revue-ecoconception/), [1.5](../rgesn/strategie/1-5_objectifs-environnementaux/), [2.2](../rgesn/specifications/2-2_anciens-terminaux/), [2.3](../rgesn/specifications/2-3_connexion-bas-debit/) |
| [RWEB](https://rweb.greenit.fr/) (Collectif GreenIT) | Référentiel de bonnes pratiques écoconception web | Plus de 115 fiches organisées par phase de cycle de vie, chacune notée sur son impact environnemental (1 à 5) et assortie d'un critère de validation chiffré | [1.2](../rgesn/strategie/1-2_cibles-utilisatrices/), [1.6](../rgesn/strategie/1-6_collecte-donnees/), [2.2](../rgesn/specifications/2-2_anciens-terminaux/) |
| [RWP — Bonnes pratiques d'écoconception WordPress](https://github.com/cnumr/best-practices-wordpress) (CNUMR, version 1, octobre 2022) | Référentiel de bonnes pratiques (CMS) | Déclinaison de RWEB spécifique à WordPress (43 % du web en 2022), avec des solutions à plusieurs niveaux de compétence technique — pour les profils non-développeurs comme pour les designers/développeurs | Aucun critère de ce site pour l'instant |
| [Web Sustainability Guidelines](https://w3c.github.io/sustainableweb-wsg/) (W3C, Sustainable Web Interest Group) | Référentiel international | Plus de 45 recommandations réparties en 4 sections (UX Design, Développement web, Hébergement/Infrastructure, Business/Produit) ; sa recommandation « User constraints » recoupe directement la logique bas débit/anciens appareils du RGESN | [2.1](../rgesn/specifications/2-1_profils-materiels/), [2.2](../rgesn/specifications/2-2_anciens-terminaux/), [2.3](../rgesn/specifications/2-3_connexion-bas-debit/) |
| [Documentation d'écoconception](https://gauthierroussilhe.com/book/ademe/) (Gauthier Roussilhe et al., mission ADEME) | Guide méthodologique | Fiches pratiques (choix techniques, gestion des assets, infrastructures, données d'audience) issues d'une mission réelle d'accompagnement à l'écoconception de la start-up d'État [Territoires en Transitions](https://beta.gouv.fr/startups/territoires-en-transitions.html) (2020-2022) | [1.4](../rgesn/strategie/1-4_revue-ecoconception/), [1.8](../rgesn/strategie/1-8_efforts-open-source/) |
| [AFNOR SPEC 2201 « Écoconception des services numériques »](https://www.boutique.afnor.org/fr-fr/norme/afnor-spec-2201/ecoconception-des-services-numeriques/fa203506/323315) (AFNOR, avril 2022, téléchargement gratuit) | Norme officielle | Grille de questionnement simple à partager en équipe projet, la « règle des 3U » (Utile, Utilisable, Utilisé), pour identifier les fonctionnalités superflues avant de les développer | [1.1](../rgesn/strategie/1-1_evaluation-utilite/) |
| [Référentiel d'écoconception Davidson](https://admin.davidson.fr/wp-content/uploads/Referentiel-Ecoconception-Davidson.pdf) (Davidson Consulting) | Synthèse pratique | Compile et reformate 150 bonnes pratiques issues de 5 référentiels (RGESN, guide Designers Éthiques, RWEB, Sustainable API Green Score, IA frugale AFNOR) en fiches uniformes avec niveau de complexité — utile comme point d'entrée unique, mais sans contenu qui ne soit déjà couvert par une source individuelle de ce tableau | — |
| [Baromètre du numérique](https://www.arcep.fr/cartes-et-donnees/nos-publications-chiffrees/barometre-du-numerique/le-barometre-du-numerique-edition-2026.html) (Arcep/CRÉDOC/ANCT/Arcom) | Enquête chiffrée annuelle | Photographie du parc d'équipements et des usages réels en France, pour objectiver un profil matériel plutôt que de le caler arbitrairement sur les derniers modèles disponibles | [2.1](../rgesn/specifications/2-1_profils-materiels/) |

{{% /tab %}}

{{% tab tabName="Mobile" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Best Practices Mobile](https://github.com/cnumr/best-practices-mobile) (CNUMR) | Référentiel de code smells | Catalogue de 60+ « code smells » environnementaux et sociaux spécifiques au développement natif Android/iOS (fuites de capteurs, wake locks, notifications intempestives...), détectables par analyse statique (plugins SonarQube [creedengo](https://github.com/green-code-initiative/creedengo-android-java), CodeQL) — publié par le même collectif que [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis), déjà cité en page [Dev Mobile](../outils/par-metier/dev-mobile/) | Complète la page [Dev Mobile](../outils/par-metier/dev-mobile/) plutôt qu'un critère RGESN précis |

{{% /tab %}}

{{% tab tabName="Backend / API" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Sustainable API Green Score](https://www.collectif-api-thinking.com/assets/deliverables/worksites/50_CAT_API_Sustainable_IT.pdf) (Collectif API Numériquement Responsable) | Référentiel de notation (A à E) | 7 domaines dédiés spécifiquement aux API (cycle de vie, échange de données, données, architecture, outils, infrastructure, communication) — un angle backend/architecte qu'aucun autre référentiel de cette liste ne couvre en détail | Aucun critère de ce site pour l'instant (famille Backend/Architecture non encore traitée) |

{{% /tab %}}

{{% tab tabName="IA" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Référentiel général pour l'IA frugale](https://www.boutique.afnor.org/fr-fr/norme/afnor-spec-2314/referentiel-general-pour-lia-frugale-mesurer-et-reduire-limpact-environneme/fa208976/421140) (AFNOR SPEC 2314, juin 2024) | Norme officielle | Méthodologie de mesure et bonnes pratiques pour réduire l'impact environnemental d'un système d'IA, avec étude de cas (dont un service de génération d'images par IA) | Aucun critère de ce site pour l'instant (famille IA du RGESN non encore traitée) |
| [RIA — Référentiel de bonnes pratiques pour l'utilisation de l'IA générative](https://ria.greenit.fr/) (Collectif GreenIT + consortium DECENZ) | Référentiel de bonnes pratiques | Bonnes pratiques organisées sur les 7 phases du cycle de vie (spécifications à fin de vie), spécifiquement pour l'IA générative, avec indicateurs d'impact environnemental, de facilité de mise en œuvre et de priorité par fiche | Aucun critère de ce site pour l'instant (famille IA du RGESN non encore traitée) |

{{% /tab %}}

{{% tab tabName="Progiciel" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [REIPRO — Bonnes pratiques pour l'intégration de progiciels](https://github.com/cnumr/best-practices-packaged-software) (CNUMR, avec Cosmo Consult et Zenika) | Référentiel de bonnes pratiques | 15 pratiques centrées sur l'intégration de progiciels/ERP plutôt que le développement sur-mesure : quantifier le besoin, minimiser les développements spécifiques, gérer sobrement les conteneurs et builds d'un projet d'intégration — un profil « intégrateur » absent des autres référentiels de cette liste | Esprit proche des critères [1.1](../rgesn/strategie/1-1_evaluation-utilite/) et [1.9](../rgesn/strategie/1-9_technologies-standard/), sans citation directe du RGESN |

{{% /tab %}}

{{% tab tabName="Sécurité" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) (guide des mécanismes cryptographiques) | Référentiel technique officiel | Dimensionnement cryptographique : tailles de clés et algorithmes recommandés pour choisir un niveau de chiffrement proportionné au besoin | [1.7](../rgesn/strategie/1-7_niveau-chiffrement/) |

{{% /tab %}}

{{% tab tabName="Communication / Sensibilisation" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Alt Impact](https://altimpact.fr/) (ADEME, avec Inria et CNRS) | Plateforme de sensibilisation | Guides pratiques par public (particuliers, salariés, organisations), dont un [guide des achats numériques responsables](https://ecoresponsable.numerique.gouv.fr/docs/2021/guide-achats-numeriques-responsables-version-beta-avril-2021.pdf) et un guide sur l'allongement de la durée de vie des smartphones | [2.1](../rgesn/specifications/2-1_profils-materiels/), [2.2](../rgesn/specifications/2-2_anciens-terminaux/) |
| [Référentiel de compétences numérique éco-responsable](https://ecoresponsable.numerique.gouv.fr/actualites/referentiel-competences-beta/) (DINUM, beta) | Référentiel de compétences | Grille de compétences pour outiller la prise de poste d'un référent écoconception ou objectiver les compétences déjà présentes dans une équipe | [1.3](../rgesn/strategie/1-3_referent-ecoconception/) |

{{% /tab %}}

{{% tab tabName="Juridique / Réglementaire" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Cahier IP9 « Données, empreinte et libertés »](https://www.cnil.fr/sites/cnil/files/2023-07/cnil_cahier_ip9_0.pdf) (CNIL) | Référentiel de réflexion | Met en tension sobriété numérique et protection des données personnelles, pour arbitrer une collecte de données raisonnée | [1.6](../rgesn/strategie/1-6_collecte-donnees/) |
| [Règlement européen sur les données](https://digital-strategy.ec.europa.eu/en/policies/data-act) (Data Act) | Référentiel légal | Impose depuis 2025 des API ouvertes et documentées pour les données générées par un objet connecté, condition légale pour éviter une fin de vie forcée | [1.10](../rgesn/strategie/1-10_api-materiel/) |
| [Guide des licences libres](https://code.gouv.fr/fr/doc/licences-libres-dinum/) (DINUM) | Référentiel juridique | Aide au choix d'une licence open source adaptée à un contexte de service public ou privé | [1.8](../rgesn/strategie/1-8_efforts-open-source/) |

{{% /tab %}}

{{% tab tabName="GreenIT" %}}

| Référentiel | Type | Cible | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|---|
| [Référentiel de maturité Green IT](https://club.greenit.fr/doc/2022-06-GREENIT-Referentiel_maturite-v3.pdf) (v3, juin 2022 — dernière édition à ce jour) | Référentiel de maturité organisationnelle | DSI | 74 bonnes pratiques et une méthode de notation sur 100, pour évaluer la maturité Green IT d'une **direction des systèmes d'information entière** plutôt que d'un seul service numérique — déployé depuis 2014 dans la plupart des grandes organisations publiques et privées françaises | [1.3](../rgesn/strategie/1-3_referent-ecoconception/), [1.4](../rgesn/strategie/1-4_revue-ecoconception/) |

{{% /tab %}}

{{% tab tabName="Environnement" %}}

| Référentiel | Type | Ce qu'il apporte | Cité notamment aux critères |
|---|---|---|---|
| [Science Based Targets initiative](https://sciencebasedtargets.org/) + [ITU-T L.1470](https://www.itu.int/rec/T-REC-L.1470) | Référentiels de trajectoire climatique | Alignent les objectifs de réduction d'émissions d'un service sur une trajectoire scientifique reconnue (Accord de Paris, secteur TIC) | [1.5](../rgesn/strategie/1-5_objectifs-environnementaux/) |

{{% /tab %}}

{{< /tabs >}}

---

Ces référentiels ne se substituent pas au RGESN : ils en précisent l'application (GR491, RWEB, guide des Designers Éthiques), ou couvrent un angle que le RGESN ne détaille pas lui-même — dimensionnement cryptographique (ANSSI), arbitrage vie privée (CNIL), trajectoire climatique (SBTi/ITU-T), ou cadre légal (Data Act). Voir la section [Outils](../outils/) pour les logiciels et services qui permettent de les mettre en œuvre concrètement.
