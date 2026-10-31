---
weight: 600
title: "9.6 - Compression des modèles"
description: "Critère 9.6 du RGESN : réduire la taille des modèles par quantification, distillation ou élagage, mesurer la qualité avant et après, et indiquer les gains obtenus dans la déclaration d'écoconception."
icon: "unfold_less"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il des techniques de compression pour les modèles utilisés lors de la phase d'entraînement ?

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
| **Critère**  | `9.6` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'entraînement` |
| **Métiers concernés** | `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.6/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Compresser les modèles d'intelligence artificielle (réduction de complexité des modèles) pour réduire l'impact environnemental.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Compresser les modèles via les méthodes suivantes :

- Sparsification ;
- Pruning ;
- Unification ;
- Local scaling (pour limiter l'impact de la quantification) ;
- Batch norm folding (réduire la redondance de certains paramètres) ;
- Quantification ;
- Distillation ;
- ...

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est validé si le service numérique justifie de la mise en œuvre de méthodes de compression de modèles, en indiquant les gains réalisés dans la déclaration d'écoconception du service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

La compression se fait pendant ou après l'entraînement, mais c'est surtout l'**inférence** qui en profite : un modèle plus petit demande moins de mémoire, moins de calcul et souvent moins de cartes graphiques, à chaque utilisation ([critère 9.7](../9-7_strategie-inference/)).

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="Les méthodes" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Architecte Logiciel`

Les principales méthodes citées par le RGESN :

| Méthode | Principe |
|---|---|
| Quantification | Stocker et calculer les paramètres avec moins de bits : 8 ou 4 au lieu de 16 ou 32 |
| Distillation | Entraîner un petit modèle « élève » à reproduire les réponses d'un grand modèle « maître » |
| Élagage (*pruning*) | Retirer les connexions ou les neurones qui contribuent peu au résultat |
| Parcimonie (*sparsification*) | Forcer une grande partie des paramètres à zéro, pour ne calculer que les autres |
| *Batch norm folding* | Fusionner les couches de normalisation dans les couches voisines, une fois l'entraînement terminé |

Le RGESN cite aussi le *local scaling*, qui sert à limiter la perte de précision due à la quantification.

Le [RIA](https://ria.greenit.fr/) du Collectif GreenIT, dans sa fiche [0021 « Compresser les modèles »](https://ria.greenit.fr/fr/fiches/RIA_0021-compresser-les-modeles), retient trois de ces méthodes (distillation, élagage, quantification) et demande d'évaluer la compression pour chaque modèle utilisé.

**Un exemple publié : la distillation.** Les auteurs de [DistilBERT](https://arxiv.org/abs/1910.01108) ont réduit la taille de BERT « by 40% », en conservant « 97% of its language understanding capabilities » et en étant « 60% faster ».

{{% /tab %}}

{{% tab tabName="Ce que la quantification change" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Responsable RSE/Numérique soutenable`

**Sur un petit modèle, testé.** Le 30 octobre 2026, la régression logistique du [critère 9.2](../9-2_methode-apprentissage/) (788 460 paramètres) a été stockée sur moins de bits :

| Précision des paramètres | Poids du modèle | Précision du classement |
|---|---:|---:|
| 64 bits | 6,31 Mo | 68,96 % |
| 32 bits | 3,15 Mo | 68,96 % |
| 16 bits | 1,58 Mo | 68,96 % |

Le modèle pèse quatre fois moins, sans perte de précision.

**Sur un grand modèle de langage, estimé.** D'après la méthode [EcoLogits](https://ecologits.ai/latest/) (version 0.11.3), le nombre de cartes graphiques nécessaires dépend de la mémoire qu'occupe le modèle. Pour un modèle de 70 milliards de paramètres et une réponse de 400 jetons :

| Quantification | Mémoire du modèle | Cartes de 80 Go | Énergie estimée par réponse |
|---|---:|---:|---:|
| 16 bits | 168 Go | 4 | 0,26 Wh |
| 8 bits | 84 Go | 2 | 0,13 Wh |
| 4 bits | 42 Go | 1 | 0,07 Wh |

L'estimation ne tient compte que du nombre de cartes : elle ne dit rien de la qualité des réponses, qui peut baisser à 4 bits. C'est cette perte qu'il faut mesurer.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Data Scientist`

**1. Mesurer la référence** avant toute compression : qualité sur le jeu de test, taille du modèle, temps de réponse, mémoire occupée.

**2. Essayer d'abord la quantification après entraînement**, la plus simple : 8 bits, puis 4 bits. Les principaux outils de déploiement la proposent (PyTorch, ONNX Runtime, llama.cpp, vLLM).

**3. Mesurer la qualité à chaque étape**, sur le même jeu de test, et s'arrêter quand elle passe sous le niveau de satisfaction du [critère 9.1](../9-1_necessite-entrainement/).

**4. Si le modèle reste trop gros**, envisager la distillation vers un modèle plus petit, ou l'élagage. Elles demandent un entraînement supplémentaire, à mesurer comme au [critère 9.3](../9-3_quantite-entrainement/).

**5. Documenter les gains**, comme l'exige le moyen de test : méthode, taille avant et après, qualité avant et après, et si possible énergie par inférence.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`

- le [critère 9.7](../9-7_strategie-inference/) (inférence) : c'est là que la compression produit ses gains ;
- le [critère 9.2](../9-2_methode-apprentissage/) (méthode) : un modèle plus simple n'a pas besoin d'être compressé ;
- le [critère 9.3](../9-3_quantite-entrainement/) (quantité d'entraînement) : la distillation et l'élagage ajoutent un entraînement.

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

Aucun des services relevés n'entraîne de modèle. **compar:IA** utilise des modèles entraînés par d'autres, et ne choisit pas leur compression. Sa [déclaration d'écoconception](https://arene.comparia.beta.gouv.fr/eco-design) cite en revanche « la présentation de modèles de tailles et de caractéristiques différentes ». Comparer un petit modèle à un grand, sur une même question, permet à l'utilisateur de juger si la différence de taille se voit dans la réponse.

{{% /tab %}}

{{< /tabs >}}
