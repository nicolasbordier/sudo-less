---
weight: 600
title: "5.6 - Compression des contenus audio adaptée"
description: "Critère 5.6 du RGESN : encoder les contenus audio avec un codec efficace (Opus, AAC), en mono pour la parole, rester sous 1 Mo par minute et documenter les codecs et débits utilisés."
icon: "audiotrack"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il des contenus audios dont le mode de compression est adapté au contenu et au contexte d'écoute ?

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
| **Critère**  | `5.6` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne propose pas de contenu audio` |
| **Métiers concernés** | `Développeur` `Responsable IT` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire la taille des contenus audio téléchargés par les utilisateurs et donc les ressources informatiques nécessaires.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Afin de réduire la taille des contenus audio, envisager les actions suivantes :

- Utiliser des codecs audio efficaces (à date : Opus, AAC, HE-AAC, HE-AAC v2, HD-AAC, Dolby E-AC-3 ou Dolby AC-4), en évitant les formats les plus volumineux. L'ensemble des navigateurs web supportent un flux audio seul (sans vidéo accompagnant le flux audio) avec le codec Opus, dans un conteneur WebM et avec le codec AAC, dans un conteneur MP4.
- Optimiser le bitrate (débit), le ratio (taux de compression) et la fréquence d'échantillonnage au sein du format.
- Faire un choix adapté : stéréo pour de la musique ou mono pour des dialogues.
- Éviter le ratio poids en mégaoctet/durée en minute supérieur à 1.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service remplit les conditions suivantes :

- Les contenus audio disponibles sur le service numérique sont proposés avec un codec audio efficace, à date Opus, AAC ou Dolby AC-4 (un codec non efficace peut être proposé en fallback, à condition qu'un codec plus performant soit proposé aux terminaux compatibles).
- Le(s) codec(s) audio utilisé(s) et le type d'encodage audio (débit, nombre de canaux) sont documentés dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe et explicitement étiquetée « RGESN 5.6 » : la fiche [**RWEB 0105 — « Adapter les sons aux contextes d'écoute »**](https://rweb.greenit.fr/fr/fiches/RWEB_0105-adapter-les-sons-aux-contextes-d-ecoute). C'est d'elle que vient le seuil du RGESN : son principe de validation compte les « pistes audio dont le ratio poids en méga octet/durée en minute est supérieur à 1 », avec un objectif de **zéro**.

Son exemple part d'un fichier WAV de 63 128 octets : converti en MP3, il pèse 10 823 octets à 128 kbit/s (6 fois plus léger) et 6 508 octets à 64 kbit/s (10 fois plus léger).

La fiche et le RGESN divergent toutefois sur les codecs :

- la fiche recommande « MP3 (MPEG-1 Audio Layer 3) ; AAC (Advanced Audio Coding) ; Opus ». Le RGESN ne cite pas le MP3 parmi les codecs efficaces : il ne l'accepte qu'en repli ;
- son principe de validation compte aussi les « codecs audio propriétaires (non libres) », ce qui vise AAC et les codecs Dolby, que le RGESN classe parmi les codecs efficaces.

Un service peut satisfaire les deux avec **Opus** et un repli en **MP3** à 128 kbit/s au plus : Opus est efficace et libre, le MP3 est libre et accepté en repli par le RGESN. Seule exception, les flux RSS de podcast, pour lesquels AAC reste nécessaire (voir l'onglet « Formats et compatibilité »).

La fiche [**RWEB 0104 — « Encoder les sons en dehors du CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0104-encoder-les-sons-en-dehors-du-cms), notée **5/5** en priorité, ajoute un principe d'organisation : convertir et optimiser les sons avant de les mettre en ligne, car « un serveur web n'est pas optimisé pour le (ré)encodage des fichiers audio ».

{{% /tab %}}

{{% tab tabName="Le seuil de 1 Mo par minute" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le seuil de la « Mise en œuvre » se convertit en débit : 1 Mo par minute (1 000 000 octets) correspond à environ **133 kbit/s**. Le poids d'un fichier audio dépend presque uniquement de son débit et de sa durée. Pour une minute, au débit nominal :

| Encodage | Débit | Poids par minute | Une heure |
|---|---:|---:|---:|
| WAV, qualité CD (non compressé) | 1 411 kbit/s | 10,6 Mo | 635 Mo |
| MP3 ou AAC stéréo | 192 kbit/s | 1,44 Mo | 86 Mo |
| AAC stéréo | 160 kbit/s | 1,20 Mo | 72 Mo |
| MP3 ou AAC stéréo | 128 kbit/s | 0,96 Mo | 58 Mo |
| Opus stéréo (musique) | 96 kbit/s | 0,72 Mo | 43 Mo |
| AAC mono (parole) | 48 kbit/s | 0,36 Mo | 22 Mo |
| Opus mono (parole) | 24 kbit/s | 0,18 Mo | 11 Mo |

Trois enseignements :

- **Le seuil est large.** Un MP3 à 128 kbit/s, réglage courant, passe juste en dessous. Le seuil écarte les fichiers non compressés ou encodés à haut débit, pas les réglages moyens.
- **Pour la parole, on peut viser bien plus bas.** Un entretien d'une heure pèse 58 Mo en MP3 stéréo à 128 kbit/s et 11 Mo en Opus mono à 24 kbit/s, soit cinq fois moins.
- **Le seuil n'est pas une condition du moyen de test.** Le RGESN le place dans la « Mise en œuvre » (« Éviter… »). Seuls le codec et la documentation conditionnent la validation. Le seuil reste un bon indicateur de contrôle, et c'est le principe de validation de la fiche RWEB 0105.

Le guide de The Shift Project présenté au [critère 5.4](../5-4_compression-videos/) juge le gain « minime » sous 160 kbit/s pour la piste son d'une vidéo, et conseille de garder le débit d'origine. Pour un contenu audio seul, un tel réglage dépasse le seuil : 1,2 Mo par minute à 160 kbit/s.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Contributeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.6 dans sa section [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons), déjà présentée aux critères 5.3 à 5.5 : « Proposer des audios dont le mode de compression est efficace et adapté au contenu et au contexte d'écoute permet de valider le critère 5.6 ».

Le guide conseille : « beaucoup de bandes sonores peuvent être compressées en mp3 avec des logiciels comme Adobe Audition, l'encodeur gratuit Lame ou encore des sites gratuits sans perte notable pour l'utilisateur final ». Au sens du RGESN, le MP3 n'est qu'un format de repli : Opus ou AAC donnent un fichier plus léger à qualité égale.

Il ajoute que « dans le secteur musical ou cinématographique, il sera préférable de ne pas compresser les fichiers ». Le conseil vaut pour la production et l'archivage, où un fichier sera retravaillé : MDN recommande alors d'éviter la compression avec perte, qui s'aggrave à chaque réencodage. Pour la **diffusion**, même musicale, le RGESN demande au contraire un codec efficace, en stéréo et à un débit adapté. Un fichier non compressé pèse plus de 10 Mo par minute (voir l'onglet précédent).

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) consacre deux conseils au son. Le premier, [« Est-ce que la définition du son est adaptée ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-les-sons-diffuses-par-le-service-sont-fea704), dans la [recommandation n°9 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=9), propose un test simple : « La qualité de son attendue est-elle spécifiée ? » Il énumère les leviers : « leurs durées, le nombre de répétitions, la qualité du son et enfin le type d'encodage (Codec) utilisé ». La **durée** reste le premier levier : à débit égal, un épisode deux fois plus court pèse deux fois moins.

Le second, [« Est-ce que les CODECS des sons sont compressés au maximum ? »](https://gr491.isit-europe.org/crit.php?id=3-contenus-le-volume-de-donnees-utilise-par-la-a013d4), déjà cité au critère 5.4, demande de vérifier que la qualité réduite reste « compréhensive ».

Les deux conseils mettent en garde contre le coût du décodage : certains codecs très compressés demanderaient « beaucoup de ressources de traitements, ce qui atténue fortement le bénéfice global ». Pour la vidéo, c'est un vrai sujet (voir le critère 5.4). Pour l'audio, il pèse peu : d'après MDN, l'API Media Capabilities des navigateurs considère tous les codecs audio pris en charge comme économes en énergie (« All supported audio codecs report `powerEfficient` as true »).

{{% /tab %}}

{{% tab tabName="Formats et compatibilité" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

D'après [Can I use](https://caniuse.com/) (consulté le 20 octobre 2026), en part des navigateurs utilisés dans le monde :

| Codec | Prise en charge | Remarque | Au sens du RGESN |
|---|---:|---|---|
| [Opus](https://caniuse.com/opus) | 92,84 % (+ 4,42 % partielle) | Safari sur macOS : uniquement à partir de macOS 15.4 | Efficace |
| [AAC](https://caniuse.com/aac) | 94,77 % (+ 2,72 % partielle) | Firefox : uniquement dans un conteneur MP4, si le système fournit le décodeur | Efficace |
| [MP3](https://caniuse.com/mp3) | 97,49 % | Lisible partout | Repli seulement |

L'affirmation du RGESN (« L'ensemble des navigateurs web supportent » Opus en WebM et AAC en MP4) est donc vraie à quelques exceptions près, qui se compensent : proposer **les deux** couvre la quasi-totalité des navigateurs.

Deux autres critères entrent dans le choix :

- **Les licences.** D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs), AAC est un format soumis à brevets (« patent-encumbered »), tandis que les brevets du MP3 ont expiré. Opus est libre.
- **Les podcasts.** Un flux RSS ne propose en pratique qu'un fichier par épisode (une seule balise `enclosure`), sans repli possible. Or, d'après ses [exigences audio](https://podcasters.apple.com/support/893-audio-requirements), Apple Podcasts n'accepte dans les flux RSS que « MP3 or AAC formats », et recommande « strongly » AAC. Pour la parole en mono, Apple indique 40 à 80 kbit/s à 22,05 ou 24 kHz. Un podcast diffusé par RSS sera donc en **AAC**, avec Opus en version principale sur le site si on le souhaite.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

**1. Encoder une fois, avant la mise en ligne** (fiche RWEB 0104), à partir du fichier original non compressé. Selon le contenu :

```bash
# Parole (podcast, conférence, entretien) : Opus mono, 24 kbit/s
ffmpeg -i entretien.wav -c:a libopus -b:a 24k -ac 1 entretien.webm

