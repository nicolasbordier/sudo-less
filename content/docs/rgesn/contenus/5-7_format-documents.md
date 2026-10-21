---
weight: 700
title: "5.7 - Format de fichier adapté à chaque document"
description: "Critère 5.7 du RGESN : choisir le format adapté à l'usage (HTML, PDF, vectoriel), compresser les documents à la source sans perdre leur accessibilité et documenter sa stratégie de compression."
icon: "description"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il un format de fichier adapté au contenu et au contexte d'utilisation pour chaque document ?

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
| **Critère**  | `5.7` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur l'utilisation de fichiers` |
| **Métiers concernés** | `Développeur` `Responsable IT` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/5.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire le poids des fichiers téléchargés par les utilisateurs.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir les paramètres de compression des documents afin de générer des fichiers de taille réduite.

Prendre en compte les besoins spécifiques du contenu et du contexte d'utilisation pour déterminer le format de fichier le plus approprié. Par exemple utiliser une image vectorielle si c'est plus pertinent qu'une image matricielle (ou images bitmap), constituée de pixels.

Avoir notamment recours à un format de fichier optimisé pour une visualisation en ligne, lorsque le document est destiné à être consulté en ligne.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Évaluer le poids du document en fonction de son contenu. Le critère est validé si les documents utilisés pour l'opération du service numérique sont compressés de façon à réduire leur poids et à s'adapter au contexte de visualisation, d'utilisation, et à leur contenu. La stratégie de compression des documents doit être documentée et auditable par un tiers, par exemple en étant détaillée dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a deux fiches explicitement étiquetées « RGESN 5.7 ».

