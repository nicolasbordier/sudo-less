---
weight: 200
title: "5.2 - Niveau de compression adapté à chaque image"
description: "Critère 5.2 du RGESN : redimensionner les images, régler leur qualité de compression d'après le rendu plutôt qu'avec une valeur fixe, proposer plusieurs résolutions et documenter sa politique de qualité."
icon: "compress"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique propose-t-il des images dont le niveau de compression est adapté au contenu et au contexte de visualisation ?

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
| **Critère**  | `5.2` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas d'image matricielle (ou images bitmap)` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire le poids des images téléchargées par les utilisateurs en augmentant le niveau de compression (et donc en dégradant légèrement la qualité) ou/et en proposant des résolutions multiples.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Lors de la génération d'une image matricielle, en mode compression avec perte (c'est le mode de compression du JPEG), la compression à une qualité de 70 % (JPEG), 72 % (WebP) ou 56 % (AVIF) peut être visuellement acceptable.

Tableau pour faire une conversion approximative de la qualité de compression (en %) entre JPEG, WebP et AVIF : (source [industrialempathy.com](https://www.industrialempathy.com/posts/avif-webp-quality-settings/))

| JPEG | WebP (compression avec perte) | AVIF (compression avec perte) |
|---:|---:|---:|
| 50 (qualité faible) | 55 (qualité faible) | 48 (qualité faible) |
| 60 | 64 | 51 |
| 70 | 72 | 56 |
| 80 (qualité élevée) | 82 (qualité élevée) | 64 (qualité élevée) |

Les formats de compression sans perte de la qualité de l'image (PNG, WebP en mode « compression sans perte », JPEG XL en mode « compression sans perte ») ne disposent pas de paramétrage de qualité, la compression ne dégradant pas la qualité de l'image. Il est toutefois possible de réduire significativement la taille en réduisant la palette de couleurs de l'image avant compression.

Des résolutions multiples peuvent être pertinentes, via les attributs « srcset » et « sizes », afin de s'adapter automatiquement à la résolution du terminal depuis lequel est consulté le site. Il faut toutefois faire attention que cela n'empêche pas le service d'adopter un « Responsive design ».

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Évaluer la qualité et le poids des images matricielles affichées sur différents types de terminaux.

Pour le mode de compression avec perte, documenter dans la déclaration d'écoconception la politique de paramétrage de la qualité lors de la génération ou conversion des images.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer UX/UI`

Le critère 5.2 prolonge le [critère incontournable du GR491](https://gr491.isit-europe.org/crit.php?id=2-contenus-la-transmission-de-donnees-compressees-est-indispensable-dc507e) déjà cité au [critère 5.1](../5-1_format-images/), dont le second test porte précisément sur la compression : « Chaque image utilise-t-elle un degré de compression adapté au rendu de l'image sur le service numérique ? »

Deux critères de la [recommandation n°9 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=9) (« Implémenter des solutions techniques dont l'impact est le plus faible ») apportent des précisions utiles :

- [« Est-ce que la définition de l'image est réduite et adaptée à son objectif (illustration, contractuel, ...) ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-les-images-dillustration-et-les-images-qui-a54c72). Ce critère distingue les images selon leur rôle : « Les images d'illustration et les images qui portent une information plus contractuelle comme l'image d'un produit n'ont pas les mêmes besoins de précisions de qualité. » Une seule valeur de qualité pour tout le service ne tient pas compte de cette différence.
- [« Les redimensionnements d'images sont-ils traités en amont et en statique (côté serveur) ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-les-services-utilisent-plusieurs-tailles-dune-meme-d5e548), en priorité **High** : le redimensionnement « effectué à la demande génère des charges de traitements, des productions de fichiers intermédiaires qui introduisent des déperditions d'énergie à chaque demande ». Les différentes tailles proposées dans un `srcset` doivent donc être produites une fois, à l'avance.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche image étiquetée « RGESN 5.2 », mais la fiche [**RWEB 0048 — « Ne pas redimensionner les images côté navigateur »**](https://rweb.greenit.fr/fr/fiches/RWEB_0048-ne-pas-redimensionner-les-images-cote-navigateur), notée **4/5** en impact environnemental, couvre le second levier du critère : les résolutions multiples. Elle part d'un principe simple : « la taille d'affichage d'une image dans le navigateur doit être la plus proche possible de celle du fichier image téléchargée ».

Son exemple montre l'enjeu : une image de 350 × 300 pixels en PNG pèse 41 Ko ; affichée en vignette à 70 × 60 pixels, elle pèse toujours 41 Ko, « alors qu'elle ne devrait pas dépasser 3 Ko ». La fiche recommande de « bien définir les attributs srcset ou sources pour que chaque type d'appareil utilise une version d'image adaptée à la taille et à la résolution de son écran ».

Son principe de validation donne un seuil chiffré que le RGESN ne fixe pas : les kilo-octets téléchargés inutilement doivent rester **inférieurs ou égaux à 5 % du total**.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Contributeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.2 dans sa section [**7.1 Images**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-1-images). Il décompose l'optimisation d'une photo de 2800 × 3823 pixels, étape par étape :

| Étape | Taille | Poids |
|---|---|---:|
| Photo d'origine | 2800 × 3823 px | 1,4 Mo |
| Après redimensionnement | 640 × 874 px | 123 Ko |
| Après redimensionnement et qualité à 70 % | 640 × 874 px | 90 Ko |
| Après redimensionnement, qualité et compression | 640 × 874 px | 72 Ko |

Le tableau montre l'ordre des priorités. Le **redimensionnement** fait passer la photo de 1,4 Mo à 123 Ko, soit plus de 90 % de gain à lui seul. Le réglage de la qualité et la compression font ensuite descendre de 123 à 72 Ko. Le guide rappelle qu'une photo non redimensionnée fait souvent « entre 2000 et 4000 pixels de largeur », pour être affichée « à environ 700 ou 800 pixels de largeur ».

Le guide met aussi en garde contre une pratique courante des sites écoconçus, le tramage (*dithering*) : « la perte de poids n'est pas systématique », et ce rendu « peut également gêner la compréhension et l'interprétation des images pour certains publics avec un handicap visuel ».

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) reprend la valeur de référence du RGESN : « On estime qu'un JPEG peut être compressé de 70 % tout en restant visuellement acceptable. »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C, déjà citée aux critères [4.6](../../ux-ui/4-6_contenu-porteur-information/), [4.7](../../ux-ui/4-7_choix-sobre-format/) et [4.12](../../ux-ui/4-12_impacts-fonctionnalites/), couvre les deux volets du critère 5.2 :

- **Optimized media** : « Resize, optimize, and compress media for different screen sizes, devices, and user needs. »
- **Media management and use** : « Create a media management and usage policy. Include guidance on compression, rendering performance, file formats, data retention, storage, review, and deletion. »

Le second critère de succès fait écho à l'exigence documentaire du RGESN (« documenter dans la déclaration d'écoconception la politique de paramétrage de la qualité »), mais sur un périmètre plus large. Le W3C demande une politique écrite pour **tous** les médias, qui couvre aussi la durée de conservation et la suppression. Ce dernier point rejoint le [critère 5.8](../5-8_archivage-suppression/) du RGESN (archivage et suppression des contenus obsolètes).

{{% /tab %}}

{{% tab tabName="D'où viennent les valeurs de référence ?" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Les valeurs du tableau de la « Mise en œuvre » (70 % en JPEG, 72 % en WebP, 56 % en AVIF) viennent d'un [article de Malte Ubl publié en février 2021](https://www.industrialempathy.com/posts/avif-webp-quality-settings/). Sa méthode explique à la fois leur intérêt et leurs limites :

- l'auteur a encodé des images JPEG, AVIF et WebP à de nombreux niveaux de qualité, puis mesuré leur différence visuelle avec l'original à l'aide de l'outil **dssim** ;
- pour chaque qualité JPEG, il a retenu la qualité AVIF et WebP qui produit **la même différence visuelle**. Le tableau établit donc une **équivalence** entre formats, pas une qualité idéale ;
- les données proviennent de **4 images seulement** (un paysage, une personne, des fleurs, une architecture), encodées avec la bibliothèque sharp.

L'auteur le dit lui-même : « Results with different encoders may vary », et ses images d'exemple « may not be representative for the images on your website and you may require different encoding settings ».

Ces valeurs sont un bon **point de départ**, en particulier pour convertir une qualité JPEG connue vers WebP ou AVIF. Elles ne remplacent pas un réglage sur les images du service lui-même, d'autant que le GR491 rappelle qu'une illustration et une photo de produit n'ont pas les mêmes besoins. C'est la démarche proposée dans l'onglet « Mise en œuvre technique ».

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`, `Designer`

**1. Redimensionner d'abord.** C'est le levier le plus important (voir l'onglet Designers Éthiques). Aucune image ne devrait être plus large que sa plus grande taille d'affichage, multipliée au besoin par la densité d'écran visée.

**2. Régler la qualité d'après le rendu, avec [Squoosh](https://squoosh.app/).** Squoosh, déjà présenté au [critère 5.1](../5-1_format-images/), affiche côte à côte l'original et l'image compressée, avec un curseur de comparaison et le poids obtenu en direct. Plutôt que d'appliquer une valeur fixe, on cherche pour chaque image la qualité la plus basse qui reste visuellement acceptable :

1. Ouvrir l'image et la **redimensionner** dans Squoosh à sa taille d'affichage réelle. Les défauts de compression ne se jugent qu'à cette taille : agrandis, ils paraissent toujours plus graves.
2. Choisir le format (AVIF ou WebP) et partir de la valeur de référence du RGESN (56 en AVIF, 72 en WebP).
3. Baisser la qualité progressivement en observant les zones les plus sensibles : **visages, texte, dégradés de ciel, contours nets**. C'est là que les défauts apparaissent en premier (aplats qui se forment, bavures autour des contours).
4. Dès qu'un défaut devient visible, remonter d'un ou deux crans, et noter la valeur et le poids obtenus.

Pour une illustration en aplats ou une capture d'écran compressée sans perte, l'option **« Reduce palette »** de Squoosh applique la réduction de palette recommandée par le RGESN pour les formats sans perte.

**3. Calibrer, puis automatiser.** Régler chaque image à la main reste réservé aux visuels importants (bannière, page d'accueil). Pour le reste, on calibre une fois par **catégorie d'images** :

- choisir 3 à 5 images représentatives de chaque catégorie (photos de personnes, paysages, captures d'écran avec du texte, illustrations…) ;
- trouver leur qualité avec Squoosh comme ci-dessus ;
- retenir pour la catégorie la valeur de l'image la plus exigeante, puis l'appliquer automatiquement à la conversion.

On obtient une **politique de qualité** propre au service, qui répond directement à l'exigence documentaire du moyen de test. Par exemple, à adapter :

| Catégorie | Format | Qualité retenue | Taille maximale |
|---|---|---:|---:|
| Photos d'illustration | AVIF (repli WebP) | à calibrer (référence RGESN : 56) | 1 200 px |
| Photos de produit (« contractuelles ») | AVIF (repli WebP) | à calibrer, plus élevée | 1 600 px |
| Captures d'écran avec texte | WebP sans perte, palette réduite | — | 1 200 px |

**4. Produire plusieurs résolutions au build**, et non à la demande (voir l'onglet GR491). Avec Hugo, par exemple :

```go-html-template
{{ $photo := resources.Get "images/photo.jpg" }}
{{ $petite := $photo.Resize "480x webp q72" }}
{{ $grande := $photo.Resize "960x webp q72" }}
<img src="{{ $petite.RelPermalink }}"
     srcset="{{ $petite.RelPermalink }} 480w, {{ $grande.RelPermalink }} 960w"
     sizes="(min-width: 60rem) 960px, 100vw"
     width="{{ $petite.Width }}" height="{{ $petite.Height }}" alt="…">
```

La qualité (`q72` ici) est celle issue du calibrage. Grâce à `srcset` et `sizes`, le navigateur choisit lui-même la version adaptée à la largeur d'affichage et à la densité de l'écran. L'image reste fluide : le responsive design n'est pas remis en cause.

**5. Contrôler sur différents terminaux**, comme le demande le moyen de test. Dans les outils de développement, le mode d'émulation des terminaux permet de simuler un mobile. En survolant une image dans l'onglet **Éléments**, on compare sa taille affichée (*rendered size*) à sa taille réelle (*intrinsic size*) : un écart important signale une image trop grande pour son affichage. Un contrôle final sur un vrai smartphone reste utile pour juger le rendu.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Ce critère forme une paire avec le [critère 5.1](../5-1_format-images/) (format de fichier adapté). Le 5.1 porte sur le **format** (AVIF, WebP, SVG…), le 5.2 sur la **taille** et la **qualité** d'encodage. Les deux se cumulent : un bon format mal dimensionné reste lourd, une bonne compression dans un format ancien aussi.

Le volet « résolutions multiples » rejoint le [critère 2.5](../../specifications/2-5_terminaux-affichage/) (terminaux d'affichage), dont il est la traduction pour les images : servir à chaque terminal une image adaptée à sa taille d'écran, sans dupliquer l'interface. Le [critère 6.4](../../frontend/6-4_dimensions-images/) (dimensions des images) en détaille la mise en œuvre : `srcset` et `sizes`, densité des écrans et redimensionnement à l'envoi des images des contributeurs.

Enfin, un niveau de compression plus fort peut faire partie d'un mode sobre au sens du [critère 4.15](../../ux-ui/4-15_controle-usages/). Les Designers Éthiques y citent par exemple « l'affichage des images au clic ».

Le RGESN demande de ne pas confondre ce critère avec le [critère 6.3](../../frontend/6-3_compression-ressources/), qui porte sur la compression des fichiers texte pendant le transfert (gzip, Brotli). Une image JPEG ou WebP, déjà compressée, n'y gagne rien ; une image SVG, qui est un fichier texte, en relève.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »**, avec deux éléments :

- « Présence de résolutions multiples : certaines images sont retirées en vue mobile car elle perdrait en visibilité. » Pour une image qui ne serait pas lisible sur un petit écran, la meilleure résolution mobile est parfois l'absence d'image.
- « Politique de paramétrage de la qualité, lors de l'enregistrement des images : N/A côté entrée utilisateur, oui côté images statiques. » La déclaration distingue les images du service, dont la qualité est maîtrisée, des images envoyées par les utilisateurs, qui ne sont pas retraitées. Elle indique en revanche qu'une politique existe sans en donner les valeurs. Publier le tableau de cette politique (format, qualité, taille maximale), comme dans l'onglet « Mise en œuvre technique », rendrait la déclaration vérifiable.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) le marque **« Non applicable »**, avec la même justification qu'au critère 5.1 : « Les seules images utilisées sont les logos et bannières chargées une seule fois (produit web de type SPA), dont le poids de données transférés est inférieur à 40 ko. » La même réserve s'applique : la non-applicabilité n'est prévue que si le service n'utilise aucune image matricielle (voir le [critère 5.1](../5-1_format-images/)).

Sur le site de [Niji](https://www.niji.fr/fr/), déjà cité aux critères 4.15 et 5.1, chaque photo de la page d'accueil est proposée en deux largeurs (375 et 768 pixels) dans chacun des trois formats (AVIF, WebP, JPEG), avec un attribut `sizes` qui laisse le navigateur choisir (constaté le 20 octobre 2026).

{{% /tab %}}

{{< /tabs >}}
