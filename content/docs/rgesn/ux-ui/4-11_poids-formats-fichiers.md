---
weight: 1100
title: "4.11 - Information sur les poids et formats de fichier attendus"
description: "Critère 4.11 du RGESN : pourquoi et comment afficher le poids et le format des fichiers à télécharger, et limiter de façon proportionnée les fichiers téléversés, avant tout transfert."
icon: "upload_file"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique informe-t-il l'utilisateur, avant le transfert, des poids et formats de fichier attendus ?

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
| **Critère**  | `4.11` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur un transfert de fichier client/serveur dans le cadre d'un formulaire` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.11/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Limiter les échanges client/serveur de fichiers volumineux en informant l'utilisateur des prérequis attendus.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

- **Fichiers téléchargés** : Indiquer clairement à l'utilisateur, au minimum pour les fichiers de plus de 10 Mo et avant le transfert, des poids et des formats de fichier attendus : un type de fichier, une taille maximale d'image, etc.
- **Fichiers téléversés (ou upload)** : la soumission du formulaire n'est pas possible si les prérequis indiqués de poids et de format de fichier ne sont pas respectés. La limite mise en place doit toutefois prendre en compte tous les usages, y compris ceux nécessitant un envoi des fichiers volumineux, car bloquer la démarche numérique de l'utilisateur serait contreproductif. Il est important également de prendre en charge les nouveaux formats de fichiers (exemple : images WebP et AVIF en plus des images JPEG et PNG) afin d'éviter d'imposer à l'utilisateur de passer par une étape de conversion contreproductive.

À noter : les limitations devront être définies de façon proportionnée afin de ne pas engendrer d'effet de bord négatif sur l'accessibilité du service, en tenant compte des cibles utilisatrices.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si :

- **Fichiers téléchargés** : les informations sur les poids et formats de fichier attendus pour le service sont correctement affichées à l'utilisateur avant le transfert, au minimum pour les fichiers de plus de 10 Mo. Un moyen de test peut consister à vérifier cet affichage préalable au transfert de fichier avec différents types et tailles de fichiers.
- **Fichiers téléversés ou upload** : des limitations de poids et de formats de fichiers sont mises en œuvre et sont affichées clairement pour l'utilisateur du service numérique (hors situation spécifique où de telles limitations nuiraient à l'utilisation du service).

