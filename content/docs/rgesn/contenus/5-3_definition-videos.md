---
weight: 300
title: "5.3 - Définition vidéo adaptée au contenu et au terminal"
description: "Critère 5.3 du RGESN : plafonner la définition des vidéos par défaut selon le terminal (480p à 1440p), proposer un mode « sobriété énergétique » mémorisé et documenter ces choix dans la déclaration d'écoconception."
icon: "hd"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il, pour chaque vidéo, une définition adaptée au contenu et au contexte de visualisation ?

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
| **Critère**  | `5.3` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A pour la diffusion de vidéos par multicast/broadcast` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` `Porteur de projet` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Il arrive parfois que le contenu vidéo soit en haute définition alors que le contexte de visualisation n'en a pas besoin, ce qui a pour effet d'augmenter la consommation énergétique du terminal et la quantité de données transférées. Il est donc important d'ajuster précisément la définition vidéo par défaut au terminal utilisé et de donner de l'autonomie à l'utilisateur pour limiter les impacts environnementaux de ses usages en lui permettant de réduire ou d'augmenter la définition de la vidéo.

L'objectif est ainsi de limiter les ressources informatiques et la consommation énergétique associée au visionnage de vidéos.

- Le critère est applicable aux vidéos diffusées en unicast, terme définissant une connexion réseau point à point, c'est-à-dire d'un hôte vers un (seul) autre hôte. C'est le mode de diffusion utilisé sur internet.
- Le critère n'est pas applicable au multicast/broadcast, puisque cela engendrerait une multiplication des flux contreproductive. Les diffusions de type multicast/broadcast concernent uniquement certains modes de diffusion TV (par exemple : TNT, certains flux transmis via le décodeur TV) et désigne une forme de diffusion d'un émetteur unique vers un groupe de récepteurs.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

La mise en œuvre diffère selon le fait que le service numérique est en mesure ou pas de proposer de multiples définitions vidéo pour un même contenu.

Si le service numérique est en mesure de proposer de multiples définitions vidéo pour un même contenu :

- Etablir une définition par défaut ne doit pas dépasser les définitions du mode « qualité standard » défini ci-après.
- Définir un mode « sobriété énergétique » (qui peut également être appelé « économie de données ») qui doit être facilement accessible sur l'interface. Son activation baisse la définition, de manière à ne pas dépasser les définitions du mode « sobriété énergétique » défini ci-après. Le service numérique doit être en mesure de mémoriser ce choix et de l'appliquer pour les prochaines lectures de vidéos.
- De manière optionnelle, proposer un mode « haute qualité », utilisé uniquement sur demande de l'utilisateur (en l'informant le cas échéant que le recours à ce mode « haute qualité » peut avoir un impact sur la quantité de données transmises et la consommation énergétique).

Définition maximum selon le terminal et le mode :

| Terminal | Mode « sobriété énergétique » | Mode « qualité standard » | Mode « haute qualité » |
|---|---:|---:|---:|
| Smartphone | 480p maximum | 720p maximum | Pas de contrainte |
| Tablette | 720p maximum | 1080p maximum | Pas de contrainte |
| PC | 720p maximum | 1080p maximum | Pas de contrainte |
| TV | 1080p maximum | 1440p maximum | Pas de contrainte |
| Type d'écran inconnu | 720p maximum | 1080p maximum | Pas de contrainte |

Si le service numérique unicast qui ne peut pas gérer de multiples définitions vidéo pour un même contenu, choisir la plus faible définition possible sans que cela altère sa compréhension ou l'expérience utilisateur : définition vidéo de 720p pouvant être portée à 1080p pour un contenu difficilement lisible (par exemple : vidéos avec du texte dans une petite police de caractères).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Tester, y compris périodiquement, la lecture des vidéos sur différents terminaux afin de vérifier que ces vidéos en mode « qualité standard » et « sobriété énergétique » ont un format adapté à ces terminaux.

