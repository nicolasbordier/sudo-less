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

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.4 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons), déjà présentée au [critère 5.3](../5-3_definition-videos/). Son exemple : « le logiciel Handbrake permet de compresser une vidéo HD de 1mn35 en 720p, réduisant ainsi son poids de 38% soit de 11,7 Mo ».

Ce gain vient surtout du passage de la HD au 720p, c'est-à-dire de la **définition**, qui relève du critère 5.3. Le critère 5.4 porte sur un autre levier : à définition égale, le **codec** et son **réglage**. Les deux se cumulent.

Le guide parle d'outils de « compression sans perte de qualité perceptible ». Tous les codecs cités par le RGESN compressent pourtant **avec perte**. Leur réglage consiste à choisir une perte qui ne se voit pas. C'est la règle du RGESN : utiliser « le niveau de qualité le plus faible sans dégrader la vidéo visuellement dans le contexte d'utilisation ».

Pour le son, le guide propose de compresser les bandes sonores « en mp3 », et rappelle que « dans le secteur musical ou cinématographique, il sera préférable de ne pas compresser les fichiers ». Pour la piste son d'une vidéo, le codec Opus fait mieux que le MP3 à débit égal (voir l'onglet « Mise en œuvre technique »).

La section renvoie enfin, pour aller plus loin, au guide de The Shift Project présenté dans l'onglet suivant.

{{% /tab %}}