Contrôler la mise en œuvre en vérifiant que les limites de poids et de formats de fichiers sont spécifiées puis correctement appliquées lors de la soumission du formulaire.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le critère 4.11 a une correspondance directe dans la [recommandation n°7 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=7) du [GR491](https://gr491.isit-europe.org/) (INR), dont trois critères de la catégorie « Transferts » couvrent le volet téléversement :

- [« Informez-vous les utilisateurs des contraintes de volume et format de fichiers acceptés ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-les-operations-sur-le-front-end-peuvent-fb5846), en priorité **High**, avec pour tests : « Les volumes et formats des fichiers sont-ils limités et exposés aux utilisateurs ? » et « Quelle est la taille maximum autorisée ? » ;
- [« Est-ce que les uploads permettent uniquement la liste des types de fichiers autorisés ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-les-fichiers-transferes-par-lutilisateur-generent-des-852309) ;
- [« Les images à uploader sont-elles bien redimensionnées et converties dans un format léger côté client avant transfert ? »](https://gr491.isit-europe.org/crit.php?id=7-frontend-les-transferts-dimages-introduisent-des-particularites-liees-04ccb4)

Les précisions du premier critère en résument l'enjeu : exposer les types et volumes acceptés permet d'« éviter des charges de transfert, des stockages et des traitements qui seraient voués à l'échec pour cause de non-respect des formats et volumes attendus ». Le deuxième rappelle que le coût d'un fichier téléversé ne s'arrête pas à son transfert : il « génère des traitements, des flux d'échange, des espaces de stockage, une redondance pour sécuriser les données, des sauvegardes ».

Le troisième critère va plus loin que le RGESN : plutôt que de refuser une image trop lourde, la **redimensionner et la convertir dans le navigateur** avant l'envoi. Le GR491 en signale lui-même la limite : ces traitements « nécessitent des ressources de traitements, des espaces de stockage intermédiaires et créent de nouveaux fichiers ».

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 4.11 dans sa section [**7.9 Documents**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-9-documents-a-telecharger), et en traite les deux sens :

- **Téléchargement** : « Avant tout téléchargement par l'utilisateur, indiquer le poids et le format du document. » Le guide ajoute un cas que le RGESN ne traite pas : « S'il s'agit d'un document généré dont le poids n'est pas connu avant export, indiquer un poids approximatif (moyenne des exports par exemple). » Il rappelle aussi que le poids des documents « ne se voit pas dans le poids de la page elle-même », et qu'il « devrait être systématiquement écrit à côté du lien de téléchargement ».
- **Téléversement** : « bien indiquer les formats acceptés et le poids maximum autorisé » et « ne pas permettre de soumettre le formulaire si les fichiers ne correspondent pas aux prérequis ». Le guide illustre l'enjeu par une « photo de profil à 1 Mo », taille disproportionnée qui « se répercute sur les usagers ou services qui chargeront le fichier ».

Un exemple du guide mérite d'être lu avec la « Mise en œuvre » du RGESN : « si les images en webp ne sont pas prises en charge, informer à l'avance l'utilisateur que seuls les jpeg et png sont acceptés ». Informer est le minimum ; le RGESN demande en plus de **prendre en charge** WebP et AVIF, pour éviter à l'utilisateur une conversion.

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), déjà citée aux critères [4.9](../4-9_requetes-saisie-utilisateur/) et [4.10](../4-10_format-saisie/), donne un ordre de grandeur concret dans sa rubrique **Documents** : « Limiter le poids des fichiers uploadés : par exemple à 300 Ko une photo mise en ligne. »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C couvrent le volet téléchargement dans la fiche [**« Reduce the impact of downloadable and physical documents »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-the-impact-of-downloadable-and-physical-documents), critère de succès « Labels and choice » :

- « Show users the document name, format, size, and a short summary before download. »
- « Let users choose the most suitable format and language. »

Le W3C ajoute deux informations au poids et au format demandés par le RGESN : le **nom** du document et un **court résumé**. Un résumé permet souvent à l'utilisateur de savoir s'il a besoin du document avant de le télécharger, ce qui évite le transfert. Le second point recommande de proposer plusieurs formats quand c'est possible, par exemple une version HTML à côté du PDF.

Pour le téléversement, la fiche [**« Reduce data transfer with compression »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-data-transfer-with-compression) demande de « Compress media files such as images, video, and audio before uploading anywhere », dans le même sens que le troisième critère GR491 ci-contre.

{{% /tab %}}

{{% tab tabName="Système de design de l'État (DSFR)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Pour les services publics français, le [Système de design de l'État](https://www.systeme-de-design.gouv.fr/) (DSFR) rend l'affichage du poids et du format obligatoire. Sa [variante « lien de téléchargement »](https://github.com/GouvernementFR/dsfr/blob/main/src/dsfr/component/link/_part/doc/design/index.md) demande de « Préciser le format et le poids du fichier de façon systématique », en plus de « Précéder le nom du document de la mention "Télécharger" » et d'« Indiquer la langue du document si elle est différente de la langue de la page courante ».

Le DSFR va donc plus loin que le RGESN : il ne fixe aucun seuil, là où le RGESN ne l'exige qu'« au minimum pour les fichiers de plus de 10 Mo ». Son code se présente ainsi :

```html
<a download="true" href="image.jpg" class="fr-link fr-link--download">
  Télécharger le document lorem ipsum
  <span class="fr-link__detail">JPG – 61,88 ko</span>
</a>
```

Le DSFR propose aussi de remplir ce détail automatiquement avec l'attribut `data-fr-assess-file`. **Point de vigilance** : d'après [son code source](https://github.com/GouvernementFR/dsfr/blob/main/src/dsfr/core/script/assess/assess-file.js), le script envoie une requête `HEAD` vers chaque fichier à chaque affichage de la page pour en lire le poids. C'est peu par lien, mais c'est une requête par lien et par visite pour une information qui ne change pas. Quand le fichier est connu à la publication, il vaut mieux écrire le poids directement dans la page, ou le calculer côté serveur ou au moment du build pour un site statique. L'ancien composant « Téléchargement de fichier » du DSFR est par ailleurs [déprécié](https://github.com/GouvernementFR/dsfr/blob/main/src/dsfr/component/download/_part/doc/index.md) au profit de cette variante du composant Lien.

{{% /tab %}}

{{% tab tabName="Gauthier Roussilhe" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le [guide d'écoconception rédigé par Gauthier Roussilhe et son équipe pour l'ADEME](https://gauthierroussilhe.com/book/ademe/DOCS.html), déjà cité au [critère 4.8](../4-8_polices-caracteres/), consacre une fiche entière à la **gestion des documents téléversés**, à partir du cas de « Territoires en Transitions ». Les conseillers y déposent des « documents preuves », PDF à 90 %. La fiche part d'un constat : « Le stockage des documents preuves peut représenter à terme le plus gros poids du service ».

Elle pose une règle : « Tous les fichiers mis en ligne (uploadé) doivent être compressés (sans prendre en lisibilité) ». L'équipe a mesuré l'effet sur l'ensemble des documents déposés par une collectivité en 4 ans (66 documents) :

| | Avant compression | Après compression | Gain |
|---|---:|---:|---:|
| PDF (44 documents) | 132 101 Ko | 58 764 Ko | 56 % |
| Ensemble (66 documents) | 143 490 Ko | 70 153 Ko | 51 % |

Seuls les PDF ont été compressés : les autres formats (XLSX, DOCX, PPTX, JPEG) sont restés identiques, et la totalité du gain vient donc des PDF. Si la compression reste à la charge des utilisateurs, la fiche recommande d'expliquer la démarche « dans l'espace de dépôt du service ». C'est l'endroit même où le critère 4.11 demande d'afficher les limites de poids et de format.

**Point de vigilance** : les outils cités par la fiche (I Love PDF, AvePDF, SmallPDF) sont des services en ligne. Y envoyer des documents administratifs pose une question de protection des données. Une compression locale (Ghostscript, `qpdf`) ou côté serveur évite de confier ces documents à un tiers.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

**Téléchargement** : le poids et le format sont écrits dans le lien lui-même, sans requête supplémentaire (voir l'onglet DSFR) :

```html
<a href="/docs/rapport-annuel-2025.pdf" download>
  Télécharger le rapport annuel 2025
  <span>PDF – 4,2 Mo</span>
</a>
```

**Téléversement** : le champ annonce les formats acceptés et le poids maximum, puis vérifie le fichier dès qu'il est choisi, avant tout envoi :

```html
<label for="justificatif">Justificatif de domicile</label>
<p id="justificatif-aide">
  Formats acceptés : PDF, JPEG, PNG, WebP ou AVIF. Poids maximum : 5 Mo.
</p>
<input id="justificatif" name="justificatif" type="file" required
       accept=".pdf,.jpg,.jpeg,.png,.webp,.avif"
       aria-describedby="justificatif-aide justificatif-erreur">
<p id="justificatif-erreur"></p>
```

```js
const POIDS_MAX = 5 * 1024 * 1024; // 5 Mo
const EXTENSIONS = ['pdf', 'jpg', 'jpeg', 'png', 'webp', 'avif'];

const champ = document.querySelector('#justificatif');
const erreur = document.querySelector('#justificatif-erreur');

champ.addEventListener('change', () => {
  const fichier = champ.files[0];
  let message = '';

  if (fichier) {
    const extension = fichier.name.split('.').pop().toLowerCase();
    if (!EXTENSIONS.includes(extension)) {
      message = 'Ce format n\'est pas accepté. Formats acceptés : PDF, JPEG, PNG, WebP ou AVIF.';
    } else if (fichier.size > POIDS_MAX) {
      const poids = (fichier.size / 1024 / 1024).toFixed(1).replace('.', ',');
      message = `Ce fichier pèse ${poids} Mo. Le poids maximum est de 5 Mo.`;
    }
  }

  champ.setCustomValidity(message);
  champ.setAttribute('aria-invalid', String(message !== ''));
  erreur.textContent = message;
});
```

- **Texte d'aide visible avant le choix du fichier** : les formats et le poids maximum sont annoncés avant l'action, comme le demande le moyen de test (« affichées clairement pour l'utilisateur »). Ils sont reliés au champ par `aria-describedby`, comme dans l'exemple du [critère 4.10](../4-10_format-saisie/).
- **`accept`** : le sélecteur de fichiers du système propose d'abord les formats acceptés. Ce n'est qu'un filtre d'affichage : l'utilisateur peut toujours choisir « Tous les fichiers ». La vérification JavaScript reste donc nécessaire.
- **`fichier.size`** : le navigateur connaît le poids du fichier dès qu'il est sélectionné. Un fichier trop lourd est signalé **avant** d'être envoyé, et non après plusieurs mégaoctets transférés pour rien.
- **`setCustomValidity()`** : le champ devient invalide, donc le navigateur bloque la soumission du formulaire. C'est l'exigence du RGESN : « la soumission du formulaire n'est pas possible si les prérequis [...] ne sont pas respectés ». Le gestionnaire de soumission présenté au critère 4.10 en tient compte aussi, puisque `checkValidity()` renvoie alors `false`.
- **WebP et AVIF dans la liste** : c'est la prise en charge des « nouveaux formats » demandée par le RGESN, pour ne pas imposer de conversion.

**Choisir une limite proportionnée.** Les 5 Mo de l'exemple ne sont pas une valeur de référence. Une photo prise au smartphone pèse souvent plusieurs mégaoctets : une limite à 1 Mo pour un justificatif obligerait beaucoup d'utilisateurs à convertir ou réduire leur photo, l'étape « contreproductive » que le RGESN demande d'éviter. La limite doit partir des fichiers que les utilisateurs ont réellement entre les mains. Si une image est ensuite réutilisée en petit format (photo de profil), il est plus efficace de la réduire automatiquement, côté serveur ou dans le navigateur comme le propose le GR491, que de refuser le fichier.

**Côté serveur**, la même limite doit être appliquée, car la vérification côté client peut être contournée. Par exemple avec Nginx :

```nginx
client_max_body_size 5m;
```

Le serveur doit aussi vérifier le **type réel** du fichier, à partir de son contenu, plutôt que de se fier à l'extension contrôlée dans le navigateur.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Ce critère applique aux fichiers la logique du [critère 4.10](../4-10_format-saisie/) (format de saisie attendu), déjà publié sur ce site : annoncer les prérequis avant la saisie, puis bloquer la soumission tant qu'ils ne sont pas respectés. L'enjeu est simplement d'un autre ordre de grandeur. Une saisie de texte invalide renvoyée par le serveur coûte quelques kilo-octets. Un fichier refusé après envoi peut représenter plusieurs mégaoctets transférés, puis parfois stockés et sauvegardés, pour rien.

Pour les **fichiers téléchargés**, ce critère complète le [critère 4.7](../4-7_choix-sobre-format/) (choix du format le plus sobre) : le 4.7 demande de choisir le format le plus léger capable de porter l'information, le 4.11 d'en annoncer le poids et le format avant le transfert. Le [critère 4.12](../4-12_impacts-fonctionnalites/) étend cette information à toute fonctionnalité significativement plus coûteuse que le reste du service, qu'elle produise un fichier ou non (vidéo en haute qualité, export, traitement long). Le [critère 5.7](../../contenus/5-7_format-documents/) (format de fichier adapté à chaque document) porte sur la compression et le choix du format des documents eux-mêmes. La fiche [**RWEB 0109 — « Optimiser les PDF »**](https://rweb.greenit.fr/fr/fiches/RWEB_0109-optimiser-les-pdf) y est rattachée ; la fiche [**RWEB 0108 — « Compresser les documents »**](https://rweb.greenit.fr/fr/fiches/RWEB_0108-compresser-les-documents) l'est aux critères 5.2, 5.4 et 5.6.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »** pour le volet téléchargement : « L'utilisateur peut télécharger le fichier Word correspondant à l'arrêté. Le poids maximum et le format sont indiqués. » L'arrêté est généré à la demande et son poids exact n'est pas connu à l'avance. Indiquer un poids **maximum** correspond au cas des documents générés évoqué par les Designers Éthiques, qui proposent pour leur part un poids approximatif.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque lui aussi ce critère **« Validé »**, avec une justification instructive parce qu'elle reconnaît une limite : « Le service numérique limite les formats pour le téléversement de pièces jointes, côté client. Mais l'information à l'utilisateur n'est pas directe sur le formulaire. » La déclaration précise que le poids est limité à 3 Mo, que cette limite est contrôlée, et que l'utilisateur est prévenu si son fichier est trop lourd.

Le volet « limitation » est donc en place : le fichier trop lourd est arrêté avant d'être transféré. Mais l'utilisateur ne découvre les limites qu'après avoir choisi son fichier, alors que le moyen de test demande qu'elles soient « affichées clairement » et que la question du critère porte sur l'information **avant** le transfert. La validation se discute, et la correction est peu coûteuse : une ligne de texte d'aide sous le champ, comme dans l'onglet « Mise en œuvre technique ».

Le cas de **Territoires en Transitions** (détaillé dans l'onglet « Gauthier Roussilhe » ci-dessus) apporte les seuls chiffres mesurés de cette fiche : une baisse de 51 % du volume des documents téléversés par une collectivité sur 4 ans, obtenue en compressant uniquement les PDF.

{{% /tab %}}

{{< /tabs >}}