Contrôler la facilité d'accès au mode « sobriété énergétique » (qui peut également être appelé « économie de données ») tel que décrit dans la partie « Mise en œuvre ».

Pour valider ce critère, documenter dans la déclaration d'écoconception les définitions proposées selon les types de terminaux, l'action du mode « sobriété énergétique », son emplacement et sa capacité à mémoriser le choix de l'utilisateur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe et explicitement étiquetée « RGESN 5.3 » : la fiche [**RWEB 0107 — « Adapter les vidéos aux contextes de visualisation »**](https://rweb.greenit.fr/fr/fiches/RWEB_0107-adapter-les-videos-aux-contextes-de-visualisation). Elle recommande de « prévoir plusieurs formats (taille, frame rate, compression audio, etc.) selon le contexte de lecture des vidéos », et précise que l'optimisation « doit être réalisée en dehors du site web, idéalement lors de la postproduction ».

Son exemple chiffre l'écart pour une aide utilisateur de 15 secondes tournée en 1 680 × 1 050 :

| Version | Poids |
|---|---:|
| Non optimisée | 49 Mo |
| Optimisée pour 1 024 × 720 (MPEG-4 / H.264 / AAC) | 3 Mo |
| Optimisée pour 480 × 320 (MPEG-4 / H.264 / AAC) | 1,2 Mo |

La fiche suggère, à défaut, de passer par des plateformes comme YouTube ou Vimeo, qui proposent plusieurs formats par défaut. Ce choix a un revers : la définition par défaut et la mémorisation du mode sobre dépendent alors de la plateforme, et plus du service (voir l'onglet « Critère associé »).

Principe de validation : **aucune** vidéo en 1080p ou plus affichée lorsque le terminal détecté est un smartphone. C'est cohérent avec le RGESN, qui plafonne le mode « qualité standard » à 720p sur smartphone.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.3 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons). Il ajoute un critère de choix que le RGESN ne détaille pas, le **type de contenu** : « pour une conférence, une interview ou un MOOC, 480p est suffisant pour un tutoriel, préférer 720p ». Il rappelle que « la taille 720p offre déjà une excellente [qualité] d'image largement suffisante pour la plupart des usages ».

Les deux logiques se complètent. Le RGESN fixe des **plafonds par terminal** ; le guide aide à descendre **sous** ces plafonds selon ce que montre la vidéo. Une conférence filmée n'a pas besoin du 720p autorisé sur smartphone en mode standard. Un tutoriel qui montre un écran avec du texte peut justifier de monter jusqu'au plafond, ce qui correspond à l'exception du RGESN pour les vidéos avec « du texte dans une petite police de caractères ».

Le guide rappelle aussi de questionner la vidéo elle-même avant sa définition : « Puis-je la faire plus courte ? », ou « proposer uniquement le son pour la musique ou les conférences ».

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) propose « 720p maximum sur smartphone et choix sobre à 420p ». Le RGESN fixe le mode sobre à **480p** sur smartphone : la valeur de 420p est vraisemblablement une coquille.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C, déjà citée aux critères [4.12](../../ux-ui/4-12_impacts-fonctionnalites/) et [5.2](../5-2_compression-images/), demande dans son critère de succès « User-controlled media » de :

- « Ensure users can control playback and resolution. »
- « Provide the option to disable data-intensive media or offer lower-bandwidth alternatives. »

Le W3C pose le principe : l'utilisateur contrôle la définition et dispose d'une alternative plus légère. Le RGESN le chiffre (plafonds par terminal) et ajoute deux exigences : un mode sobre **mémorisé**, et une définition **par défaut** déjà plafonnée, avant tout choix de l'utilisateur.

{{% /tab %}}

