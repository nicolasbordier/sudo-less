---
weight: 300
title: "Déclaration d'écoconception"
description: "Déclaration d'écoconception de sudo-less.dev selon le RGESN 2024 : score d'avancement, résultat de chaque critère et plan d'avancement."
icon: "fact_check"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

Cette page est la déclaration d'écoconception propre à **sudo-less.dev**, rédigée selon le [RGESN](../../rgesn/). Vous cherchez plutôt à rédiger la vôtre ? Voir le [guide complet](../../declaration/) (contenu obligatoire, modèles officiels, formule de calcul du score).

| | |
|---|---|
| **Service évalué** | sudo-less.dev, publié à l'adresse [nicolasbordier.github.io/sudo-less](https://nicolasbordier.github.io/sudo-less/) |
| **Date de rédaction** | 31 octobre 2026 |
| **Dernière mise à jour** | 31 octobre 2026 |
| **Référentiel appliqué** | RGESN, version 2024 |
| **Méthode** | Auto-évaluation par le mainteneur du site, avec des mesures dans Chromium 155 |
| **Contact écoconception** | Le mainteneur du site, par les [issues du dépôt GitHub](https://github.com/nicolasbordier/sudo-less/issues) |

---

## Score d'avancement

| Score actuel | Score précédent | Score visé (octobre 2028) |
|---|---|---|
| **58 %** | Aucun, première déclaration | 78 % |

**34 critères validés sur 56 applicables** ; 22 critères ne s'appliquent pas au site. Le score pondère chaque critère par sa priorité :

| Priorité | Pondération | Critères applicables | Critères validés |
|---|---:|---:|---:|
| Prioritaire | 1,5 | 20 | 9 |
| Recommandé | 1,25 | 26 | 15 |
| Modéré | 1 | 10 | 10 |

Score = (9 × 1,5 + 15 × 1,25 + 10 × 1) / (20 × 1,5 + 26 × 1,25 + 10 × 1) = 42,25 / 72,5 = **58 %**.

Ce score mesure l'avancement dans le référentiel, pas l'impact environnemental du site. Le score visé suppose que les actions 1 à 5 du plan d'avancement soient réalisées ; il ne compte pas les critères d'hébergement, qui dépendent de GitHub.

---

## Chemins critiques et unités fonctionnelles évalués

Quatre parcours ont été testés le 31 octobre 2026 dans Chromium 155, cache désactivé, page entièrement défilée, sur trois écrans : 1 366 × 768, 1 200 × 720 et 390 × 844 pixels.

1. Arriver sur la page d'accueil.
2. Ouvrir une fiche RGESN depuis le menu, et passer d'un onglet à l'autre.
3. Rechercher un terme, ici « cache », et ouvrir un résultat.
4. Consulter les pages de synthèse « Retours d'expérience » et « Autres référentiels ».

| Page | Requêtes | Poids transféré |
|---|---:|---:|
| Accueil | 8 | 49 Ko |
| Sommaire de la documentation | 8 | 68 Ko |
| Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) | 8 | 79 Ko |
| Retours d'expérience | 8 | 77 Ko |
| Autres référentiels | 8 | 77 Ko |

Sur une fiche, ce poids se répartit en 22 Ko de HTML, 14 Ko de CSS, 31 Ko de JavaScript (Bootstrap 19 Ko, FlexSearch 6,4 Ko, thème 5 Ko) et 11,3 Ko pour la police d'icônes. La première recherche télécharge en plus l'index de recherche : 336 Ko compressés, 1 058 Ko une fois décompressés.

---

## Budget par page

Chaque page du site doit respecter ce budget au premier chargement : cache désactivé, page entièrement défilée, sans interaction.

| | Budget | Maximum mesuré | Page la plus lourde |
|---|---:|---:|---|
| Poids transféré | 100 Ko | 79 Ko | Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) |
| Requêtes | 10 | 8 | Toutes les pages de la documentation |
| Éléments du DOM | 1 500 | 1 390 | Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) |

Mesuré le 31 octobre 2026 dans Chromium 155 sur les 132 pages du site, page d'erreur comprise, à 1 366 × 768 et 390 × 844 pixels : toutes respectent le budget. Le DOM compte toutes les balises de la page, y compris celles des images SVG.

À 512 kbit/s, le débit testé pour le critère 2.3, 100 Ko se transfèrent en 1,6 seconde environ.

