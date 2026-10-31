---
weight: 600
title: "6.6 - Usage des capteurs limité au besoin du service"
description: "Critère 6.6 du RGESN : ne déclencher la géolocalisation, la caméra ou le micro qu'à la demande de l'utilisateur, proposer une alternative sans capteur, arrêter le capteur dès qu'il ne sert plus et désactiver les capteurs inutilisés avec l'en-tête Permissions-Policy."
icon: "sensors"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique restreint-il l'usage des capteurs des terminaux utilisateurs au besoin du service ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Frontend` |
| **Critère**  | `6.6` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique fonctionne sans l'usage de capteurs des terminaux des utilisateurs` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire ou limiter les données échangées, dont des données personnelles (comme la webcam, le micro ou la géolocalisation, par exemple), avec le service numérique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Prévoir des mécanismes d'alerte, d'information et de consentement et une validation avant tout déclenchement de capteur du terminal par l'utilisateur. Il s'agit de limiter l'activation des capteurs aux moments où ils sont réellement nécessaires au bon fonctionnement du service, ou par l'activation d'une fonctionnalité expressément demandée par l'utilisateur. La définition du « moment où ils sont réellement nécessaires » doit être objectivée pour chaque usage : l'usage des capteurs doit être minimal par défaut, mais peut également être proposé à l'utilisateur un « mode dégradé » permettant de répondre à l'usage essentiel souhaité, optimisant les ressources matérielles et en particulier la batterie, sans aller jusqu'au fonctionnement nominal ou idéal.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier l'affichage de mécanismes d'alerte et de consentement avant tout déclenchement de capteur du terminal accepté par l'utilisateur. Examiner périodiquement que la durée d'utilisation des capteurs des terminaux utilisateurs est minimisée.

Le critère est validé si un mécanisme d'alerte et de consentement s'enclenche pour tout déclenchement de capteur du terminal.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

