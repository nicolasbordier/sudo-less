---
weight: 500
title: "6.5 - Chargement des seules ressources utiles"
description: "Critère 6.5 du RGESN : différer le chargement des images, iframes et vidéos hors écran sans retarder l'image principale, charger le JavaScript d'une fonctionnalité quand elle sert, limiter les styles aux composants utilisés et repérer les ressources téléchargées sans jamais être affichées."
icon: "downloading"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique évite-t-il de déclencher le chargement de ressources et de contenus inutilisés pour chaque fonctionnalité ?

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
| **Critère**  | `6.5` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique n'utilise pas d'interface graphique` |
| **Métiers concernés** | `Développeur` `Concepteur UX / UI` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/6.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire ou limiter les données téléchargées et optimiser la consommation énergétique des terminaux.

Il est souvent plus simple pour l'équipe de développement de charger tous les composants, packagés dans un fichier compressé quelle que soit la fonctionnalité. Il en résulte que l'utilisateur charge des composants qui ne seront pas forcément utilisés. N'utiliser que ce qui est effectivement nécessaire au fonctionnement du service permet d'économiser de la ressource informatique.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Ressources et composants ne doivent être chargés que lorsqu'ils sont effectivement utilisés.

Prévoir des mécanismes de chargement progressif pour les éléments graphiques et les médias qui nécessitent un téléchargement. Par exemple : streaming pour la vidéo, chargement uniquement des images ou ressources affichées à l'écran (« lazy loading ») lorsque l'utilisateur les atteint en faisant défiler la page (Illustration : [Documentation MDN sur le chargement progressif](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps/Tutorials/js13kGames/Loading)).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier le contenu des ressources chargées et leur utilisation effective en s'assurant qu'elles correspondent aux fonctionnalités effectivement utilisées : pour valider ce critère, il ne doit pas y avoir de ressources chargées inutilement.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :


{{< tabs tabTotal="8">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache six fiches au critère 6.5 :

- [**RWEB 0051 — « Utiliser le chargement paresseux »**](https://rweb.greenit.fr/fr/fiches/RWEB_0051-utiliser-le-chargement-paresseux) (priorité 5/5) : `loading="lazy"` sur les images et iframes « en dessous de la ligne de flottaison » ;
- [**RWEB 0046 — « Ne charger des données ou du code que lorsque c'est indispensable »**](https://rweb.greenit.fr/fr/fiches/RWEB_0046-ne-charger-des-donneesdu-code-que-lorsqu-elles-sontil-est-necessaire) : pas de `preload`, `prefetch` ou `preconnect` pour une ressource « utilisée uniquement sous certaines conditions » ;
- [**RWEB 0015 — « N'utilisez que les portions indispensables des bibliothèques JavaScript et frameworks CSS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0015-n-utilisez-que-les-portions-indispensables-des-bibliotheques-javascript-et-frameworks-css) (priorité 5/5). Les « 17 Ko » économisés par la version « slim » de jQuery sont non compressés : l'écart n'est que de 6 Ko en gzip ;
- [**RWEB 0035 — « Limiter le nombre de CSS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0035-limiter-le-nombre-de-css) (priorité 5/5) : une feuille par media query, que le navigateur « dépriorise ». Il la télécharge quand même : dans Chromium 155 et Firefox 158, une feuille `media="print"` est téléchargée à chaque chargement ;
- [**RWEB 0069 — « Bien choisir son thème et limiter les extensions dans un CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0069-bien-choisir-son-theme-et-limiter-le-nombre-d-extensions-dans-un-cms) et [**RWEB 0022 — « Favoriser un développement sur-mesure à l'usage d'un CMS »**](https://rweb.greenit.fr/fr/fiches/RWEB_0022-favoriser-un-developpement-sur-mesure-a-l-usage-d-un-cms), car « chaque extension ajoute ses données en base, ses fichiers CSS et JavaScript ».

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Dans la famille Frontend du [GR491](https://gr491.isit-europe.org/) (INR) :

- la [recommandation n°9](https://gr491.isit-europe.org/?famille=frontend&num_reco=9) demande : [« Est-ce que le lazy load apporte un gain (poids de la page, ressource CPU) ? »](https://gr491.isit-europe.org/crit.php?id=9-frontend-lors-du-chargement-du-service-sur-le-29fe88) Elle estime qu'il agit « sans vraiment réduire le volume de chargement ». Il le réduit pourtant pour chaque visiteur qui ne fait pas défiler toute la page : 528 Ko au Musée d'arts de Nantes ;
- la [recommandation n°3](https://gr491.isit-europe.org/?famille=frontend&num_reco=3) contient deux critères en priorité **High** : [« Les bibliothèques utilisées permettent-elles de ne prendre que les composants effectivement utiles ? »](https://gr491.isit-europe.org/crit.php?id=3-frontend-bien-souvent-les-composants-issus-de-bibliotheques-83dc17) et [« Les dépendances non utilisées sont-elles identifiées et retirées ? »](https://gr491.isit-europe.org/crit.php?id=3-frontend-les-arbres-de-dependance-donnent-la-cartographie-d4ea50), à contrôler avec « CHROME : console / coverage ».

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques en traite dans trois rubriques :

- [**7.1 Images**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-1-images) : « Différer le chargement des images » avec `loading="lazy"`, mais jamais celles visibles à l'ouverture, qu'il retarde ;
- [**7.2 Vidéos et sons**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-2-videos-et-sons) : un lecteur HTML5 qui « ne charge la vidéo qu'une fois que l'utilisateur appuie sur le bouton play ». Ce n'est vrai qu'avec `preload="none"` : sinon, Chromium lit le début et la fin du fichier avant tout clic ;
- [**7.5 Plugins et widgets**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-5-plugins-et-widgets) : « Tous les utilisateurs ont-ils besoin de charger la carte ? » La question vaut aussi pour son code, comme le montre DiaLog.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) :

- [**« Modularize bandwidth-heavy components »**](https://www.w3.org/TR/web-sustainability-guidelines/#modularize-bandwidth-heavy-components) : des modules « that load only when needed », sans découpage excessif, qui « can increase overhead, reduce caching efficiency » ;
- [**« Minify and remove unused code »**](https://www.w3.org/TR/web-sustainability-guidelines/#minify-and-remove-unused-code) : « Identify and remove unused or dead code » ;
- [**« Optimize media to reduce resource use »**](https://www.w3.org/TR/web-sustainability-guidelines/#optimize-media-to-reduce-resource-use) et [**« Treat third parties the same as first parties »**](https://www.w3.org/TR/web-sustainability-guidelines/#treat-third-parties-the-same-as-first-parties) : une façade pour les médias lourds et les contenus tiers.

Attention à l'exemple de [**« Defer the loading of non-critical resources »**](https://www.w3.org/TR/web-sustainability-guidelines/#defer-the-loading-of-non-critical-resources) : son `<link rel="prefetch">` fait télécharger une page à chaque visiteur, qu'il l'ouvre ou non. Le niveau `conservative` des Speculation Rules, utilisé par [WordPress 6.8](https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/), ne précharge qu'au début du clic.

{{% /tab %}}

{{% tab tabName="Le chargement différé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**Le navigateur charge d'avance.** Une image en `loading="lazy"` est téléchargée quand elle approche de l'écran. Testé le 30 octobre 2026, Chromium 155 charge tout ce qui se trouve à moins de cette distance sous l'écran, comme le prévoit son [code source](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/settings.json5) :

| Connexion estimée par Chromium | Images | Iframes |
|---|---:|---:|
| 4G et plus rapide | 1 250 px | 2 500 px |
| 3G | 2 500 px | 3 500 px |
| 2G | 6 000 px | 6 000 px |

Firefox 158 s'en tient à environ 600 pixels. Sur une page de deux ou trois écrans, l'attribut ne change donc presque rien dans Chromium.

**Jamais sur l'image principale.** Elle ne serait demandée qu'après les feuilles de style : testé dans Chromium 155, 0,65 s après la page au lieu de 7 ms. D'après le [Web Almanac 2025](https://almanac.httparchive.org/en/2025/performance#lcp-lazy-loading), 16 à 17 % des pages font cette erreur.

**Vidéos et services tiers.** `preload="none"` pour une vidéo (voir le [critère 4.1](../../ux-ui/4-1_lecture-automatique/)), une façade pour le lecteur ou la carte d'un service tiers (voir les critères [2.10](../../specifications/2-10_services-tiers/) et [4.4](../../ux-ui/4-4_activation-service-tiers/)).

**À vérifier dans l'onglet Réseau.** Lighthouse ne contrôle plus le chargement différé depuis sa [version 13](https://developer.chrome.com/blog/moving-lighthouse-to-insights) : comparer le poids de la page à l'ouverture et après défilement complet.

{{% /tab %}}

{{% tab tabName="Téléchargé sans être affiché" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Une variante de logo pour le mode sombre ou le contenu d'une fenêtre fermée peuvent être téléchargés sans jamais s'afficher. Testé le 30 octobre 2026, avec le même résultat dans Chromium 155 et Firefox 158 :

| Élément masqué | Téléchargé ? |
|---|---|
| `<img>` en `display: none` ou `visibility: hidden` | Oui |
| `<img loading="lazy">` en `display: none` | **Non** |
| Image d'arrière-plan CSS d'un élément en `display: none` | Non |
| Image d'arrière-plan CSS dans une media query qui ne s'applique pas | Non |
| `<picture>` avec plusieurs `<source media="…">` | Seulement la source retenue |
| SVG externe appelé par `<use href="…">`, même dans un `<dialog>` fermé | **Oui** |

D'où trois règles :

- une variante détectable par media query (mode sombre, largeur d'écran) : `<picture>` et `media` ;
- une image masquée par `display: none` : `loading="lazy"` ;
- une fenêtre rarement ouverte : insérer son contenu à l'ouverture.

Exemple : la fenêtre « Paramètres d'affichage » du DSFR, fermée, appelle ses trois pictogrammes par `<use href>`. Chaque visiteur les télécharge : 11,5 Ko sur le site du RGESN, 22,2 Ko sur SPOTE.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**1. Faire l'inventaire.** Pour chaque type de page (accueil, liste, fiche, carte…), ouvrir l'onglet **Réseau**, cache désactivé, sans faire défiler ni cliquer : chaque ressource doit correspondre à un élément visible ou à une fonctionnalité de la page.

**2. Images et iframes : `loading="lazy"` sous le premier écran, jamais au-dessus.**

```html
<!-- Image principale, visible à l'ouverture : chargement normal, priorité haute -->
<img src="bandeau.webp" width="1200" height="600" fetchpriority="high" alt="…">

