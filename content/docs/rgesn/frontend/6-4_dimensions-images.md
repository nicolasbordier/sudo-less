---
weight: 400
title: "6.4 - Dimensions des images adaptées à l'affichage"
description: "Critère 6.4 du RGESN : classer les images (vectorielles, à taille fixe, fluides), régler srcset et sizes en tenant compte de la densité de l'écran, redimensionner à l'envoi les images des contributeurs et contrôler le résultat sur plusieurs contextes d'affichage."
icon: "photo_size_select_large"
date: "2026-10-21T00:00:00+01:00"
lastmod: "2026-10-21T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique affiche-t-il majoritairement des images dont les dimensions d'origine correspondent aux dimensions du contexte d'affichage ?

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
| **Critère**  | `6.4` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de graphiques et/ou médias` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire ou limiter les données téléchargées en proposant un redimensionnement côté serveur pour les images dans une définition trop importante. Il s'agit également de minimiser la consommation d'énergie du terminal.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Les images matricielles (ou images bitmap) proposées par un service numérique sont soit affichées dans leur taille d'origine, soit proposées dans de multiples définitions, afin de ne pas charger une image avec une définition significativement supérieure à celle du contexte d'affichage utilisé par le client.

Lors de l'ajout des images matricielles au service numérique, les dimensions d'affichage sont requises ou un redimensionnement est réalisé côté serveur, lors de l'ajout du fichier par un contributeur.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour être validé ce critère, les images du service numérique doivent entrer dans une des trois catégories suivantes :

- Images vectorielles ;
- Images matricielles, affichées dans leur taille d'origine (pas de redimensionnement) ;
- Dans le cas d'images fluides (l'image occupe un pourcentage de la largeur du parent), plusieurs variantes d'images existent avec des définitions différentes, et la meilleure est proposée à l'écran, en fonction du contexte d'affichage.

Si le service numérique permet à un contributeur d'ajouter des images, un redimensionnement doit être réalisé côté serveur pour les images qui dépasseraient une certaine taille ou définition d'image.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="8">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche étiquetée « RGESN 6.4 ». La plus proche, déjà présentée au [critère 5.2](../../contenus/5-2_compression-images/), est [**RWEB 0048 — « Dimensionner correctement les images coté navigateur »**](https://rweb.greenit.fr/fr/fiches/RWEB_0048-ne-pas-redimensionner-les-images-cote-navigateur) (priorité 5/5) : « la taille d'affichage d'une image dans le navigateur doit être la plus proche possible de celle du fichier image téléchargée ». Elle apporte :

- **une mesure** : « Comparez le nombre de pixels de l'image chargée au nombre de pixels réellement affichés », la taille d'affichage étant surtout fixée par le CSS ;
- **un seuil**, que le RGESN ne donne pas : les kilo-octets téléchargés inutilement doivent rester **inférieurs ou égaux à 5 % du total**. DiaLog et le site du RGESN le dépassent sur ordinateur ;
- **un exemple à corriger** : dans `srcset="image_3ko.png 640w, image_41ko.png 1920w"`, le descripteur `w` doit donner la largeur réelle du fichier, ici 70 et 350 pixels. Et sans attribut `sizes`, le navigateur suppose que l'image occupe toute la largeur de l'écran.

Pour les images vectorielles, [**RWEB 0038 — « Eviter d'utiliser des images matricielles pour l'interface »**](https://rweb.greenit.fr/fr/fiches/RWEB_0038-eviter-d-utiliser-des-images-matricielles-pour-l-interface) (voir le [critère 5.1](../../contenus/5-1_format-images/)) : un logo en SVG n'a jamais de mauvaises dimensions.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La [recommandation n°9 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=9) du [GR491](https://gr491.isit-europe.org/) (INR) demande : [« Les alternatives de formats d'images sont-elles mises à disposition via srcset ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-la-selection-des-differentes-tailles-dimages-disponibles-acd0d6) Elle ajoute une réserve : « Cette technique n'est pas toujours la plus efficace du point de vue NR », d'où son test : « Les gains ont-ils été mesurés avec l'utilisation de srcset ? »

La réserve est fondée : `srcset` choisit l'image la plus **nette** pour l'écran, pas la plus légère. Sur smartphone, les photos de la page d'accueil du Musée d'arts de Nantes pèsent 1 460 Ko à la densité 3, contre 899 Ko à la densité 2 (voir l'onglet « Densité d'écran et srcset »).

Le critère [« Les redimensionnements d'images sont-ils traités en amont et en statique (côté serveur) ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-les-services-utilisent-plusieurs-tailles-dune-meme-d5e548), en priorité **High**, est détaillé au [critère 5.2](../../contenus/5-2_compression-images/).

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite le critère 6.4 dans sa section [**7.1 Images**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-1-images). Il demande au designer de fournir chaque image « en plusieurs résolutions au développeur », « à minima une pour Desktop et une pour Mobile ». Deux précisions :

- **la version mobile dépend de la densité de l'écran.** Un smartphone de 375 pixels de large et de densité 3 affiche 1 125 pixels physiques : une version mobile de 375 pixels y serait floue ;
- **l'exemple de code fait de la direction artistique.** `<picture>` avec des conditions `media` impose une version selon la largeur de l'écran, sans tenir compte de sa densité. C'est la technique pour un **cadrage** différent ; pour la même image en plusieurs tailles, `srcset` et `sizes` laissent le navigateur choisir.

Le guide renvoie aussi à [« La petite clinique des images responsives »](https://talks.nicolas-hoizey.com/b23Bwm/la-petite-clinique-des-images-responsives) de Nicolas Hoizey, qui passe en revue les erreurs courantes.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

La fiche [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) demande : « Resize, optimize, and compress media for different screen sizes, devices, and user needs. »

Les mots « user needs » vont plus loin que le RGESN : une personne qui agrandit la page pour la lire a besoin d'images plus nettes. Plafonner la résolution des images (voir l'onglet « Densité d'écran et srcset ») est donc un choix à faire en connaissance de cause.

{{% /tab %}}

{{% tab tabName="Densité d'écran et srcset" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**Le contexte d'affichage se compte en pixels physiques.** Un écran de densité 2 affiche 2 × 2 pixels physiques par pixel CSS (`window.devicePixelRatio`). La largeur utile d'une image est donc sa largeur d'affichage multipliée par la densité :

| Terminal | Largeur de l'écran | Densité | Largeur utile d'une image pleine largeur |
|---|---:|---:|---:|
| Ordinateur portable courant | 1 366 px | 1 | 1 366 px |
| Ordinateur à écran haute densité | 1 440 px | 2 | 2 880 px |
| Smartphone récent | 390 px | 3 | 1 170 px |

**Sans `sizes`, le navigateur suppose une image pleine largeur.** Il choisit dans le `srcset` avant la mise en page, d'après l'attribut `sizes`, qui vaut `100vw` par défaut. Testé dans Chromium 155, une image affichée à 300 pixels sur un ordinateur de 1 366 pixels : avec `sizes="100vw"`, il télécharge la version de **1 600 pixels**, plus de cinq fois trop large. Avec `sizes="auto"`, il prend celle de 400 pixels.

**`sizes="auto"` lit la vraie largeur**, mais seulement avec `loading="lazy"`, quand l'image est chargée après la mise en page. Pour les navigateurs qui ne le prennent pas en charge ([MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Reference/Elements/img#sizes)), on garde une liste après `auto` : `sizes="auto, (min-width: 62em) 600px, 100vw"`. WordPress l'ajoute de lui-même depuis sa [version 6.7](https://make.wordpress.org/core/2024/10/18/auto-sizes-for-lazy-loaded-images-in-wordpress-6-7/).

**La densité 3, un surcoût que l'œil ne voit pas.** En 2019, Twitter a plafonné ses images à la densité 2 : d'après son [blog d'ingénierie](https://blog.x.com/engineering/en_us/topics/infrastructure/2019/capping-image-fidelity-on-ultra-high-resolution-devices), elles se chargeaient alors « roughly 33% faster while using 1/3rd less data, and with no visible quality change ». Mesurée le 21 octobre 2026 sur un smartphone de 390 × 844 pixels, la page d'accueil du Musée d'arts de Nantes donne :

| Densité de l'écran | Poids des 11 photos | Poids de la page |
|---|---:|---:|
| 3 | 1 460 Ko | 1 928 Ko |
| 2 | 899 Ko | 1 368 Ko |

Le RGESN n'interdit pas de rester en deçà de la définition de l'écran : plafonner à la densité 2 est un choix sobre, à valider sur de vrais écrans (voir l'onglet « Mise en œuvre technique »).

{{% /tab %}}

{{% tab tabName="Le coût pour le terminal" %}}

Profil(s) métier concerné(s) : `Développeur`

Le RGESN vise « également » la consommation d'énergie du terminal. Avant d'afficher une image, le navigateur doit la **décoder** pixel par pixel, puis la réduire. Testé le 21 octobre 2026 dans Chromium 155 (`createImageBitmap`, médiane de 40 décodages, processeur AMD Ryzen 7 7735HS) :

| Image (WebP) | Fichier d'origine | Décodage | À la taille d'affichage | Décodage |
|---|---:|---:|---:|---:|
| Bannière du site du RGESN | 1 920 × 1 080 px | 12,5 ms | 792 × 446 px | 3,5 ms |
| Fond de carte de DiaLog | 2 377 × 1 137 px | 20,2 ms | 1 366 × 653 px | 9,0 ms |
| Image d'accueil de ce site | 1 600 × 1 200 px | 15,8 ms | 522 × 392 px | 2,6 ms |

Ces durées sont courtes sur un ordinateur récent, mais se répètent à chaque page, car le cache évite le téléchargement, pas le décodage. Elles s'allongent sur les terminaux anciens (voir le [critère 2.2](../../specifications/2-2_anciens-terminaux/)).

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`, `Contributeur`