Le budget porte sur le chargement de la page. Il ne compte pas la recherche : à sa première ouverture, elle télécharge son index en une requête de 336 Ko (critère 4.12).

Avec le cache, passer d'une page à l'autre ne télécharge que le HTML : 1 requête et 22 Ko au plus. Une page revue dans les 10 minutes ne demande aucune requête ; au-delà, le navigateur revérifie ses 8 fichiers sans les télécharger de nouveau (critère 6.2).

---

## Résultats par critère

{{< tabs tabTotal="9">}}

{{% tab tabName="1. Stratégie" %}}

| Critère | Statut | Justification |
|---|---|---|
| [1.1](../../rgesn/strategie/1-1_evaluation-utilite/) Évaluation de l'utilité | Non validé | L'utilité du site n'a pas fait l'objet d'une étude écrite : réponses aux questions du moyen de test et arbre des conséquences. |
| [1.2](../../rgesn/strategie/1-2_cibles-utilisatrices/) Cibles utilisatrices | Non validé | Les publics visés sont décrits par métier dans la page [Getting Started](../../getting-started/) : porteur de projet, designer UX, développeurs, ops, architecte, responsable RSE. Leurs besoins n'ont pas été étudiés auprès d'eux. |
| [1.3](../../rgesn/strategie/1-3_referent-ecoconception/) Référent écoconception | Validé | Contact : le mainteneur du site, par les issues du dépôt GitHub. |
| [1.4](../../rgesn/strategie/1-4_revue-ecoconception/) Revue d'écoconception | Non validé | Cette déclaration est la première auto-évaluation. La suivante sera réalisée à chaque évolution importante du site, et au plus tard en octobre 2027. Il manque encore des audits de performance réguliers ; des tests de charge n'auraient pas de sens pour un site statique servi par un CDN mutualisé. |
| [1.5](../../rgesn/strategie/1-5_objectifs-environnementaux/) Objectifs environnementaux | Non validé | Ni indicateur d'empreinte ni objectif de réduction. |
| [1.6](../../rgesn/strategie/1-6_collecte-donnees/) Collecte de données | Validé | Le site ne pose aucun cookie et n'a ni mesure d'audience, ni formulaire, ni compte : il ne collecte aucune donnée. GitHub Pages enregistre l'adresse IP des visiteurs « for security purposes » ([documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection)). |
| [1.7](../../rgesn/strategie/1-7_niveau-chiffrement/) Niveau de chiffrement | Non applicable | Aucun chiffrement au-delà du HTTPS. |
| [1.8](../../rgesn/strategie/1-8_efforts-open-source/) Efforts d'open source | Validé | Code sous licence MIT et contenu sous CC BY-SA 4.0, dans un [dépôt public](https://github.com/nicolasbordier/sudo-less). Le site repose lui-même sur des logiciels libres : Hugo, le thème Lotus Docs, Bootstrap et FlexSearch. |
| [1.9](../../rgesn/strategie/1-9_technologies-standard/) Technologies standard | Validé | Site web statique en HTML, CSS et JavaScript standard, avec la même interface sur tous les terminaux. |
| [1.10](../../rgesn/strategie/1-10_api-materiel/) API ouvertes pour le matériel | Non applicable | Aucun objet connecté. |

{{% /tab %}}

{{% tab tabName="2. Spécifications" %}}

