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

L'étude citée dans l'objectif du critère (le RGESN écrit « Priest ») est l'article de Chris Preist, Paul Shabajee et Daniel Schien, [**« Evaluating Sustainable Interaction Design of Digital Services: The Case of YouTube »**](https://research-information.bris.ac.uk/en/publications/evaluating-sustainable-interaction-design-of-digital-services-the/), présenté à la conférence CHI 2019, où il a reçu une [mention honorable](https://chi2019.acm.org/2019/03/15/chi-2019-best-papers-honourable-mentions/). Selon son résumé et le [communiqué de l'université de Bristol](https://www.sciencedaily.com/releases/2019/05/190506080833.htm) :

- les émissions liées à la diffusion de YouTube sont estimées à environ **10 MtCO2e** pour l'année 2016, « approximately that of a city the size of Glasgow » ;
- ne plus envoyer d'images aux utilisateurs qui se servent de YouTube seulement pour écouter permettrait d'économiser **100 à 500 ktCO2e** par an (environ 300 ktCO2e dans le résumé), soit **1 à 5 %** de ce total ;
- pour un service de ce type, « most of the energy is used in the network, particularly the mobile network ».

Deux précisions pour lire ces chiffres. D'abord, il s'agit d'une **estimation**, pas de la mesure d'un bouton existant : les auteurs ont remplacé les données d'usage de YouTube par des « aggregate estimates from publicly available sources ». Ensuite, l'étude chiffre le premier objectif du critère, le trafic évité. Le second objectif, l'écran éteint, s'y ajoute côté terminal.

L'ordre de grandeur suffit à justifier le critère pour un service vidéo : l'image représente l'essentiel du volume transféré (onze fois plus que le son sur l'entretien Framatube cité dans les retours d'expériences), et une partie de ce volume n'est regardée par personne.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.5 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons), déjà présentée aux critères [5.3](../5-3_definition-videos/) et [5.4](../5-4_compression-videos/) : « Proposer un mode « écoute seule » pour les vidéos permet de valider le critère 5.5 ».

La section présente ce critère après une série de questions, dont l'une va plus loin : « Est-qu'on peut faire autrement ? Par exemple, proposer uniquement le son pour la musique ou les conférences ». Pour une conférence filmée en plan fixe, la version audio n'est pas seulement un mode de secours : elle peut être le format principal, la vidéo devenant l'option. C'est le raisonnement du [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) (choix du format le plus sobre).