{{% tab tabName="Recommandation de l'Arcom" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Le mode « sobriété énergétique » du critère 5.3 fait écho à la [recommandation de l'Arcom du 26 juillet 2023](https://www.arcom.fr/nos-ressources/espace-juridique/textes-juridiques/recommandation-de-larcom-sur-larticle-26-de-la-loi-visant-reduire-lempreinte-environnementale-du-numerique-loi-reen), déjà détaillée au [critère 4.15](../../ux-ui/4-15_controle-usages/). Destinée aux services de télévision, de vidéo à la demande et de partage de vidéos, elle demande :

- une fonctionnalité de type « sobriété énergétique », « aisément accessible (le chemin depuis l'écran d'accueil nécessite un nombre d'actions limité, par exemple en un ou deux « clics ») et permettant d'appliquer automatiquement l'ensemble des réglages les plus respectueux de l'environnement » ;
- parmi les actions à valoriser, « la proposition par défaut sur le service ou la plateforme d'une qualité d'image sobre énergétiquement ».

La recommandation de l'Arcom ne fixe pas de définition maximale. Le RGESN la complète sur ce point avec son tableau de plafonds par terminal. Un service vidéo peut donc appliquer les deux ensemble : l'accès en un ou deux clics de l'Arcom, et les plafonds du RGESN pour définir ce que fait ce mode.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Contributeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) n'a pas de critère dédié à la définition des vidéos, mais la [recommandation n°3 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=3) en situe l'enjeu. Les précisions de son critère [« Est-ce que la durée des vidéos ayant été validées comme nécessaires est optimisée ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-limpact-des-flux-video-est-lie-a-8fef04), en priorité **High**, rappellent que « l'impact des flux vidéo est lié à la durée de la vidéo, à la qualité des images et du son, au nombre de diffusion ».

La définition n'est donc que l'un des leviers. À débit égal, le poids d'une vidéo est proportionnel à sa durée : raccourcir le montage, comme le propose ce critère, réduit le volume transféré sans toucher à la qualité d'image.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

**Cas 1 : une seule définition par vidéo.** C'est le cas le plus courant pour un site qui héberge quelques vidéos. Le RGESN demande alors 720p, ou 1080p si la vidéo contient du texte en petits caractères. Avec ffmpeg :

```bash
ffmpeg -i source.mp4 -vf "scale=-2:720" -c:v libx264 -crf 23 -preset slow \
       -c:a aac -b:a 128k -movflags +faststart video-720p.mp4
```

`scale=-2:720` ramène la hauteur à 720 pixels en conservant les proportions. Pour une vidéo verticale, filmée au smartphone par exemple, la définition se lit sur le plus petit côté, la largeur : utiliser `scale=720:-2`, qui donne du 720×1280. Avec `scale=-2:720`, une vidéo verticale en 1080×1920 sort en 406×720, bien en dessous du 720p visé. Le choix du codec et de son réglage relève du critère suivant, le [5.4](../5-4_compression-videos/) (mode de compression des vidéos).

**Cas 2 : plusieurs définitions, en streaming adaptatif.** La vidéo est découpée en plusieurs définitions (par exemple 480p, 720p et 1080p) au format HLS ou DASH, et le lecteur choisit la définition selon le débit disponible. Par défaut, ce choix ne tient compte que du débit : sur une bonne connexion, un smartphone peut recevoir du 1080p. Il faut donc **plafonner** la définition selon le terminal et le mode choisi. Avec la bibliothèque [hls.js](https://github.com/video-dev/hls.js) :

```js
const PLAFONDS = {
  sobre:    { smartphone: 480, autre: 720 },
  standard: { smartphone: 720, autre: 1080 },
};
const mode = localStorage.getItem('mode-video') ?? 'standard';
const terminal = matchMedia('(max-width: 600px)').matches ? 'smartphone' : 'autre';
const hauteurMax = PLAFONDS[mode][terminal];

const hls = new Hls({ capLevelToPlayerSize: true });
hls.loadSource('/videos/conference/index.m3u8');
hls.attachMedia(document.querySelector('#video'));

hls.on(Hls.Events.MANIFEST_PARSED, () => {
  for (let index = hls.levels.length - 1; index > 0; index--) {
    if (hls.levels[index].height > hauteurMax) hls.removeLevel(index);
  }
});
```

- **`hls.removeLevel()`** retire du lecteur, dès la lecture du manifeste, les définitions qui dépassent le plafond du RGESN. La boucle part de la fin et garde toujours la première définition, la plus légère, pour que le lecteur ait au moins une définition à lire. La [documentation de hls.js](https://github.com/video-dev/hls.js/blob/master/docs/API.md#hlsremovelevellevelindex) indique que cette méthode s'utilise « after the manifest is parsed ».
- **Ne pas plafonner avec `hls.autoLevelCapping`.** Cette propriété semble faite pour cela, mais avec `capLevelToPlayerSize: true`, hls.js la recalcule d'après la taille du lecteur à chaque redimensionnement et écrase la valeur fixée par le script. Testé avec hls.js 1.7.3 : en mode sobre, le lecteur chargeait du 720p sur smartphone et du 1080p sur PC (voir la vérification ci-dessous).
- **`capLevelToPlayerSize: true`** limite en plus la définition, parmi celles qui restent, à la taille réelle du lecteur. Une vidéo affichée en vignette ne charge pas une définition prévue pour le plein écran : sur PC, avec un lecteur de 320 pixels de large, le test charge du 480p.
- **`localStorage`** mémorise le mode choisi, comme l'exige le RGESN (« mémoriser ce choix et l'appliquer pour les prochaines lectures »). Un bouton « Économie de données » visible près du lecteur fait basculer cette valeur ; voir l'exemple de bouton du [critère 4.15](../../ux-ui/4-15_controle-usages/). Les définitions retirées ne reviennent qu'au rechargement du manifeste : après un changement de mode, le bouton recharge la page.
- **Détection du terminal** : la largeur d'écran est une approximation. Elle distingue bien un smartphone d'un PC ; une tablette ou un téléviseur sont rangés ici dans « autre », avec les plafonds du PC, ce qui reste dans les limites du RGESN pour la tablette et en dessous pour la TV.

**Vérifier les fichiers.** Le moyen de test du RGESN demande de vérifier, « y compris périodiquement », que les vidéos ont un format adapté aux terminaux. `ffprobe`, fourni avec FFmpeg, donne la définition, la fréquence d'images et la durée d'une vidéo :

```bash
ffprobe -v error -select_streams v:0 \
        -show_entries stream=width,height,avg_frame_rate:format=duration \
        -of default=nw=1 video-720p.mp4
```

```
width=1280
height=720
avg_frame_rate=30/1
duration=24.000000
```

- La **définition** (`width`, `height`) est l'objet du critère. Elle se lit sur le plus petit côté : une vidéo verticale en 1080×1920 est une vidéo 1080p.
- La **durée**, en secondes, permet de rapporter le poids du fichier à une minute de vidéo. Elle rejoint le critère du GR491 sur la durée des vidéos (onglet « INR - GR491 »).
- La **fréquence d'images** n'entre pas dans le critère 5.3. Elle pèse sur le débit, qui relève du [5.4](../5-4_compression-videos/) : une conférence filmée n'a pas besoin de 60 images par seconde.

Pour un contrôle périodique de toute une médiathèque, cette boucle liste les vidéos au-dessus de 720p, le plafond du cas 1 :

```bash
for f in videos/*.mp4; do
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$f" \
    | awk -F, -v f="$f" '{ d = ($1 < $2) ? $1 : $2; if (d > 720) print f " : " d "p" }'
done
```

Sur un dossier de test qui contient une vidéo en 720p, une en 1080p, une vidéo verticale en 1080×1920 et une vidéo de smartphone avec une indication de rotation, la boucle signale les trois dernières, en `1080p`. Une vidéo qui contient du texte en petits caractères peut légitimement monter à 1080p : la liste sert à vérifier que chaque dépassement est justifié. Dans le cas 2, les définitions proposées se lisent directement dans le manifeste HLS : `grep -o 'RESOLUTION=[0-9x]*' index.m3u8`.

Pour les profils qui n'utilisent pas le terminal, [MediaInfo](https://mediaarea.net/fr/MediaInfo), logiciel libre disponible sous Windows, macOS et Linux, affiche les mêmes informations dans une interface graphique.

**Vérifier la lecture.** Dans le cas 2, les fichiers ne disent pas quelle définition le lecteur charge réellement, alors que c'est ce que le RGESN demande de tester, terminal par terminal. Dans les outils de développement du navigateur, en émulation smartphone puis en taille PC, lancer la vidéo dans chaque mode, attendre une dizaine de secondes que le lecteur se stabilise (il démarre souvent sur la définition la plus basse), puis lire dans la console la définition affichée :

```js
const v = document.querySelector('video');
`${v.videoWidth}×${v.videoHeight}`
```

Dans Chrome, le panneau **Media** des outils de développement donne la même information (« Resolution »).

**Documenter**, comme l'exige le moyen de test, dans la déclaration d'écoconception : le tableau des définitions proposées par terminal et par mode, l'emplacement du bouton « Économie de données », le fait que le choix est mémorisé, et les définitions relevées lors du contrôle de lecture.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Ce critère précise, pour la vidéo, plusieurs critères déjà publiés sur ce site :

- le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) (information sur les fonctionnalités à fort impact) : le RGESN demande d'informer l'utilisateur avant le mode « haute qualité » ;
- le [critère 4.15](../../ux-ui/4-15_controle-usages/) (moyen de contrôle et mode sobre) : le mode « sobriété énergétique » du 5.3 en est la déclinaison pour la vidéo, avec des plafonds chiffrés ;
- le [critère 4.1](../../ux-ui/4-1_lecture-automatique/) (lecture automatique) : la définition la plus sobre reste celle d'une vidéo qui n'est pas lancée sans action de l'utilisateur.

La présence du **porteur de projet** parmi les métiers concernés s'explique par une décision en amont : héberger soi-même ses vidéos ou les intégrer depuis une plateforme. Avec une vidéo intégrée depuis une plateforme tierce, la définition par défaut, le mode sobre et sa mémorisation dépendent de la plateforme. Le service ne peut plus garantir le respect du critère. Ce choix rejoint aussi le [critère 4.4](../../ux-ui/4-4_activation-service-tiers/) (activation des services tiers).

Les deux critères suivants du RGESN complètent celui-ci : le [5.4](../5-4_compression-videos/) (mode de compression des vidéos) et le [5.5](../5-5_ecoute-seule/) (mode « écoute seule »).

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les deux déclarations publiques citées sur ce site marquent ce critère **« Non applicable »**, à juste titre : [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (« Le service numérique n'utilise pas de vidéos. ») et [DiaLog](https://dialog.beta.gouv.fr/ecoconception) (« Pas de vidéo »). Ne pas proposer de vidéo reste la façon la plus sobre de traiter le sujet, à condition que ce soit un choix et non un manque : le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) demande justement de préférer le format le plus léger capable de porter l'information.

Pour un service vidéo grand public, l'[aide de Netflix](https://help.netflix.com/fr/node/87) (consultée le 20 octobre 2026) donne la mesure des écarts entre réglages, par heure de visionnage :

| Réglage | Données utilisées par heure |
|---|---:|
| Faible (« qualité vidéo de base ») | jusqu'à 0,3 Go |
| Moyenne (« qualité vidéo standard ») | jusqu'à 0,7 Go |
| Élevée, haute définition | jusqu'à 3 Go |
| Élevée, ultra haute définition (4K) | jusqu'à 7 Go |

Entre le réglage le plus sobre et la 4K, le volume de données est multiplié par plus de 20. Netflix remplit une partie des exigences du critère : le réglage est **mémorisé** par profil, dans les paramètres de lecture. En revanche, l'option par défaut est « Auto », qui « s'ajuste automatiquement pour offrir la meilleure qualité possible » selon la connexion. C'est l'inverse de la logique du RGESN, qui plafonne la définition par défaut, quelle que soit la qualité de la connexion.

{{% /tab %}}

{{< /tabs >}}
