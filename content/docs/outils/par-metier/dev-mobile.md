---
weight: 300
title: "Dev Mobile"
description: "Tableau récapitulatif des outils gratuits et payants pour mesurer et piloter l'écoconception d'une application mobile, Android et iOS."
icon: "smartphone"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

Ce tableau récapitule les outils déjà présentés dans les fiches RGESN, spécifiques au développement mobile : mesure d'énergie sur terminal réel, automatisation de parcours, et suivi natif en production (voir notamment le [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/)).

| Outil | Catégorie | Ce qu'il mesure | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [GreenSpector](https://greenspector.com/en/consulting-and-services/) | Éditeur français (labo + Studio) | Audit statique et sonde de mesure dynamique sur banc de 100+ terminaux réels (Android/iOS) ; suit un budget de performance dans le temps | Non (solution commerciale) | Oui (Greenspector Studio) |
| [Maestro](https://maestro.dev/) | CLI open source | Automatise un parcours utilisateur reproductible sur émulateur ou terminal réel (Android/iOS) | Oui | Oui |
| [Flashlight](https://flashlight.dev/) | CLI open source (BAM.tech) | Score de performance CPU/RAM/FPS ; supporte nativement les flows Maestro | Oui | Oui |
| [Proxyman](https://proxyman.com/) | Proxy de débogage réseau | Capture le trafic HTTP/HTTPS d'un parcours pour en chiffrer le volume de données | Basique gratuit, licence payante pour les fonctions avancées | Non |
| [Android Vitals](https://developer.android.com/topic/performance/vitals) | Natif Play Console | Réveils excessifs, wake locks partiels, données réelles remontées depuis les terminaux en production | Oui | Non (natif, suivi continu) |
| [Rapport de pré-lancement](https://support.google.com/googleplay/android-developer/answer/9842757) (Firebase Test Lab) | Natif Play Console | Teste automatiquement chaque build importé sur un panel d'appareils réels avant mise en production | Oui | Oui (à chaque build) |
| [MetricKit](https://developer.apple.com/documentation/MetricKit) | Framework natif iOS | CPU, mémoire, réseau et impact énergétique, agrégés quotidiennement depuis les terminaux réels des utilisateurs | Oui | Non (natif, suivi continu) |
| [Profiler Android Studio](https://developer.android.com/studio/profile/power-profiler) / [Power Profiler Xcode](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) | Profiler natif de l'IDE | Inspection CPU/mémoire/énergie en local, pour investiguer une régression ponctuelle | Oui | Non (manuel) |
| [py-ios-device](https://github.com/YueChen-C/py-ios-device) | CLI Python communautaire | Accès scriptable au protocole `instruments` d'Apple (CPU, GPU, mémoire) sans passer par l'interface Xcode | Oui | Oui |
| [PWABuilder](https://www.pwabuilder.com/) | Outil open source (Microsoft) | Empaquette une Progressive Web App existante en application installable App Store / Play Store | Oui | Non |

---

Ces outils se combinent plutôt qu'ils ne se remplacent : **Maestro** automatise le parcours, **Flashlight** ou **Proxyman** mesurent ce qui se passe pendant ce parcours (CPU/RAM/FPS ou réseau), tandis qu'**Android Vitals** et **MetricKit** prennent le relais une fois l'application publiée, en continu et sans instrumentation. **GreenSpector** reste la seule option qui mesure une consommation énergétique réelle sur banc de terminaux physiques — les autres outils gratuits en restent des proxys (réseau, CPU, wake locks). Voir le détail complet de cette logique au [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) et le choix des technologies standard au [critère 1.9](../../../rgesn/strategie/1-9_technologies-standard/).