# Repli et flux RSS : AAC mono, 48 kbit/s à 24 kHz
ffmpeg -i entretien.wav -c:a aac -b:a 48k -ac 1 -ar 24000 -movflags +faststart entretien.m4a

# Musique : Opus stéréo, 96 kbit/s
ffmpeg -i concert.wav -c:a libopus -b:a 96k concert.webm
```

- **Débit** : 24 kbit/s en mono pour un livre audio ou un podcast, 64 à 96 kbit/s en stéréo pour de la musique sont les valeurs du [wiki de Xiph.Org](https://wiki.xiph.org/Opus_Recommended_Settings), qui invite à les ajuster à l'écoute. Pour AAC, les valeurs viennent des exigences d'Apple Podcasts.
- **Canaux** : `-ac 1` passe en mono, comme le demande le RGESN pour les dialogues. Une interview enregistrée en stéréo ne contient en général pas d'information spatiale utile.
- **Fréquence d'échantillonnage** : avec Opus, il n'y a rien à régler. L'encodeur choisit lui-même la bande de fréquences restituée selon le débit, et restitue toute la bande audible dès 16 kbit/s en mono pour la voix, d'après le même wiki. Avec AAC, `-ar 24000` suit la recommandation d'Apple pour la parole à bas débit.
- **Qualité** : réécouter le résultat au casque, sur un passage exigeant (voix aiguë, musique de générique, rires). Si des défauts apparaissent, monter d'un cran, comme pour les images au critère 5.2.

**2. Proposer les deux formats dans l'élément `<audio>`.** Le navigateur prend le premier qu'il sait lire et ne télécharge que lui :

```html
<audio controls preload="none">
  <source src="entretien.webm" type='audio/webm; codecs="opus"'>
  <source src="entretien.m4a" type='audio/mp4; codecs="mp4a.40.2"'>
