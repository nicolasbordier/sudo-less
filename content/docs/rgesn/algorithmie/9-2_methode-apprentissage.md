---
weight: 200
title: "9.2 - Méthode d'apprentissage la plus sobre"
description: "Critère 9.2 du RGESN : commencer par la méthode d'apprentissage la plus simple, mesurer sa précision et son coût, et ne passer à un modèle plus complexe que si le gain est démontré."
icon: "scatter_plot"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il une phase d'apprentissage avec un niveau de complexité minimisé et proportionné à l'usage effectif du service ?

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
| **Critère**  | `9.2` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'entraînement` |
| **Métiers concernés** | `Porteur de projet` `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Mettre en question le choix de la méthode d'apprentissage pour le service numérique et choisir la méthode d'entraînement la plus frugale, adéquate et proportionnée à l'usage du service.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Faire le choix de la frugalité en privilégiant des méthodes simples, comme une régression ou à défaut des réseaux de neurones simples, à des technologies d'apprentissage profond (deep-learning) plus consommatrices de ressources de calcul.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Vérifier la consommation énergétique et en ressources matérielles de la méthode d'entraînement utilisée par le service numérique : cette dernière doit être testée ou reconnue comme pauvre en consommation d'énergie et de ressources.

Si le service ne repose pas sur des méthodes de régression ou autres méthodes peu coûteuses (low-complex, low-cost), justifier dans la déclaration d'écoconception du service le besoin de méthodes plus consommatrices par une référence à un état de l'art précisant la nécessité de méthodes plus complexes pour le cas d'usage cible.

Le critère est validé si le choix de la méthode d'apprentissage est l'alternative la plus sobre disponible selon l'état de l'art et les caractéristiques du service, et que ces choix sont documentés dans la déclaration d'écoconception associée ainsi qu'auditables par un tiers.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="AFNOR et W3C" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Architecte Logiciel`

L'[AFNOR Spec 2314](https://www.boutique.afnor.org/en-gb/standard/afnor-spec-2314/fa208976/421140) traite le 9.2 sous l'angle de l'**efficience** du système : à besoin égal, le modèle qui consomme le moins.

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026), dans la fiche [**« Establish responsible practices around AI and emerging or disruptive technologies »**](https://www.w3.org/TR/web-sustainability-guidelines/#establish-responsible-practices-around-ai-and-emerging-or-disruptive-technologies), demandent de « Prioritize approaches that minimize negative environmental impacts ».

{{% /tab %}}

{{% tab tabName="L'état de l'art" %}}

Profil(s) métier concerné(s) : `Data Scientist`

Le moyen de test demande de justifier toute méthode complexe par « un état de l'art ». Une étude répond à la question pour les grands modèles.

Dans [**« Power Hungry Processing: Watts Driving the Cost of AI Deployment? »**](https://arxiv.org/abs/2311.16863) (FAccT 2024), Alexandra Sasha Luccioni, Yacine Jernite et Emma Strubell ont mesuré l'énergie de 1 000 inférences sur de nombreuses tâches. Leur conclusion : les architectures génératives polyvalentes sont « orders of magnitude more expensive than task-specific systems », « even when controlling for the number of model parameters ».

Pour classer des textes, extraire des informations ou détecter un sujet, un modèle spécialisé est donc la référence de départ. Un grand modèle génératif, entraîné ou affiné pour une tâche simple, doit prouver ce qu'il apporte de plus.

{{% /tab %}}

{{% tab tabName="Un test : simple ou réseau de neurones" %}}

Profil(s) métier concerné(s) : `Data Scientist`

Testé le 30 octobre 2026 avec scikit-learn 1.9.1, sur le jeu de données public **20 Newsgroups**. Il s'agit de classer des messages en 20 thèmes : 11 314 textes d'entraînement, 7 532 de test, représentés par 39 423 termes (TF-IDF). L'énergie est l'estimation de CodeCarbon 3.3.2, à partir de la charge d'un processeur AMD Ryzen 7 7735HS.

| Méthode | Précision | Entraînement | Énergie estimée |
|---|---:|---:|---:|
| Naive Bayes (ComplementNB) | **71,4 %** | moins de 0,1 s | moins de 0,001 Wh |
| Régression logistique | 69,0 % | 15 s | 0,31 Wh |
| Réseau de neurones (une couche cachée de 256) | 70,8 % | 169 s | 1,6 Wh |

**La méthode la plus simple est ici la plus précise.** Le réseau de neurones coûte cinq fois plus d'énergie que la régression logistique, et plus de mille fois plus de temps que Naive Bayes, pour une précision inférieure.

Le résultat dépend du jeu de données : sur des images ou des textes longs et ambigus, un réseau peut faire mieux. C'est précisément ce que la mesure doit montrer, avant de choisir.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Architecte Logiciel`

**1. Établir une référence simple** : régression logistique ou linéaire, Naive Bayes, arbre de décision. Elle s'entraîne en quelques secondes sur un ordinateur ordinaire.

**2. Comparer au niveau de satisfaction** fixé au [critère 9.1](../9-1_necessite-entrainement/). Si la référence l'atteint, s'arrêter.

**3. Augmenter la complexité par paliers** : forêt d'arbres, petit réseau, puis apprentissage profond. À chaque palier, mesurer la précision gagnée et l'énergie dépensée, avec CodeCarbon par exemple ([critère 9.3](../9-3_quantite-entrainement/)).

**4. Garder le tableau des essais**, comme celui de l'onglet précédent : méthode, précision, durée, énergie. Il rend le choix « auditable par un tiers », comme l'exige le moyen de test.

**5. Documenter** dans la déclaration d'écoconception : la méthode retenue, les alternatives testées et la référence de l'état de l'art si la méthode est complexe.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`

- le [critère 9.1](../9-1_necessite-entrainement/) (nécessité) : le niveau de satisfaction qui borne le choix ;
- le [critère 9.3](../9-3_quantite-entrainement/) (quantité d'entraînement) : mesurer la consommation de chaque essai ;
- le [critère 9.7](../9-7_strategie-inference/) (inférence) : un modèle simple coûte aussi moins cher à chaque utilisation.

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

Aucun des services relevés n'entraîne de modèle : le critère ne s'applique pas. Le test de l'onglet « Un test : simple ou réseau de neurones » montre la démarche attendue d'un service qui en entraînerait un.

{{% /tab %}}

{{< /tabs >}}
