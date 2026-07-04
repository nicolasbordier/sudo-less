---
weight: 100
title: "Dev Front"
description: "Tableau récapitulatif des outils gratuits et payants pour mesurer et piloter l'écoconception d'une application web côté front."
icon: "code"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Ce tableau récapitule les outils déjà présentés dans les fiches RGESN, spécifiques au développement web front-end : mesure d'impact, audit de performance, vérification de compatibilité et budgets de revue régulière (voir notamment le [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/)).

| Outil | Catégorie | Ce qu'il mesure | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis) | Extension navigateur | Score **EcoIndex** en direct (complexité du DOM, poids transféré, nombre de requêtes) + estimation eau/GES, sur un parcours complet même derrière authentification | Oui | Non (usage manuel) |
| [EcoIndex.fr](https://www.ecoindex.fr/) | Outil en ligne | Même méthodologie EcoIndex que GreenIT-Analysis, sans installation, pour toute URL publique | Oui | Non |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse) / [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) | Audit intégré (DevTools / CLI) | Performance, accessibilité, bonnes pratiques, SEO, PWA — avec budgets de performance en CI | Oui | Oui |
| [Core Web Vitals](https://web.dev/articles/vitals) ([PageSpeed Insights](https://pagespeed.web.dev/)) | Métriques Google | LCP, INP, CLS — données de laboratoire et de terrain (Search Console) | Oui | Via API |
| [EcoSonar](https://github.com/green-code-initiative/EcoSonar) | Plugin SonarQube | Combine GreenIT-Analysis/EcoIndex, Lighthouse et le validateur W3C, avec analyse statique du code | Oui (open source) | Oui |
| [Fruggr](https://www.fruggr.io/fr/) | Plateforme SaaS | ACV numérique multicritère (au-delà du seul EcoIndex), budget par unité fonctionnelle | Non (essai limité) | Oui |
| [PerformanceBudget.io](https://www.performancebudget.io/) | Définition de budget | Aide à fixer des cibles chiffrées (poids, requêtes, temps de chargement) avant développement | Oui | Non |
| [Baseline](https://web.dev/baseline) / [Can I Use](https://caniuse.com/) / [MDN](https://developer.mozilla.org/) | Référence de compatibilité | Vérifie qu'une API ou fonctionnalité web est standard et largement supportée, avant de l'adopter | Oui | Non (consultation) |
| [GreenFrame](https://greenframe.io/) | CLI open source | Consommation (CPU, mémoire, réseau) d'un scénario Cypress rejoué dans une stack Dockerisée | Oui (CLI) | Oui |

---

Le choix dépend surtout du moment où l'outil intervient : **avant développement** (PerformanceBudget.io, Baseline), **en revue ponctuelle** (EcoIndex.fr), ou **en surveillance continue** (Lighthouse CI, EcoSonar, GreenFrame) — voir le détail de cette logique de revue régulière au [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/).