<!-- Plus bas dans la page : chargement différé -->
<img src="photo.webp" width="600" height="400" loading="lazy" alt="…">
<iframe src="https://exemple.fr/formulaire/" width="600" height="800" loading="lazy" title="…"></iframe>
```

**3. JavaScript : charger le code d'une fonctionnalité quand elle sert**, avec `import()` :

```js
// Module de recherche : téléchargé au premier clic seulement
document.querySelector('#ouvrir-recherche').addEventListener('click', async () => {
  const { ouvrirRecherche } = await import('./recherche.js');
  ouvrirRecherche();
});

// Module de la carte : téléchargé quand son conteneur approche de l'écran
const conteneur = document.querySelector('#carte');
new IntersectionObserver(async (entrees, observateur) => {
  if (!entrees[0].isIntersecting) return;
  observateur.disconnect();
  const { init } = await import('./carte.js');
  init(conteneur);
}, { rootMargin: '600px' }).observe(conteneur);
```

Les outils de build font de chaque `import()` un fichier séparé, sauf si la bibliothèque est aussi importée de façon statique ailleurs. Avec Symfony, un contrôleur Stimulus se charge à la demande grâce au commentaire `/* stimulusFetch: 'lazy' */`, placé avant `export default class` ([documentation de StimulusBundle](https://symfony.com/bundles/StimulusBundle/current/index.html#lazy-stimulus-controllers)).

**4. CSS : ne charger que les composants utilisés.** Le [DSFR](https://github.com/GouvernementFR/dsfr#readme) se charge par composant, et chaque fichier existe en version `.main`, sans les styles pour Internet Explorer 11 : compressé, `dsfr.main.min.css` 1.15.4 pèse 77,5 Ko au lieu de 94,3 Ko, le noyau seul 24,9 Ko. Avec un autre framework CSS, [PurgeCSS](https://purgecss.com/) retire les sélecteurs inutilisés ; avec Hugo, l'option [`build.buildStats`](https://gohugo.io/configuration/build/#build-stats) lui fournit les classes de toutes les pages.

**5. Vérifier chaque préchargement.** Chaque `preload`, `prefetch` ou `preconnect` doit servir à tous les visiteurs de la page. La console de Chrome signale un `preload` inutilisé, le panneau **Performance** un « Unused preconnect ».

**6. Mesurer le code inutilisé.** Dans Chrome et Edge, ouvrir le panneau [Coverage](https://developer.chrome.com/docs/devtools/coverage) (`Ctrl+Maj+P`, « Show Coverage »), cliquer sur **Reload**, puis utiliser la page. Il mesure ce qui n'a pas servi pendant l'enregistrement, pas ce qui est inutile : sur les cinq sites relevés, 61 à 94 % du code ne sert pas à la page d'accueil. Le levier, ce sont les gros blocs inutiles à **tous** les visiteurs, comme une bibliothèque qui ne sert que sur une autre page. [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) ou [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer) montrent les bibliothèques que contient un fichier.

**7. Repérer les images téléchargées sans être affichées**, avec ce script à coller dans la console après avoir fait défiler la page (l'icône du site y apparaît aussi ; c'est normal) :

```js
const affichees = new Set();
const ajouter = (url) => { try { affichees.add(new URL(url, document.baseURI).href.split('#')[0]); } catch {} };
for (const el of document.querySelectorAll('*')) {
  if (!el.getClientRects().length || getComputedStyle(el).visibility === 'hidden') continue;
  if (el.currentSrc) ajouter(el.currentSrc);
  if (el.tagName === 'use') ajouter(el.getAttribute('href') || el.getAttribute('xlink:href'));
  for (const pseudo of [null, '::before', '::after']) {
    const cs = getComputedStyle(el, pseudo);
    for (const valeur of [cs.backgroundImage, cs.maskImage, cs.webkitMaskImage]) {
      for (const m of String(valeur).matchAll(/url\("?([^")]+)"?\)/g)) ajouter(m[1]);
    }
  }
}
const lignes = performance.getEntriesByType('resource')
  .filter((r) => /\.(avif|webp|png|jpe?g|gif|svg)(\?|#|$)/i.test(r.name) && !affichees.has(r.name.split('#')[0]))
  .map((r) => ({fichier: r.name.split('/').pop(), Ko: r.transferSize ? Math.round(r.transferSize / 100) / 10 : '?'}));
console.table(lignes);
console.log(`${lignes.length} image(s) téléchargée(s) sans élément visible`);
```

**8. Documenter** dans la déclaration d'écoconception. Par exemple : « Images sous le premier écran en chargement différé, jamais l'image principale. Bibliothèque cartographique chargée seulement sur les pages qui affichent une carte. Contrôle à chaque mise en production : aucune ressource téléchargée sans élément visible ni fonctionnalité correspondante. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le 6.5 complète les leviers du budget fixé par le [critère 6.1](../6-1_poids-requetes-ecran/) : le cache ([6.2](../6-2_cache-navigateur/)), la compression ([6.3](../6-3_compression-ressources/)) et le redimensionnement ([6.4](../6-4_dimensions-images/)) allègent une ressource, le 6.5 la retire. Voir aussi :

- le [critère 4.1](../../ux-ui/4-1_lecture-automatique/) : `preload="none"` pour les vidéos et les sons ;
- le [critère 4.2](../../ux-ui/4-2_defilement-infini/) : la pagination plutôt que le défilement infini ;
- les critères [2.10](../../specifications/2-10_services-tiers/) et [4.4](../../ux-ui/4-4_activation-service-tiers/) : la façade pour les services tiers ;
- les critères [2.9](../../specifications/2-9_composants-interface/) et [3.1](../../architecture/3-1_architecture-composants/) : choisir des bibliothèques modulaires avant le développement.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Cinq pages d'accueil ont été relevées le 30 octobre 2026 dans Chromium 155, sans cache ni consentement aux cookies, sur un écran de 1 366 × 768 pixels, puis après défilement complet. Le code non utilisé est mesuré comme le fait le panneau Coverage.

| Site | Poids au chargement | Ajouté par le défilement | JavaScript : transféré, non exécuté | CSS : transféré, non utilisé |
|---|---:|---:|---:|---:|
| [DiaLog](https://dialog.beta.gouv.fr/) | 1 042 Ko | 132 Ko | 536 Ko, 66 % | 71 Ko, 79 % |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/) | 1 475 Ko | 528 Ko | 228 Ko, 67 % | 89 Ko, 86 % |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | 1 038 Ko | 0 | 194 Ko, 76 % | 150 Ko, 91 % |
| [Site du RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | 595 Ko | 0 | 65 Ko, 61 % | 138 Ko, 91 % |
| Ce site, sudo-less | 105 Ko | 0 | 6 Ko, 77 % | 39 Ko, 94 % |

Ces proportions sont courantes (voir l'étape 6 de l'onglet « Mise en œuvre technique ») ; les constats ci-dessous portent sur ce qui ne sert à aucun visiteur.

**DiaLog** marque le critère **« Validé »** dans sa [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf). Pourtant, sa page d'accueil, sans carte, télécharge MapLibre GL JS, la bibliothèque cartographique (276 Ko compressée) : dans le [code source](https://github.com/MTES-MCT/dialog), quatre contrôleurs Stimulus l'importent sans le commentaire `stimulusFetch: 'lazy'`. Les rendre différés ramènerait l'accueil sous le budget de 900 Ko que DiaLog s'est fixé (voir le [critère 6.1](../6-1_poids-requetes-ecran/)).

**Le Musée d'arts de Nantes** classe le critère **« En cours de validation »** dans sa [déclaration d'écoconception](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/). Son chargement différé est efficace : 528 Ko d'images ne sont téléchargés qu'au défilement. Mais l'image principale (628 Ko) porte `loading="lazy"` à côté de `fetchpriority="high"` : elle n'est demandée qu'à 0,28 s, après la feuille de style.

**SPOTE** n'utilise pas le chargement différé : quatre images (350 Ko, le tiers de la page), situées à plus de 2 000 pixels du haut, sont téléchargées à l'ouverture. Le site charge aussi deux versions du JavaScript du DSFR, la 1.12.1 et la 1.14.2.

**Le site du RGESN** télécharge son logo blanc pour le mode sombre (10,9 Ko), masqué en mode clair, et les pictogrammes de la fenêtre « Paramètres d'affichage ». Sa feuille `utility.min.css` (41 Ko), qui contient les classes des 1 038 icônes du DSFR, n'est utilisée qu'à 0,2 %. Les versions `.main` du DSFR lui feraient gagner 38 Ko compressés.

**Ce site, sudo-less**, ne valide pas le critère. Son thème, [Lotus Docs](https://lotusdocs.dev/), écrit dans chaque page de documentation l'index de recherche de tout le site : 257 Ko des 284 Ko du HTML de la page du [critère 6.3](../6-3_compression-ressources/), téléchargés de nouveau à chaque page, que le visiteur cherche ou non. Il faudrait le placer dans un fichier séparé, chargé au premier usage de la recherche.

{{% /tab %}}

{{< /tabs >}}