**1. Classer les images selon les trois catégories du moyen de test.**

| Catégorie du RGESN | Exemples | À prévoir |
|---|---|---|
| Image vectorielle | Logo, icône, schéma | Un SVG optimisé (voir le [critère 5.1](../../contenus/5-1_format-images/)) |
| Image matricielle à taille fixe | Avatar, vignette | Un fichier aux dimensions d'affichage, plus une version 2x |
| Image fluide | Photo pleine largeur, illustration dans une colonne | Plusieurs largeurs, avec `srcset` et `sizes` |

**2. Images à taille fixe : une version 1x et une version 2x.** Une version 3x n'est pas utile.

```html
<img src="avatar-48.webp" srcset="avatar-48.webp 1x, avatar-96.webp 2x"
     width="48" height="48" alt="…">
```

**3. Images fluides : des largeurs espacées d'environ 1,5 fois et un `sizes` fidèle au CSS.** Produire les largeurs une fois, au build ou à l'enregistrement (voir l'exemple Hugo du [critère 5.2](../../contenus/5-2_compression-images/)) :

```html
<img src="photo-600.webp"
     srcset="photo-400.webp 400w, photo-600.webp 600w, photo-900.webp 900w, photo-1350.webp 1350w"
     sizes="(min-width: 62em) 600px, (min-resolution: 3dppx) 67vw, 100vw"
     width="600" height="400" alt="…">
```

La condition `(min-resolution: 3dppx) 67vw` plafonne les écrans de densité 3 à la densité 2, car 3 × 2/3 = 2. Testé dans Chromium 155 : un smartphone de 390 pixels de densité 3 télécharge la version de 900 pixels au lieu de 1 350. `sizes="auto"` ne permet pas ce plafonnement.

**4. Images d'arrière-plan CSS.** `srcset` ne s'y applique pas : prévoir une version par point de rupture, et [`image-set()`](https://developer.mozilla.org/fr/docs/Web/CSS/Reference/Values/image/image-set) pour les densités.

```css
.bandeau { background-image: url("carte-800.webp"); }
@media (min-width: 40em) {
  .bandeau { background-image: image-set("carte-1366.webp" 1x, "carte-2732.webp" 2x); }
}
```

**5. Redimensionner à l'envoi les images des contributeurs**, en **remplaçant l'original** : sinon, il reste la plus grande version du `srcset`, et les écrans les plus denses le reçoivent.

- **WordPress** ne réduit que les images de plus de 2 560 pixels ([filtre `big_image_size_threshold`](https://developer.wordpress.org/reference/hooks/big_image_size_threshold/)). Le seuil s'abaisse dans le thème : `add_filter( 'big_image_size_threshold', fn() => 1920 );`
- **Drupal** propose des « Maximum image dimensions » dans les réglages de chaque champ image, vides par défaut.
- **Sans CMS**, ImageMagick à l'enregistrement : `magick envoi.jpg -auto-orient -resize '1920x1920>' -quality 82 image.jpg` (le suffixe `>` ne réduit que les images plus grandes).

**6. Contrôler sur trois contextes d'affichage** avec l'émulation des outils de développement : ordinateur de densité 1 (1 366 × 768), ordinateur de densité 2 (1 440 × 900) et smartphone de densité 3 (390 × 844). Faire défiler toute la page, puis coller ce script dans la console. Il recharge chaque image pour lire la largeur réelle du fichier et la compare à sa largeur utile :

```js
const dpr = window.devicePixelRatio;
const lignes = await Promise.all([...document.images]
  .filter((img) => img.currentSrc && !/\.svg(\?|#|$)/i.test(img.currentSrc) && img.getClientRects().length > 0)
  .map(async (img) => {
    const fichier = new Image();
    fichier.src = img.currentSrc;
    await fichier.decode().catch(() => {});
    const utile = Math.round(img.getBoundingClientRect().width * dpr);
    return {image: img.currentSrc.split('/').pop(), fichier: fichier.naturalWidth, utile,
            rapport: Number((fichier.naturalWidth / utile).toFixed(2))};
  }));
console.table(lignes.sort((a, b) => b.rapport - a.rapport));
console.log(`${lignes.filter((l) => l.rapport <= 1.5).length} / ${lignes.length} images matricielles à moins de 1,5 fois leur taille utile (densité ${dpr})`);
```

Les images d'arrière-plan CSS, que ni ce script ni l'indicateur « Improve image delivery » de [Lighthouse 13](https://developer.chrome.com/blog/moving-lighthouse-to-insights) ne contrôlent, se vérifient dans l'onglet **Réseau**. [RespImageLint](https://ausi.github.io/respimagelint/) signale en plus les `sizes` qui ne correspondent pas à la mise en page.

**7. Documenter** dans la déclaration d'écoconception. Par exemple : « Logos et pictogrammes en SVG. Photos en quatre largeurs avec `srcset` et `sizes`, densité plafonnée à 2. Images des contributeurs réduites à 1 920 pixels à l'enregistrement. Contrôle à chaque mise en production sur trois contextes d'affichage : aucune image matricielle à plus de 1,5 fois sa largeur utile. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Les images sont souvent la plus grosse part du poids d'une page : le 6.4 est un levier majeur du budget du [critère 6.1](../6-1_poids-requetes-ecran/), à mesurer sur plusieurs densités d'écran.

- le [critère 5.1](../../contenus/5-1_format-images/) (format) : une image vectorielle entre d'office dans la première catégorie ;
- le [critère 5.2](../../contenus/5-2_compression-images/) (compression) : le 6.4 règle le nombre de pixels, le 5.2 le poids de chaque pixel ;
- le [critère 2.5](../../specifications/2-5_terminaux-affichage/) (terminaux d'affichage) présente les images responsives ;
- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) : informer les contributeurs des dimensions attendues et réduire l'image avant l'envoi ;
- le [critère 6.5](../6-5_chargement-ressources/) : le chargement différé et les images téléchargées sans être affichées.

Avant tout, les critères [4.6](../../ux-ui/4-6_contenu-porteur-information/) et [4.7](../../ux-ui/4-7_choix-sobre-format/) demandent si l'image est utile.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Trois pages d'accueil ont été relevées le 21 octobre 2026 dans Chromium 155, entièrement défilées, sur les trois contextes de l'étape 6 de la « Mise en œuvre technique », images d'arrière-plan CSS comprises. Le poids évitable est estimé en réencodant à leur taille utile les images plus de 1,5 fois trop larges. SPOTE, en maintenance ce jour-là, n'a pas pu être mesuré.

| Site | Images matricielles affichées | Avec `srcset` | Plus de 1,5 fois trop larges (densité 1 / 2 / 3) | Poids évitable (densité 1) |
|---|---:|---:|---:|---:|
| [DiaLog](https://dialog.beta.gouv.fr/) | 12 | 0 | 6 / 1 / 0 | ~120 Ko (11 %) |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | 9 à 11 | toutes | 1 / 0 / 0 | ~24 Ko (1 %) |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | 2 | 0 | 2 / 1 / 2 | ~77 Ko (14 %) |

**DiaLog** marque le critère **« Non validé »** dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf), à cause de son fond de carte, qui « devrait prévoir plusieurs variantes pour s'adapter à la taille de l'écran ». Le relevé lui donne raison : cette image d'arrière-plan fait 2 377 pixels de large pour 1 366 affichés, et pèse 211 Ko au lieu d'environ 110.

**Le Musée d'arts de Nantes** marque le critère **« Validé »** dans sa [déclaration d'écoconception](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/). Chaque photo existe bien en quatre à neuf largeurs. Mais la plus grande version de chaque photo est l'**original envoyé** par le contributeur : l'image en tête de page y figure en JPEG de qualité maximale, **4,7 Mo** contre 628 Ko pour la version de 1 720 pixels. Sur un ordinateur de densité 2, le navigateur la choisit, et la page passe de 2,1 à 6,2 Mo. C'est le redimensionnement à l'envoi, demandé par le moyen de test, qui manque.

**Le site du RGESN** n'affiche que deux images matricielles, toutes deux trop grandes : une bannière de 1 920 pixels affichée à 792 (109 Ko, environ 41 Ko à la bonne taille) et un logo de 681 pixels affiché à 144 (11,5 Ko, environ 3 Ko), qui gagnerait à être en SVG.

{{% /tab %}}

{{< /tabs >}}