| Critère | Statut | Justification |
|---|---|---|
| [2.1](../../rgesn/specifications/2-1_profils-materiels/) Profils de matériels | Validé | Profil minimal établi par l'analyse du code servi : tout terminal équipé de Chrome ou Edge 88 (janvier 2021), Firefox 89 (juin 2021) ou Safari 15 (septembre 2021), versions imposées par la propriété CSS `aspect-ratio`. La recherche fonctionne dès Chrome 85, Firefox 79 et Safari 14 (2020), à cause de l'opérateur `??=`. Sur iPhone, Safari 15 est disponible dès l'iPhone 6s (2015). Aucune évolution n'est prévue. |
| [2.2](../../rgesn/specifications/2-2_anciens-terminaux/) Anciens modèles de terminaux | Validé | Testé le 31 octobre 2026 sur un ordinateur de bureau équipé d'un processeur Intel Core i5 760 (2010), sous Linux Mint 22.3 avec Firefox 158 : les parcours essentiels fonctionnent. |
| [2.3](../../rgesn/specifications/2-3_connexion-bas-debit/) Connexion bas débit | Validé | Débit limité dans Chromium. À 512 kbit/s (latence 100 ms), une fiche s'affiche en 0,9 s, et la recherche donne ses résultats 6 s après son ouverture. À 400 kbit/s (latence 400 ms), 1,4 s et 7,8 s. Débit minimum testé : 400 kbit/s. |
| [2.4](../../rgesn/specifications/2-4_anciennes-versions-os/) Anciennes versions d'OS et de navigateurs | Validé | Testé le 31 octobre 2026 sur Chrome 120 (décembre 2023) et Firefox 115 ESR (juillet 2023), dans des versions sans mise à jour automatique : les parcours essentiels fonctionnent. Safari n'a pas encore été testé. Les versions minimales du critère 2.1 restent estimées par l'analyse du code. |
| [2.5](../../rgesn/specifications/2-5_terminaux-affichage/) Terminaux d'affichage | Validé | Testé le 31 octobre 2026 sur les 130 pages du site, à 1 200, 768 et 390 pixels de large : aucune page ne déborde, les tableaux larges défilant dans leur propre cadre. Les menus sont des boutons : ils s'ouvrent au clavier comme à la souris ou au doigt. |
| [2.6](../../rgesn/specifications/2-6_revue-conception-code/) Revue de conception et de code | Validé | Revue de conception : l'[arbre des conséquences](../revue-conception/) de chaque fonctionnalité, selon le niveau 1 de la méthode Empreinte Projet de l'ADEME (31 octobre 2026). Revue de code : le mainteneur relit chaque commit, code ou contenu, et chaque contribution externe avant de l'intégrer, selon les points décrits dans la page [Contribuer](../contribuer/). |
| [2.7](../../rgesn/specifications/2-7_maintenance-decommissionnement/) Maintenance et décommissionnement | Non validé | Pas de stratégie écrite de maintenance et de fin de vie. |
| [2.8](../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) Fournisseurs | Non validé | Le seul fournisseur, GitHub (hébergement et intégration continue), a été choisi sans critère environnemental documenté. |
| [2.9](../../rgesn/specifications/2-9_composants-interface/) Composants d'interface prêts à l'emploi | Validé | Le thème Lotus Docs apporte Bootstrap 5, allégé à la construction du site. Depuis le 31 octobre 2026, le CSS est réduit aux règles qui s'appliquent aux pages : 14 Ko compressés sur une fiche, au lieu de 43 Ko. Le JavaScript de Bootstrap (19 Ko) se limite à cinq composants, dont un seul ne sert sur aucune page : l'infobulle. La police d'icônes est réduite aux icônes utilisées (11,3 Ko), et l'index de recherche n'est téléchargé qu'à la demande. |
| [2.10](../../rgesn/specifications/2-10_services-tiers/) Services tiers | Non validé | Deux services tiers : GitHub Pages (hébergement, avec le CDN Fastly) et GitHub Actions (construction du site). Leur avancement sur les critères 1.4 et 1.5 n'a pas été vérifié. |

{{% /tab %}}

{{% tab tabName="3. Architecture" %}}

| Critère | Statut | Justification |
|---|---|---|
| [3.1](../../rgesn/architecture/3-1_architecture-composants/) Architecture et composants | Non validé | L'architecture est sobre : un site statique généré par Hugo, sans serveur d'application ni base de données. Mais ce choix n'est pas comparé par écrit à d'autres options, et le critère 2.10 n'est pas validé. |
| [3.2](../../rgesn/architecture/3-2_architecture-elastique/) Architecture élastique | Validé | Aucune ressource serveur n'est réservée au site : ses fichiers statiques sont servis par l'infrastructure mutualisée de GitHub Pages et le CDN Fastly. |
| [3.3](../../rgesn/architecture/3-3_evolution-protocoles/) Évolution des protocoles | Validé | Le site répond en HTTPS (HTTP redirigé), avec TLS 1.3, HTTP/2 et IPv6, des protocoles adaptés à des fichiers statiques. Depuis le 31 octobre 2026, la page d'accueil ne charge plus le badge Ecoindex, qui venait d'un serveur sans IPv6 : aucune ressource ne vient plus d'un service tiers. |
| [3.4](../../rgesn/architecture/3-4_mises-a-jour-correctives/) Mises à jour correctives des équipements | Non applicable | Aucun terminal vendu avec le service. |
| [3.5](../../rgesn/architecture/3-5_dissociation-mises-a-jour/) Dissociation des mises à jour | Non applicable | Site web, sans mise à jour à installer. |
| [3.6](../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) Mises à jour incrémentielles | Non applicable | Site web, sans mise à jour à installer. |
| [3.7](../../rgesn/architecture/3-7_environnements-developpement-test/) Environnements de développement | Validé | Développement en local avec `hugo server`, sans environnement de préproduction. GitHub Actions construit le site seulement à chaque publication, sur une machine éphémère. |

