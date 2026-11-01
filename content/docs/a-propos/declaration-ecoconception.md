---
weight: 300
title: "Déclaration d'écoconception"
description: "Déclaration d'écoconception de sudo-less.dev selon le RGESN 2024 : score d'avancement, résultat de chaque critère et plan d'avancement."
icon: "fact_check"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

Cette page est la déclaration d'écoconception propre à **sudo-less.dev**, rédigée selon le [RGESN](../../rgesn/). Vous cherchez plutôt à rédiger la vôtre ? Voir le [guide complet](../../declaration/) (contenu obligatoire, modèles officiels, formule de calcul du score).

| | |
|---|---|
| **Service évalué** | sudo-less.dev, publié à l'adresse [nicolasbordier.github.io/sudo-less](https://nicolasbordier.github.io/sudo-less/) |
| **Date de rédaction** | 31 octobre 2026 |
| **Dernière mise à jour** | 1er novembre 2026 |
| **Référentiel appliqué** | RGESN, version 2024 |
| **Méthode** | Auto-évaluation par le mainteneur du site, avec des mesures dans Chromium 155 et une évaluation d'empreinte avec l'API Boavizta |
| **Contact écoconception** | Le mainteneur du site, par les [issues du dépôt GitHub](https://github.com/nicolasbordier/sudo-less/issues) |

---

## Score d'avancement

| Score actuel | Score précédent | Score visé (octobre 2028) |
|---|---|---|
| **77 %** | Aucun, première déclaration | 79 % |

**44 critères validés sur 56 applicables** ; 22 critères ne s'appliquent pas au site. Le score pondère chaque critère par sa priorité :

| Priorité | Pondération | Critères applicables | Critères validés |
|---|---:|---:|---:|
| Prioritaire | 1,5 | 20 | 14 |
| Recommandé | 1,25 | 26 | 20 |
| Modéré | 1 | 10 | 10 |

Score = (14 × 1,5 + 20 × 1,25 + 10 × 1) / (20 × 1,5 + 26 × 1,25 + 10 × 1) = 56 / 72,5 = **77 %**.

Ce score mesure l'avancement dans le référentiel, pas l'impact environnemental du site. Le score visé suppose que les actions 1 et 2 du plan d'avancement soient réalisées ; il ne compte pas les critères d'hébergement, qui dépendent de GitHub.

---

## Utilité du service

Les équipes qui débutent en écoconception ne savent pas par où commencer. Les référentiels (RGESN, GR491, RWEB, W3C…) se recoupent, chacun avec sa structure et son vocabulaire, et décrivent le résultat attendu plus souvent que la manière de l'obtenir. sudo-less part du RGESN et réunit, pour chaque critère, ce qu'en disent les autres référentiels, avec des exemples de mise en œuvre à copier et à adapter. Ce besoin a été recueilli auprès des publics visés (voir [Publics visés et besoins](#publics-visés-et-besoins)).

**Objectifs de développement durable.** Le site transmet les connaissances nécessaires au développement durable, ce que visent trois cibles des [ODD](https://sdgs.un.org/fr/goals) :

- **4.7** : faire acquérir à tous les apprenants les connaissances et compétences nécessaires pour promouvoir le développement durable ;
- **12.8** : donner à tous les informations et connaissances nécessaires au développement durable ;
- **13.3** : améliorer l'éducation, la sensibilisation et les capacités individuelles et institutionnelles en matière d'atténuation du changement climatique.

**Solutions existantes**, recensées dans la page [Autres référentiels](../../autres-referentiels/) :

| Solution | Limite pour ce besoin |
|---|---|
| Le RGESN seul, en ligne ou en PDF (131 pages) | Il décrit le résultat attendu et le moyen de le contrôler, rarement la configuration qui l'obtient. |
| Les autres référentiels, un par un : GR491, RWEB, Web Sustainability Guidelines, guide des Designers Éthiques… | Certains indiquent leur correspondance avec le RGESN (RWEB, RIA, REIPRO), mais aucun de ceux recensés ne réunit, critère par critère, ce que disent les autres. |
| Les formations et l'accompagnement | Ils répondent aux questions en direct, mais ne touchent que leurs participants, le temps de la session. Les questions de mise en œuvre se posent souvent ensuite, sur le projet. |
| Les livres et guides imprimés | Figés à leur date d'édition, alors que les référentiels, les outils et les versions des serveurs évoluent. |

**Réponses aux questions du moyen de test du critère 1.1 :**

1. **L'utilisation du numérique est-elle nécessaire ?** Oui. Les publics visés conçoivent des services numériques, et ce qu'ils cherchent se copie : configurations, commandes, liens vers les sources et les outils. Une page web se corrige à chaque nouvelle version d'un référentiel ou d'un outil, et reste gratuite pour tous.
2. **Existe-t-il d'autres solutions non numériques ?** La formation et les livres (tableau ci-dessus). Le site ne remplace pas la formation : il la prolonge, quand les questions de mise en œuvre se posent sur le projet.
3. **Quels sont les réels besoins justifiant la création du service ?** Trouver les bonnes pratiques pertinentes parmi des référentiels qui se recoupent, savoir les mettre en œuvre, et automatiser la mesure. Voir [Publics visés et besoins](#publics-visés-et-besoins).
4. **La valeur ajoutée du service justifie-t-elle les ressources mobilisées ?** Les ressources sont connues : 1,4 à 1,6 g CO2e par lecture d'une fiche, 14 à 16 kg CO2e par an pour une hypothèse de 10 000 lectures, et le temps du mainteneur. La valeur ajoutée n'est pas mesurée : faute de mesure d'audience, elle s'apprécie à chaque revue annuelle, d'après les retours des participants aux formations, les issues et les retours d'expérience proposés. Si le site cesse d'être utilisé, sa [fin de vie](#maintenance-et-fin-de-vie) est prévue.
5. **Est-ce qu'on crée plus de valeur qu'on en détruit ?** Probablement, sans pouvoir le démontrer : le gain dépend de ce que les équipes appliquent ensuite sur leurs propres services, ce qui n'est pas suivi. Les conséquences négatives, effets rebond compris, sont décrites dans l'[arbre des conséquences](../revue-conception/#arbre-des-conséquences).
6. **Pour chaque fonctionnalité, est-elle vraiment nécessaire ?** La [revue de conception](../revue-conception/) examine sept fonctionnalités. Toutes sont gardées ; la page d'accueil a été allégée, et la recherche ne se charge qu'à la première saisie.
7. **Que se passerait-il si on ne l'avait pas ?** Les équipes partiraient du PDF du RGESN, chercheraient elles-mêmes les référentiels complémentaires, site par site, et trouveraient seules la configuration, souvent par essais et erreurs. C'est le [scénario de référence](../revue-conception/#scénario-de-référence) de la revue de conception.

---

## Publics visés et besoins

**Recueil.** Le mainteneur du site forme et accompagne des équipes à l'écoconception de services numériques depuis 2020 : environ 1 000 participants, dans des organisations de toutes tailles, du groupe multinational à la PME, et de secteurs variés : assurance, banque, énergie, transport, luxe, télévision, aérospatiale, ESN, agences web. Ces formations sont certifiées Qualiopi : chacune commence par le recueil des attentes de chaque participant, et les échanges pendant la session font remonter les questions restées sans réponse.

**Publics visés :**

- **primaires** : les équipes qui débutent en écoconception, soit les porteurs de projet, designers UX, développeurs front, back et mobile, ops et architectes. Ce sont l'essentiel des participants aux formations. La page [Getting Started](../../getting-started/) les oriente par métier ;
- **secondaires** : les responsables RSE ou numérique soutenable, qui pilotent la démarche, et les formateurs et accompagnateurs, qui peuvent réutiliser le contenu sous licence CC BY-SA.

**Besoins exprimés et choix du site :**

| Question récurrente en formation | Réponse du site |
|---|---|
| Où trouver les bonnes pratiques les plus pertinentes, alors que de nombreux référentiels se recoupent ? | Le RGESN sert de fil conducteur : chaque fiche réunit ce que disent les autres référentiels du même critère, et la page [Autres référentiels](../../autres-referentiels/) les présente par domaine. Getting Started indique par où commencer, par métier et par phase de projet. |
| Comment les mettre en œuvre ? Les référentiels décrivent le résultat attendu, par exemple des requêtes en HTTP/2 au minimum, rarement la configuration qui l'obtient. | Des onglets de mise en œuvre technique, à copier et à adapter : par exemple « Activer HTTP/2 et HTTP/3 » pour Nginx et Apache, dans la fiche [3.3](../../rgesn/architecture/3-3_evolution-protocoles/). Les [retours d'expérience](../../retours-experience/) montrent ce que des services réels ont fait. |
| Comment automatiser la mesure de l'empreinte et bloquer une version qui dépasse un seuil ? | Les fiches [1.4](../../rgesn/strategie/1-4_revue-ecoconception/) et [6.1](../../rgesn/frontend/6-1_poids-requetes-ecran/) automatisent les audits et bloquent une version hors budget, avec Lighthouse CI dans GitHub Actions. La fiche [1.5](../../rgesn/strategie/1-5_objectifs-environnementaux/) évalue l'empreinte, et la page [Outils](../../outils/) recense les outils par métier et par phase. |

**Limites.** Les besoins ont été recueillis pendant les formations, par le mainteneur, et non lors d'entretiens dédiés. Les participants sont des personnes que leur organisation a déjà engagées dans la démarche : celles qui n'ont jamais été formées sont moins représentées. Le site n'a pas de mesure d'audience (critère 1.6) : les besoins sont réexaminés à chaque revue annuelle, en octobre, d'après les questions posées en formation et les issues du dépôt.

---

## Chemins critiques et unités fonctionnelles évalués

Quatre parcours ont été testés le 31 octobre 2026 dans Chromium 155, cache désactivé, page entièrement défilée, sur trois écrans : 1 366 × 768, 1 200 × 720 et 390 × 844 pixels.

1. Arriver sur la page d'accueil.
2. Ouvrir une fiche RGESN depuis le menu, et passer d'un onglet à l'autre.
3. Rechercher un terme, ici « cache », et ouvrir un résultat.
4. Consulter les pages de synthèse « Retours d'expérience » et « Autres référentiels ».

| Page | Requêtes | Poids transféré |
|---|---:|---:|
| Accueil | 7 | 44 Ko |
| Sommaire de la documentation | 7 | 62 Ko |
| Fiche [6.5](../../rgesn/frontend/6-5_chargement-ressources/) | 7 | 73 Ko |
| Retours d'expérience | 7 | 71 Ko |
| Autres référentiels | 7 | 71 Ko |

Sur une fiche, ce poids se répartit en 22 Ko de HTML, 14 Ko de CSS, 24 Ko de JavaScript (Bootstrap 19 Ko, thème 5 Ko) et 11,3 Ko pour la police d'icônes. La première saisie dans la recherche télécharge en plus la bibliothèque FlexSearch et l'index de recherche : 344 Ko compressés, 1 076 Ko une fois décompressés.

---

## Empreinte environnementale et budget par page

Détaillés dans la page [Empreinte environnementale](../empreinte-environnementale/), évaluée le 1er novembre 2026 :

- **Empreinte** : lire une fiche émet 1,4 à 1,6 g CO2e, à plus de 95 % pour la fabrication du terminal du lecteur ; 14 à 16 kg CO2e par an pour une hypothèse de 10 000 lectures.
- **Objectifs** : aucune hausse de l'empreinte d'une lecture jusqu'en 2030 ; −50 % par publication d'ici octobre 2027.
- **Budget par page**, vérifié à chaque publication : 100 Ko transférés, 10 requêtes et 1 500 éléments du DOM au plus.

---

## Maintenance et fin de vie

Inventaire au 31 octobre 2026 des fonctionnalités, composants et environnements du site. Il est revu chaque année en octobre, avec cette déclaration ; la construction du site signale cette page si elle n'a pas été mise à jour depuis 12 mois.

| Élément | État d'utilisation | Maintenance |
|---|---|---|
| Fonctionnalités de la [revue de conception](../revue-conception/) : fiches, recherche, pages de synthèse, déclaration, page d'accueil, mode sombre | Utilisées. Faute de mesure d'audience (critère 1.6), leur usage est estimé à chaque revue d'après les issues et les retours reçus. | Une fonctionnalité retirée passe par la revue de conception ; son code et ses fichiers sont supprimés. |
| Contenus | 129 pages, 27 Mo une fois le site construit | Durée de vie décrite dans la page [Contribuer](../contribuer/#durée-de-vie-des-contenus). |
| Production : GitHub Pages | Utilisé | Voir la famille 8. Hébergement. |
| Construction : GitHub Actions | Utilisé à chaque publication | L'archive de déploiement expire après 1 jour, le cache après 7 jours sans usage, les journaux après 30 jours. |
| Développement : `hugo server` sur le poste du mainteneur | Utilisé | Pas d'environnement de préproduction. |
| Outils de construction : Hugo 0.168, Go, Dart Sass 1.105, Python et 6 scripts | Utilisés | Versions fixées dans la construction, mises à jour à chaque revue. |
| Thème Lotus Docs 0.3.0 et Bootstrap 5.3 | Utilisés. La dernière version du thème date d'avril 2026 ; il emploie des fonctions que Hugo a dépréciées, et Bootstrap 5 des règles Sass que Dart Sass 3 supprimera. | À chaque revue, vérifier leur compatibilité avec Hugo et Dart Sass. Si le thème n'est plus maintenu, le figer dans le dépôt ou le remplacer. |

Retirés le 31 octobre 2026, car inutilisés : l'analyse de sécurité GitLab (le dépôt n'est que sur GitHub), l'installation de Node.js dans la construction (aucune dépendance JavaScript), LibSass, remplacé par Dart Sass qui était installé sans servir, les cartes de source du CSS publiées sans utilité (1,7 Mo) et le JavaScript de Bootstrap sur la page d'accueil, qui n'a pas d'onglets.

**Fin de vie du service.** Si le site ne reçoit aucune publication pendant 12 mois, si son mainteneur l'arrête ou si le RGESN est remplacé :

1. un bandeau indique sur chaque page que le site n'est plus maintenu, et depuis quand ;
2. le dépôt GitHub est archivé en lecture seule, et une copie déposée sur [Software Heritage](https://www.softwareheritage.org/) ;
3. le site est dépublié 12 mois plus tard.

Le code (MIT) et le contenu (CC BY-SA 4.0) restent ainsi réutilisables, y compris pour reprendre le projet. Le site ne détient aucune donnée personnelle, et aucun équipement ne lui est dédié : il n'y a rien à reconditionner.

---

## Résultats par critère

{{< tabs tabTotal="9">}}

{{% tab tabName="1. Stratégie" %}}

| Critère | Statut | Justification |
|---|---|---|
| [1.1](../../rgesn/strategie/1-1_evaluation-utilite/) Évaluation de l'utilité | Validé | Étude d'utilité dans la section [Utilité du service](#utilité-du-service) : ODD 4.7, 12.8 et 13.3, solutions existantes, réponses aux questions du moyen de test. L'arbre des conséquences est dans la [revue de conception](../revue-conception/). Le bénéfice du site pour les services de ses lecteurs n'est pas mesuré. |
| [1.2](../../rgesn/strategie/1-2_cibles-utilisatrices/) Cibles utilisatrices | Validé | Publics primaires et secondaires, besoins recueillis auprès d'environ 1 000 participants aux formations du mainteneur depuis 2020, et choix du site qui y répondent : section [Publics visés et besoins](#publics-visés-et-besoins). Les besoins n'ont pas été recueillis lors d'entretiens dédiés. |
| [1.3](../../rgesn/strategie/1-3_referent-ecoconception/) Référent écoconception | Validé | Contact : le mainteneur du site, par les issues du dépôt GitHub. |
| [1.4](../../rgesn/strategie/1-4_revue-ecoconception/) Revue d'écoconception | Non validé | Cette déclaration est la première auto-évaluation. La suivante sera réalisée à chaque évolution importante du site, et au plus tard en octobre 2027. Il manque encore des audits de performance réguliers ; des tests de charge n'auraient pas de sens pour un site statique servi par un CDN mutualisé. |
| [1.5](../../rgesn/strategie/1-5_objectifs-environnementaux/) Objectifs environnementaux | Validé | Empreinte évaluée sur les quatre indicateurs prioritaires, par lecture de fiche, par publication et par an (14 à 16 kg CO2e pour 10 000 lectures, une hypothèse), selon le référentiel de l'ADEME et avec l'API Boavizta. Objectifs : aucune hausse par lecture jusqu'en 2030, −50 % par publication d'ici octobre 2027. Réévaluation chaque année en octobre. Voir la page [Empreinte environnementale](../empreinte-environnementale/). L'eau ne couvre que l'électricité, faute de données ouvertes sur la fabrication des terminaux. |
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
| [2.3](../../rgesn/specifications/2-3_connexion-bas-debit/) Connexion bas débit | Validé | Débit limité dans Chromium. À 512 kbit/s (latence 100 ms), une fiche s'affiche en 0,8 s, et la recherche donne ses résultats 6,4 s après son ouverture. À 400 kbit/s (latence 400 ms), 1,3 s et 8,2 s. Débit minimum testé : 400 kbit/s. |
| [2.4](../../rgesn/specifications/2-4_anciennes-versions-os/) Anciennes versions d'OS et de navigateurs | Validé | Testé le 31 octobre 2026 sur Chrome 120 (décembre 2023) et Firefox 115 ESR (juillet 2023), dans des versions sans mise à jour automatique : les parcours essentiels fonctionnent. Safari n'a pas encore été testé. Les versions minimales du critère 2.1 restent estimées par l'analyse du code. |
| [2.5](../../rgesn/specifications/2-5_terminaux-affichage/) Terminaux d'affichage | Validé | Testé le 31 octobre 2026 sur les 130 pages du site, à 1 200, 768 et 390 pixels de large : aucune page ne déborde, les tableaux larges défilant dans leur propre cadre. Les menus sont des boutons : ils s'ouvrent au clavier comme à la souris ou au doigt. |
| [2.6](../../rgesn/specifications/2-6_revue-conception-code/) Revue de conception et de code | Validé | Revue de conception : l'[arbre des conséquences](../revue-conception/) de chaque fonctionnalité, selon le niveau 1 de la méthode Empreinte Projet de l'ADEME (31 octobre 2026). Revue de code : le mainteneur relit chaque commit, code ou contenu, et chaque contribution externe avant de l'intégrer, selon les points décrits dans la page [Contribuer](../contribuer/). |
| [2.7](../../rgesn/specifications/2-7_maintenance-decommissionnement/) Maintenance et décommissionnement | Validé | Inventaire et stratégie dans la section [Maintenance et fin de vie](#maintenance-et-fin-de-vie) : revue chaque année en octobre, avec un rappel automatique ; cinq éléments inutilisés retirés le 31 octobre 2026 ; en fin de vie, dépôt archivé et site dépublié 12 mois plus tard. |
| [2.8](../../rgesn/specifications/2-8_fournisseurs-impacts-environnementaux/) Fournisseurs | Non validé | Le seul fournisseur, GitHub (hébergement et intégration continue), a été choisi sans critère environnemental documenté. |
| [2.9](../../rgesn/specifications/2-9_composants-interface/) Composants d'interface prêts à l'emploi | Validé | Le thème Lotus Docs apporte Bootstrap 5, allégé à la construction du site. Depuis le 31 octobre 2026, le CSS est réduit aux règles qui s'appliquent aux pages : 14 Ko compressés sur une fiche, au lieu de 43 Ko. Le JavaScript de Bootstrap (19 Ko) se limite à cinq composants, dont un seul ne sert sur aucune page : l'infobulle. La police d'icônes est réduite aux icônes utilisées (11,3 Ko), et l'index de recherche n'est téléchargé qu'à la demande. |
| [2.10](../../rgesn/specifications/2-10_services-tiers/) Services tiers | Non validé | Deux services tiers : GitHub Pages (hébergement, avec le CDN Fastly) et GitHub Actions (construction du site). Leur avancement sur les critères 1.4 et 1.5 n'a pas été vérifié. |

{{% /tab %}}

{{% tab tabName="3. Architecture" %}}

| Critère | Statut | Justification |
|---|---|---|
| [3.1](../../rgesn/architecture/3-1_architecture-composants/) Architecture et composants | Validé | Site statique généré par Hugo : rien ne s'exécute sur un serveur à la consultation, et le navigateur n'exécute que 24 Ko de JavaScript. Ce choix est comparé à un autre générateur statique, à un générateur qui hydrate un framework JavaScript, à un CMS et à une plateforme hébergée, et chaque composant (thème, recherche, icônes, hébergement) à ses alternatives, dans la [revue de conception](../revue-conception/#comparaison-darchitecture). Aucune brique énergivore. Le critère 2.9 est validé ; le 2.10 ne l'est pas, car l'hébergeur a été choisi sans critère environnemental. |
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
| [4.12](../../rgesn/ux-ui/4-12_impacts-fonctionnalites/) Fonctionnalités à fort impact | Validé | La fonctionnalité la plus lourde, la recherche, annonce son poids dès son ouverture : « La recherche télécharge l'index du site, soit 344 Ko, à la première saisie. » Rien n'est téléchargé avant cette saisie. Ce poids, plus de quatre fois celui d'une page, est recalculé à chaque publication. |
| [4.13](../../rgesn/ux-ui/4-13_notifications/) Notifications | Validé | Aucune notification. |
| [4.14](../../rgesn/ux-ui/4-14_dark-patterns/) Dark patterns | Validé | Interface relue au regard des exemples de l'article 25 du DSA : ni compte à rebours, ni case précochée, ni bandeau de consentement, ni incitation à s'inscrire. |
| [4.15](../../rgesn/ux-ui/4-15_controle-usages/) Contrôle des usages et mode sobre | Validé | **Information** : depuis le 1er novembre 2026, chaque fiche affiche sous son titre l'empreinte de sa lecture, à 0,23 g CO2e par minute selon la méthode de la page [Empreinte environnementale](../empreinte-environnementale/) ; chaque page affiche en pied de page son poids et son nombre de requêtes. **Mode sobre par défaut** : le site n'a pas de mode distinct, car il est sobre pour tous ses lecteurs. Ses paramètres : un budget de 100 Ko et 10 requêtes par page, vérifié à chaque publication ; aucune vidéo ; une recherche téléchargée seulement à la première saisie, avec son poids annoncé dès son ouverture. **Gains** : une page consultée sans recherche évite 344 Ko, soit au plus 0,004 g CO2e, 0,3 % d'une lecture sur réseau mobile. Aucun mode ne réduirait sensiblement l'empreinte d'une lecture : plus de 95 % vient de la fabrication du terminal, au prorata du temps de lecture, que la page [Contribuer](../contribuer/) limite à 10 minutes par fiche. Le mode sombre n'est pas compté comme mode sobre : il ne réduit pas le poids des pages, et n'économise l'énergie de l'écran que sur un smartphone OLED, de 39 à 47 % à pleine luminosité et de 3 à 9 % entre 30 et 50 %, selon une [étude de l'université Purdue](https://www.purdue.edu/research/features/stories/dark-mode-may-not-save-your-phones-battery-life-as-much-as-you-think-but-there-are-a-few-silver-linings) (2021). |

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
| [5.8](../../rgesn/contenus/5-8_archivage-suppression/) Archivage et suppression | Validé | Stratégie décrite dans la page [Contribuer](../contribuer/#durée-de-vie-des-contenus) : chaque page est relue au plus tard 12 mois après sa dernière mise à jour, puis mise à jour, fusionnée ou retirée, et chaque fiche suit la version en vigueur du RGESN. La construction du site signale automatiquement les pages à relire. Les pages retirées restent dans l'historique du dépôt. |

{{% /tab %}}

{{% tab tabName="6. Frontend" %}}

| Critère | Statut | Justification |
|---|---|---|
| [6.1](../../rgesn/frontend/6-1_poids-requetes-ecran/) Poids et requêtes par écran | Validé | Budget par page, détaillé dans la page [Empreinte environnementale](../empreinte-environnementale/#budget-par-page) : 100 Ko transférés, 10 requêtes et 1 500 éléments au plus, au chargement de la page, recherche non comprise. Toutes les pages le respectent : 73 Ko, 7 requêtes et 1 389 éléments au plus. Il est vérifié à chaque publication : si une page le dépasse, le site n'est pas mis en ligne. |
| [6.2](../../rgesn/frontend/6-2_cache-navigateur/) Cache côté utilisateur | Validé | À la deuxième visite d'une fiche, les 8 ressources viennent du cache. GitHub Pages fixe la durée de cache à 10 minutes (`max-age=600`) pour tous les fichiers, sans réglage possible. Au-delà, le navigateur revalide chaque fichier, sans le télécharger de nouveau (réponse 304). Les CSS et JavaScript ont un nom qui change avec leur contenu : ils pourraient être gardés bien plus longtemps. |
| [6.3](../../rgesn/frontend/6-3_compression-ressources/) Compression des ressources | Validé | Tous les fichiers texte arrivent compressés en gzip. GitHub Pages ne propose pas Brotli. |
| [6.4](../../rgesn/frontend/6-4_dimensions-images/) Dimensions des images | Validé | L'illustration d'accueil existe en quatre largeurs, de 480 à 1 280 pixels, et l'attribut `sizes` indique sa largeur affichée à chaque taille d'écran. Vérifié dans Chromium de 360 à 1 920 pixels de large : en densité 1 et 2, le navigateur charge une version au plus 1,5 fois plus large que l'affichage. Sur un ordinateur de densité 1, elle pèse 17,6 Ko au lieu de 45 Ko. |
| [6.5](../../rgesn/frontend/6-5_chargement-ressources/) Ressources utiles | Validé | Depuis le 31 octobre 2026, chaque ressource chargée sert sur la page : la bibliothèque de recherche et son index ne se téléchargent qu'à la première saisie, la page d'accueil ne charge plus le JavaScript de Bootstrap, le CSS est réduit aux règles utilisées et la police d'icônes aux icônes utilisées. Seul le module d'infobulle de Bootstrap reste inutilisé, dans un fichier qui sert par ailleurs (critère 2.9). |
| [6.6](../../rgesn/frontend/6-6_capteurs-terminaux/) Capteurs | Non applicable | Aucun capteur. |
| [6.7](../../rgesn/frontend/6-7_domaine-unique/) Ressources statiques sur un même domaine | Validé | Toutes les ressources du site viennent de son propre domaine, en HTTP/2. |

{{% /tab %}}

{{% tab tabName="7. Backend" %}}

| Critère | Statut | Justification |
|---|---|---|
| [7.1](../../rgesn/backend/7-1_cache-serveur/) Cache serveur | Validé | Site statique : chaque page est calculée une seule fois, à la construction, puis servie depuis le cache du CDN de GitHub Pages, renouvelé à chaque publication. |
| [7.2](../../rgesn/backend/7-2_durees-conservation/) Durées de conservation | Validé | Le site ne stocke aucune donnée de visiteur. Les contenus sont relus au plus tard 12 mois après leur dernière mise à jour (critère 5.8). Chez GitHub, l'archive de chaque déploiement expire après 1 jour, le cache de construction après 7 jours sans usage, et les journaux de construction après 30 jours. Le 31 octobre 2026, le site construit pèse 27 Mo, dont 1 Mo d'index de recherche ; ce poids est relevé à chaque mise à jour de cette déclaration. |
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
| [8.8](../../rgesn/hebergement/8-8_donnees-chaudes-froides/) Données chaudes et froides | Non applicable | Le site construit pèse 27 Mo, loin du seuil de 10 To. |
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
| 1. Tester les parcours sur un Safari de plus de deux ans, pour compléter le critère 2.4 | 2.4 |
| 2. Refaire cette évaluation à chaque évolution importante, et au plus tard en octobre 2027 | 1.4 |
| 3. Demander à GitHub ses indicateurs environnementaux, ou comparer avec un hébergeur qui les publie et permet de régler la durée de cache | 2.8, 2.10, 8.1 à 8.9 |