</audio>
<p><a href="entretien.m4a" download>Télécharger l'entretien (AAC, 22 Mo)</a></p>
```

`preload="none"` évite tout téléchargement avant la lecture (fiche RWEB 0106, critère 4.1). Le lien de téléchargement indique le poids du fichier, comme le demande le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) au-delà de 10 Mo.

**3. Contrôler le seuil de 1 Mo par minute** sur tous les fichiers audio publiés, avec `ffprobe` (fourni avec FFmpeg) :

```bash
for f in *.webm *.m4a *.mp3; do
  [ -e "$f" ] || continue
  ffprobe -v error -show_entries format=duration,size -of csv=p=0 "$f" \
    | awk -F, -v f="$f" '{ r = $2 / 1e6 / ($1 / 60); printf "%s : %.2f Mo/min%s\n", f, r, (r > 1 ? "  <- au-dessus de 1 Mo/min" : "") }'
done
```

Testée le 20 octobre 2026 sur une source de test de 60 secondes (bruit et son sinusoïdal), la commande affiche 0,17 Mo/min pour l'Opus mono à 24 kbit/s, 0,37 Mo/min pour l'AAC mono à 48 kbit/s et 1,44 Mo/min, au-dessus du seuil, pour un MP3 à 192 kbit/s.

**4. Documenter**, comme l'exige le moyen de test, dans la déclaration d'écoconception. Par exemple :

| Type de contenu | Codec | Repli | Débit | Canaux |
|---|---|---|---:|---|
| Podcasts et entretiens | Opus (WebM) | AAC (MP4), aussi utilisé dans le flux RSS | 24 kbit/s (repli : 48 kbit/s) | Mono |
| Musique | Opus (WebM) | AAC (MP4) | 96 kbit/s (repli : 128 kbit/s) | Stéréo |

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le critère 5.6 s'applique aux contenus audio seuls, mais il est lié aux deux critères vidéo qui le précèdent, déjà publiés sur ce site :

- le [critère 5.4](../5-4_compression-videos/) (compression des vidéos) renvoie au 5.6 pour la piste son des vidéos : mêmes codecs, même choix entre mono et stéréo ;
- le [critère 5.5](../5-5_ecoute-seule/) (mode « écoute seule ») : dans ce mode, la piste son est tout ce qui est transféré. Une piste en AAC stéréo à 128 kbit/s réduit fortement le gain, une piste en Opus mono à 24 kbit/s le maximise.

Plusieurs critères UX/UI, déjà publiés, entrent aussi en jeu :

- le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) (choix du format le plus sobre) : pour une conférence ou un entretien, l'audio seul peut remplacer la vidéo ;
- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) (poids et formats des fichiers) : un épisode d'une heure en MP3 à 128 kbit/s dépasse 10 Mo, son poids doit être affiché avant le téléchargement ;
- le [critère 4.1](../../ux-ui/4-1_lecture-automatique/) (lecture automatique) : un son qui ne se lance pas tout seul n'est pas téléchargé pour rien.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque le critère 5.6 **« Non applicable »** : « Pas d'audio ».

Trois fichiers audio publics, issus de deux services, analysés avec `ffprobe` le 20 octobre 2026 :

| Fichier | Codec | Canaux | Débit | Poids par minute |
|---|---|---|---:|---:|
| Chronique du podcast France Inter [« Signé Anne Rosencher »](https://radiofrance-podcast.net/podcast09/podcast_34fde451-ca3d-463e-b8b3-fe132776cd78.xml) (3 min 01, épisode du 3 juillet 2026) | AAC | Stéréo | 192 kbit/s | 1,46 Mo |
| Version audio d'un entretien de 56 min sur [Framatube](https://framatube.org/) (PeerTube), fichier pour les podcasts | AAC | Stéréo | 109 kbit/s | 0,83 Mo |
| Même entretien, version audio du lecteur HLS | AAC | Stéréo | 129 kbit/s | 0,98 Mo |

Tous ces fichiers utilisent un codec efficace au sens du RGESN : la condition de codec du moyen de test est remplie. Mais il s'agit de parole, encodée en stéréo à un débit pensé pour la musique :

- **Radio France** dépasse le seuil de 1 Mo par minute. Le flux RSS annonce pourtant 2 896 000 octets pour cet épisode, ce qui correspondrait à 128 kbit/s ; le fichier servi en pèse 4 405 209. En AAC mono à 48 kbit/s, la recommandation d'Apple pour la parole, la chronique pèserait quatre fois moins.
- **PeerTube** conserve le débit audio du fichier envoyé (dans la limite de 384 kbit/s) et force la stéréo quand il réencode le son, comme l'indique un commentaire de son [code source](https://github.com/Chocobozzz/PeerTube/blob/develop/packages/ffmpeg/src/ffmpeg-default-transcoding-profile.ts) (« Force stereo as it causes some issues with HLS playback in Chrome »). Le réglage audio se fait donc **avant** l'envoi, comme le recommande la fiche RWEB 0104. En Opus mono à 24 kbit/s, cet entretien de 56 minutes pèserait environ 10 Mo, contre 47 et 55 Mo.

{{% /tab %}}

{{< /tabs >}}
