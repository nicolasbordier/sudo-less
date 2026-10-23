---
weight: 100
title: "5.1 - Format de fichier adapté à chaque image"
description: "Critère 5.1 du RGESN : choisir le bon format pour chaque image (SVG, WebP, AVIF, JPEG XL), prévoir un format de repli pour les navigateurs non compatibles et vérifier le seuil de 75 % d'images dans un format efficace."
icon: "image"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un format de fichier adapté au contenu et au contexte de visualisation de chaque image ?

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
| **Critère**  | `5.1` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas d'image matricielle (ou images bitmap)` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

La réduction des volumes de données transmises associées aux images matricielles (ou images bitmap) est un levier d'optimisation du trafic internet et de minimisation de la consommation en ressources associée. L'objectif est donc d'optimiser le poids des fichiers téléchargés par les utilisateurs en utilisant des formats d'image performants.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Choisir le format image adapté à la typologie d'image et au contexte d'affichage :

- Format vectoriel (exemple SVG) : utiliser ce format lorsque cela est possible (illustrations, icônes, logos, graphes...);
- Format matriciel, compression sans perte ou « lossless » (c'est le mode de compression du PNG) : pour des illustrations avec aplats de couleur (remplacer le PNG peu efficace par des images WebP ou JPEG XL, en mode « compression sans perte »);
- Format matriciel, compression avec perte (c'est le mode de compression du JPEG) : pour des photos ou des illustrations avec des milliers de couleurs (remplacer le JPEG peu efficace par des images WebP, AVIF ou JPEG XL en mode « compression avec perte »).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier périodiquement que les images matricielles ne sont plus dans les formats JPEG, PNG ou GIF. Utiliser WebP, AVIF, JPEG XL ou un format d'image plus performant pour les images matricielles. Le critère est validé si plus de 75 % des images matricielles utilisées pour le service numérique sont dans un format efficace (WebP, AVIF, JPEG XL ou un format d'image plus performant).

Un service numérique qui propose chaque image dans deux formats (exemple : JPEG XL avec un fallback vers JPEG / PNG pour les navigateurs non compatibles) valide également le critère si un des formats est WebP, AVIF, JPEG XL ou un format d'image plus performant.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer UX/UI`

Le critère 5.1 a une correspondance directe dans la [recommandation n°2 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=2) du [GR491](https://gr491.isit-europe.org/) (INR), « Réduire l'empreinte des contenus statiques ». Son critère [« Est-ce que les images ont été compressées en amont dans un format adapté pour sa visualisation ? »](https://gr491.isit-europe.org/crit.php?id=2-contenus-la-transmission-de-donnees-compressees-est-indispensable-dc507e) est classé **incontournable**, en priorité **High**. Son premier test recoupe la règle du double format du RGESN : « Chaque image utilise-t-elle un format standard du web et propose une alternative pour certains formats optimisés qui ne seraient pas disponibles sur tous les environnements ? »

Ses précisions apportent une nuance que le RGESN n'aborde pas : « les algorithmes de compression sont consommateurs de ressources techniques de traitement, de stockage intermédiaire. Lorsque les compressions sont effectuées à chaque demande d'échange, le bénéfice de la compression peut disparaître ou même augmenter l'impact. » Convertir une image en AVIF ou en WebP doit donc se faire **une fois**, à la publication ou au build, et non à chaque affichage.

Dans la famille Frontend, le critère [« Les différents formats d'images disponibles ont-ils été évalués pour ne retenir que le plus efficace ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-les-services-numeriques-utilisent-des-images-a-a37a8d), lui aussi en priorité **High**, propose un indicateur simple à suivre : « Quel est le volume total des images du service ? »

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a deux fiches explicitement étiquetées « RGESN 5.1 », toutes deux notées **4/5** sur l'échelle d'impact environnemental.

[**RWEB 0038 — « Eviter d'utiliser des images matricielles pour l'interface »**](https://rweb.greenit.fr/fr/fiches/RWEB_0038-eviter-d-utiliser-des-images-matricielles-pour-l-interface) part de la première ligne de la « Mise en œuvre » du RGESN, le format vectoriel, et la pousse plus loin : avant même le SVG, elle recommande de remplacer les images d'interface par des styles CSS ou des glyphes, pour que l'internaute n'ait « aucune ressource supplémentaire à télécharger ». Son exemple chiffre l'écart pour une image de 198 × 198 pixels :

| Format | Poids |
|---|---:|
| Matriciel non compressé | 118 Ko |
| JPEG (compression à 90 %) | 6,5 Ko |
| PNG | 3,8 Ko |
| SVG minifié | 0,7 Ko |

Principe de validation : **5** images matricielles au plus par URL testée, pour l'interface.

[**RWEB 0049 — « Optimiser les images »**](https://rweb.greenit.fr/fr/fiches/RWEB_0049-optimiser-les-images) traite les images matricielles. Elle donne un ordre de grandeur entre formats : « En moyenne, une image .webp est 30 % plus légère qu'une image .jpg ou .png mais 20 % plus lourde qu'une image .avif ». Elle montre aussi comment proposer deux formats avec l'élément `<picture>`, en laissant le navigateur choisir.

Une troisième fiche, [**RWEB 0100 — « Optimiser les images vectorielles »**](https://rweb.greenit.fr/fr/fiches/RWEB_0100-optimiser-les-images-vectorielles), non rattachée au RGESN, rappelle que le SVG n'est pas léger par nature. Les fichiers exportés depuis un logiciel de dessin contiennent souvent des métadonnées inutiles à l'affichage, que des outils comme SVGO suppriment. Dans l'exemple de la fiche, un SVG passe de 1 101 à 700 octets.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.1 dans sa section [**7.1 Images**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-1-images). Il rappelle l'enjeu : d'après les données du HTTP Archive qu'il cite, les images représentaient en 2022 « en moyenne 44 % du poids d'une page web ».

Le guide apporte deux nuances utiles au choix du format :

- **Le SVG n'est pas toujours le plus léger** : « Si un fichier .svg est très complexe, il peut être plus lourd qu'un fichier .png. Il convient de faire des tests et de prendre la décision la plus pertinente. »
- **WebP ou AVIF ?** Le guide chiffre l'impact d'un format mal pris en charge : « En avril 2025, au moins 1,12 % de la population française n'avait pas une version de navigateur supportant le format AVIF », soit « plus de 570 000 personnes », contre « seulement 0,35 % » pour WebP. D'où sa recommandation : utiliser WebP « si vous n'avez pas les compétences techniques pour prévoir un backup pour de l'AVIF ».

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) en tire la même règle : « si vous choisissez le format AVIF ou JPEG XL, le service numérique devra encoder ses images dans un deuxième format afin de prendre en charge les navigateurs web qui ne supportent pas encore ces formats (fallback en JPEG / PNG ou WebP) ».

{{% /tab %}}

{{% tab tabName="Compatibilité des navigateurs" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Les trois formats cités par le RGESN ne sont pas pris en charge de la même façon. D'après les données de [Can I use](https://caniuse.com/) consultées le 20 octobre 2026, en part des navigateurs utilisés dans le monde :

| Format | Prise en charge complète | Remarque |
|---|---:|---|
| [WebP](https://caniuse.com/webp) | 97,08 % | Utilisable seul dans la plupart des cas |
| [AVIF](https://caniuse.com/avif) | 96,33 % | Prévoir un repli (WebP ou JPEG) pour les navigateurs anciens |
| [JPEG XL](https://caniuse.com/jpegxl) | 43,26 % (+ 16,93 % partielle) | Récemment ajouté à Chrome et Firefox ; pas encore pris en charge par Edge ni Samsung Internet. Repli indispensable |

Le RGESN cite JPEG XL à égalité avec WebP et AVIF, mais en octobre 2026, un service qui n'utiliserait que du JPEG XL afficherait des images manquantes pour une part importante de ses utilisateurs. C'est pour ce cas que le moyen de test prévoit explicitement la validation « dans deux formats ».

Ce repli rejoint le [critère 2.4](../../specifications/2-4_anciennes-versions-os/) (anciennes versions d'OS et de navigateurs), déjà publié sur ce site : un format récent sans repli exclut précisément les utilisateurs des terminaux les plus anciens. Avec l'élément `<picture>`, le navigateur ne télécharge qu'**un seul** des formats proposés. Prévoir un repli ne coûte donc rien en transfert aux navigateurs récents, seulement un peu de stockage côté serveur.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

**1. Choisir le format selon le type d'image**, en reprenant la « Mise en œuvre » du RGESN :

| Type d'image | Format à privilégier | Repli |
|---|---|---|
| Icône, logo, schéma, graphique | SVG optimisé (ou CSS, glyphe) | — |
| Illustration en aplats de couleurs, capture d'écran | WebP sans perte | PNG |
| Photo | AVIF ou WebP avec perte | JPEG |

**2. Convertir une fois, à la publication** (et non à chaque affichage, voir l'onglet GR491), par exemple en ligne de commande :

```bash
# Photo : AVIF et WebP avec perte
avifenc -q 60 photo.jpg photo.avif
cwebp -q 75 photo.jpg -o photo.webp

# Illustration en aplats : WebP sans perte
cwebp -lossless schema.png -o schema.webp

# SVG : suppression des métadonnées inutiles
npx svgo logo.svg
```

Sans ligne de commande, [Squoosh](https://squoosh.app/), une application web open source de Google Chrome Labs, fait la même conversion dans le navigateur : AVIF, WebP et JPEG XL, ainsi que MozJPEG et OxiPNG pour les formats de repli. Son curseur de comparaison avant/après affiche en direct le rendu et le poids obtenus. On peut ainsi régler la qualité en fonction de l'image elle-même plutôt que d'appliquer une valeur fixe. D'après le [README du projet](https://github.com/GoogleChromeLabs/squoosh), les images sont traitées localement, sans être envoyées à un serveur ; le site utilise en revanche Google Analytics. Le traitement se fait image par image. Pour un grand nombre d'images, on peut s'en servir pour trouver la bonne qualité sur quelques images types, puis l'appliquer en ligne de commande ou au build.

Pour un site statique, le générateur peut s'en charger au build. Avec Hugo, par exemple, une seule ligne produit une version WebP redimensionnée, mise en cache entre deux builds :

```go-html-template
{{ $photo := resources.Get "images/photo.jpg" }}
{{ $webp := $photo.Resize "800x webp q75" }}
<img src="{{ $webp.RelPermalink }}" width="{{ $webp.Width }}" height="{{ $webp.Height }}" alt="…">
```

**3. Proposer plusieurs formats avec `<picture>`.** Le navigateur prend le premier format qu'il sait afficher et ne télécharge que celui-là :

```html
<picture>
  <source srcset="photo.avif" type="image/avif">
  <source srcset="photo.webp" type="image/webp">
  <img src="photo.jpg" alt="…" width="800" height="533" loading="lazy">
</picture>
```

**4. Vérifier le seuil de 75 %**, page par page. Dans la console des outils de développement, ce script compte les images matricielles réellement affichées et la part servie dans un format efficace :

```js
const matricielles = [...document.images]
  .map((img) => img.currentSrc)
  .filter((src) => src && !src.startsWith('data:') && !/\.svg(\?|$)/i.test(src));
const efficaces = matricielles.filter((src) => /\.(webp|avif|jxl)(\?|$)/i.test(src));
console.log(`${efficaces.length} / ${matricielles.length} images matricielles dans un format efficace`,
  `(${Math.round((100 * efficaces.length) / matricielles.length)} %)`);
```

La propriété `currentSrc` donne le fichier réellement choisi par le navigateur dans un `<picture>`. Le script se fie à l'extension du fichier. Il ne compte pas les images d'arrière-plan CSS, à vérifier séparément dans l'onglet **Réseau**, filtre **Img**.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le critère 5.1 intervient **après** deux questions traitées par des critères déjà publiés sur ce site :

- le [critère 4.6](../../ux-ui/4-6_contenu-porteur-information/) : ce média est-il porteur d'information, ou seulement décoratif ?
- le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) : faut-il une image, ou un texte suffirait-il ?

Une fois l'image jugée utile, le 5.1 porte sur le **format** du fichier. Le [critère 5.2](../5-2_compression-images/) (niveau de compression adapté), qui le suit directement dans le RGESN, porte sur la **qualité** et la **taille** d'encodage. Les deux se complètent : une photo en AVIF mais en 4 000 pixels de large reste bien plus lourde qu'une photo en JPEG redimensionnée à sa taille d'affichage. Les Designers Éthiques donnent l'exemple d'une photo de 1,4 Mo rendue « 14 fois plus légère » par redimensionnement, ajustement de la qualité et compression.

Enfin, la règle du double format renvoie au [critère 2.4](../../specifications/2-4_anciennes-versions-os/) (anciennes versions de navigateurs) : voir l'onglet « Compatibilité des navigateurs ».

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »** : « La plupart des images sont au format svg et webp. Certaines sont en PNG mais elles sont très légères et comprises entre 1 et 4 Ko. » La justification combine les deux leviers du critère : le vectoriel (SVG) quand c'est possible, un format matriciel efficace (WebP) sinon. Les quelques PNG restants ne remettent pas en cause la validation, puisque le seuil porte sur la **proportion** d'images (plus de 75 %) et non sur leur poids.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) le marque **« Non applicable »** : « Les seules images utilisées sont les logos et bannières chargées une seule fois (produit web de type SPA), dont le poids de données transférés est inférieur à 40 ko. » Le RGESN ne prévoit toutefois la non-applicabilité que si le service « n'utilise pas d'image matricielle ». Si ces logos et bannières sont des images matricielles, le critère s'applique au sens strict. Leur faible poids justifie de ne pas en faire une priorité, pas de déclarer le critère non applicable.

Deux sites déjà analysés pour le [critère 4.15](../../ux-ui/4-15_controle-usages/) appliquent la règle du double format (constaté le 20 octobre 2026). [Niji](https://www.niji.fr/fr/) sert ses photos dans un `<picture>` en AVIF, puis WebP, puis JPEG en dernier recours. Le [Low-tech Lab](https://lowtechlab.org/fr/actualites-blog) propose les images de ses articles en WebP, avec un repli en PNG.

{{% /tab %}}

{{< /tabs >}}
