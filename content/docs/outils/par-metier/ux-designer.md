---
weight: 400
title: "UX Designer"
description: "Tableau récapitulatif des outils et ressources pour intégrer l'écoconception dès la phase de design, avant le développement."
icon: "palette"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

Contrairement aux outils des pages [Dev Front](../dev-front/), [Dev Back](../dev-back/) et [Dev Mobile](../dev-mobile/) qui mesurent un service déjà codé, les ressources ci-dessous interviennent **avant le développement** — au moment où la plupart des choix qui déterminent l'empreinte finale du service sont pris (voir le [critère 1.1](../../../rgesn/strategie/1-1_evaluation-utilite/) et le [critère 1.2](../../../rgesn/strategie/1-2_cibles-utilisatrices/)).

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégré au poste de travail ? |
|---|---|---|---|---|
| [EcoSimulateur](https://www.figma.com/community/plugin/1430170108116488365/ecosimulateur) (Adveris) | Plugin Figma | Prédit en temps réel le score **EcoIndex** d'une maquette (complexité visuelle, structure) directement dans Figma, avant tout développement | Oui | Oui (plugin Figma) |
| [Guide d'écoconception des Designers Éthiques](https://eco-conception.designersethiques.org/guide/fr/) | Méthodologie + arbre de décision | Questionne la pertinence du besoin, aide à définir le périmètre fonctionnel minimal et propose un [arbre de décision Figma](https://www.figma.com/design/f0Rw3DFIYBmXN1DaPDg0In/Arbre-de-d%C3%A9cision?node-id=2-6) | Oui | Oui (fichier Figma) |
| [Matrice de captologie](https://docs.google.com/spreadsheets/d/1dj_KIKzyPlSND1-fSYNb0BgupCmh2XoYTPkFTKPiaq0/edit?gid=1991215211#gid=1991215211) (Designers Éthiques) | Grille d'évaluation | Évalue la captation de l'attention et la persuasion d'un service par des questions oui/non (notifications, défilement infini, lecture automatique, gamification, dark patterns, trackers…), converties en un score de A à G, avec des exemples d'application à des services connus. Utile pour les critères [4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/), [4.2](../../../rgesn/ux-ui/4-2_defilement-infini/), [4.13](../../../rgesn/ux-ui/4-13_notifications/) et [4.14](../../../rgesn/ux-ui/4-14_dark-patterns/). Document de travail (version 0.1) | Oui (CC-BY) | Non (tableur en ligne) |
| [Squoosh](https://squoosh.app/) (Google Chrome Labs) | Application web de compression d'images | Convertit une image en AVIF, WebP ou JPEG XL (ou en JPEG et PNG optimisés pour le repli) et règle sa qualité grâce à une comparaison avant/après en direct, avec le poids obtenu. La compression est ainsi choisie d'après le rendu de chaque image plutôt qu'avec une valeur fixe. Utile pour le critère [5.1](../../../rgesn/contenus/5-1_format-images/). Images traitées localement dans le navigateur (le site utilise Google Analytics) | Oui (open source) | Oui (application web installable) |
| [Formations DesignGouv](https://design.numerique.gouv.fr/formations/recherche-utilisateur/introduction-recherche-utilisateur/) | Formations gratuites | Recherche utilisateur, définition de proto-personas, priorisation des segments d'utilisateurs à étudier | Oui | Non (formation) |
| [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis) | Extension navigateur | Auditer une maquette déjà en ligne ou un concurrent, pour objectiver un existant avant de concevoir une alternative plus sobre | Oui | Oui (extension navigateur) |
| [NumEcoDiag](https://ecoresponsable.numerique.gouv.fr/ressources/documents-reference/referentiel-general-ecoconception/numecodiag/) (MiNumEco/DINUM) | Extension navigateur | Auto-évaluation sur les 79 critères du RGESN — utile pour situer les responsabilités du design dans l'ensemble de la démarche | Oui | Oui (extension navigateur) |
| [TRIZ — 40 principes d'innovation](https://innover-malin.com/triz-pour-les-nuls-partie-2-40-principes-d-innovation/) | Méthodologie de créativité | Grille de 40 principes de résolution de problèmes (théorie TRIZ, Altshuller) pour explorer des solutions de conception alternatives — segmenter, simplifier, faire autrement — avant de figer un choix technique coûteux à revenir en arrière | Oui | Non (méthode) |

---

**EcoSimulateur** est l'outil le plus directement actionnable pendant la conception : il donne un retour immédiat sur des choix encore modifiables (densité d'éléments, images, structure), là où les outils de mesure classiques (GreenIT-Analysis, NumEcoDiag) n'interviennent qu'une fois le service déjà codé — trop tard pour revenir sur un choix de conception sans repasser par le développement. C'est cette logique de **détection précoce** que porte le critère 1.1 en demandant d'évaluer l'utilité dès l'exploration, avant d'écrire la moindre ligne de code.
