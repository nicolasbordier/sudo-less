---
weight: 400
title: "9.4 - Données d'apprentissage limitées au nécessaire"
description: "Critère 9.4 du RGESN : réutiliser des jeux de données existants, mesurer la quantité de données réellement utile avec une courbe d'apprentissage, et appliquer cache, compression et durées de conservation aux données d'entraînement."
icon: "dataset"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique limite-il la quantité de données utilisées pour la phase d'apprentissage au strict nécessaire ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Algorithmie` |
| **Critère**  | `9.4` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'entraînement` |
| **Métiers concernés** | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` `Responsable de la protection des données` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.4/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Il s'agit de s'interroger sur les données collectées et de minimiser les impacts environnementaux associés à leur collecte et à leur traitement pour la phase d'entraînement, en privilégiant des données existantes et en limitant la collecte de nouvelles données. Ce critère est pertinent pour la phase d'apprentissage, caractérisée le plus souvent par une forte obsolescence des bases de données utilisées.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Veiller à réutiliser, si possible, des données existantes (notamment libres de droit) afin de limiter la collecte de nouvelles données et la puissance de calcul requise pour l'analyse incrémentielle de données. Questionner l'empreinte environnementale de l'acquisition de nouveau matériel de stockage contre celui du téléchargement systématique des données lorsque nécessaire.

Veiller à limiter la captation de nouvelles données pour la phase d'apprentissage.

Appliquer les critères 7.1 et 7.2 pour la mise en place de cache, de compression et de politique de gestion pour les données de la phase d'apprentissage.

Comme le souligne le rapport de la CNIL « Données, Empreinte et Libertés » (2023), certains impératifs de respect de la vie privée et objectifs d'écoconception se rejoignent.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Utiliser des bases de données existantes pour l'entraînement de son service numérique. Vérifier que la collecte de données est minimisée et mentionner les méthodes mises en œuvre dans la déclaration d'écoconception du service numérique.

Examiner également, la mise en place des critères 7.1 et 7.2 pour la mise en place de cache, de compression et de politique de gestion pour les données utilisées pour la phase d'apprentissage.

Le critère est validé si le service utilise, dès que cela est possible, des bases de données existantes et applique les critères 7.1 et 7.2 pour la phase d'apprentissage tout en documentant sa gestion de données, et l'inclusion des enjeux de sobriété, dans sa déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="CNIL et W3C" %}}

Profil(s) métier concerné(s) : `Responsable de la protection des données`, `Data Scientist`

Le rapport cité par le RGESN est le neuvième cahier Innovation et prospective de la CNIL, [**« Données, empreinte et libertés »**](https://www.cnil.fr/sites/cnil/files/2023-07/cnil_cahier_ip9_0.pdf) (juin 2023). Il montre que plusieurs principes du RGPD réduisent aussi l'empreinte : la **minimisation** des données, la limitation des **durées de conservation** et la limitation des **finalités**. Le **responsable de la protection des données** et le data scientist poursuivent donc ici le même but.

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) le demandent dans le critère « AI and data collection » de la fiche [**« Establish responsible practices around AI and emerging or disruptive technologies »**](https://www.w3.org/TR/web-sustainability-guidelines/#establish-responsible-practices-around-ai-and-emerging-or-disruptive-technologies) : des jeux de données « no larger than necessary for the task ».

{{% /tab %}}

{{% tab tabName="Combien de données suffisent ?" %}}

Profil(s) métier concerné(s) : `Data Scientist`

La précision n'augmente pas en proportion des données. Testé le 30 octobre 2026 sur le jeu **20 Newsgroups**, avec le même modèle Naive Bayes qu'au [critère 9.2](../9-2_methode-apprentissage/), entraîné sur une part croissante des textes :

| Part des données | Textes | Précision |
|---:|---:|---:|
| 10 % | 1 131 | 60,4 % |
| 25 % | 2 828 | 66,4 % |
| 50 % | 5 657 | 69,5 % |
| 75 % | 8 485 | 70,7 % |
| 100 % | 11 314 | 71,4 % |

La seconde moitié des données n'apporte que 1,9 point. Si le niveau de satisfaction fixé au [critère 9.1](../9-1_necessite-entrainement/) est de 69 %, la moitié des textes suffit : deux fois moins de données à collecter, stocker et traiter.

Cette courbe d'apprentissage se trace avant toute nouvelle collecte, sur les données déjà disponibles. Si elle est plate, collecter davantage ne servira pas.

Le [RIA](https://ria.greenit.fr/) du Collectif GreenIT le demande aussi, dans sa fiche [0020 « Minimiser la taille des jeux de données d'entraînement »](https://ria.greenit.fr/fr/fiches/RIA_0020-minimiser-la-taille-des-jeux-de-donnees-d-entrainement) : aucun entraînement sans avoir qualifié la taille et la qualité du jeu. Elle cite des jeux ouverts à réutiliser avant de collecter (Kaggle, Hugging Face, portail open data de l'ADEME).

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Développeur`

**1. Chercher des données existantes avant d'en collecter** : jeux ouverts de [data.gouv.fr](https://www.data.gouv.fr/), catalogues de jeux de données pour l'apprentissage, données déjà détenues par le service.

**2. Tracer la courbe d'apprentissage** de l'onglet précédent, pour connaître la quantité utile.

**3. Ne collecter que les champs qui servent au modèle**, avec le [critère 1.6](../../strategie/1-6_collecte-donnees/) et le responsable de la protection des données. Un champ qui n'améliore pas la précision n'a rien à faire dans le jeu d'entraînement.

**4. Télécharger une fois, réutiliser ensuite.** Les bibliothèques gardent les jeux de données en cache local : `data_home` dans scikit-learn, `HF_HOME` pour les bibliothèques de Hugging Face. Partager ce cache entre les essais et les membres de l'équipe évite de télécharger les mêmes données à chaque entraînement ([critère 7.1](../../backend/7-1_cache-serveur/)).

**5. Compresser et dater les jeux d'entraînement** : un format compressé comme Parquet pour le stockage, une durée de conservation pour chaque version, et la suppression des versions qui ne servent plus ([critère 7.2](../../backend/7-2_durees-conservation/)).

**6. Documenter** dans la déclaration d'écoconception : les jeux réutilisés, les données collectées et pourquoi, la quantité retenue et la règle de conservation.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Responsable de la protection des données`

- le [critère 1.6](../../strategie/1-6_collecte-donnees/) (collecte des données) : la même minimisation, pour tout le service ;
- les critères [7.1](../../backend/7-1_cache-serveur/) (cache) et [7.2](../../backend/7-2_durees-conservation/) (durées de conservation), que le 9.4 demande d'appliquer aux données d'entraînement ;
- le [critère 9.3](../9-3_quantite-entrainement/) (quantité d'entraînement) : moins de données, c'est aussi moins de calcul.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues le 30 octobre 2026.

| Site | Déclaration |
|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | Non applicable |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Non applicable |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Non applicable |

**compar:IA** est du côté de ceux qui fournissent les données. Les questions posées et les votes sont publiés librement, après anonymisation, sur [data.gouv.fr](https://www.data.gouv.fr/datasets/compar-ia/) et sur [Hugging Face](https://huggingface.co/datasets/ministere-culture/comparia-fr-arena). Le service les présente comme une ressource pour affiner les modèles sur le français. Pour un service qui veut adapter un modèle au français, c'est un jeu existant à réutiliser plutôt qu'une collecte à lancer.

{{% /tab %}}

{{< /tabs >}}
