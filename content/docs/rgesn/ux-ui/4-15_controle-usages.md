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
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le critère 4.15 correspond à une recommandation entière du [GR491](https://gr491.isit-europe.org/) (INR) : la [recommandation n°6 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=6), « Permettre aux utilisateurs de réduire leurs impacts ». Son critère [« L'utilisation du service permet-elle d'envisager des configurations logicielles ou matérielles moins impactantes pour l'environnement ? »](https://gr491.isit-europe.org/crit.php?id=6-uxui-les-equipements-utilisateurs-sont-de-plus-en-4faa80) apporte deux précisions utiles :

- « Dès la première utilisation, un mode d'interface "dégradé", Off line ou moins énergivore du service, est-il poussé à l'utilisateur via une phase d'installation et/ou onboarding ? » Le mode sobre ne doit donc pas être caché dans les paramètres : il peut être proposé dès la première utilisation.
- « L'utilisateur a-t-il un accès simple et identifié pour gérer la qualité des médias ? »

Ses précisions ajoutent un argument social à l'argument environnemental. Les services exploitent toujours plus les capacités des terminaux récents, ce qui a « pour effet d'accentuer la fracture numérique en excluant une partie des utilisateurs qui ne peuvent se procurer ces terminaux ». Un mode sobre profite aussi à ces utilisateurs.

Le volet « information » du critère rejoint la recommandation n°2 de la même famille, déjà citée au [critère 4.12](../4-12_impacts-fonctionnalites/). Celle-ci propose des compteurs (« un compteur de temps de visionnage », « un compteur de la consommation électrique ») et demande si « les settings à impact NR du service sont-ils clairement identifiables et facilement accessibles par l'utilisateur ».

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

La ressource des Designers Éthiques [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) donne trois exemples concrets de ce que peut contenir un mode sobre : « Informer l'utilisateur sur l'impact environnemental de ses usages et lui permettre de réduire son empreinte par la mise à disposition d'un mode d'affichage ou d'usage « sobres » (ex : résolution plus faible des vidéos, affichage des images au clic, actualisation de la boîte de réception espacée…). »

Le troisième exemple, l'actualisation espacée d'une boîte de réception, montre qu'un mode sobre ne se limite pas à l'affichage. Il peut aussi réduire la fréquence des échanges avec le serveur, sans rien changer de visible.

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/), dans sa section [**7.10 Options par défaut**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-10-options-par-defaut), rappelle pourquoi la condition « par défaut » du critère compte : les options par défaut sont « par définition les plus utilisées et donc celles avec le plus d'impact ». Son exemple est celui d'Unsplash. Le téléchargement rapide d'une photo y propose uniquement la taille originale, alors que la taille « Small » est « environ 20 fois plus légère », pour une qualité « tout à fait suffisante pour la plupart des usages ». Or le nombre de téléchargements mensuels « avoisine les 100 millions de photos ».

Un mode sobre activé par défaut, que l'utilisateur peut désactiver s'il en a besoin, aura donc beaucoup plus d'effet qu'un mode sobre à activer soi-même. Le RGESN accepte les deux (« par défaut ou dont l'activation est laissée à la discrétion de l'utilisateur »).

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C proposent une piste complémentaire dans la fiche [**« Use media queries that support sustainability goals »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-media-queries-that-support-sustainability-goals) : respecter les préférences que l'utilisateur a **déjà** exprimées dans son système ou son navigateur. Le critère de succès « Media and preference queries » cite notamment `prefers-reduced-motion` et `prefers-reduced-data`.

Ces préférences permettent d'activer un mode sobre sans demander quoi que ce soit à l'utilisateur. Leur prise en charge est toutefois très inégale :

- **`prefers-reduced-motion`** (réduction des animations) est prise en charge par tous les navigateurs courants. C'est d'abord une préférence d'accessibilité, mais elle supprime aussi des animations coûteuses en calcul.
- **`prefers-reduced-data`** (réduction des données) est, d'après la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-data), une fonctionnalité expérimentale « not supported by any user agent ».
- L'en-tête HTTP **`Save-Data`**, qui exprime la même intention, est lui aussi marqué comme expérimental et à disponibilité limitée par la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Save-Data).

Les préférences système ne suffisent donc pas encore : le service doit proposer son propre réglage. Il peut en revanche s'appuyer sur ces préférences pour choisir la valeur par défaut de ce réglage, quand elles sont disponibles.

{{% /tab %}}