{{% /tab %}}

{{% tab tabName="4. UX/UI" %}}

| Critère | Statut | Justification |
|---|---|---|
| [4.1](../../rgesn/ux-ui/4-1_lecture-automatique/) Lecture automatique | Validé | Aucune lecture automatique, aucune animation de plus de 4 secondes. |
| [4.2](../../rgesn/ux-ui/4-2_defilement-infini/) Défilement infini | Validé | Chaque page s'affiche en entier ; la recherche limite ses résultats à 10. |
| [4.3](../../rgesn/ux-ui/4-3_parcours-navigation/) Parcours de navigation | Non validé | Ni outil UX ni statistiques d'usage : le site ne mesure pas son audience (critère 1.6). |
| [4.4](../../rgesn/ux-ui/4-4_activation-service-tiers/) Activation d'un service tiers | Validé | Aucun service tiers ne se charge sans action de l'utilisateur : depuis le 31 octobre 2026, le badge Ecoindex de la page d'accueil est remplacé par un simple lien vers le résultat. |
| [4.5](../../rgesn/ux-ui/4-5_composants-natifs/) Composants natifs | Validé | Liens, listes, tableaux et titres sont en HTML natif. Deux composants reposent sur JavaScript, faute d'équivalent natif : les onglets des fiches (Bootstrap) et la recherche (FlexSearch). |
| [4.6](../../rgesn/ux-ui/4-6_contenu-porteur-information/) Contenu porteur d'information | Validé | Ni vidéo, ni son, ni animation décorative. |
| [4.7](../../rgesn/ux-ui/4-7_choix-sobre-format/) Format le plus sobre | Validé | Contenu textuel, sans vidéo, son ni animation. |
| [4.8](../../rgesn/ux-ui/4-8_polices-caracteres/) Polices de caractères | Validé | Une seule police téléchargée, celle des icônes (11,3 Ko). Le texte utilise les polices du système. |
| [4.9](../../rgesn/ux-ui/4-9_requetes-saisie-utilisateur/) Requêtes lors de la saisie | Validé | La recherche s'exécute dans le navigateur : aucune requête au serveur pendant la saisie, et un seul téléchargement de l'index par page. |
| [4.10](../../rgesn/ux-ui/4-10_format-saisie/) Format de saisie | Non applicable | Aucun formulaire envoyé au serveur ; le champ de recherche reste local. |
| [4.11](../../rgesn/ux-ui/4-11_poids-formats-fichiers/) Poids et formats de fichier | Non applicable | Aucun envoi ni téléchargement de fichier. |
| [4.12](../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) Fonctionnalités à fort impact | Non validé | La fonctionnalité la plus lourde, la recherche, télécharge à sa première ouverture un index de 336 Ko compressés, plus de quatre fois le poids d'une page, sans l'annoncer. |
| [4.13](../../rgesn/ux-ui/4-13_notifications/) Notifications | Validé | Aucune notification. |
| [4.14](../../rgesn/ux-ui/4-14_dark-patterns/) Dark patterns | Validé | Interface relue au regard des exemples de l'article 25 du DSA : ni compte à rebours, ni case précochée, ni bandeau de consentement, ni incitation à s'inscrire. |
| [4.15](../../rgesn/ux-ui/4-15_controle-usages/) Contrôle des usages et mode sobre | Non validé | Le site a un mode sombre, mais ni information sur l'empreinte de son usage, ni mode sobre. |

{{% /tab %}}

{{% tab tabName="5. Contenus" %}}

