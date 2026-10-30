---
weight: 1500
title: "4.15 - Moyen de contrôle des usages et mode sobre"
description: "Critère 4.15 du RGESN : informer l'utilisateur sur l'empreinte environnementale de ses usages et lui proposer un mode d'affichage et d'usage sobre, documenté et mesuré."
icon: "tune"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique fournit-il à l'utilisateur un moyen de contrôle sur ses usages afin de suivre et de réduire les impacts environnementaux associés ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Expérience et Interface utilisateur (UX / UI)` |
| **Critère**  | `4.15` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'IHM` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.15/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'objectif est la limitation de l'impact environnemental en donnant de l'autonomie à l'utilisateur pour limiter les impacts environnementaux de ses usages.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Le service numérique devrait informer l'utilisateur sur son temps d'utilisation et sur l'impact environnemental associé à l'usage du service. Cette information, comme toute allégation environnementale, devra utiliser les normes et standards reconnus de quantification et calcul d'impact (par exemple, les « Product Category Rules », développées pour les services numériques par l'ADEME). L'utilisateur devrait également avoir la possibilité, par défaut ou à sa demande, de choisir des modes d'affichage et d'usage « sobres », permettant de réduire les ressources utilisées et la consommation énergétique.

En ce qui concerne les services et contenus vidéo, il est conseillé de se référer à la [recommandation article 26 de la loi du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique (loi REEN)](https://www.arcom.fr/nos-ressources/espace-juridique/textes-juridiques/recommandation-de-larcom-sur-larticle-26-de-la-loi-visant-reduire-lempreinte-environnementale-du-numerique-loi-reen), publiée par l'Arcom, en lien avec l'Arcep et l'ADEME, quant à l'information des consommateurs par les services de télévision, les services de médias audiovisuels à la demande et les services de plateformes de partage de vidéos en matière de consommation d'énergie et d'équivalents d'émissions de gaz à effet de serre, sur la consommation de données liée à l'utilisation de ces services.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service numérique respecte les conditions cumulatives suivantes :

- Le service affiche sur son interface une information à destination des utilisateurs sur l'empreinte environnementale de l'usage du service.
- Le service numérique propose un mode d'affichage et d'usage sobre, par défaut ou dont l'activation est laissée à la discrétion de l'utilisateur, pour diminuer l'empreinte environnementale associée à son usage. L'utilisateur pourra avoir accès à une information détaillant les paramètres de ce mode « sobriété énergétique » et les gains environnementaux associés.
- Documenter les actions mises en place dans la déclaration d'écoconception, en particulier l'information environnementale délivrée à l'utilisateur et le paramétrage du mode de « sobriété énergétique », y compris les gains environnementaux associés.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le critère 4.15 correspond à la [recommandation n°6 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=6) du [GR491](https://gr491.isit-europe.org/) (INR), « Permettre aux utilisateurs de réduire leurs impacts ». Son [critère principal](https://gr491.isit-europe.org/crit.php?id=6-uxui-les-equipements-utilisateurs-sont-de-plus-en-4faa80) apporte deux précisions :

- « Dès la première utilisation, un mode d'interface "dégradé", Off line ou moins énergivore du service, est-il poussé à l'utilisateur via une phase d'installation et/ou onboarding ? » Le mode sobre peut donc être proposé dès la première visite, pas caché dans les paramètres ;
- « L'utilisateur a-t-il un accès simple et identifié pour gérer la qualité des médias ? »

Il ajoute un argument social : les services qui exploitent les terminaux récents accentuent « la fracture numérique ». Un mode sobre profite aussi à ceux qui ne peuvent pas s'en procurer.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) des Designers Éthiques donne trois exemples de mode sobre : « résolution plus faible des vidéos, affichage des images au clic, actualisation de la boîte de réception espacée… ». Le dernier montre qu'un mode sobre peut aussi réduire les échanges avec le serveur, sans rien changer de visible.

La section [**7.10 Options par défaut**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-10-options-par-defaut) de leur guide explique pourquoi la valeur par défaut compte : ce sont les options « les plus utilisées et donc celles avec le plus d'impact ». Sur Unsplash, le téléchargement rapide ne propose que la taille originale, alors que la taille « Small » est « environ 20 fois plus légère », pour près de 100 millions de téléchargements par mois. Un mode sobre activé par défaut a donc beaucoup plus d'effet qu'un mode à activer soi-même ; le RGESN accepte les deux.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`

La fiche [**« Use media queries that support sustainability goals »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-media-queries-that-support-sustainability-goals) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C propose de respecter les préférences **déjà** exprimées dans le système ou le navigateur. Leur prise en charge est très inégale :

- **`prefers-reduced-motion`** est prise en charge partout. Préférence d'accessibilité, elle supprime aussi des animations coûteuses en calcul ;
- **`prefers-reduced-data`** n'est prise en charge par aucun navigateur, d'après [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data), et l'en-tête **`Save-Data`** reste [expérimental](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Save-Data).

Le service doit donc proposer son propre réglage, dont ces préférences peuvent fixer la valeur par défaut.

{{% /tab %}}

{{% tab tabName="Arcom et RCP de l'ADEME" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Concepteur UX / UI`

**La recommandation de l'Arcom.** Le RGESN renvoie à la [recommandation de l'Arcom du 26 juillet 2023](https://www.arcom.fr/nos-ressources/espace-juridique/textes-juridiques/recommandation-de-larcom-sur-larticle-26-de-la-loi-visant-reduire-lempreinte-environnementale-du-numerique-loi-reen) (loi REEN). Destinée aux services vidéo, elle décrit un dispositif transposable :

- une **rubrique dédiée** à l'impact environnemental, « facilement accessible », signalée à l'accès au service ;
- une fonctionnalité **« sobriété énergétique »** accessible « en un ou deux « clics » », qui applique « automatiquement l'ensemble des réglages les plus respectueux de l'environnement » ;
- « la proposition par défaut […] d'une qualité d'image sobre énergétiquement ».

Elle donne ainsi des repères que le RGESN ne chiffre pas : **un ou deux clics**, et **tous** les réglages sobres d'un coup.

**Le RCP de l'ADEME.** Pour afficher une information environnementale, le RGESN demande une méthode reconnue, comme le [Référentiel par catégorie de produit (RCP) d'un service numérique](https://librairie.ademe.fr/societe-et-politiques-publiques/9418-methodologie-d-evaluation-environnementale-basee-sur-l-analyse-du-cycle-de-vie-acv-pour-un-service-numerique.html) de l'ADEME. L'onglet « Équivalences » du [critère 4.12](../4-12_impacts-fonctionnalites/) montre pourquoi une information sans méthode reconnue peut induire en erreur.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

**Un bouton « Mode sobre »**, accessible en un clic comme le recommande l'Arcom, dont la valeur par défaut suit les préférences du navigateur quand elles existent :

```html
<button type="button" id="mode-sobre" aria-pressed="false">Mode sobre</button>
<a href="/mode-sobre">Ce que change le mode sobre</a>

<video controls preload="none" poster="conference.jpg"
       data-src-sobre="conference-360p.mp4"
       data-src-standard="conference-720p.mp4"></video>
```

```js
const bouton = document.querySelector('#mode-sobre');
const preferenceNavigateur = navigator.connection?.saveData === true;

function appliquer(actif) {
  document.documentElement.classList.toggle('sobre', actif);
  bouton.setAttribute('aria-pressed', String(actif));
  for (const video of document.querySelectorAll('video[data-src-sobre]')) {
    video.src = actif ? video.dataset.srcSobre : video.dataset.srcStandard;
  }
}

const choix = localStorage.getItem('mode-sobre');
appliquer(choix === null ? preferenceNavigateur : choix === 'oui');

bouton.addEventListener('click', () => {
  const actif = !document.documentElement.classList.contains('sobre');
  localStorage.setItem('mode-sobre', actif ? 'oui' : 'non');
  appliquer(actif);
});
```

```css
.sobre *, .sobre *::before, .sobre *::after {
  animation: none !important;
  transition: none !important;
}
```

- **`aria-pressed`** annonce l'état de l'interrupteur aux lecteurs d'écran.
- **`localStorage`** conserve le choix dans le navigateur, sans compte, sans cookie et sans requête.
- **`navigator.connection?.saveData`** active le mode sobre par défaut si le navigateur transmet une préférence d'économie de données (voir l'onglet W3C).
- **Vidéos** : avec `preload="none"`, rien n'est téléchargé avant la lecture, et le mode sobre choisit la source en 360p.

**Une limite pour les images.** Masquer une balise `<img>` par une classe CSS n'empêche pas son téléchargement (voir le [critère 6.5](../../frontend/6-5_chargement-ressources/)). Pour « l'affichage des images au clic », la version sobre doit être produite côté serveur, ou les images insérées par JavaScript à la demande, comme au Low-tech Lab (voir les retours d'expériences).

**Documenter les gains**, comme l'exige le moyen de test : mesurer le poids transféré de chaque page principale dans les deux modes (onglet **Réseau**, cache désactivé), puis publier ces mesures dans la page « Ce que change le mode sobre » et dans la déclaration d'écoconception. Ne les convertir en CO2 ou en énergie qu'avec une méthode reconnue (voir l'onglet « Arcom et RCP de l'ADEME »).

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Concepteur UX / UI`

Ce critère généralise le [critère 4.12](../4-12_impacts-fonctionnalites/) : le 4.12 informe **au moment** d'utiliser une fonctionnalité coûteuse, le 4.15 donne une information **globale** et un réglage **durable** pour tout le service. Cette information suppose d'avoir évalué l'empreinte du service (voir le [critère 1.5](../../strategie/1-5_objectifs-environnementaux/)).

Un mode sobre peut désactiver la lecture automatique ([4.1](../4-1_lecture-automatique/)), privilégier les formats légers ([4.7](../4-7_choix-sobre-format/)) ou se passer des polices téléchargées ([4.8](../4-8_polices-caracteres/)). Un service qui applique déjà ces critères **par défaut** a moins à y gagner : c'est l'argument de DiaLog.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les deux déclarations publiques citées sur ce site marquent ce critère **« Non validé »**.

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (déclaration du 23 avril 2025) l'argumente : « Pour ce service, cela ne ferait pas de sens d'ajouter de la confusion et des fonctionnalités pour estimer un impact qui serait moindre dans tous les cas. […] L'interface est conçue pour être sobre par défaut. » Pour un service déjà léger, un compteur d'impact et un mode sobre ajoutent du code pour un gain marginal, et un « Non validé » argumenté vaut mieux qu'une conformité de façade. Il manque surtout à DiaLog l'information environnementale dans l'interface et la documentation des gains.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) constate simplement : « Le service numérique ne propose pas de suivi ou de moyen de contrôle pour réduire ses impacts environnementaux. »

**Deux exemples de mode sobre**, analysés le 20 octobre 2026, illustrent les deux options du critère, sans être des déclarations de conformité au RGESN :

- [Niji](https://www.niji.fr/fr/) propose un **« Mode éco+ »** que l'utilisateur active par un interrupteur en bas de chaque page, en un clic comme le recommande l'Arcom. Les photos y sont remplacées par des illustrations SVG et ne sont pas téléchargées. Le choix est mémorisé, et l'interrupteur est annoncé aux lecteurs d'écran (`role="switch"`). Le mode est désactivé par défaut : « Nous ne voulons rien imposer, mais simplement poser la question de l'utilité » ([« Notre site est écoconçu »](https://www.niji.fr/fr/we/notre-site-est-ecoconcu)) ;
- le [Low-tech Lab](https://lowtechlab.org/fr/actualites-blog) **masque les images par défaut** sur sa page d'actualités, avec un message d'explication et un interrupteur « Afficher les images ». Les balises `<img>` ne contiennent qu'une image transparente, l'adresse réelle étant dans `data-src` : les images ne sont téléchargées qu'à la demande. Le réglage n'est toutefois pas mémorisé.

Aucun des deux ne publie de gain chiffré propre à son mode sobre, alors que le moyen de test le demande. Mesurer le poids des pages dans les deux modes suffirait.

{{% /tab %}}

{{< /tabs >}}
