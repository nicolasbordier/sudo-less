---
weight: 400
title: "5.4 - Mode de compression des vidéos efficace et adapté"
description: "Critère 5.4 du RGESN : encoder les vidéos de 720p et plus avec un codec efficace (AV1, VP9 ou HEVC) et H.264 en repli, en débit variable plafonné, vérifier leur décodage matériel et adapter l'encodage audio."
icon: "video_settings"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il des vidéos dont le mode de compression est efficace et adapté au contenu et au contexte de visualisation ?

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
| **Critère**  | `5.4` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne propose pas de vidéos` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

La majeure partie du trafic sur internet est liée au visionnage de vidéos (la vidéo représente près de 68 % du trafic internet en 2023 selon le rapport de Sandvine The Global Internet Phenomena Report). Or le transport de données numériques s'appuie sur des infrastructures ainsi que l'usage d'équipements et de terminaux qui ont une empreinte environnementale à minimiser. L'emploi d'un codec vidéo efficace (à date : AV1, VP9 et HEVC) permet de réduire significativement la bande passante utilisée.

Par ailleurs, le mode de décodage du codec vidéo par le terminal influe directement sur la consommation énergétique de l'appareil. Si le codec n'est pas accéléré matériellement par le processeur graphique (GPU), la lecture vidéo sera possible, mais via le microprocesseur (CPU). Dans ce cas, la consommation d'énergie du terminal sera plus importante, ce qui va diminuer l'autonomie d'un terminal sur batterie et possiblement sa durée de vie.

L'objectif est donc d'optimiser la taille des flux téléchargés par les utilisateurs et les ressources mobilisées grâce à l'utilisation d'un codec et d'un encodage efficaces.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Les vidéos sont proposées avec au moins un codec performant (à date : AV1, VP9 et HEVC) tenant compte de l'efficacité de compression du codec et son accélération matérielle dans les définitions 720p et au-delà. H.264 peut être proposé en complément du codec performant.

Pour économiser de la bande passante sur les scènes simples à encoder, un encodage à débit variable doit être préféré. Ce mode d'encodage peut dans certains cas être associé à un plafond pour le débit maximal afin d'assurer que les contenus plus complexes restent lisibles avec une connexion internet à bas débit.

Par ailleurs, la qualité d'encodage de la vidéo devrait être adaptée au besoin de l'utilisateur. Par exemple, utiliser le niveau de qualité le plus faible sans dégrader la vidéo visuellement dans le contexte d'utilisation.

La qualité d'encodage des flux audio devrait être adaptée au besoin de l'utilisateur :

- Optimisation du bitrate (débit), du ratio (taux de compression) et de la fréquence d'échantillonnage au sein du format ;
- Choix adapté de nombre de canaux : stéréo pour de la musique ou mono pour des dialogues (voir critère 5.6. dédié à l'audio).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service remplit les conditions suivantes :

- Les vidéos sont encodées avec un débit variable, quel que soit le codec vidéo utilisé. Ce mode d'encodage peut dans certains cas être associé à un plafond pour le débit maximal afin d'assurer que les contenus plus complexes restent lisibles avec une connexion internet à bas débit.
- Les vidéos disponibles sur le service numérique ont une définition inférieure à 720p ou sont proposées avec un codec vidéo efficace, à date AV1, VP9 ou HEVC. Le codec H.264 peut être utilisé en secours, en cas d'incompatibilité, à condition qu'un codec plus performant soit proposé aux terminaux compatibles.
- Le ou les codecs utilisés sont accélérés matériellement par la majorité du parc des terminaux.
- Sont documentés dans la déclaration d'écoconception du service numérique le(s) codec(s) vidéo et audio utilisé(s) pour chaque définition vidéo, le type d'encodage vidéo : débit fixe, variable, variable avec débit maximum/présence de HDR, et le type d'encodage audio : débit, nombre de canaux.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="8">}}
{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Contributeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.4 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons). Son exemple : HandBrake réduit « une vidéo HD de 1mn35 en 720p » de 38 %. Ce gain vient surtout du passage au 720p, c'est-à-dire de la **définition**, qui relève du [critère 5.3](../5-3_definition-videos/). Le 5.4 porte sur un autre levier, à définition égale : le **codec** et son **réglage**. Les deux se cumulent.

Le guide parle de « compression sans perte de qualité perceptible ». Tous les codecs cités par le RGESN compressent pourtant **avec perte** : les régler consiste à choisir une perte qui ne se voit pas.

{{% /tab %}}

{{% tab tabName="The Shift Project" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le guide [**« Comment réduire en 5 minutes le poids d'une vidéo tout en gardant une bonne qualité »**](https://theshiftproject.org/guide-reduire-poids-video-5-minutes/), de Gauthier Roussilhe et The Shift Project (2019), détaille un réglage du logiciel libre [HandBrake](https://handbrake.fr/) :

| Réglage du guide | Valeur | Au regard du critère 5.4 |
|---|---|---|
| Encodeur vidéo | « H264 (x264) » | À partir de 720p, H.264 n'est plus accepté qu'en repli d'un codec plus efficace |
| Qualité | « Constant Quality », valeur 22 (19 à 23 en 720p, 20 à 24 en 1080p) | Débit variable : conforme |
| Dimensions | 1280 × 720 | Définition qui relève du [critère 5.3](../5-3_definition-videos/) |
| Audio | Stéréo, débit d'origine conservé | À adapter : le RGESN demande le mono pour les dialogues |

La méthode reste valable en changeant d'encodeur : HandBrake propose AV1 (SVT-AV1) depuis sa [version 1.6.0](https://github.com/HandBrake/HandBrake/blob/master/NEWS.markdown), mais la valeur 22 ne vaut que pour x264. Le guide se termine sur un constat qui dépasse la compression : réduire le poids de ses vidéos « m'a fait remettre en question l'utilité de leur présence. J'ai décidé d'en supprimer trois ».

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a qu'une fiche étiquetée « RGESN 5.4 » : [**RWEB 0108 — « Compresser les documents »**](https://rweb.greenit.fr/fr/fiches/RWEB_0108-compresser-les-documents), qui recommande de compresser les fichiers téléchargeables, vidéos comprises. Pour une vidéo, ce levier ne joue presque pas : une compression ZIP ne fait gagner que 2,2 % sur la vidéo AV1 de l'onglet « Mise en œuvre technique ». Tout se joue à l'encodage.

Plus utile, [**RWEB 0098 — « Optimiser et générer les médias avant importation sur un CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0098-optimiser-et-generer-les-medias-avant-importation-sur-un-cms) (priorité 5/5) recommande d'encoder les médias avant de les importer, avec FFmpeg par exemple, plutôt que par des plugins de CMS « consommateurs en terme de CPU, de mémoire vive, de réseau et de stockage ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) rejoint le 5.4 :

- « Use widely supported, efficient formats that enable native presentation or playback where possible. »
- « Use hardware-accelerated playback when available and compatible with security requirements. »

Un lecteur qui décode lui-même la vidéo, en JavaScript ou en WebAssembly, se prive du décodeur matériel du terminal.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) n'a pas de critère sur les codecs vidéo. Son conseil sur l'audio, [« Est-ce que les CODECS des sons sont compressés au maximum ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-le-volume-de-donnees-utilise-par-la-a013d4) ([recommandation n°3 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=3)), pose pourtant le compromis au cœur du 5.4 : la compression réduit les données échangées, mais demande « plus de ressources CPU pour décoder ».

Le RGESN le tranche par l'accélération matérielle : un codec très efficace, mais décodé par le processeur, déplace l'impact du réseau vers le terminal.

{{% /tab %}}

{{% tab tabName="Codecs et décodage matériel" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le RGESN cite trois codecs efficaces (AV1, VP9 et HEVC) et accepte H.264 en repli. D'après [Can I use](https://caniuse.com/) (consulté le 20 octobre 2026), en part des navigateurs utilisés dans le monde, et la [documentation MDN sur les codecs vidéo](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs) :

| Codec | Prise en charge | Décodage matériel | Rôle |
|---|---:|---|---|
| [AV1](https://caniuse.com/av1) | 79,04 % (+ 16,93 % partielle) | Terminaux récents. Safari ne lit AV1 qu'avec un décodeur matériel : Mac M3 et suivants, iPhone 15 Pro, iPhone 16 et suivants (MDN) | Codec principal, si le parc le décode matériellement |
| VP9 ([WebM](https://caniuse.com/webm)) | 96,41 % (conteneur WebM) | « Assez courant » (MDN) | Codec efficace le plus largement lisible |
| [HEVC](https://caniuse.com/hevc) | 19,99 % (+ 74,95 % partielle) | Dans Chrome, Edge et Firefox, prise en charge souvent limitée aux terminaux équipés d'un décodeur matériel | Codec breveté, soumis à licence (MDN) |
| [H.264](https://caniuse.com/mpeg4) | 97,49 % | Très répandu (MDN) | Repli uniquement, à partir de 720p |

**Lisible ne veut pas dire décodé matériellement.** Chrome et Firefox lisent AV1 sur tous les terminaux grâce à un décodeur logiciel (dav1d), donc par le processeur quand le terminal n'a pas de décodeur matériel. La condition « majorité du parc des terminaux » dépend du public : AV1 peut la remplir pour un outil interne utilisé sur des ordinateurs récents ; pour un service grand public, consulté aussi sur d'anciens terminaux (voir le [critère 2.1](../../specifications/2-1_profils-materiels/)), VP9 est le choix le plus sûr.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

**1. Encoder une fois, avant la mise en ligne.** En reprenant la vidéo 720p du [critère 5.3](../5-3_definition-videos/), avec FFmpeg :

```bash
# Version principale : AV1 + Opus (WebM), débit variable plafonné
ffmpeg -i source.mp4 -vf "scale=-2:720" \
       -c:v libsvtav1 -preset 6 -crf 35 -maxrate 1500k -bufsize 3000k \
       -c:a libopus -b:a 24k -ac 1 video-720p.webm