[**RWEB 0109 — « Optimiser les PDF »**](https://rweb.greenit.fr/fr/fiches/RWEB_0109-optimiser-les-pdf) demande de vérifier, avant la mise en ligne, le « taux d'échantillonnage et de compression des images, polices incorporées, résolution ». Pour un rapport annuel, elle recommande des images « fortement compressées et à une résolution maximale de 72 dpi », de « n'inclure que les principales polices » et de découper le rapport en chapitres. La valeur de 72 dpi vaut pour un document lu à l'écran. Pour un document destiné à être imprimé, elle est trop basse : c'est là que le RGESN demande de s'adapter au « contexte d'utilisation » (voir l'onglet « Compression et accessibilité »).

[**RWEB 0033 — « Ne pas afficher les documents à l'intérieur des pages »**](https://rweb.greenit.fr/fr/fiches/RWEB_0033-ne-pas-afficher-les-documents-a-l-interieur-des-pages) part d'un constat simple : « À chaque consultation de la page, le fichier est téléchargé pour être affiché ». Elle recommande un lien de téléchargement, « afin que seuls les utilisateurs concernés le téléchargent ». Son principe de validation : **aucun** document affiché dans un contenu.

La fiche [**RWEB 0108 — « Compresser les documents »**](https://rweb.greenit.fr/fr/fiches/RWEB_0108-compresser-les-documents), présentée au [critère 5.4](../5-4_compression-videos/), propose de compresser les documents en ZIP, « sauf si la compression n'apporte pas un gain évident (par exemple, cas d'un PDF parfaitement optimisé pour le Web) ». Elle est rattachée aux critères 5.2, 5.4 et 5.6, pas au 5.7. Sur le PDF du RGESN lui-même, une archive ZIP fait gagner 32 % ; mais l'utilisateur doit alors la décompresser avant de lire le document, que le navigateur n'affiche plus directement. Optimiser le PDF lui-même reste préférable.

{{% /tab %}}

{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Contributeur`, `Développeur`

Le [GR491](https://gr491.isit-europe.org/) (INR) consacre au sujet un critère **incontournable** de la [recommandation n°5 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=5), en priorité **High** : [« Les documents à télécharger sont-ils compressés, optimisés et accessibles ? »](https://gr491.isit-europe.org/crit.php?id=5-contenus-les-documents-disponibles-pour-lutilisateur-dans-le-c66540) Ses tests : « Tous vos documents sont-ils compressés ? » et « Les tailles et formats des fichiers sont-ils connus de l'utilisateur avant son opération de téléchargement ? » Sa règle d'évaluation donne un indicateur simple : « Documents compressés / Documents disponibles ».

Le mot **accessibles** compte. Une compression mal choisie peut supprimer le balisage qui rend un PDF lisible par un lecteur d'écran (voir l'onglet « Compression et accessibilité »).

Le conseil [« Dans le cas d'un long document de type PDF, est-il possible de le télécharger chapitre par chapitre ? »](https://gr491.isit-europe.org/crit.php?id=5-contenus-les-documents-volumineux-sont-rarement-integralement-lus-86e8e7) part d'un constat : « Les documents volumineux sont rarement intégralement lus par les utilisateurs ou du moins en une seule fois. » Ses tests posent les bonnes questions avant de produire un fichier :

- « Au delà de quel volume, proposez-vous un chargement segmenté ? »
- « Un fichier à télécharger est-il indispensable et la meilleure solution pour l'utilisateur, par rapport à une version en ligne ? »
- « Une fonction de preview, ou de vue dans le browser est-elle disponible ? »

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Contributeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 5.7 dans sa section [**7.9 Documents**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-9-documents-a-telecharger), déjà présentée au [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) pour l'affichage du poids : « Compresser les documents et choisir le format de fichier adapté à l'usage permet de valider le critère 5.7 ».

Sur la compression, le guide demande d'éviter « la surqualité des documents à télécharger » et rappelle que « dans PowerPoint ou Keynote, il existe une option pour compresser et réduire la taille des images et du fichier ». Il cite aussi le service en ligne iLovePDF pour compresser les PDF. Comme le relève le critère 4.11, envoyer un document à un service en ligne pose une question de protection des données ; les outils locaux de l'onglet « Mise en œuvre technique » l'évitent.

Sur le format, le guide reprend l'analyse de Praticable ([« Le pdf, ce format en carton »](https://praticable.fr/publications/le-probleme-des-etudes)) : un PDF est « Non responsive donc peu confortable à lire sur mobile », « Peu accessible », « Non référencé », et pose une « Difficulté à mettre à jour ». D'où deux conseils :

- **Fournir un résumé** dans la page, pour éviter un téléchargement inutile ;
- **Proposer plusieurs versions** d'un même document. Le guide donne l'exemple d'un rapport de GreenIT.fr proposé en rapport complet (PDF de 40 pages, 716 Ko), en page HTML, en synthèse (PDF de 13 pages, 289 Ko) et en infographie (PNG, 222 Ko).

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

La fiche [**« Reduce the impact of downloadable and physical documents »**](https://www.w3.org/TR/web-sustainability-guidelines/#reduce-the-impact-of-downloadable-and-physical-documents) des [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026), déjà citée au [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) pour l'affichage du poids, couvre aussi l'essentiel du critère 5.7 :

- **Optimized documents** : « Optimize and compress downloadable documents, provide them in accessible formats that suit different user needs, and choose open, widely supported formats (such as HTML) over proprietary file formats. »
- **Optimized delivery** : « When a document is reused, generate and store it once on the server so it can be reused efficiently ».
- **Labels and choice** : « Avoid embedding documents directly in pages; instead provide download or browser-view links. »

Le premier point associe, comme le GR491, compression et **accessibilité**, et cite HTML comme format de référence : c'est le « format de fichier optimisé pour une visualisation en ligne » du RGESN. Le deuxième vise les documents générés à la demande (attestations, exports) : les produire une fois et les conserver, plutôt que de les régénérer à chaque téléchargement. Le troisième rejoint la fiche RWEB 0033 : un lien, que le navigateur ouvre dans sa propre visionneuse si l'utilisateur le souhaite, plutôt qu'un document intégré dans la page.

{{% /tab %}}

{{% tab tabName="Compression et accessibilité" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Pour comparer les outils, le PDF du RGESN lui-même ([version de mai 2024](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/referentiel_general_ecoconception_des_services_numeriques_version_2024.pdf), 131 pages, produit avec Word 2019) a été traité le 20 octobre 2026 avec Ghostscript 10.06 et qpdf 12.4 :

| Traitement | Poids | Gain | Balisé (accessible) | Linéarisé (affichage rapide) |
|---|---:|---:|---|---|
| Original | 4,18 Mo | — | Oui | Non |
| Ghostscript, réglage `/printer` | 3,85 Mo | 8 % | **Non** | Oui |
| Ghostscript, réglage `/ebook` | 3,82 Mo | 9 % | **Non** | Oui |
| Ghostscript, réglage `/screen` | 1,84 Mo | 56 % | **Non** | Oui |
| qpdf, sans perte | 3,49 Mo | 16 % | Oui | Oui |

Trois constats :

- **Ghostscript supprime le balisage.** Les trois réglages produisent un PDF non balisé : la structure qui permet à un lecteur d'écran de lire les titres, listes et tableaux dans l'ordre disparaît. Pour un service public, soumis au RGAA, c'est une régression. C'est aussi la condition « accessibles » du GR491 et du W3C.
- **La compression forte dégrade les images.** Le réglage `/screen` divise le poids par deux en réduisant les images à 72 ppi : elles deviennent floues et bruitées dès qu'on zoome. Les réglages `/ebook` et `/printer` gagnent peu, car les images de ce document, à 200 ppi, sont déjà proches de leur cible.
- **qpdf optimise sans perte.** Il réorganise le fichier, compresse mieux sa structure interne et le linéarise, sans toucher aux images ni au balisage.

La leçon : la compression des images se règle **à la source**, au moment de l'export depuis le traitement de texte, qui produit un PDF balisé. qpdf intervient ensuite pour optimiser et linéariser sans perte. Un outil qui réécrit tout le PDF ne s'emploie que sur un document dont l'accessibilité a été vérifiée après coup.

**Linéarisé** désigne un PDF organisé pour l'affichage en ligne (« Fast Web View », « Optimisé pour le Web ») : la première page peut s'afficher avant la fin du téléchargement. C'est le sens du « format de fichier optimisé pour une visualisation en ligne » du RGESN, quand le document reste un PDF.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

**1. Choisir le format selon l'usage**, avant de compresser :

| Usage du document | Format à privilégier | Pourquoi |
|---|---|---|
| Lu en ligne (guide, actualité, rapport) | Page HTML, PDF en option | Responsive, accessible, référencé, mis à jour sans nouveau fichier |
| Imprimé, rempli ou signé (formulaire, contrat) | PDF balisé et linéarisé | Mise en page figée, accessible si balisé |
| Données (tableau chiffré) | CSV ou ODS | Réutilisable, bien plus léger qu'un tableau en PDF |
| Schéma, logo, illustration simple | Vectoriel (SVG, formes du traitement de texte) | Quelques centaines d'octets, net à toutes les tailles |

**2. Régler la compression à l'export**, dans l'outil qui produit le document. Avec LibreOffice, en ligne de commande (testé avec LibreOffice 26.2) :

```bash
soffice --headless --convert-to 'pdf:writer_pdf_Export:{
  "UseTaggedPDF":{"type":"boolean","value":"true"},
  "ReduceImageResolution":{"type":"boolean","value":"true"},
  "MaxImageResolution":{"type":"long","value":"150"},
  "Quality":{"type":"long","value":"75"}}' rapport.odt
```

- **`UseTaggedPDF`** produit un PDF balisé, donc accessible. C'est déjà la valeur par défaut de LibreOffice 26.2.
- **`MaxImageResolution`** réduit les images à 150 ppi, au lieu de 300 par défaut. 150 ppi suffisent à l'écran et pour une impression courante ; 300 ppi ne se justifient que pour une impression soignée.
- **`Quality`** règle la compression JPEG des photos (90 par défaut).

Sur un document de test contenant une image pleine page, ces réglages font passer le PDF de 136 Ko à 63 Ko, en restant balisé. Dans l'interface, les mêmes options se trouvent dans **Fichier > Exporter au format PDF**. Dans Word, la résolution des images se règle dans **Fichier > Options > Avancé**, rubrique « Taille et qualité d'image » ; d'après [Microsoft](https://support.microsoft.com/fr-fr/office/r%C3%A9duire-la-taille-de-fichier-de-vos-images-dans-microsoft-office-8db7211c-d958-457c-babd-194109eb9535), « La résolution d'image par défaut dans Microsoft 365 est de 220 ppi ».

**3. Optimiser et linéariser sans perte** avec [qpdf](https://qpdf.readthedocs.io/), logiciel libre :

```bash
qpdf --linearize --object-streams=generate --recompress-flate rapport.pdf rapport-web.pdf
```

`--linearize` organise le fichier pour l'affichage en ligne ; `--object-streams=generate` et `--recompress-flate` compressent mieux sa structure interne. Les images, le texte et le balisage ne changent pas (−16 % sur le PDF du RGESN).

**4. Contrôler** avec `pdfinfo` et `pdfimages`, de la suite libre Poppler :

```bash
pdfinfo rapport-web.pdf | grep -E 'Tagged|Optimized|File size'
pdfimages -list rapport-web.pdf
```

`Tagged: yes` confirme que le balisage est conservé, `Optimized: yes` que le fichier est linéarisé. La colonne `x-ppi` de `pdfimages` signale les images de résolution excessive ; si une même image apparaît sur plusieurs lignes avec le même numéro d'objet, elle n'est stockée qu'une fois.

**5. Proposer un lien plutôt qu'un document intégré** (fiche RWEB 0033, W3C) : pas d'`<iframe>` ni d'`<embed>` qui télécharge le PDF à chaque affichage de la page. Le lien indique le format et le poids (voir le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/)), et le navigateur ouvre le PDF dans sa propre visionneuse si l'utilisateur clique.

**6. Documenter** la stratégie dans la déclaration d'écoconception, comme l'exige le moyen de test (« documentée et auditable par un tiers »). Par exemple : « Les contenus destinés à la lecture en ligne sont publiés en HTML. Les PDF sont exportés depuis LibreOffice, balisés, avec des images limitées à 150 ppi et une qualité JPEG de 75, puis linéarisés avec qpdf. Les données chiffrées sont proposées en CSV. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Contributeur`

Ce critère est le pendant, pour les documents, de plusieurs critères déjà publiés sur ce site :

- le [critère 4.11](../../ux-ui/4-11_poids-formats-fichiers/) (poids et formats des fichiers) : le 4.11 demande d'**annoncer** le poids et le format, le 5.7 de les **réduire**. Le 4.11 présente aussi la compression des PDF **téléversés** par les utilisateurs, avec le cas mesuré de Territoires en Transitions ;
- le [critère 4.7](../../ux-ui/4-7_choix-sobre-format/) (choix du format le plus sobre) : avant de choisir le format d'un fichier, se demander si un fichier est nécessaire ;
- les critères [5.1](../5-1_format-images/) et [5.2](../5-2_compression-images/) (format et compression des images) : les images d'un document obéissent aux mêmes règles que celles d'une page, vectoriel quand c'est possible et résolution adaptée à l'affichage ;
- le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) (fonctionnalités à fort impact) : un export de document généré à la demande en fait partie.

Le critère suivant du RGESN, le [5.8](../5-8_archivage-suppression/) (archivage et suppression des contenus obsolètes), complète celui-ci : le document le plus léger reste celui qu'on a retiré quand il n'était plus utile.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

**Le référentiel lui-même.** Le PDF du RGESN (mai 2024, 4,18 Mo) illustre la « Mise en œuvre » de son critère 5.7. D'après `pdfimages`, ses 11 images pleine page à 200 ppi, dont la couverture et les pages d'ouverture de chapitre, pèsent à elles seules 2,19 Mo, soit **plus de la moitié du fichier**. Les pages de chapitre montrent un triangle en dégradé, son contour et un court texte, le tout enregistré comme une photo JPEG de 1 654 × 2 338 pixels (146 Ko pour la page « Contenus »). Le même triangle, dessiné en SVG, tient en **420 octets**, le texte restant du texte. C'est exactement l'exemple du RGESN : « utiliser une image vectorielle si c'est plus pertinent qu'une image matricielle ».

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, [déclaration du 23 avril 2025](https://dialog.beta.gouv.fr/files/2025-04-23%20-%20Declaration.ecoconception.DiaLog-2_compressed.pdf)) marque le critère **« Validé »** : « Stratégie de compression des documents : le fichier Word que l'utilisateur peut exporter est léger (en dessous de 100 Ko) ». La déclaration donne le résultat, pas la stratégie elle-même (format, réglages, outils), que le moyen de test demande de rendre « auditable par un tiers ». Le PDF de la déclaration a d'ailleurs été compressé : son nom se termine par « _compressed » et ses métadonnées indiquent iLovePDF comme logiciel producteur. Il pèse 185 Ko pour 13 pages, mais n'est pas balisé.

{{% /tab %}}

{{< /tabs >}}