{{% tab tabName="Arcom et RCP de l'ADEME" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Concepteur UX / UI`

**La recommandation de l'Arcom pour les services vidéo.** Le RGESN renvoie à la [recommandation de l'Arcom du 26 juillet 2023](https://www.arcom.fr/nos-ressources/espace-juridique/textes-juridiques/recommandation-de-larcom-sur-larticle-26-de-la-loi-visant-reduire-lempreinte-environnementale-du-numerique-loi-reen), prise en application de l'article 26 de la loi REEN. Elle ne vise que les services de télévision, de vidéo à la demande et de partage de vidéos, mais elle décrit un dispositif transposable à d'autres services :

- une **rubrique dédiée** sur l'impact environnemental, « facilement accessible », et un message d'information visible à l'accès au service pour la signaler ;
- une fonctionnalité de type **« sobriété énergétique »**, « aisément accessible (le chemin depuis l'écran d'accueil nécessite un nombre d'actions limité, par exemple en un ou deux « clics ») et permettant d'appliquer automatiquement l'ensemble des réglages les plus respectueux de l'environnement » ;
- parmi les actions à valoriser, « la proposition par défaut sur le service ou la plateforme d'une qualité d'image sobre énergétiquement ».

Les deux derniers points donnent des repères concrets que le RGESN ne chiffre pas : un mode sobre accessible en **un ou deux clics**, qui applique **tous** les réglages sobres d'un coup plutôt que de les laisser à configurer un par un.

**Le RCP de l'ADEME pour l'information environnementale.** Pour la première condition du critère (afficher une information sur l'empreinte environnementale), le RGESN demande d'utiliser des méthodes reconnues, comme les « Product Category Rules » de l'ADEME. Le document de référence est le [Référentiel par catégorie de produit (RCP) d'un service numérique](https://librairie.ademe.fr/societe-et-politiques-publiques/9418-methodologie-d-evaluation-environnementale-basee-sur-l-analyse-du-cycle-de-vie-acv-pour-un-service-numerique.html), dont la version 2 est disponible sur la librairie de l'ADEME. Il fixe la méthode d'analyse du cycle de vie d'un service numérique. L'onglet « Équivalences » du [critère 4.12](../4-12_impacts-fonctionnalites/) montre pourquoi une information environnementale sans méthodologie reconnue peut induire en erreur.

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

- **`aria-pressed`** : le bouton est un interrupteur, et son état est annoncé par les lecteurs d'écran.
- **`localStorage`** : le choix de l'utilisateur est conservé dans le navigateur, sans compte, sans cookie et sans requête vers le serveur.
- **`navigator.connection?.saveData`** : si le navigateur transmet une préférence d'économie de données (voir l'onglet W3C), le mode sobre est activé par défaut. Dans les navigateurs qui ne la prennent pas en charge, la valeur est `undefined` et le mode reste désactivé tant que l'utilisateur ne l'a pas choisi.
- **Vidéos** : avec `preload="none"`, rien n'est téléchargé avant la lecture. Le mode sobre choisit simplement la source en 360p plutôt qu'en 720p.

**Une limite à connaître pour les images.** Une classe CSS ne suffit pas à empêcher le téléchargement d'une image présente dans le HTML : masquer une balise `<img>` ne garantit pas que le navigateur ne la télécharge pas. Pour « l'affichage des images au clic » cité par les Designers Éthiques, la version sobre doit être produite **avant** l'envoi de la page, côté serveur ou au moment du build, ou les images doivent être insérées par JavaScript à la demande. C'est la technique du Low-tech Lab, détaillée dans les retours d'expériences ci-dessous.

**Documenter les gains**, comme l'exige la troisième condition du moyen de test. Pour chaque page principale, mesurez le poids transféré dans l'onglet **Réseau** des outils de développement, cache désactivé, dans les deux modes. Publiez ensuite ces mesures dans la page « Ce que change le mode sobre » et dans la déclaration d'écoconception. Ne les convertissez en impact environnemental (CO2, énergie) qu'avec une méthodologie reconnue (voir l'onglet « Arcom et RCP de l'ADEME »).

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Concepteur UX / UI`

Ce critère généralise le [critère 4.12](../4-12_impacts-fonctionnalites/) (information sur les fonctionnalités à fort impact), déjà publié sur ce site :

- le 4.12 informe l'utilisateur **au moment** d'utiliser une fonctionnalité coûteuse, et lui propose une alternative ponctuelle (l'audio seul plutôt que la vidéo) ;
- le 4.15 lui donne une information **globale** sur l'empreinte de ses usages, et un réglage **durable** qui s'applique à tout le service (le mode sobre).

L'information environnementale demandée par le 4.15 suppose d'avoir évalué l'empreinte du service, ce qui renvoie au [critère 1.5](../../strategie/1-5_objectifs-environnementaux/) (objectifs environnementaux) et à son analyse multicritère.

Le contenu d'un mode sobre recoupe enfin plusieurs critères déjà publiés. Il peut désactiver la lecture automatique ([critère 4.1](../4-1_lecture-automatique/)), privilégier les formats les plus légers ([critère 4.7](../4-7_choix-sobre-format/)) ou se passer des polices téléchargées ([critère 4.8](../4-8_polices-caracteres/)). Un service qui applique déjà ces critères **par défaut** a moins à gagner avec un mode sobre. C'est précisément l'argument de DiaLog dans les retours d'expériences ci-dessous.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les deux déclarations publiques citées sur ce site marquent ce critère **« Non validé »**, pour des raisons différentes.

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) assume ce choix et l'argumente : « Ce critère n'est pas validé au sens du RGESN car il ne contient pas de moyen de contrôle de l'empreinte environnementale de son usage outre la page de déclaration d'écoconception et les parcours évalués avec GreenIT Analysis. Pour ce service, cela ne ferait pas de sens d'ajouter de la confusion et des fonctionnalités pour estimer un impact qui serait moindre dans tous les cas. Il n'y a pas non plus de cas d'usage pour un mode sobriété énergétique. L'interface est conçue pour être sobre par défaut. »

Cette justification soulève une vraie question. Pour un service déjà léger, ajouter un compteur d'impact et un mode sobre ajoute des fonctionnalités, donc du code et des ressources, pour un gain marginal. Le critère est classé « Recommandé », pas « Prioritaire », et un « Non validé » argumenté vaut mieux qu'une conformité de façade. On peut noter qu'une interface « sobre par défaut » remplit déjà en partie la deuxième condition du moyen de test (« un mode d'affichage et d'usage sobre, par défaut »). Ce qui manque à DiaLog pour valider le critère, c'est surtout l'information environnementale affichée dans l'interface et la documentation des gains.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) constate simplement l'absence de dispositif : « Le service numérique ne propose pas de suivi ou de moyen de contrôle pour réduire ses impacts environnementaux. »

**Deux exemples de mode sobre.** Deux sites qui proposent un mode sobre, analysés le 20 octobre 2026, illustrent les deux options que le critère autorise : « par défaut ou dont l'activation est laissée à la discrétion de l'utilisateur ». Il ne s'agit pas de déclarations de conformité au RGESN.

[Niji](https://www.niji.fr/fr/) propose un **« Mode éco+ »** que l'utilisateur active lui-même, avec un interrupteur fixé en bas de chaque page. C'est l'accès « en un ou deux clics » recommandé par l'Arcom. En mode éco+, les photos sont remplacées par des illustrations au trait en SVG. Comme les photos sont chargées en différé et masquées, elles ne sont pas téléchargées. Le choix est mémorisé dans le navigateur, et l'interrupteur est annoncé aux lecteurs d'écran (`role="switch"`, `aria-checked`). La page [« Notre site est écoconçu »](https://www.niji.fr/fr/we/notre-site-est-ecoconcu) explique le principe : « Chaque page a donc deux versions, l'une moins consommatrice que l'autre. » Le mode est volontairement désactivé par défaut : « Nous ne voulons rien imposer, mais simplement poser la question de l'utilité pour sensibiliser à la pollution numérique. » Les clics sur l'interrupteur sont comptés dans l'outil de mesure d'audience du site (Plausible), ce qui permet de suivre combien de visiteurs adoptent le mode.

Le [Low-tech Lab](https://lowtechlab.org/fr/actualites-blog) fait le choix inverse sur sa page d'actualités : les images y sont **masquées par défaut**. Un message l'explique (« Vous ne voyez pas les images ? C'est normal ! Vous êtes sur un site à basse consommation. Si les visuels vous manquent, vous pouvez tout de même choisir d'afficher les images. »), et un interrupteur « Afficher les images » permet de les faire apparaître. La mise en œuvre évite le piège signalé dans l'onglet « Mise en œuvre technique ». Les balises `<img>` ne contiennent qu'une image transparente d'un pixel, et l'adresse réelle est stockée dans un attribut `data-src` : les images ne sont téléchargées qu'à la demande. C'est l'« affichage des images au clic » cité par les Designers Éthiques, avec la valeur par défaut la plus sobre, celle qui a le plus d'effet selon leur guide. Le réglage ne vaut toutefois que pour cette page, et il n'est pas mémorisé d'une visite à l'autre.

Aucun des deux sites ne publie de gain chiffré propre à son mode sobre. Niji met en avant une note EcoIndex A sur l'ensemble de ses pages, sans distinguer les deux modes. C'est pourtant ce que demandent la deuxième et la troisième condition du moyen de test. Mesurer le poids des pages dans chacun des deux modes, comme le propose l'onglet « Mise en œuvre technique », suffirait à combler ce manque.

{{% /tab %}}

{{< /tabs >}}