# Repli : H.264 + AAC (MP4), même logique
ffmpeg -i source.mp4 -vf "scale=-2:720" \
       -c:v libx264 -preset slow -crf 23 -maxrate 1500k -bufsize 3000k \
       -c:a aac -b:a 64k -ac 1 -movflags +faststart video-720p.mp4
```

- **`-crf`** fixe une qualité cible plutôt qu'un débit : c'est le débit variable demandé par le RGESN. Plus la valeur est haute, plus le fichier est léger (35 est la valeur par défaut de SVT-AV1, 23 celle de x264).
- **`-maxrate` et `-bufsize`** plafonnent le débit à 1,5 Mbit/s en moyenne sur 2 secondes. Ce plafond se choisit d'après la connexion la plus lente visée (voir le [critère 2.3](../../specifications/2-3_connexion-bas-debit/)).
- **Audio** : `-ac 1` passe la piste en mono pour une vidéo de parole. D'après le [wiki de Xiph.Org](https://wiki.xiph.org/Opus_Recommended_Settings), Opus suffit à 24 kbit/s en mono pour de la parole, 64 à 96 kbit/s en stéréo pour de la musique.

**2. Régler la qualité d'après le rendu**, comme pour les images au [critère 5.2](../5-2_compression-images/) : encoder un extrait difficile (mouvements rapides, texte à l'écran, dégradés) à plusieurs niveaux de qualité.

```bash
for crf in 35 40 45; do
  ffmpeg -ss 00:01:00 -t 20 -i source.mp4 -vf "scale=-2:720" -an \
         -c:v libsvtav1 -preset 6 -crf $crf extrait-crf$crf.webm