| Critère | Statut | Justification |
|---|---|---|
| [5.1](../../rgesn/contenus/5-1_format-images/) Format des images | Validé | La seule image matricielle affichée, l'illustration de la page d'accueil, est en WebP. L'icône de l'onglet existe en SVG, avec des versions PNG et ICO pour les anciens navigateurs. |
| [5.2](../../rgesn/contenus/5-2_compression-images/) Compression des images | Validé | L'illustration d'accueil est convertie en WebP, en qualité 85, en quatre largeurs : de 12 Ko (480 pixels) à 42 Ko (1 280 pixels). |
| [5.3](../../rgesn/contenus/5-3_definition-videos/) Définition vidéo | Non applicable | Aucune vidéo. |
| [5.4](../../rgesn/contenus/5-4_compression-videos/) Compression des vidéos | Non applicable | Aucune vidéo. |
| [5.5](../../rgesn/contenus/5-5_ecoute-seule/) Mode « écoute seule » | Non applicable | Aucune vidéo. |
| [5.6](../../rgesn/contenus/5-6_compression-audio/) Compression audio | Non applicable | Aucun contenu audio. |
| [5.7](../../rgesn/contenus/5-7_format-documents/) Format des documents | Non applicable | Aucun document à télécharger. |
| [5.8](../../rgesn/contenus/5-8_archivage-suppression/) Archivage et suppression | Non validé | Chaque fiche affiche sa date de mise à jour, mais aucune stratégie écrite ne prévoit leur revue, leur archivage ou leur suppression. |

{{% /tab %}}

{{% tab tabName="6. Frontend" %}}