La même section rappelle l'inverse pour l'accessibilité : « 85% des vidéos Facebook sont regardées sans le son ». Le mode « écoute seule » sert ceux qui écoutent sans regarder ; les sous-titres et la transcription servent ceux qui regardent ou lisent sans écouter.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`

La fiche [**« Use sustainable JavaScript and APIs »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-javascript-and-apis) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) comporte un critère de succès « Energy-relevant APIs » : « Leverage JavaScript APIs, such as Compression Streams, Page Visibility, or Vibration, when they help reduce energy use or improve efficiency. »

L'API Page Visibility est précisément celle qui permet de détecter qu'une vidéo n'est plus affichée. Mais l'exemple du W3C **met en pause** le média quand la page est masquée (`if (document.hidden) { audio.pause(); }`). Le RGESN demande autre chose pour les vidéos : **continuer le son et arrêter l'image**. La pause convient à un média que personne n'écoute en arrière-plan ; pour une vidéo écoutée pendant une autre activité, elle supprimerait l'usage au lieu de l'alléger.

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use), citée au [critère 5.3](../5-3_definition-videos/), demande aussi, dans son critère « User-controlled media », de « Provide the option to disable data-intensive media or offer lower-bandwidth alternatives ». La version audio d'une vidéo est cette alternative.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) n'a pas de critère sur le mode « écoute seule ». Dans la [recommandation n°3 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=3), citée aux critères 5.3 et 5.4, le critère [« Est-ce que le son de la vidéo peut-être restitué sous forme texte ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-lacces-au-son-est-difficile-ou-impossible-236851), en priorité **High**, suit le mouvement inverse : « L'accès au son est difficile ou impossible pour certains publics. La fourniture d'un texte en support ou remplacement du son est indispensable. » Son test : « Avez-vous une piste de sous-titre pour chaque vidéo ? »

Les deux démarches se complètent. Le mode « écoute seule » retire l'image pour ceux qui écoutent ; la transcription donne accès au contenu sans le son, et c'est la version la plus légère des trois. Pour une conférence, proposer la vidéo, le son seul et la transcription couvre les trois usages.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche étiquetée « RGESN 5.5 ». La fiche [**RWEB 0106 — « Éviter la lecture et le chargement automatique des vidéos et des sons »**](https://rweb.greenit.fr/fr/fiches/RWEB_0106-eviter-la-lecture-et-le-chargement-automatique-des-videos-et-des-sons), rattachée au [critère 4.1](../../ux-ui/4-1_lecture-automatique/), répond pourtant à une condition du moyen de test : la version audio proposée sous une vidéo hébergée par un tiers doit l'être « sans préchargement de la vidéo associée ».

La fiche rappelle que « même en n'activant pas l'autoplay, certaines parties de la vidéo ou du fichier audio peuvent être téléchargées », et demande l'attribut `preload="none"` sur les balises `<video>` et `<audio>`. Son principe de validation : **aucun** élément `<video>` ou `<audio>` sans cet attribut.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

**1. Ce que le navigateur ne fait pas seul.** Depuis Chrome 62, le navigateur désactive la piste vidéo d'une vidéo lue dans un onglet en arrière-plan, mais seulement pour les vidéos diffusées avec Media Source Extensions (MSE) ([Chrome for Developers](https://developer.chrome.com/blog/media-updates-in-chrome-61)). Il économise ainsi le décodage, mais pas le téléchargement. Pour un fichier vidéo classique, le test de l'étape 4 le confirme : sans intervention du service, Chromium continue de télécharger la vidéo en arrière-plan. Dans un fichier MP4 ou WebM, l'image et le son sont entrelacés : impossible de ne télécharger que le son. Il faut donc une **version audio séparée**.

**2. Produire la version audio**, sans réencodage, la piste son est reprise telle quelle :

```bash
ffmpeg -i conference-720p.webm -vn -c:a copy conference-audio.webm
ffmpeg -i conference-720p.mp4 -vn -c:a copy conference-audio.m4a
```

`-vn` supprime la piste vidéo et `-c:a copy` copie la piste son sans la modifier. En mode « écoute seule », cette piste est tout ce qui est transféré : son réglage (mono pour la parole, voir le critère 5.4) pèse alors directement sur le volume.

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

- **`visibilitychange`** se déclenche quand l'utilisateur change d'onglet, réduit le navigateur, passe à une autre application sur mobile ou éteint l'écran : la page est alors masquée « because the device's screen is off » ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)). Ce sont les cas cités par le RGESN.
- **Changer `src`** sur le lecteur remplace les éléments `<source>` et interrompt le téléchargement en cours. La position est conservée : affectée avant le chargement, `currentTime` devient la position de départ du nouveau fichier.
- **Le même élément `<video>`** sert pour les deux versions. Le navigateur l'a déjà autorisé à jouer du son au premier clic de l'utilisateur ; un nouvel élément `<audio>` lancé en arrière-plan risquerait d'être bloqué par les règles de lecture automatique.
- **L'image d'aperçu** (`poster`) reste affichée en mode « écoute seule » : un `<video>` dont le fichier n'a pas de piste vidéo affiche son image d'aperçu.
- **Le retour à la vidéo** n'est automatique que si le passage au son l'était. Si l'utilisateur a choisi « Écoute seule », le service respecte son choix, même quand il revient sur l'onglet.

**4. Vérifier le comportement.** Ce code a été testé le 20 octobre 2026 dans Chromium 155, avec la règle de lecture automatique la plus stricte (son autorisé seulement après un geste de l'utilisateur) et une vidéo de test de 60 secondes (720p, 6,6 Mbit/s) servie à 8 Mbit/s au plus. On lance la lecture d'un clic, puis on passe 10 secondes sur un autre onglet :

| Pendant les 10 s en arrière-plan | Sans bascule | Avec bascule |
|---|---:|---:|
| Vidéo téléchargée | 10,2 Mo | 0 (requête interrompue 0,1 s après le changement d'onglet) |
| Son téléchargé | inclus dans la vidéo | 0,28 Mo |
| Lecture | continue | continue, sans nouveau clic, à la même position |

Au retour sur l'onglet, la vidéo reprend à la bonne position, mais après 3 à 4 secondes de chargement sur ce serveur bridé : le lecteur doit retélécharger l'image depuis l'image clé précédente. Le comportement reste à vérifier sur Safari et Firefox, et sur de vrais smartphones écran éteint. Pour contrôler soi-même, ouvrir l'onglet **Réseau** des outils de développement, filtre **Media**, lancer la vidéo puis changer d'onglet : la requête vers le fichier vidéo doit s'arrêter, remplacée par celle du fichier audio.

**5. En streaming adaptatif (HLS, DASH)**, la solution passe par un flux audio **séparé** des flux vidéo dans le manifeste. Le lecteur peut alors cesser de télécharger les segments vidéo et ne garder que le son. C'est ce que fait PeerTube quand l'option correspondante est activée (voir les retours d'expériences).

**6. Avec une plateforme tierce sans mode « écoute seule »**, le moyen de test accepte un enregistrement audio sous chaque vidéo, sans préchargement de la vidéo associée :

```html
<!-- Lecteur tiers chargé seulement au clic : voir le critère 4.4 -->
<p>Écouter seulement :</p>
<audio controls preload="none" src="conference-audio.m4a"></audio>
```

Pour que la vidéo tierce ne soit pas préchargée, son lecteur ne doit être chargé qu'au clic de l'utilisateur (façade), comme le demande le [critère 4.4](../../ux-ui/4-4_activation-service-tiers/).

**7. Documenter** dans la déclaration d'écoconception, comme l'exige le moyen de test. Par exemple : « Un bouton « Écoute seule », sous chaque lecteur vidéo, remplace la vidéo par sa piste son (Opus, 24 kbit/s mono). Le passage en écoute seule est automatique quand l'onglet est masqué ou l'écran éteint ; la vidéo reprend au retour sur l'onglet. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Ce critère prolonge les deux précédents, déjà publiés sur ce site :

- le [critère 5.3](../5-3_definition-videos/) (définition adaptée) : le mode « écoute seule » en est le cas extrême, une définition nulle. PeerTube nomme d'ailleurs sa version audio « 0p » dans sa configuration ;
- le [critère 5.4](../5-4_compression-videos/) (compression des vidéos) : en mode « écoute seule », la piste son est tout ce qui reste. Son encodage, mono pour la parole, devient décisif. Le RGESN renvoie pour cela au [critère 5.6](../5-6_compression-audio/) (compression des contenus audio).

Plusieurs critères UX/UI, déjà publiés, entrent aussi en jeu :

- le [critère 4.15](../../ux-ui/4-15_controle-usages/) (moyen de contrôle et mode sobre) : le bouton « Écoute seule » est l'un de ces moyens de contrôle ;
- le [critère 4.4](../../ux-ui/4-4_activation-service-tiers/) (activation des services tiers) et le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers), qui demande qu'une vidéo tierce valide notamment le 5.5 ;
- le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) (choix du format le plus sobre) : quand l'image n'apporte rien, la version audio peut devenir le format principal.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque les critères 5.3, 5.4 et 5.5 **« Non-applicable »** : « Pas de vidéo ».

[PeerTube](https://joinpeertube.org/), le logiciel libre de diffusion vidéo de Framasoft, intègre le mode « écoute seule » depuis sa version 6.3.0. D'après son [journal des modifications](https://github.com/Chocobozzz/PeerTube/blob/develop/CHANGELOG.md), quand l'administrateur sépare les flux audio et vidéo, « an "Audio only" resolution is available in the HLS player ». L'option est désactivée par défaut (`split_audio_and_video: false` dans le [fichier de configuration](https://github.com/Chocobozzz/PeerTube/blob/develop/config/production.yaml.example)). D'après l'API publique de quatre instances en version 8.3.1, constaté le 20 octobre 2026 :

| Instance | Flux audio séparé (« Audio only » dans le lecteur) | Résolution audio seule « 0p » | Exemple |
|---|---|---|---|
| [peertube.fr](https://peertube.fr/) | Oui | Non | Vidéo de 6 min : 50,7 Mo d'image en 720p, 5,9 Mo de son |
| [Framatube](https://framatube.org/) | Non | Oui | Entretien de 56 min : 595 Mo en 720p, 55 Mo en audio seul |
| Deux instances d'[apps.education.fr](https://apps.education.fr/) | Non | Non | — |

Sur Framatube, la version audio existe mais le manifeste HLS de la vidéo ne la déclare pas : le lecteur ne peut donc pas la proposer. Sur cet entretien d'une heure, le mode « écoute seule » diviserait pourtant par onze le volume transféré par rapport au 720p. Sur peertube.fr, le manifeste déclare le son comme un flux séparé, que toutes les définitions partagent : c'est ce qui permet au lecteur d'arrêter l'image sans couper le son.

{{% /tab %}}

{{< /tabs >}}
