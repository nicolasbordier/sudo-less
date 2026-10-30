---
weight: 300
title: "Dev Mobile"
description: "Tableau récapitulatif des outils gratuits et payants pour mesurer et piloter l'écoconception d'une application mobile, Android et iOS."
icon: "smartphone"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-10-23T00:00:00+01:00"
draft: false
toc: true
---

Cette page récapitule les outils déjà présentés dans les fiches RGESN, spécifiques au développement mobile : mesure d'énergie sur terminal réel, automatisation de parcours, suivi natif en production, et mécanismes natifs qui réduisent les données échangées (voir notamment le [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/)).

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de contenu, un écosystème ou un fournisseur particulier), sont payants, ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [Maestro](https://maestro.dev/) | CLI open source | Automatise un parcours utilisateur reproductible sur émulateur ou terminal réel (Android/iOS) | Oui | Oui |
| [Flashlight](https://flashlight.dev/) | CLI open source (BAM.tech) | Score de performance CPU/RAM/FPS ; supporte nativement les flows Maestro | Oui | Oui |
| [Android Vitals](https://developer.android.com/topic/performance/vitals) | Natif Play Console | Réveils excessifs, wake locks partiels, données réelles remontées depuis les terminaux en production | Oui | Non (natif, suivi continu) |
| [Rapport de pré-lancement](https://support.google.com/googleplay/android-developer/answer/9842757) (Firebase Test Lab) | Natif Play Console | Teste automatiquement chaque build importé sur un panel d'appareils réels avant mise en production | Oui | Oui (à chaque build) |
| [MetricKit](https://developer.apple.com/documentation/MetricKit) | Framework natif iOS | CPU, mémoire, réseau et impact énergétique, agrégés quotidiennement depuis les terminaux réels des utilisateurs | Oui | Non (natif, suivi continu) |
| [Profiler Android Studio](https://developer.android.com/studio/profile/power-profiler) / [Power Profiler Xcode](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) | Profiler natif de l'IDE | Inspection CPU/mémoire/énergie en local, pour investiguer une régression ponctuelle | Oui | Non (manuel) |

## Outils complémentaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Intégrable en CI/CD ? |
|---|---|---|---|---|
| [GreenSpector](https://greenspector.com/en/consulting-and-services/) | Éditeur français (labo + Studio) | Audit statique et sonde de mesure dynamique sur banc de 100+ terminaux réels (Android/iOS) ; suit un budget de performance dans le temps | Non (solution commerciale) | Oui (Greenspector Studio) |
| [Proxyman](https://proxyman.com/) | Proxy de débogage réseau | Capture le trafic HTTP/HTTPS d'un parcours pour en chiffrer le volume de données | Basique gratuit, licence payante pour les fonctions avancées | Non |
| [py-ios-device](https://github.com/YueChen-C/py-ios-device) | CLI Python communautaire | Accès scriptable au protocole `instruments` d'Apple (CPU, GPU, mémoire) sans passer par l'interface Xcode | Oui | Oui |
| [PWABuilder](https://www.pwabuilder.com/) / [Bubblewrap](https://github.com/GoogleChromeLabs/bubblewrap) | Outils open source (Microsoft / Google Chrome Labs) | Empaquette une Progressive Web App existante en application installable App Store / Play Store ; PWABuilder s'appuie sur Bubblewrap pour le Play Store | Oui | Non |
| [Room](https://developer.android.com/training/data-storage/room) / [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) (Android), [Core Data](https://developer.apple.com/documentation/coredata) / [Background Tasks](https://developer.apple.com/documentation/backgroundtasks) (iOS) | Bibliothèques natives | Gardent en local les données déjà consultées pour les afficher sans réseau (Room, Core Data), et rejouent à la reconnexion les actions faites hors ligne grâce à une tâche différée (WorkManager, Background Tasks). Utiles pour le critère [2.3](../../../rgesn/specifications/2-3_connexion-bas-debit/) | Oui | Sans objet (intégrées à l'application) |
| [Android App Bundle](https://developer.android.com/guide/app-bundle) / [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery), [App Thinning](https://help.apple.com/xcode/mac/current/en.lproj/devbbdc5ce4f.html) (iOS) | Mécanismes de distribution natifs | Google Play sert des APK optimisés par appareil, ne télécharge certains modules qu'à la demande et ne retransmet que les portions modifiées à chaque mise à jour (patch delta) ; App Thinning ne livre à chaque appareil que les ressources de sa configuration (Slicing) et télécharge certains contenus au besoin (On-Demand Resources). Utiles pour le critère [3.6](../../../rgesn/architecture/3-6_mises-a-jour-incrementielles/) | Oui | Oui (à la publication) |
| [Dependency Analysis Gradle Plugin](https://github.com/autonomousapps/dependency-analysis-gradle-plugin) | Plugin Gradle open source | Détecte les dépendances inutilisées, mal déclarées ou transitives non explicites, et repère les plus lourdes grâce à un « dominator tree ». Utile pour le critère [2.9](../../../rgesn/specifications/2-9_composants-interface/) | Oui | Oui |

---

Ces outils se combinent plutôt qu'ils ne se remplacent : **Maestro** automatise le parcours, **Flashlight** ou **Proxyman** mesurent ce qui se passe pendant ce parcours (CPU/RAM/FPS ou réseau), tandis qu'**Android Vitals** et **MetricKit** prennent le relais une fois l'application publiée, en continu et sans instrumentation. **GreenSpector** reste la seule option qui mesure une consommation énergétique réelle sur banc de terminaux physiques — les autres outils gratuits en restent des proxys (réseau, CPU, wake locks). Les bibliothèques hors ligne et les mécanismes de mise à jour incrémentielle ne mesurent rien : ils réduisent directement les données échangées. Voir le détail complet de cette logique au [critère 1.4](../../../rgesn/strategie/1-4_revue-ecoconception/) et le choix des technologies standard au [critère 1.9](../../../rgesn/strategie/1-9_technologies-standard/).
