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
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une fiche explicitement étiquetée « RGESN 5.3 » : [**RWEB 0107 — « Adapter les vidéos aux contextes de visualisation »**](https://rweb.greenit.fr/fr/fiches/RWEB_0107-adapter-les-videos-aux-contextes-de-visualisation). Elle recommande de « prévoir plusieurs formats (taille, frame rate, compression audio, etc.) selon le contexte de lecture des vidéos », optimisés « idéalement lors de la postproduction ». Son exemple, une aide utilisateur de 15 secondes tournée en 1 680 × 1 050 :

| Version | Poids |
|---|---:|
| Non optimisée | 49 Mo |
| Optimisée pour 1 024 × 720 (MPEG-4 / H.264 / AAC) | 3 Mo |
| Optimisée pour 480 × 320 (MPEG-4 / H.264 / AAC) | 1,2 Mo |

Son principe de validation : **aucune** vidéo en 1080p ou plus sur smartphone, cohérent avec le plafond de 720p du RGESN. La fiche suggère, à défaut, YouTube ou Vimeo ; la définition par défaut et la mémorisation du mode sobre dépendent alors de la plateforme (voir l'onglet « Critère associé »).

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Porteur de projet`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.3 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons). Il ajoute un critère de choix, le **type de contenu** : « pour une conférence, une interview ou un MOOC, 480p est suffisant pour un tutoriel, préférer 720p ».

Les deux logiques se complètent : le RGESN fixe des **plafonds par terminal**, le guide aide à descendre **sous** ces plafonds selon ce que montre la vidéo. Il invite aussi à questionner la vidéo elle-même : « Puis-je la faire plus courte ? », ou « proposer uniquement le son pour la musique ou les conférences ».

Sa ressource [« RGESN, ce que doivent faire les designers »](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) propose un « choix sobre à 420p » : le RGESN dit **480p**, c'est vraisemblablement une coquille.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C demande : « Ensure users can control playback and resolution » et « Provide the option to disable data-intensive media or offer lower-bandwidth alternatives ». Le RGESN va plus loin : des plafonds chiffrés, un mode sobre **mémorisé** et une définition **par défaut** déjà plafonnée.

{{% /tab %}}

{{% tab tabName="Recommandation de l'Arcom" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

La [recommandation de l'Arcom du 26 juillet 2023](https://www.arcom.fr/nos-ressources/espace-juridique/textes-juridiques/recommandation-de-larcom-sur-larticle-26-de-la-loi-visant-reduire-lempreinte-environnementale-du-numerique-loi-reen), détaillée au [critère 4.15](../../ux-ui/4-15_controle-usages/), demande aux services vidéo :

- une fonctionnalité « sobriété énergétique » « aisément accessible », par exemple « en un ou deux « clics » », qui applique « automatiquement l'ensemble des réglages les plus respectueux de l'environnement » ;
- de valoriser « la proposition par défaut […] d'une qualité d'image sobre énergétiquement ».

L'Arcom ne fixe pas de définition maximale : le RGESN la complète avec ses plafonds par terminal.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Contributeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) rappelle, dans le critère [« Est-ce que la durée des vidéos ayant été validées comme nécessaires est optimisée ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-limpact-des-flux-video-est-lie-a-8fef04) (priorité **High**), que « l'impact des flux vidéo est lié à la durée de la vidéo, à la qualité des images et du son, au nombre de diffusion ». La définition n'est qu'un levier : raccourcir le montage réduit aussi le volume transféré.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

**Cas 1 : une seule définition par vidéo**, le cas le plus courant. Le RGESN demande alors 720p, ou 1080p si la vidéo contient du texte en petits caractères. Avec ffmpeg :

```bash
ffmpeg -i source.mp4 -vf "scale=-2:720" -c:v libx264 -crf 23 -preset slow \
       -c:a aac -b:a 128k -movflags +faststart video-720p.mp4
```

`scale=-2:720` ramène la hauteur à 720 pixels en conservant les proportions. Pour une vidéo verticale, la définition se lit sur la largeur : utiliser `scale=720:-2`. Le choix du codec relève du critère [5.4](../5-4_compression-videos/).

**Cas 2 : plusieurs définitions, en streaming adaptatif** (HLS ou DASH). Le lecteur choisit la définition selon le débit : sur une bonne connexion, un smartphone peut recevoir du 1080p. Il faut donc **plafonner** la définition selon le terminal et le mode choisi. Avec [hls.js](https://github.com/video-dev/hls.js) :

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

- **`hls.removeLevel()`** retire, dès la lecture du manifeste, les définitions qui dépassent le plafond, en gardant toujours la plus légère.
- **Ne pas plafonner avec `hls.autoLevelCapping`** : avec `capLevelToPlayerSize: true`, hls.js le recalcule à chaque redimensionnement. Testé avec hls.js 1.7.3, le mode sobre chargeait alors du 720p sur smartphone.
- **`capLevelToPlayerSize: true`** limite en plus la définition à la taille réelle du lecteur : une vignette ne charge pas une définition de plein écran.
- **`localStorage`** mémorise le mode choisi, comme l'exige le RGESN. Un bouton « Économie de données » près du lecteur fait basculer cette valeur (voir l'exemple du [critère 4.15](../../ux-ui/4-15_controle-usages/)).

**Vérifier les fichiers**, « y compris périodiquement », comme le demande le moyen de test. `ffprobe`, fourni avec FFmpeg, donne la définition, la fréquence d'images et la durée :

```bash
ffprobe -v error -select_streams v:0 \
        -show_entries stream=width,height,avg_frame_rate:format=duration \
        -of default=nw=1 video-720p.mp4
```

Pour toute une médiathèque, cette boucle liste les vidéos au-dessus de 720p, en lisant la définition sur le plus petit côté :

```bash
for f in videos/*.mp4; do
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$f" \
    | awk -F, -v f="$f" '{ d = ($1 < $2) ? $1 : $2; if (d > 720) print f " : " d "p" }'
done
```

Chaque dépassement doit être justifié, par exemple par du texte en petits caractères. Sans terminal, [MediaInfo](https://mediaarea.net/fr/MediaInfo) affiche les mêmes informations.

**Vérifier la lecture.** Dans le cas 2, seule la lecture montre la définition réellement chargée. En émulation smartphone puis en taille PC, lancer la vidéo dans chaque mode, attendre une dizaine de secondes, puis lire la définition dans la console :

```js
const v = document.querySelector('video');
`${v.videoWidth}×${v.videoHeight}`
```

**Documenter** dans la déclaration d'écoconception : les définitions par terminal et par mode, l'emplacement du bouton « Économie de données », la mémorisation du choix et les définitions relevées.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Ce critère précise, pour la vidéo :

- le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) : informer l'utilisateur avant le mode « haute qualité » ;
- le [critère 4.15](../../ux-ui/4-15_controle-usages/) : le mode « sobriété énergétique » en est la déclinaison pour la vidéo ;
- le [critère 4.1](../../ux-ui/4-1_lecture-automatique/) : pas de lecture sans action de l'utilisateur.

Le **porteur de projet** décide en amont d'héberger ses vidéos ou de les intégrer depuis une plateforme. Dans le second cas, la définition par défaut et le mode sobre dépendent de la plateforme, et le service ne peut plus garantir le critère (voir aussi le [critère 4.4](../../ux-ui/4-4_activation-service-tiers/)). Les critères [5.4](../5-4_compression-videos/) (compression) et [5.5](../5-5_ecoute-seule/) (écoute seule) complètent celui-ci.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) et [DiaLog](https://dialog.beta.gouv.fr/ecoconception) marquent ce critère **« Non applicable »**, faute de vidéo. C'est la façon la plus sobre de traiter le sujet, si c'est un choix : le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) demande de préférer le format le plus léger capable de porter l'information.

L'[aide de Netflix](https://help.netflix.com/fr/node/87) (consultée le 20 octobre 2026) donne la mesure des écarts, par heure de visionnage :

| Réglage | Données utilisées par heure |
|---|---:|
| Faible (« qualité vidéo de base ») | jusqu'à 0,3 Go |
| Moyenne (« qualité vidéo standard ») | jusqu'à 0,7 Go |
| Élevée, haute définition | jusqu'à 3 Go |
| Élevée, ultra haute définition (4K) | jusqu'à 7 Go |

Netflix **mémorise** le réglage par profil, mais l'option par défaut, « Auto », vise « la meilleure qualité possible » selon la connexion. C'est l'inverse du RGESN, qui plafonne la définition par défaut, quelle que soit la connexion.

{{% /tab %}}

{{< /tabs >}}