{{% tab tabName="The Shift Project" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le guide [**« Comment réduire en 5 minutes le poids d'une vidéo tout en gardant une bonne qualité »**](https://theshiftproject.org/guide-reduire-poids-video-5-minutes/), conçu par Gauthier Roussilhe et finalisé avec The Shift Project (document de 2019), détaille un réglage du logiciel libre [HandBrake](https://handbrake.fr/). Ses principaux réglages, au regard du critère 5.4 :

| Réglage du guide | Valeur | Au regard du critère 5.4 |
|---|---|---|
| Encodeur vidéo | « H264 (x264) » | À partir de 720p, H.264 n'est plus accepté qu'en repli d'un codec plus efficace |
| Qualité | « Constant Quality », valeur 22 (19 à 23 en 720p, 20 à 24 en 1080p) | Débit variable : conforme |
| Dimensions | 1280 × 720 | Définition qui relève du critère 5.3 |
| Audio | Stéréo, débit d'origine conservé | À adapter : le RGESN demande le mono pour les dialogues |

Le mode « Constant Quality » correspond au débit variable demandé par le RGESN. L'encodeur vise une qualité constante et dépense donc moins de données sur les scènes simples. La méthode reste valable, à condition de changer d'encodeur : HandBrake propose un encodeur AV1 (SVT-AV1) depuis sa version 1.6.0 ([notes de version](https://github.com/HandBrake/HandBrake/blob/master/NEWS.markdown)). Les valeurs ne se transposent pas d'un encodeur à l'autre : la valeur 22 vaut pour x264, et le réglage est à refaire pour AV1 (voir l'onglet « Mise en œuvre technique »).

Pour l'audio, le guide juge le gain « minime » sous 160 kbit/s, la qualité sonore étant « très importante pour l'usager ». L'argument se comprend pour une vidéo H.264, dont la piste image pèse beaucoup plus lourd que le son. Avec un codec vidéo plus efficace, la piste son pèse proportionnellement plus. Passer en mono pour une vidéo de parole, comme le demande le RGESN, devient alors un gain réel.

Le guide se termine sur un constat qui dépasse la compression : réduire le poids de ses vidéos « m'a fait remettre en question l'utilité de leur présence. J'ai décidé d'en supprimer trois ».

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a qu'une fiche étiquetée « RGESN 5.4 » : [**RWEB 0108 — « Compresser les documents »**](https://rweb.greenit.fr/fr/fiches/RWEB_0108-compresser-les-documents), également rattachée aux critères 5.2 et 5.6. Elle recommande de compresser les fichiers téléchargeables (avec WinZip dans son exemple) et cite parmi eux les « contenus multimédias (images, audio et vidéo) ».

Pour une vidéo, ce levier ne joue presque pas : un fichier produit par un codec vidéo est déjà compressé. Sur les fichiers de test de l'onglet « Mise en œuvre technique », une compression ZIP au niveau maximal ne fait gagner que 2,2 % sur la vidéo AV1 et 0,34 % sur la vidéo VP9. La fiche prévoit d'ailleurs cette exception : « sauf si la compression n'apporte pas un gain évident ». Pour le critère 5.4, tout se joue à l'encodage.

Deux autres fiches sont plus utiles, même sans l'étiquette :

- [**RWEB 0098 — « Optimiser et générer les médias avant importation sur un CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0098-optimiser-et-generer-les-medias-avant-importation-sur-un-cms), notée **5/5** en priorité. Elle recommande d'encoder les médias sur son poste, avant de les importer, plutôt que par des plugins de CMS, « consommateurs en terme de CPU, de mémoire vive, de réseau et de stockage ». Elle cite FFmpeg, l'outil utilisé dans l'onglet « Mise en œuvre technique ».
- [**RWEB 0107**](https://rweb.greenit.fr/fr/fiches/RWEB_0107-adapter-les-videos-aux-contextes-de-visualisation), présentée au [critère 5.3](../5-3_definition-videos/). Son exemple encode les vidéos en « MPEG-4 / H.264 / AAC ». Au sens du critère 5.4, ce format n'est plus qu'un repli à partir de 720p.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C, déjà citée aux critères [5.2](../5-2_compression-images/) et [5.3](../5-3_definition-videos/), comporte un critère de succès « Optimized media » qui rejoint le 5.4 point par point (version du 16 octobre 2026) :

- « Use widely supported, efficient formats that enable native presentation or playback where possible. »
- « Avoid unnecessary custom or non-native media players. »
- « Use hardware-accelerated playback when available and compatible with security requirements. »

Le troisième point est l'exigence d'accélération matérielle du RGESN. Le W3C y ajoute une réserve que le RGESN ne formule pas : la compatibilité avec les exigences de sécurité. Le deuxième point va dans le même sens : un lecteur qui décode lui-même la vidéo, en JavaScript ou en WebAssembly, se prive du décodeur matériel du terminal.

La fiche [**« Reduce data transfer with compression »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-data-transfer-with-compression) demande aussi, dans son critère « Media compression », de « Compress media files such as images, video, and audio before uploading anywhere ». C'est le principe de la fiche RWEB 0098 : encoder avant la mise en ligne.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) n'a pas de critère sur les codecs vidéo. Dans la [recommandation n°3 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=3), déjà citée au [critère 5.3](../5-3_definition-videos/), le conseil [« Est-ce que les CODECS des sons sont compressés au maximum ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-le-volume-de-donnees-utilise-par-la-a013d4) pose pourtant le compromis au cœur du critère 5.4 : « Les mécanismes de compression audio (CODEC) vont réduire le volume de données échangées mais demander plus de ressources CPU pour décoder et restituer les sons sur le périphérique utilisateur. »

Le RGESN tranche ce compromis pour la vidéo. Un codec plus efficace réduit le volume transféré, mais son décodage demande plus de calcul, sauf si le terminal dispose d'un décodeur matériel. D'où la condition du moyen de test : des codecs « accélérés matériellement par la majorité du parc des terminaux ». Un codec très efficace, mais décodé par le processeur sur la plupart des terminaux, déplace l'impact du réseau vers le terminal, au détriment de son autonomie et de sa durée de vie.

Le test associé à ce conseil, « La qualité du son est-elle réduite et testée pour rester compréhensive ? », suit la même logique que le RGESN : la qualité la plus faible qui reste compréhensible.

{{% /tab %}}

{{% tab tabName="Codecs et décodage matériel" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le RGESN cite trois codecs efficaces (AV1, VP9 et HEVC) et accepte H.264 en repli. D'après [Can I use](https://caniuse.com/) (consulté le 20 octobre 2026), en part des navigateurs utilisés dans le monde, et la [documentation MDN sur les codecs vidéo](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs) pour le décodage matériel :

| Codec | Prise en charge | Décodage matériel | Rôle |
|---|---:|---|---|
| [AV1](https://caniuse.com/av1) | 79,04 % (+ 16,93 % partielle) | Terminaux récents. Safari ne lit AV1 qu'avec un décodeur matériel : Mac M3 et suivants, iPhone 15 Pro, iPhone 16 et suivants (MDN) | Codec principal, si le parc le décode matériellement |
| VP9 ([WebM](https://caniuse.com/webm)) | 96,41 % (conteneur WebM) | « Assez courant » (MDN) | Codec efficace le plus largement lisible |
| [HEVC](https://caniuse.com/hevc) | 19,99 % (+ 74,95 % partielle) | Dans Chrome, Edge et Firefox, prise en charge souvent limitée aux terminaux équipés d'un décodeur matériel | Codec breveté, soumis à licence (MDN) |
| [H.264](https://caniuse.com/mpeg4) | 97,49 % | Très répandu (MDN) | Repli uniquement, à partir de 720p |

**Lisible ne veut pas dire décodé matériellement.** Chrome et Firefox intègrent un décodeur AV1 logiciel (dav1d) : ils lisent AV1 sur tous les terminaux, y compris sans décodeur matériel. La vidéo est alors décodée par le processeur, ce que l'objectif du critère cherche justement à éviter. Safari fait l'inverse et ne lit AV1 qu'avec un décodeur matériel.

La condition « majorité du parc des terminaux » dépend donc du public du service. Pour un outil interne utilisé sur des ordinateurs récents, AV1 peut la remplir. Pour un service grand public, consulté aussi sur d'anciens terminaux (voir le [critère 2.1](../../specifications/2-1_profils-materiels/)), VP9 peut être le choix le plus sûr. Dans tous les cas, la décision se vérifie sur des terminaux représentatifs, avec la méthode de l'étape 5 de l'onglet « Mise en œuvre technique ».

L'API Media Capabilities (`navigator.mediaCapabilities.decodingInfo()`) semble faite pour ce choix : elle indique si un décodage serait `powerEfficient`. Mais MDN précise que les navigateurs répondent `smooth` et `powerEfficient` tant qu'ils n'ont pas enregistré de statistiques sur l'appareil (« until stats on this device have been recorded »). On ne peut donc pas s'y fier dès la première visite.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

**1. Encoder une fois, avant la mise en ligne** (voir les onglets RWEB et W3C). En reprenant la vidéo 720p du [critère 5.3](../5-3_definition-videos/), avec FFmpeg :

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

- **`-crf`** fixe une qualité cible plutôt qu'un débit : c'est l'encodage à débit variable demandé par le RGESN. 35 est la valeur par défaut de SVT-AV1 (échelle de 1 à 70), 23 celle de x264. Plus la valeur est haute, plus le fichier est léger.
- **`-maxrate` et `-bufsize`** ajoutent le plafond : en moyenne sur 2 secondes (3 000 kbit de tampon à 1 500 kbit/s), le débit ne doit pas dépasser 1,5 Mbit/s. Ce plafond se choisit d'après la connexion la plus lente visée. Le [critère 2.3](../../specifications/2-3_connexion-bas-debit/) teste le service à 512 kbit/s en fixe : à ce débit, seule une version de plus faible définition (critère 5.3) se lit sans attente.
- **`-preset`** règle le compromis entre vitesse d'encodage et taille du fichier : plus la valeur est basse, plus l'encodage est lent et le fichier compact.
- **Audio** : `-ac 1` passe la piste en mono, ce qui convient à une vidéo de parole (conférence, tutoriel). Le [wiki de Xiph.Org](https://wiki.xiph.org/Opus_Recommended_Settings), qui maintient la bibliothèque de référence d'Opus, recommande 24 kbit/s en mono pour un livre audio ou un podcast, et 64 à 96 kbit/s en stéréo pour de la musique, débits auxquels « Opus has better quality than MP3, AAC and Vorbis ». Pour une vidéo musicale, remplacer `-b:a 24k -ac 1` par `-b:a 96k`. AAC, moins efficace, demande un débit plus élevé dans la version de repli.

**2. Régler la qualité d'après le rendu.** Le RGESN demande « le niveau de qualité le plus faible sans dégrader la vidéo visuellement ». La démarche est la même qu'au [critère 5.2](../5-2_compression-images/) pour les images. On encode un extrait de 20 secondes, choisi parmi les scènes les plus difficiles (mouvements rapides, texte à l'écran, dégradés), à plusieurs niveaux de qualité :

```bash
for crf in 35 40 45; do
  ffmpeg -ss 00:01:00 -t 20 -i source.mp4 -vf "scale=-2:720" -an \
         -c:v libsvtav1 -preset 6 -crf $crf extrait-crf$crf.webm
done
```

Regarder les extraits **à leur taille d'affichage réelle** et retenir la valeur la plus haute sans défaut visible : aplats dans les dégradés, texte flou, blocs dans les scènes en mouvement. Comme au critère 5.2, on calibre une fois par **type de vidéo** (conférence filmée, capture d'écran, animation…), puis on applique la valeur retenue à toutes les vidéos du même type. Dans HandBrake, la même démarche passe par l'aperçu (*Preview*) et le curseur « Constant Quality ».

**3. Proposer les deux versions dans l'élément `<video>`.** Le navigateur prend la première source qu'il sait lire et ne télécharge qu'elle :

```html
<video controls preload="none" width="1280" height="720" poster="conference.webp">
  <source src="video-720p.webm" type='video/webm; codecs="av01.0.05M.08, opus"'>
  <source src="video-720p.mp4" type='video/mp4; codecs="avc1.64001F, mp4a.40.2"'>
</video>
```

- Le paramètre `codecs` permet au navigateur de choisir sans télécharger le fichier. `av01.0.05M.08` désigne de l'AV1 en profil Main, niveau 3.1, 8 bits, ce que produit la commande de l'étape 1 en 720p. `avc1.64001F` désigne du H.264 en profil High, niveau 3.1.
- L'ordre des sources traduit le choix de l'onglet « Codecs et décodage matériel ». AV1 ne passe en premier que si la majorité du parc le décode matériellement ; sinon, une version VP9 prend sa place (encodeur `libvpx-vp9` de FFmpeg, mais voir la limite de son plafond à l'étape 4).
- `preload="none"` évite tout téléchargement avant que l'utilisateur lance la lecture (voir le [critère 4.1](../../ux-ui/4-1_lecture-automatique/)).

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

Exemple sur une séquence de test de 10 secondes : 5 secondes d'aplat de couleur, puis 5 secondes d'image animée couverte de bruit, le contenu le plus difficile à compresser. Encodage en 720p avec la commande de l'étape 1 (FFmpeg avec SVT-AV1 3.1.2) :

| | Sans plafond | Avec plafond à 1,5 Mbit/s |
|---|---:|---:|
| Débit sur l'aplat | quelques kbit/s | quelques kbit/s |
| Débit sur le bruit, seconde par seconde | 13,8 à 19,6 Mbit/s | 1,1 à 2,8 Mbit/s |
| Poids du fichier | 10,8 Mo | 1,3 Mo |

Le débit variable fait chuter le débit sur la scène simple, avec ou sans plafond. Le plafond contient la scène complexe, au prix d'une qualité dégradée sur cette scène : c'est le compromis voulu par le RGESN pour rester « lisible avec une connexion internet à bas débit ». Ce n'est pas une limite stricte. SVT-AV1 autorise par défaut un dépassement de 50 % (paramètre [`mbr-overshoot-pct`](https://gitlab.com/AOMediaCodec/SVT-AV1/-/blob/master/Docs/Parameters.md)), d'où les pointes à 2,8 Mbit/s. L'encodeur VP9 l'est encore moins : sur la même séquence en 1080p, `libvpx-vp9` avec `-crf 33 -b:v 3M` a produit 10,9 Mbit/s en moyenne, contre 2,2 Mbit/s pour SVT-AV1 plafonné à 3 Mbit/s.

**5. Vérifier le décodage matériel** sur des terminaux représentatifs du parc. Dans Chrome ou Edge, ouvrir les outils de développement, puis le panneau **Media** (menu « More tools »). Pendant la lecture, la propriété **Hardware decoder** (décodeur matériel) vaut `true` si la vidéo est décodée par le processeur graphique. La propriété **Decoder name** donne le décodeur utilisé : `Dav1dVideoDecoder` (AV1), `VpxVideoDecoder` (VP9) ou `FFmpegVideoDecoder` signalent un décodage logiciel, par le processeur. La page `chrome://gpu`, section « Video Acceleration Information », liste aussi les codecs que le terminal décode matériellement.

**6. Documenter**, comme l'exige le moyen de test, dans la déclaration d'écoconception. Par exemple :

| Définition | Codec vidéo | Encodage vidéo | Codec audio | Encodage audio |
|---|---|---|---|---|
| 720p | AV1 (WebM), repli H.264 (MP4) | Débit variable plafonné à 1,5 Mbit/s, sans HDR | Opus, repli AAC | 24 kbit/s mono (repli : 64 kbit/s mono) |

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Le critère 5.4 forme une paire avec le [critère 5.3](../5-3_definition-videos/) (définition adaptée), déjà publié sur ce site. Le 5.3 porte sur la **définition**, le 5.4 sur le **codec** et son **réglage**. Les deux partagent le seuil de 720p : en dessous, le moyen de test du 5.4 accepte H.264 seul. Le mode « sobriété énergétique » du 5.3, plafonné à 480p sur smartphone, peut donc rester en H.264, à condition d'être encodé en débit variable.

Le RGESN renvoie lui-même au [critère 5.6](../5-6_compression-audio/) (compression des contenus audio) pour le choix entre mono et stéréo. Le [critère 5.5](../5-5_ecoute-seule/) (mode « écoute seule ») donne encore plus de poids à ce réglage : dans ce mode, la piste son est tout ce qui est transféré.

Plusieurs critères de la famille Spécifications, déjà publiés, entrent en jeu :

- le [critère 2.10](../../specifications/2-10_services-tiers/) (services tiers) demande qu'une vidéo intégrée depuis un service tiers valide, entre autres, le critère 5.4. Sur YouTube, par exemple, un clic droit sur le lecteur, puis « Stats for nerds », affiche les codecs effectivement reçus (`av01`, `vp09` ou `avc1` pour la vidéo, `opus` ou `mp4a` pour le son) ;
- le [critère 2.4](../../specifications/2-4_anciennes-versions-os/) (anciennes versions d'OS et de navigateurs) : la version de repli en H.264 sert précisément les terminaux qui ne lisent pas le codec principal ;
- le [critère 2.3](../../specifications/2-3_connexion-bas-debit/) (connexion bas débit) donne le débit de référence pour choisir le plafond.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque les critères 5.3, 5.4 et 5.5 **« Non-applicable »** : « Pas de vidéo ». La justification correspond exactement au cas prévu par le RGESN (« N/A si le service numérique ne propose pas de vidéos »).

Netflix indique selon un [billet de son blog technique](https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80) de décembre 2025, repris par [Streaming Media Blog](https://www.streamingmediablog.com/2025/12/netflix-av1.html) :

- AV1 représente environ **30 %** des visionnages, derrière H.264 (AVC), qui reste le premier codec ;
- les sessions en AV1 consomment **un tiers de bande passante en moins** qu'en H.264 ou en HEVC, avec **45 %** d'interruptions pour chargement en moins ;
- **88 %** des téléviseurs, box et clés de streaming soumis à la certification Netflix entre 2021 et 2025 prennent en charge AV1.

Ce dernier chiffre porte sur les modèles récents, pas sur l'ensemble du parc installé. Il montre que, sur les téléviseurs récents, AV1 peut remplir la condition de décodage matériel du RGESN. Netflix garde H.264 pour les autres terminaux : c'est le schéma du critère 5.4, un codec efficace accompagné d'un repli.

{{% /tab %}}

{{< /tabs >}}
