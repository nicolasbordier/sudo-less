---
weight: 500
title: "5.5 - Mode « écoute seule » pour les vidéos"
description: "Critère 5.5 du RGESN : proposer un mode « écoute seule » qui ne télécharge plus que le son, le déclencher automatiquement quand la vidéo n'est plus affichée et documenter son fonctionnement."
icon: "headphones"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il un mode « écoute seule » pour ses vidéos ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Contenus` |
| **Critère**  | `5.5` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique ne propose pas de contenu vidéo avec piste audio` |
| **Métiers concernés** | `Développeur` `Responsable IT` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Une partie significative du trafic vidéo sur internet est constitué de vidéos qui sont écoutées (source : étude de Chris Priest, de l'université de Bristol au Royaume-Uni sur l'usage d'un bouton « audio-seul » sur l'application YouTube de mai 2019) :

- Vidéos musicales utilisées en fond sonore ;
- Podcasts filmés écoutés et non visionnés ;
- Émissions écoutées pendant une autre activité.

Le premier objectif est de réduire le trafic en permettant à l'utilisateur de couper son flux vidéo via une option « écoute seule », « audio only », ou « zéro pixel » afin de réduire le trafic généré par la vidéo qui n'est pas regardée.

Le second objectif est de réduire la consommation d'énergie des terminaux en leur permettant d'activer l'écoute de la piste audio d'une vidéo lorsque l'écran est éteint.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Proposer une option permettant à l'utilisateur de basculer en mode « écoute seule » simplement sur le lecteur vidéo (et si possible de repasser en mode vidéo, s'il souhaite regarder de nouveau la vidéo). En mode « écoute seule », le flux vidéo n'est plus téléchargé par le lecteur vidéo, qui se limite au flux audio.

Basculer automatiquement les vidéos en « écoute seule » quand le service numérique détecte que le média n'est plus visualisé ou que l'utilisateur éteint son écran. Par exemple :

- Utilisation de service numérique sur smartphone / tablette / équipement connecté (application native ou via un navigateur web) : le fait d'appuyer sur le bouton de mise en veille doit basculer la vidéo en mode audio seul, de façon à permettre à l'utilisateur de continuer à écouter la vidéo en limitant fortement la consommation d'énergie, l'écran étant éteint et seules les données nécessaires à l'audio étant transférées.
- Si le service numérique est utilisé dans un navigateur web, le fait de passer dans un autre onglet que celui de la vidéo doit déclencher le mode « écoute seule ». Quand l'utilisateur affiche de nouveau l'onglet de la vidéo, celle-ci peut rebasculer en mode vidéo.

Dans le cas d'un service numérique qui utilise une plateforme de vidéo ne proposant pas de mode « écoute seule », une alternative est de proposer sous la vidéo un lien vers la version audio, afin de permettre à l'utilisateur de choisir son mode de diffusion.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si :

- Le service propose un mode « écoute seule » sur les vidéos, activable à la demande de l'utilisateur et qui s'enclenche lorsqu'il peut être détecté que la vidéo n'est pas affichée sur le terminal (par exemple : changement d'onglet dans un navigateur ou d'application sur un terminal, fermeture d'écran, etc.). Dans l'éventualité où les vidéos du service sont déjà hébergées par un service tiers qui ne propose pas ce mode « écoute seule », il est possible de valider le critère en proposant un enregistrement « écoute seule » sous chaque vidéo (sans préchargement de la vidéo associée).
- Sont documentés dans la déclaration d'écoconception du service numérique l'emplacement et le fonctionnement du mode « écoute seule ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="D'où vient l'étude citée ?" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable IT`

L'étude citée dans l'objectif du critère (le RGESN écrit « Priest ») est l'article de Chris Preist, Paul Shabajee et Daniel Schien, [**« Evaluating Sustainable Interaction Design of Digital Services: The Case of YouTube »**](https://research-information.bris.ac.uk/en/publications/evaluating-sustainable-interaction-design-of-digital-services-the/) (CHI 2019). Selon son résumé et le [communiqué de l'université de Bristol](https://www.sciencedaily.com/releases/2019/05/190506080833.htm) :

- la diffusion de YouTube représentait environ **10 MtCO2e** en 2016, « approximately that of a city the size of Glasgow » ;
- ne plus envoyer d'images à ceux qui ne font qu'écouter économiserait **100 à 500 ktCO2e** par an, soit **1 à 5 %** de ce total ;
- « most of the energy is used in the network, particularly the mobile network ».

C'est une **estimation**, fondée sur des données publiques, pas la mesure d'un bouton existant. Elle chiffre le trafic évité ; l'écran éteint, second objectif du critère, s'y ajoute côté terminal.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.5 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons). Il va plus loin : « proposer uniquement le son pour la musique ou les conférences ». Pour une conférence filmée en plan fixe, la version audio peut devenir le format principal, la vidéo l'option (voir le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/)).

Il rappelle aussi l'inverse : « 85% des vidéos Facebook sont regardées sans le son ». Les sous-titres et la transcription servent ceux qui regardent ou lisent sans écouter.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`

La fiche [**« Use sustainable JavaScript and APIs »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-javascript-and-apis) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) recommande l'API Page Visibility, celle qui détecte qu'une vidéo n'est plus affichée. Mais son exemple **met en pause** le média quand la page est masquée. Le RGESN demande autre chose : **continuer le son et arrêter l'image**. Pour une vidéo écoutée pendant une autre activité, la pause supprimerait l'usage au lieu de l'alléger.

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) demande d'« offer lower-bandwidth alternatives » : la version audio d'une vidéo en est une.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) n'a pas de critère sur le mode « écoute seule », mais suit le mouvement inverse avec [« Est-ce que le son de la vidéo peut-être restitué sous forme texte ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-lacces-au-son-est-difficile-ou-impossible-236851), en priorité **High**. La transcription donne accès au contenu sans le son, et c'est la plus légère des versions. Pour une conférence, proposer la vidéo, le son seul et la transcription couvre les trois usages.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche étiquetée « RGESN 5.5 ». [**RWEB 0106 — « Éviter la lecture et le chargement automatique des vidéos et des sons »**](https://rweb.greenit.fr/fr/fiches/RWEB_0106-eviter-la-lecture-et-le-chargement-automatique-des-videos-et-des-sons) répond pourtant à une condition du moyen de test, une version audio « sans préchargement de la vidéo associée » : elle demande `preload="none"` sur **toutes** les balises `<video>` et `<audio>`.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

**1. Ce que le navigateur ne fait pas seul.** Chrome cesse de décoder l'image d'une vidéo en arrière-plan, mais seulement en streaming MSE, et sans arrêter le téléchargement ([Chrome for Developers](https://developer.chrome.com/blog/media-updates-in-chrome-61)). Pour un fichier classique, le test de l'étape 4 le confirme : Chromium continue de télécharger la vidéo. Comme l'image et le son sont entrelacés dans le fichier, il faut une **version audio séparée**.

**2. Produire la version audio**, sans réencodage, la piste son est reprise telle quelle :

```bash
ffmpeg -i conference-720p.webm -vn -c:a copy conference-audio.webm
ffmpeg -i conference-720p.mp4 -vn -c:a copy conference-audio.m4a
```

`-vn` supprime la piste vidéo et `-c:a copy` copie la piste son sans la modifier.

**3. Basculer entre vidéo et son dans le même lecteur**, à la demande ou quand la page n'est plus affichée :

```html
<video id="lecteur" controls preload="none" width="1280" height="720" poster="conference.webp">
  <source src="conference-720p.webm" type='video/webm; codecs="av01.0.05M.08, opus"'>
  <source src="conference-720p.mp4" type='video/mp4; codecs="avc1.64001F, mp4a.40.2"'>
</video>
<button type="button" id="ecoute-seule" aria-pressed="false">Écoute seule</button>
```

```js
const lecteur = document.querySelector('#lecteur');
const bouton = document.querySelector('#ecoute-seule');
const VERSIONS = {
  video: [
    { src: 'conference-720p.webm', type: 'video/webm; codecs="av01.0.05M.08, opus"' },
    { src: 'conference-720p.mp4', type: 'video/mp4; codecs="avc1.64001F, mp4a.40.2"' },
  ],
  audio: [
    { src: 'conference-audio.webm', type: 'audio/webm; codecs="opus"' },
    { src: 'conference-audio.m4a', type: 'audio/mp4; codecs="mp4a.40.2"' },
  ],
};
let ecouteChoisie = false; // mode « écoute seule » demandé par l'utilisateur
let ecouteAuto = false;    // mode « écoute seule » déclenché par la mise en arrière-plan

function charger(type) {
  const version = VERSIONS[type].find((v) => lecteur.canPlayType(v.type));
  const position = lecteur.currentTime;
  const enLecture = !lecteur.paused;
  lecteur.src = version.src;      // interrompt le téléchargement du fichier précédent
  lecteur.currentTime = position; // reprend au même endroit
  if (enLecture) lecteur.play().catch(() => {});
}

bouton.addEventListener('click', () => {
  ecouteChoisie = !ecouteChoisie;
  ecouteAuto = false;
  bouton.setAttribute('aria-pressed', ecouteChoisie);
  charger(ecouteChoisie ? 'audio' : 'video');
});

document.addEventListener('visibilitychange', () => {
  if (document.hidden && !ecouteChoisie && !lecteur.paused) {
    ecouteAuto = true;
    charger('audio');
  } else if (!document.hidden && ecouteAuto) {
    ecouteAuto = false;
    charger('video');
  }
});
```

- **`visibilitychange`** se déclenche quand l'utilisateur change d'onglet, passe à une autre application ou éteint l'écran ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)) : ce sont les cas cités par le RGESN.
- **Changer `src`** interrompt le téléchargement en cours ; `currentTime` conserve la position.
- **Le même élément `<video>`** sert pour les deux versions : déjà autorisé à jouer du son, il ne sera pas bloqué par les règles de lecture automatique. Son image d'aperçu reste affichée.
- **Le retour à la vidéo** n'est automatique que si le passage au son l'était : un choix explicite de l'utilisateur est respecté.

**4. Vérifier le comportement.** Ce code a été testé le 20 octobre 2026 dans Chromium 155, avec la règle de lecture automatique la plus stricte (son autorisé seulement après un geste de l'utilisateur) et une vidéo de test de 60 secondes (720p, 6,6 Mbit/s) servie à 8 Mbit/s au plus. On lance la lecture d'un clic, puis on passe 10 secondes sur un autre onglet :

| Pendant les 10 s en arrière-plan | Sans bascule | Avec bascule |
|---|---:|---:|
| Vidéo téléchargée | 10,2 Mo | 0 (requête interrompue 0,1 s après le changement d'onglet) |
| Son téléchargé | inclus dans la vidéo | 0,28 Mo |
| Lecture | continue | continue, sans nouveau clic, à la même position |

Au retour, la vidéo reprend à la bonne position après 3 à 4 secondes de chargement. Le comportement reste à vérifier sur Safari, Firefox et de vrais smartphones écran éteint. Pour contrôler soi-même : onglet **Réseau**, filtre **Media**, lancer la vidéo puis changer d'onglet. La requête vers la vidéo doit s'arrêter, remplacée par celle du fichier audio.

**5. En streaming adaptatif (HLS, DASH)**, la solution passe par un flux audio **séparé** des flux vidéo dans le manifeste. Le lecteur peut alors cesser de télécharger les segments vidéo et ne garder que le son. C'est ce que fait PeerTube quand l'option correspondante est activée (voir les retours d'expériences).

**6. Avec une plateforme tierce sans mode « écoute seule »**, le moyen de test accepte un enregistrement audio sous chaque vidéo, sans préchargement de la vidéo associée :

```html
<!-- Lecteur tiers chargé seulement au clic : voir le critère 4.4 -->
<p>Écouter seulement :</p>
<audio controls preload="none" src="conference-audio.m4a"></audio>
```

Le lecteur tiers ne doit alors être chargé qu'au clic (voir le [critère 4.4](../../ux-ui/4-4_activation-service-tiers/)).

**7. Documenter** dans la déclaration d'écoconception, comme l'exige le moyen de test. Par exemple : « Un bouton « Écoute seule », sous chaque lecteur vidéo, remplace la vidéo par sa piste son (Opus, 24 kbit/s mono). Le passage en écoute seule est automatique quand l'onglet est masqué ou l'écran éteint ; la vidéo reprend au retour sur l'onglet. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Ce critère prolonge les deux précédents :

- le [critère 5.3](../5-3_definition-videos/) (définition) : l'écoute seule en est le cas extrême, une définition nulle, que PeerTube nomme d'ailleurs « 0p » ;
- le [critère 5.4](../5-4_compression-videos/) (compression) : la piste son est alors tout ce qui reste, et son encodage devient décisif (voir aussi le [critère 5.6](../5-6_compression-audio/)).

Côté UX/UI, le bouton « Écoute seule » est l'un des moyens de contrôle du [critère 4.15](../../ux-ui/4-15_controle-usages/). Une vidéo tierce doit aussi valider le 5.5 (critères [2.10](../../specifications/2-10_services-tiers/) et [4.4](../../ux-ui/4-4_activation-service-tiers/)).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque les critères [5.3](../5-3_definition-videos/), [5.4](../5-4_compression-videos/) et 5.5 **« Non-applicable »** : « Pas de vidéo ».

[PeerTube](https://joinpeertube.org/), le logiciel libre de diffusion vidéo de Framasoft, intègre le mode « écoute seule » depuis sa version 6.3.0. D'après son [journal des modifications](https://github.com/Chocobozzz/PeerTube/blob/develop/CHANGELOG.md), quand l'administrateur sépare les flux audio et vidéo, « an "Audio only" resolution is available in the HLS player ». L'option est désactivée par défaut (`split_audio_and_video: false` dans le [fichier de configuration](https://github.com/Chocobozzz/PeerTube/blob/develop/config/production.yaml.example)). D'après l'API publique de quatre instances en version 8.3.1, constaté le 20 octobre 2026 :

| Instance | Flux audio séparé (« Audio only » dans le lecteur) | Résolution audio seule « 0p » | Exemple |
|---|---|---|---|
| [peertube.fr](https://peertube.fr/) | Oui | Non | Vidéo de 6 min : 50,7 Mo d'image en 720p, 5,9 Mo de son |
| [Framatube](https://framatube.org/) | Non | Oui | Entretien de 56 min : 595 Mo en 720p, 55 Mo en audio seul |
| Deux instances d'[apps.education.fr](https://apps.education.fr/) | Non | Non | — |

Sur Framatube, la version audio existe, mais le manifeste HLS ne la déclare pas : le lecteur ne peut pas la proposer, alors qu'elle diviserait par onze le volume transféré. Sur peertube.fr, le son est un flux séparé, partagé par toutes les définitions : le lecteur peut arrêter l'image sans couper le son.

{{% /tab %}}

{{< /tabs >}}
