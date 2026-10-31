---
weight: 300
title: "9.3 - Limiter la quantité d'entraînement"
description: "Critère 9.3 du RGESN : réutiliser un modèle pré-entraîné, affiner seulement ce qui est nécessaire, mesurer l'énergie de chaque entraînement face à sa précision, et entraîner là où l'électricité est peu carbonée."
icon: "model_training"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il mis en place des mécanismes visant à limiter la quantité d'entraînement nécessaire à son fonctionnement ?

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
| **Critère**  | `9.3` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'entraînement` |
| **Métiers concernés** | `Porteur de projet` `Data Scientist` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Limiter la phase d'entraînement utilisée par le service numérique en choisissant des modèles déjà existants et pré-entraînés. Éviter le surentraînement en maîtrisant la consommation énergétique du mécanisme choisi.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Utiliser un modèle déjà entraîné ou, à défaut, un fine-tuning d'un modèle pré-entraîné.

Mettre en œuvre les outils permettant la production de métriques de consommation de ressources (CPU / GPU / TPU / énergies, etc.) et les mettre en corrélation avec des métriques de qualité (précision, etc.) afin de limiter la consommation au juste nécessaire.

S'assurer de l'utilisation de CPU, de GPU ou de TPU efficaces, dont la localisation géographique est cohérente avec les activités concernées et qui minimise l'empreinte environnementale (en particulier, dans un pays à l'intensité carbone la plus faible possible).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Avant la conception du service, faire un état de l'art des modèles existants pouvant s'apparenter à la fonctionnalité visée. Utiliser un modèle pré-entraîné, si nécessaire en ajoutant des composants complémentaires (fine-tuning). Si le service n'utilise pas un modèle préexistant (déjà entraîné ou pré-entraîné), justifier dans la déclaration d'écoconception en quoi le cas d'usage est différent de ce qui existe dans l'état de l'art.

Par ailleurs, pour valider le critère, le service devrait avoir mis en place le suivi d'indicateurs de consommation de ressources et de qualité des fonctions de la phase d'apprentissage pour assurer l'optimisation de la quantité d'entraînement sous-jacente au fonctionnement du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="AFNOR et W3C" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Responsable RSE/Numérique soutenable`

L'[AFNOR Spec 2314](https://www.boutique.afnor.org/en-gb/standard/afnor-spec-2314/fa208976/421140) propose une méthode d'évaluation des impacts sur tout le cycle de vie du service d'IA, entraînement compris : c'est le cadre des indicateurs que le 9.3 demande de suivre.

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026), dans la fiche [**« Establish responsible practices around AI and emerging or disruptive technologies »**](https://www.w3.org/TR/web-sustainability-guidelines/#establish-responsible-practices-around-ai-and-emerging-or-disruptive-technologies), demandent d'« Optimize models and deployment processes for efficiency » et de mesurer les impacts « throughout their lifecycle », y compris ceux des tiers, avec « credible estimates » à défaut de données directes.

{{% /tab %}}

{{% tab tabName="Réutiliser plutôt qu'entraîner" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Architecte Logiciel`

Du moins coûteux au plus coûteux :

| Approche | Ce qui est entraîné |
|---|---|
| Modèle pré-entraîné utilisé tel quel | Rien |
| Affinage partiel (LoRA, dernières couches) | Une petite partie des paramètres |
| Affinage complet d'un modèle pré-entraîné | Tous les paramètres, à partir d'un point de départ |
| Entraînement depuis zéro | Tous les paramètres, depuis le hasard |

**L'état de l'art se consulte avant de concevoir**, comme le demande le moyen de test : catalogues de modèles par tâche (le Hub de Hugging Face, par exemple), articles et modèles publiés par la communauté. Le [RIA](https://ria.greenit.fr/) du Collectif GreenIT en fait sa fiche [0018 « Utiliser des modèles déjà entraînés »](https://ria.greenit.fr/fr/fiches/RIA_0018-utiliser-des-modeles-deja-entraines), qui cite aussi les catalogues de Kaggle et de TensorFlow.

**L'affinage partiel change l'ordre de grandeur.** Pour GPT-3, les auteurs de [LoRA](https://arxiv.org/abs/2106.09685) indiquent que la méthode « can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times », par rapport à un affinage complet.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Data Scientist`

**1. Mesurer chaque entraînement** et le mettre en regard de sa qualité. Avec CodeCarbon :

```python
from codecarbon import OfflineEmissionsTracker

suivi = OfflineEmissionsTracker(country_iso_code="FRA", save_to_file=False)
suivi.start()
modele.fit(X_entrainement, y_entrainement)
emissions = suivi.stop()                                 # kgCO2eq
energie = suivi.final_emissions_data.energy_consumed     # kWh
precision = modele.score(X_test, y_test)
```

Testé le 30 octobre 2026 avec CodeCarbon 3.3.2 (voir le [critère 9.2](../9-2_methode-apprentissage/)). Sans accès en lecture aux compteurs RAPL du processeur (`/sys/class/powercap`), CodeCarbon se replie sur une estimation à partir de la charge du processeur, et l'indique dans son journal. Pour une mesure, il faut lui donner cet accès.

**2. Arrêter l'entraînement quand la qualité ne progresse plus.** La plupart des bibliothèques le permettent : `early_stopping=True` dans scikit-learn, le rappel `EarlyStopping` dans Keras. L'entraînement s'interrompt dès que la précision sur un jeu de validation stagne.

**3. Tracer la courbe précision–énergie** des essais successifs : au-delà d'un certain point, chaque point de précision coûte beaucoup plus d'énergie que le précédent. Le niveau de satisfaction du [critère 9.1](../9-1_necessite-entrainement/) indique où s'arrêter.

**4. Choisir où et quand entraîner** : dans un pays dont l'électricité est peu carbonée ([critère 8.6](../../hebergement/8-6_localisation/)), sur du matériel récent et bien occupé, et au moment où le réseau est le moins carboné pour les entraînements qui peuvent attendre ([critère 8.10](../../hebergement/8-10_decalage-asynchrone/)).

**5. Documenter** dans la déclaration d'écoconception : le modèle de départ, ce qui a été entraîné, l'énergie et la précision obtenues.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`

- le [critère 9.2](../9-2_methode-apprentissage/) (méthode) : la méthode la plus simple d'abord ;
- le [critère 9.4](../9-4_donnees-apprentissage/) (données) : moins de données, c'est aussi moins d'entraînement ;
- le [critère 9.5](../9-5_frequence-reentrainement/) (réentraînement) : chaque nouvel entraînement repasse par la même mesure ;
- le [critère 8.10](../../hebergement/8-10_decalage-asynchrone/) (traitements décalés) : un entraînement est un calcul asynchrone.

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

**compar:IA** illustre la première ligne du tableau « Réutiliser plutôt qu'entraîner » : il n'entraîne aucun modèle et fait appel à des modèles existants. Sa [déclaration d'écoconception](https://arene.comparia.beta.gouv.fr/eco-design) reconnaît une limite : l'impact de l'entraînement de ces modèles, réalisé par leurs éditeurs, ne peut pas être mesuré directement.

{{% /tab %}}

{{< /tabs >}}