done
```

Regarder les extraits **à leur taille d'affichage réelle** et retenir la valeur la plus haute sans défaut visible, une fois par **type de vidéo** (conférence filmée, capture d'écran, animation…).

**3. Proposer les deux versions dans l'élément `<video>`.** Grâce au paramètre `codecs`, le navigateur prend la première source qu'il sait lire, sans télécharger les autres :

```html
<video controls preload="none" width="1280" height="720" poster="conference.webp">
  <source src="video-720p.webm" type='video/webm; codecs="av01.0.05M.08, opus"'>
  <source src="video-720p.mp4" type='video/mp4; codecs="avc1.64001F, mp4a.40.2"'>
</video>
```

AV1 ne passe en premier que si la majorité du parc le décode matériellement ; sinon, une version VP9 prend sa place. `preload="none"` évite tout téléchargement avant le clic (voir le [critère 4.1](../../ux-ui/4-1_lecture-automatique/)).

**4. Vérifier l'encodage.** `ffprobe`, fourni avec FFmpeg, donne les codecs, la définition et le nombre de canaux à reporter dans la déclaration :

```bash
ffprobe -v error -show_entries stream=codec_name,width,height,channels,sample_rate \
        -of default=nw=1 video-720p.webm
```

Le débit seconde par seconde montre si l'encodage est bien variable et si le plafond tient :

```bash
ffprobe -v error -select_streams v:0 -show_entries packet=pts_time,size -of csv=p=0 video-720p.webm \
  | awk -F, '{ s = int($1); b[s] += $2 * 8 } END { for (i in b) printf "%d s : %d kbit/s\n", i, b[i] / 1000 }' \
  | sort -n