| Critère | Statut | Justification |
|---|---|---|
| [6.1](../../rgesn/frontend/6-1_poids-requetes-ecran/) Poids et requêtes par écran | Validé | Budget par page, détaillé dans la section [Budget par page](#budget-par-page) : 100 Ko transférés, 10 requêtes et 1 500 éléments au plus, au chargement de la page, recherche non comprise. Toutes les pages le respectent : 79 Ko, 8 requêtes et 1 390 éléments au plus. Le contrôle se fait encore à la main. |
| [6.2](../../rgesn/frontend/6-2_cache-navigateur/) Cache côté utilisateur | Validé | À la deuxième visite d'une fiche, les 8 ressources viennent du cache. GitHub Pages fixe la durée de cache à 10 minutes (`max-age=600`) pour tous les fichiers, sans réglage possible. Au-delà, le navigateur revalide chaque fichier, sans le télécharger de nouveau (réponse 304). Les CSS et JavaScript ont un nom qui change avec leur contenu : ils pourraient être gardés bien plus longtemps. |
| [6.3](../../rgesn/frontend/6-3_compression-ressources/) Compression des ressources | Validé | Tous les fichiers texte arrivent compressés en gzip. GitHub Pages ne propose pas Brotli. |
| [6.4](../../rgesn/frontend/6-4_dimensions-images/) Dimensions des images | Validé | L'illustration d'accueil existe en quatre largeurs, de 480 à 1 280 pixels, et l'attribut `sizes` indique sa largeur affichée à chaque taille d'écran. Vérifié dans Chromium de 360 à 1 920 pixels de large : en densité 1 et 2, le navigateur charge une version au plus 1,5 fois plus large que l'affichage. Sur un ordinateur de densité 1, elle pèse 17,6 Ko au lieu de 45 Ko. |
| [6.5](../../rgesn/frontend/6-5_chargement-ressources/) Ressources utiles | Non validé | L'index de recherche ne se télécharge qu'à l'ouverture de la recherche. Mais la bibliothèque FlexSearch (6,4 Ko) se charge sur chaque page, même sans recherche. |
| [6.6](../../rgesn/frontend/6-6_capteurs-terminaux/) Capteurs | Non applicable | Aucun capteur. |
| [6.7](../../rgesn/frontend/6-7_domaine-unique/) Ressources statiques sur un même domaine | Validé | Toutes les ressources du site viennent de son propre domaine, en HTTP/2. |

{{% /tab %}}

{{% tab tabName="7. Backend" %}}

| Critère | Statut | Justification |
|---|---|---|
| [7.1](../../rgesn/backend/7-1_cache-serveur/) Cache serveur | Validé | Site statique : chaque page est calculée une seule fois, à la construction, puis servie depuis le cache du CDN de GitHub Pages, renouvelé à chaque publication. |
| [7.2](../../rgesn/backend/7-2_durees-conservation/) Durées de conservation | Non validé | Le site ne stocke aucune donnée d'utilisateur. La durée de vie des contenus reste à fixer (critère 5.8). |
| [7.3](../../rgesn/backend/7-3_traitement-arriere-plan/) Information sur un traitement en cours | Validé | Seul traitement long : le chargement de l'index de recherche. Le message « Chargement de l'index de recherche… » s'affiche, et une saisie pendant le chargement ne relance pas le téléchargement. |
| [7.4](../../rgesn/backend/7-4_mecanisme-consensus/) Mécanisme de consensus | Non applicable | Aucune blockchain. |

{{% /tab %}}

{{% tab tabName="8. Hébergement" %}}

Le site est hébergé par GitHub Pages et servi par le CDN Fastly. Aucune information propre à GitHub Pages n'a été trouvée sur les indicateurs demandés par cette famille : ni dans sa documentation, ni par recherche.

| Critère | Statut | Justification |
|---|---|---|
| [8.1](../../rgesn/hebergement/8-1_demarche-hebergeur/) Démarche de l'hébergeur | Non validé | Ni indicateurs environnementaux publiés pour GitHub Pages, ni adhésion connue au Code de conduite européen sur les centres de données. |
| [8.2](../../rgesn/hebergement/8-2_gestion-equipements/) Gestion des équipements | Non validé | Information non trouvée pour GitHub Pages. |
| [8.3](../../rgesn/hebergement/8-3_pue/) PUE | Non validé | Information non trouvée pour GitHub Pages. |
| [8.4](../../rgesn/hebergement/8-4_wue/) WUE | Non validé | Information non trouvée pour GitHub Pages. |
| [8.5](../../rgesn/hebergement/8-5_electricite-renouvelable/) Électricité renouvelable | Non validé | Information non trouvée pour GitHub Pages. |
| [8.6](../../rgesn/hebergement/8-6_localisation/) Localisation | Non validé | L'adresse du site est enregistrée par GitHub aux États-Unis. Les pages sont servies par un cache Fastly à Paris, mais l'emplacement des serveurs d'origine n'est pas publié. |
| [8.7](../../rgesn/hebergement/8-7_chaleur-fatale/) Chaleur fatale | Non validé | Information non trouvée pour GitHub Pages. |
| [8.8](../../rgesn/hebergement/8-8_donnees-chaudes-froides/) Données chaudes et froides | Non applicable | Le site construit pèse 38 Mo, loin du seuil de 10 To. |
| [8.9](../../rgesn/hebergement/8-9_duplication-donnees/) Duplication des données | Non validé | Aucun niveau de service défini : la redondance est celle de GitHub. Le site peut être reconstruit à tout moment depuis son dépôt. |
| [8.10](../../rgesn/hebergement/8-10_decalage-asynchrone/) Calculs asynchrones | Non applicable | Aucun calcul ni transfert asynchrone. La construction du site se lance à chaque publication. |

{{% /tab %}}

{{% tab tabName="9. Algorithmie" %}}

| Critère | Statut | Justification |
|---|---|---|
| [9.1](../../rgesn/algorithmie/9-1_necessite-entrainement/) Nécessité d'un entraînement | Validé | Aucun apprentissage automatique : la recherche utilise un index plein texte. |
| [9.2](../../rgesn/algorithmie/9-2_methode-apprentissage/) à [9.7](../../rgesn/algorithmie/9-7_strategie-inference/) | Non applicable | Ni entraînement ni inférence de modèle. |

{{% /tab %}}

{{< /tabs >}}

---

## Plan d'avancement

Les actions sont classées de la plus simple à la plus longue.

| Action | Critères |
|---|---|
| 1. Charger FlexSearch à l'ouverture de la recherche, avec l'index, et annoncer le poids de l'index | 6.5, 4.12 |
| 2. Contrôler le budget par page à chaque publication, dans l'intégration continue | 6.1 |
| 3. Tester les parcours sur un Safari de plus de deux ans, pour compléter le critère 2.4 | 2.4 |
| 4. Écrire l'étude d'utilité, la description des besoins des publics visés, les objectifs environnementaux, la comparaison d'architecture, la stratégie de maintenance et de fin de vie, et la règle de revue des fiches | 1.1, 1.2, 1.5, 3.1, 2.7, 5.8, 7.2 |
| 5. Refaire cette évaluation à chaque évolution importante, et au plus tard en octobre 2027 | 1.4 |
| 6. Demander à GitHub ses indicateurs environnementaux, ou comparer avec un hébergeur qui les publie et permet de régler la durée de cache | 2.8, 2.10, 8.1 à 8.9 |
