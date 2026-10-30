---
weight: 300
title: "Implémentation"
description: "Tableau récapitulatif des outils spécifiques à la phase d'implémentation : mesurer l'impact du code au fur et à mesure de son écriture, avant la mise en production."
icon: "code_blocks"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-23T00:00:00+01:00"
draft: false
toc: true
---

Une fois les choix de [conception](../conception/) arrêtés, la phase d'**implémentation** consiste à écrire le code et à produire les contenus en vérifiant, au fil de l'eau, qu'ils respectent les budgets et standards définis en amont — voir les pages [Dev Front](../../par-metier/dev-front/), [Dev Back](../../par-metier/dev-back/) et [Dev Mobile](../../par-metier/dev-mobile/) pour le détail complet par métier.

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de contenu, un écosystème ou un fournisseur particulier), sont payants, ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [GreenIT-Analysis](https://github.com/cnumr/GreenIT-Analysis) | Extension navigateur | Score EcoIndex en direct pendant le développement, y compris derrière authentification | Oui |
| [EcoIndex CLI](https://github.com/cnumr/EcoIndex_python/tree/main/projects/ecoindex_cli) (CNUMR) | CLI / Docker | Même score EcoIndex, calculé en CI sur une liste d'URL ou tout un site (sitemap, crawl), avec un export CSV ou JSON à comparer au budget | Oui (licence CC BY-NC-ND 3.0, usage non commercial) |
| [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) | Audit intégré CI | Fait échouer une pull request si un budget de performance est dépassé | Oui |
| Outils de développement des navigateurs (DevTools de Chrome, Edge, Firefox) | Outils intégrés au navigateur | Simulent une connexion dégradée et n'importe quelle taille d'écran, en local et sans matériel ([critères 2.2](../../../rgesn/specifications/2-2_anciens-terminaux/), [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) et [2.5](../../../rgesn/specifications/2-5_terminaux-affichage/)) | Oui |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) / [GreenFrame](https://greenframe.io/) | Mesure backend | Consommation par processus (Scaphandre) ou par scénario API complet en conteneurs (GreenFrame) | Oui |
| [Maestro](https://maestro.dev/) + [Flashlight](https://flashlight.dev/) | CLI mobile | Automatise un parcours et mesure CPU/RAM/FPS pendant son exécution | Oui |
| [Baseline](https://web.dev/baseline) / [Can I Use](https://caniuse.com/) | Référence de compatibilité | Vérifie qu'une API utilisée dans le code est standard et largement supportée | Oui |
| [Squoosh](https://squoosh.app/) (Google Chrome Labs) | Application web de compression d'images | Convertit une image en AVIF, WebP ou JPEG XL et règle sa qualité d'après le rendu, avec une comparaison avant/après et le poids obtenu en direct ([critères 5.1](../../../rgesn/contenus/5-1_format-images/) et [5.2](../../../rgesn/contenus/5-2_compression-images/)) | Oui (open source) |
| [FFmpeg](https://ffmpeg.org/) (avec `ffprobe`) | Outil en ligne de commande | Convertit les GIF animés en vidéo, réduit la définition et le débit des vidéos, extrait la piste son pour un mode « écoute seule », encode l'audio en Opus, puis vérifie le résultat ([critères 4.1](../../../rgesn/ux-ui/4-1_lecture-automatique/), [5.3](../../../rgesn/contenus/5-3_definition-videos/) à [5.6](../../../rgesn/contenus/5-6_compression-audio/)) | Oui (open source) |

## Outils complémentaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? |
|---|---|---|---|
| [Boaviztapi](https://boavizta.org/en/blog/empreinte-de-la-fabrication-d-un-serveur) / [Datavizta](https://dataviz.boavizta.org/) | API et dashboard | Compare l'empreinte de plusieurs composants ou instances avant de les intégrer au code | Oui |
| [Guide ANSSI-PG-083](https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf) | Référentiel officiel | Implémente le niveau de chiffrement choisi en conception avec l'algorithme le moins coûteux à sécurité égale | Oui |
| [sitespeed.io](https://www.sitespeed.io/documentation/sitespeed.io/connectivity/) | CLI / Docker open source | Rejoue en CI un chargement sous débit simulé (`-c 3g`) pour détecter une régression avant la production ([critère 2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/)) | Oui |
| [Playwright](https://playwright.dev/) | Framework de test open source | Vérifie à chaque pull request l'absence de débordement ou de perte de fonctionnalité à des tailles d'écran précises ([critère 2.5](../../../rgesn/specifications/2-5_terminaux-affichage/)) | Oui |
| [CodeCarbon](https://github.com/mlco2/codecarbon) (Data For Good) | Package Python open source | Estime la consommation d'une fonction Python et la convertit en kg de CO2e selon l'intensité carbone du réseau électrique local ([critère 3.1](../../../rgesn/architecture/3-1_architecture-composants/)) | Oui |
| [tarteaucitron.js](https://tarteaucitron.io/fr/) | Gestionnaire de consentement open source | Bloque les services tiers jusqu'au consentement explicite de l'utilisateur ([critère 4.4](../../../rgesn/ux-ui/4-4_activation-service-tiers/)) | Oui |
| [systemfontstack.com](https://www.systemfontstack.com/) / [pyftsubset](https://fonttools.readthedocs.io/en/latest/subset/) / [glyphhanger](https://github.com/zachleat/glyphhanger) | Référence / outils en ligne de commande | Évitent de télécharger une police, ou la réduisent aux seuls caractères affichés par le service ([critère 4.8](../../../rgesn/ux-ui/4-8_polices-caracteres/)) | Oui |
| [esbuild](https://esbuild.github.io/), [Terser](https://terser.org/), [Lightning CSS](https://lightningcss.dev/), [cssnano](https://cssnano.github.io/cssnano/), [SVGO](https://svgo.dev/), [html-minifier-terser](https://github.com/terser/html-minifier-terser) | Minifieurs | Minifient JavaScript, CSS, SVG et HTML au moment du build ([critère 6.3](../../../rgesn/frontend/6-3_compression-ressources/)) | Oui |
| Compression des réponses : [ngx_brotli](https://github.com/google/ngx_brotli), [`mod_brotli`](https://httpd.apache.org/docs/2.4/mod/mod_brotli.html), directive [`encode`](https://caddyserver.com/docs/caddyfile/directives/encode) de Caddy | Modules serveur | Compressent les ressources texte à la volée, ou une fois au déploiement pour les fichiers statiques ([critère 6.3](../../../rgesn/frontend/6-3_compression-ressources/)) | Oui |
| [`cwebp`](https://developers.google.com/speed/webp/docs/cwebp), [`avifenc`](https://github.com/AOMediaCodec/libavif), [ImageMagick](https://imagemagick.org/) | Outils en ligne de commande | Convertissent des images en lot et redimensionnent à l'envoi celles qui dépassent la taille d'affichage maximale ([critères 5.1](../../../rgesn/contenus/5-1_format-images/) et [6.4](../../../rgesn/frontend/6-4_dimensions-images/)) | Oui |
| [RespImageLint](https://ausi.github.io/respimagelint/) | Bookmarklet open source | Signale les erreurs des images responsives (`sizes` qui ne correspond pas à la largeur affichée, version manquante pour certaines largeurs) ([critère 6.4](../../../rgesn/frontend/6-4_dimensions-images/)) | Oui |
| [hls.js](https://github.com/video-dev/hls.js) | Bibliothèque JavaScript | Plafonne la définition d'une vidéo en streaming adaptatif selon le terminal ([critère 5.3](../../../rgesn/contenus/5-3_definition-videos/)) | Oui |
| [HandBrake](https://handbrake.fr/) / [MediaInfo](https://mediaarea.net/fr/MediaInfo) | Logiciels libres avec interface graphique | Encodent une vidéo à qualité constante et en contrôlent la définition et les codecs, sans ligne de commande ([critères 5.3](../../../rgesn/contenus/5-3_definition-videos/) et [5.4](../../../rgesn/contenus/5-4_compression-videos/)) | Oui |
| [qpdf](https://qpdf.readthedocs.io/), [LibreOffice](https://www.libreoffice.org/), `pdfinfo` / `pdfimages` ([Poppler](https://poppler.freedesktop.org/)) | Outils en ligne de commande | Exportent un PDF balisé avec des images compressées à la source, l'optimisent sans perte, puis contrôlent le résultat ([critère 5.7](../../../rgesn/contenus/5-7_format-documents/)) | Oui |
| [Room](https://developer.android.com/training/data-storage/room) / [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager), [Core Data](https://developer.apple.com/documentation/coredata) / [Background Tasks](https://developer.apple.com/documentation/backgroundtasks) | Bibliothèques mobiles natives | Affichent sans réseau les données déjà consultées et rejouent à la reconnexion les actions faites hors ligne ([critère 2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/)) | Oui |
| [Android App Bundle](https://developer.android.com/guide/app-bundle), [App Thinning](https://help.apple.com/xcode/mac/current/en.lproj/devbbdc5ce4f.html) (iOS) | Mécanismes de distribution natifs | Ne livrent à chaque appareil que ce qui le concerne, et ne retransmettent que les portions modifiées à la mise à jour ([critère 3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/)) | Oui |
| [testssl.sh](https://testssl.sh/) / [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) / [test-ipv6.com](https://test-ipv6.com/) | Outils de test | Vérifient la configuration TLS d'un serveur et son accessibilité en IPv6 avant la mise en production ([critère 3.3](../../../rgesn/architecture/3-3_evolution-protocoles/)) | Oui |

---

Le point commun de ces outils : ils s'utilisent **pendant que le code est encore modifiable à faible coût**, contrairement aux outils de la phase [Run](../run/) qui n'observent qu'un système déjà déployé. Intégrer ces vérifications en CI (Lighthouse CI, EcoSonar) plutôt qu'en revue manuelle ponctuelle permet de détecter une régression au moment précis où elle est introduite. Les outils de traitement des médias suivent la même logique : une image ou une vidéo s'encode une fois, avant sa mise en ligne, plutôt qu'à chaque affichage.