```

Testé sur une séquence de 10 secondes, 5 secondes d'aplat de couleur puis 5 secondes de bruit, le contenu le plus difficile à compresser (720p, SVT-AV1 3.1.2) :

| | Sans plafond | Avec plafond à 1,5 Mbit/s |
|---|---:|---:|
| Débit sur l'aplat | quelques kbit/s | quelques kbit/s |
| Débit sur le bruit, seconde par seconde | 13,8 à 19,6 Mbit/s | 1,1 à 2,8 Mbit/s |
| Poids du fichier | 10,8 Mo | 1,3 Mo |

Le plafond contient la scène complexe, au prix de sa qualité. Ce n'est pas une limite stricte : SVT-AV1 autorise un dépassement de 50 % ([`mbr-overshoot-pct`](https://gitlab.com/AOMediaCodec/SVT-AV1/-/blob/master/Docs/Parameters.md)), et l'encodeur VP9 `libvpx-vp9` le respecte encore moins.

**5. Vérifier le décodage matériel** sur des terminaux représentatifs du parc. Dans Chrome ou Edge, ouvrir le panneau **Media** des outils de développement (menu « More tools ») : pendant la lecture, **Hardware decoder** vaut `true` si la vidéo est décodée par le processeur graphique. Dans **Decoder name**, `Dav1dVideoDecoder` (AV1) ou `VpxVideoDecoder` (VP9) signalent un décodage logiciel.

**6. Documenter**, comme l'exige le moyen de test, dans la déclaration d'écoconception. Par exemple :

| Définition | Codec vidéo | Encodage vidéo | Codec audio | Encodage audio |
|---|---|---|---|---|
| 720p | AV1 (WebM), repli H.264 (MP4) | Débit variable plafonné à 1,5 Mbit/s, sans HDR | Opus, repli AAC | 24 kbit/s mono (repli : 64 kbit/s mono) |

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Le 5.4 forme une paire avec le [critère 5.3](../5-3_definition-videos/) : le 5.3 porte sur la **définition**, le 5.4 sur le **codec**. Sous 720p, le moyen de test du 5.4 accepte H.264 seul, à condition d'un encodage en débit variable.

- le [critère 5.6](../5-6_compression-audio/) (compression audio) : le choix entre mono et stéréo ;
- le [critère 5.5](../5-5_ecoute-seule/) (écoute seule) : la piste son est alors tout ce qui est transféré ;
- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) : une vidéo YouTube intégrée doit aussi valider le 5.4. Un clic droit sur le lecteur, puis « Stats for nerds », affiche les codecs reçus ;
- le [critère 2.3](../../specifications/2-3_connexion-bas-debit/) (bas débit) : le débit de référence pour choisir le plafond.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque les critères [5.3](../5-3_definition-videos/), 5.4 et [5.5](../5-5_ecoute-seule/) **« Non-applicable »** : « Pas de vidéo », le cas prévu par le RGESN.

Netflix indique, dans un [billet de son blog technique](https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80) de décembre 2025 repris par [Streaming Media Blog](https://www.streamingmediablog.com/2025/12/netflix-av1.html), qu'AV1 représente environ **30 %** des visionnages, derrière H.264. Les sessions en AV1 consomment **un tiers de bande passante en moins**, avec **45 %** d'interruptions pour chargement en moins. **88 %** des téléviseurs et boîtiers certifiés entre 2021 et 2025 prennent en charge AV1. Netflix garde H.264 pour les autres terminaux : c'est le schéma du 5.4, un codec efficace accompagné d'un repli.

{{% /tab %}}

{{< /tabs >}}