La [recommandation n°7 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=7) du [GR491](https://gr491.isit-europe.org/) (INR), « Limiter les utilisations de composants hardware ou capteurs sur les terminaux utilisateurs », ajoute un argument que le RGESN ne donne pas : la sollicitation des capteurs « peut entraîner une usure prématurée et en cas de panne pousser au renouvellement du périphérique ». Elle contient :

- [« Les capteurs sont-ils sollicités au besoin réel, plutôt qu'en permanence ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-les-operations-techniques-realisees-sur-le-front-6a9fb3), en priorité **Medium**, à revoir à chaque mise à jour ;
- [« Les fonctions de mise en pause sont-elles disponibles ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-loptimisation-des-utilisations-des-composants-physiques-du-e35f50) ;
- le conseil [« Des algorithmes prédictifs sont-ils mis en place pour éviter l'utilisation de capteurs physiques ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-les-capteurs-physiques-fournissent-des-donnees-reputees-235fca), dont le test aide à objectiver le besoin : « Quelle perte de précision est acceptée par les métiers ? » ;
- le conseil [« L'inaccessibilité d'un capteur […] est-elle traitée pour permettre au service d'être néanmoins fonctionnel (si possible) ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-linaccessibilite-de-composants-physiques-du-peripherique-utilisateur-aa442f) : un service qui fonctionne sans capteur reste utilisable sur un terminal ancien ou dont le capteur est en panne.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) des Designers Éthiques cite le critère 6.6 : « Éviter de recourir à des capteurs des terminaux utilisateurs. » Ses trois exemples sont autant d'alternatives à prévoir dès la conception :

- « géolocaliser l'utilisateur n'est pas forcément requis si une simple recherche par code postal est disponible » ;
- « éviter d'utiliser la webcam pour la double authentification si le SMS peut suffire » ;
- « privilégier l'écriture à l'usage du microphone ».

C'est le « mode dégradé » du RGESN : l'usage essentiel reste possible sans capteur, ce qui sert aussi les personnes qui refusent l'accès ou n'ont pas le capteur.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) ne parlent pas des capteurs, mais deux critères de succès s'y appliquent :

- « API requests », dans la fiche [**« Use sustainable JavaScript and APIs »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-javascript-and-apis) : « Only call client-side or server-side APIs when needed » ;
- « Data ownership », dans la fiche [**« Promote responsible data practices »**](https://www.w3.org/TR/web-sustainability-guidelines/#promote-responsible-data-practices) : « Only collect and retain personal data for a defined purpose and for no longer than necessary ».

Une position, une image ou un son sont des données personnelles : l'objectif du 6.6 rejoint ici le RGPD et le [critère 1.6](../../strategie/1-6_collecte-donnees/).

{{% /tab %}}

{{% tab tabName="Permissions du navigateur" %}}

Profil(s) métier concerné(s) : `Développeur`

**L'autorisation du navigateur ne suffit pas.** Géolocalisation, caméra et micro ne fonctionnent qu'après l'accord de l'utilisateur, donné dans une fenêtre du navigateur. Cette fenêtre ne dit pas pourquoi le service a besoin du capteur, et si l'accès est accordé durablement, le navigateur ne le redemande plus. L'information et le déclenchement au bon moment restent donc à la charge du service.

**L'en-tête `Permissions-Policy` désactive ce qui ne sert pas.** Testé le 30 octobre 2026 dans Chromium 155, sur une page qui demande la position, autorisation accordée :

| Configuration | Résultat |
|---|---|
| Sans en-tête | Position obtenue |
| `Permissions-Policy: geolocation=()` | Refus immédiat, sans fenêtre : « Geolocation has been disabled in this document by permissions policy » |
| `Permissions-Policy: geolocation=(self)` | Position obtenue |
| iframe d'une autre origine, sans attribut `allow` | Refus immédiat |
| iframe d'une autre origine, avec `allow="geolocation"` | Position obtenue |
| Même iframe, page en `geolocation=(self)` | Refus immédiat |

Les iframes d'autres origines sont donc protégées par défaut. L'en-tête verrouille surtout les scripts tiers chargés dans la page elle-même, et documente les capteurs que le service utilise. D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy), une liste vide `()` désactive la fonctionnalité « in top-level and nested browsing contexts ».

**Le code d'un capteur n'est pas son usage.** Chercher `geolocation` dans le JavaScript d'un service ne suffit pas : celui de DiaLog contient tout le code de géolocalisation de MapLibre, sans jamais l'appeler (voir les retours d'expériences). Le contrôle porte sur les appels réels.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**1. Inventorier les capteurs** et, pour chacun, la fonctionnalité qui le justifie, la précision nécessaire et l'alternative sans capteur : géolocalisation, caméra, micro, mais aussi accéléromètre, gyroscope ou orientation.

**2. Ne déclencher le capteur qu'à la demande, avec une alternative.** La saisie reste le parcours principal, la géolocalisation une aide, expliquée avant la fenêtre du navigateur :

```html
<label for="commune">Commune ou code postal</label>
<input id="commune" name="commune" autocomplete="postal-code">
<button type="button" id="me-localiser">Utiliser ma position</button>
<p>Votre position sert uniquement à trouver les lieux les plus proches. Elle n'est pas enregistrée.</p>
```

```js
// afficherAutourDe et proposerSaisie : fonctions du service
document.querySelector('#me-localiser').addEventListener('click', () => {
  navigator.geolocation.getCurrentPosition(afficherAutourDe, proposerSaisie, {
    enableHighAccuracy: false,  // position approchée
    maximumAge: 10 * 60 * 1000, // réutilise une position de moins de 10 minutes
    timeout: 10000,
  });
});
```

D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition), `enableHighAccuracy: true` peut entraîner « increased power consumption (with a GPS chip on a mobile device for example) » ; `false`, la valeur par défaut, laisse l'appareil économiser ses ressources. C'est le « mode dégradé » du RGESN. Pour un suivi continu (`watchPosition`), appeler `clearWatch()` dès qu'il ne sert plus.

**3. Arrêter le capteur dès qu'il ne sert plus.** Retirer la vidéo de la page ne coupe pas la caméra. Testé dans Chromium 155 : deux secondes après le retrait de l'élément `<video>`, la piste est toujours active (`live`) ; seul `stop()` la passe à `ended`.

```js
let flux;
async function ouvrirCamera(video) {
  // Définition et fréquence limitées au besoin
  flux = await navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480, frameRate: 15 } });
  video.srcObject = flux;
}
function fermerCamera(video) {
  flux?.getTracks().forEach((piste) => piste.stop());
  video.srcObject = null;
}
```

Dans le test, la caméra a bien été ouverte en 640 × 480 à 15 images par seconde. Fermer aussi la caméra quand la page est masquée (événement `visibilitychange`, voir le [critère 5.5](../../contenus/5-5_ecoute-seule/)).

**4. Désactiver les capteurs inutilisés** avec l'en-tête `Permissions-Policy`. Pour un service sans capteur, avec Nginx :

```nginx
add_header Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=()" always;
```

Un service qui géolocalise ses utilisateurs remplace `geolocation=()` par `geolocation=(self)`.

**5. Vérifier.** À l'ouverture de chaque page, aucune demande d'autorisation ne doit apparaître. Le panneau **Sensors** des outils de développement de Chrome simule une position ou une orientation. Pour « examiner périodiquement » la durée d'utilisation, mesurer dans le code le temps entre l'ouverture et l'arrêt du capteur.

**6. Documenter** dans la déclaration d'écoconception. Par exemple : « Géolocalisation proposée en option, au clic, en précision standard ; recherche par commune ou code postal toujours disponible. Caméra arrêtée dès la fin de la lecture du document. Autres capteurs désactivés par l'en-tête Permissions-Policy. » Un service sans capteur marque le critère « Non applicable ».

{{% /tab %}}

{{% tab tabName="Applications natives" %}}

Profil(s) métier concerné(s) : `Développeur`

Les mêmes règles valent pour une application Android ou iOS. Le référentiel [Best Practices Mobile](https://github.com/cnumr/best-practices-mobile) du CNUMR les décrit comme des défauts de code : capteur laissé actif quand l'application passe en arrière-plan (« Sensor Leak »), géolocalisation plus précise ou plus fréquente que nécessaire (« Thrifty Geolocation »), événements de capteur livrés un par un (« Sensor Coalesce »). Avec les API actuelles :

| Règle | Android | iOS |
|---|---|---|
| Arrêter le capteur dès qu'il ne sert plus | `SensorManager.unregisterListener()` dans `onPause()`, `removeLocationUpdates()` | `stopUpdatingLocation()`, `stopAccelerometerUpdates()` |
| Précision juste nécessaire | `Priority.PRIORITY_BALANCED_POWER_ACCURACY` du fournisseur de position de Google Play ; permission `ACCESS_COARSE_LOCATION` si une position approximative suffit | `desiredAccuracy = kCLLocationAccuracyHundredMeters` (précision de cent mètres) |
| Une position ponctuelle plutôt qu'un suivi | `getCurrentLocation()` | `requestLocation()` |
| Regrouper ou espacer les mesures | `registerListener(…, maxReportLatencyUs)` | `accelerometerUpdateInterval` ; laisser `pausesLocationUpdatesAutomatically` à `true`, sa valeur par défaut |

**Ces défauts se détectent dans le code.** Les extensions SonarQube [creedengo](https://github.com/green-code-initiative/creedengo-rules-specifications/blob/main/RULES.md) signalent, sur Android et iOS, un capteur ou une localisation jamais arrêtés (règles GCI514 et GCI513) et une précision de géolocalisation trop élevée (GCI524) ; sur Android seulement, des événements non regroupés (GCI500). Les exemples Android du référentiel ont en partie vieilli : l'API `Camera` qu'il cite est dépréciée depuis Android 5.0, au profit de `camera2` ([documentation](https://developer.android.com/reference/android/hardware/Camera)).

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

- le [critère 1.6](../../strategie/1-6_collecte-donnees/) (collecte de données) : une position, une image ou un son sont des données personnelles ;
- le [critère 2.2](../../specifications/2-2_anciens-terminaux/) (anciens terminaux) : un service qui fonctionne sans capteur reste utilisable quand le capteur manque ou ne fonctionne plus ;
- les critères [2.10](../../specifications/2-10_services-tiers/) et [4.4](../../ux-ui/4-4_activation-service-tiers/) (services tiers) : un script tiers ne doit pas déclencher de capteur, ce que l'en-tête `Permissions-Policy` empêche ;
- le [critère 4.1](../../ux-ui/4-1_lecture-automatique/) (lecture automatique) : comme une vidéo, un capteur ne démarre pas sans action de l'utilisateur ;
- le [critère 6.5](../6-5_chargement-ressources/) (ressources utiles) : le code d'un capteur jamais utilisé est aussi une ressource chargée pour rien.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les pages ont été relevées le 30 octobre 2026 dans Chromium 155, en émulation smartphone. Les appels aux API de capteurs (géolocalisation, caméra, micro, orientation, mouvement) ont été surveillés dès le chargement, puis pendant le défilement.

**Aucun des sites des fiches précédentes n'utilise de capteur**, et aucun n'envoie d'en-tête `Permissions-Policy`. Leurs déclarations le disent de deux façons :

- [DiaLog](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf) et [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) marquent le critère **« Non applicable »** : « Pas d'usage de capteurs des terminaux utilisateurs » (DiaLog). Le relevé le confirme pour DiaLog, y compris sur sa carte des restrictions. Son JavaScript contient pourtant `getCurrentPosition` et `watchPosition` : c'est le contrôle de géolocalisation de MapLibre, livré avec la bibliothèque, mais absent de la carte ;
- le [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) le marque **« Validé »** : « Les capteurs des terminaux utilisateurs ne sont pas utilisés. » Le RGESN prévoit « Non applicable » dans ce cas, et un critère non applicable ne compte pas dans le score.

[Prix des carburants](https://www.prix-carburants.gouv.fr/) montre un usage sobre. La recherche se fait « Par commune ou code postal » ; la géolocalisation est une option, que la page ne déclenche pas à l'ouverture. Son en-tête `Permissions-Policy` n'autorise la géolocalisation que pour le site lui-même (`geolocation=(self)`) et désactive les autres capteurs : `accelerometer=()`, `camera=()`, `gyroscope=()`, `magnetometer=()`, `microphone=()`…

[cartes.gouv.fr](https://cartes.gouv.fr/explorer-les-cartes/) et [France services](https://www.france-services.gouv.fr/) proposent aussi la géolocalisation sans la déclencher à l'ouverture, mais sans en-tête `Permissions-Policy`.

{{% /tab %}}

{{< /tabs >}}
