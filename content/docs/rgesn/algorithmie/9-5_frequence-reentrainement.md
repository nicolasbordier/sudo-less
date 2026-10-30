---
weight: 500
title: "9.5 - Fréquence de réentraînement des modèles"
description: "Critère 9.5 du RGESN : déclencher un réentraînement sur un signal mesuré (baisse de qualité, dérive des données, retours des utilisateurs, contrainte légale) plutôt que sur un calendrier fixe, et documenter ces conditions."
icon: "event_repeat"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique optimise-t-il l'occurrence de mise à jour et de réentraînement des modèles en fonction de ses besoins et des cibles utilisatrices ?

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
| **Critère**  | `9.5` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'entraînement` |
| **Métiers concernés** | `Porteur de projet` `Data Scientist` `Chef de produit marketing` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.5/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Il s'agit de questionner la fréquence des mises à jour et des réentraînements des modèles sous-jacents au service numérique en fonction des besoins réels du service (en termes de qualité et de vérifiabilité) et des besoins des cibles utilisatrices. Chaque mise à jour ou nouvel entraînement est consommateur en ressources et génère des émissions de gaz à effet de serre.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Etablir dès la conception du service les paramètres de déclenchement d'un réentraînement du modèle. Ces paramètres devront tenir compte des besoins réels du service et des utilisateurs, notamment en termes de qualité, de fiabilité et de vérifiabilité. Analyser les données d'utilisation du service numérique pour ajuster en continu les besoins en termes de mise à jour des modèles. Prendre en compte les retours des utilisateurs, les évolutions technologiques et les changements dans l'environnement concurrentiel pour déterminer la fréquence optimale des mises à jour et de réentraînement. Minimiser autant que possible le réentraînement des modèles algorithmiques du service.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Fixer les conditions de déclenchement du réentraînement ou de la mise à jour des modèles algorithmiques du service en se basant sur les besoins réels des utilisateurs ou sur d'éventuelles contraintes légales. Minimiser la fréquence de ces opérations dans une démarche de sobriété. Documenter ces périmètres et les choix effectués dans la déclaration d'écoconception du service, en justifiant la prise en compte des principes d'écoconception.

Le critère est validé s'il est démontré que la fréquence de réentraînement est proportionnelle aux besoins du service et des cibles utilisatrices et est, autant que possible, minimisée grâce au suivi d'indicateurs (de performance, de satisfaction et de consommation en ressources).

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="W3C" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Data Scientist`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) posent une règle proche pour les données, dans la fiche [**« Define the frequency of data refreshes »**](https://www.w3.org/TR/web-sustainability-guidelines/#define-the-frequency-of-data-refreshes) : fixer le rythme de mise à jour « based on user needs, accuracy requirements, and resource efficiency ». Le 9.5 applique la même logique aux modèles.

Dans la fiche sur l'IA, le critère « Environmental responsibilities » demande de mesurer les impacts sur tout le cycle de vie du modèle : chaque réentraînement en fait partie.

{{% /tab %}}

{{% tab tabName="Déclencher sur un signal" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Chef de produit marketing`

Un réentraînement « tous les mois » se déclenche même quand le modèle fonctionne encore. Le RGESN demande au contraire des **conditions de déclenchement**, fixées dès la conception. Un exemple, à adapter :

| Signal | Mesure | Seuil de déclenchement |
|---|---|---|
| Baisse de qualité | Précision sur un échantillon récent, annoté chaque mois | Sous le niveau de satisfaction du [critère 9.1](../9-1_necessite-entrainement/) |
| Dérive des données | Part des entrées inconnues du modèle : nouveaux termes, nouvelles catégories | Au-delà d'une part fixée à la conception, 10 % par exemple |
| Retours des utilisateurs | Signalements d'erreurs, taux de correction manuelle | Hausse durable sur plusieurs semaines |
| Contrainte légale | Nouvelle réglementation, données à retirer | Dès qu'elle s'applique |

Une **évolution technologique**, comme un nouveau modèle publié, n'est un signal que si elle apporte un gain mesuré sur l'une de ces lignes.

**Le chef de produit marketing** a ici un rôle, car la pression concurrentielle pousse à mettre à jour plus souvent. Le RGESN la cite parmi les éléments à considérer, mais demande de minimiser la fréquence : une nouvelle version doit apporter un gain que l'utilisateur perçoit.

{{% /tab %}}

{{% tab tabName="Mise en œuvre" %}}

Profil(s) métier concerné(s) : `Data Scientist`, `Porteur de projet`

**1. Constituer un échantillon de contrôle** : quelques centaines d'entrées récentes, annotées, renouvelées régulièrement. C'est lui qui montre si le modèle se dégrade.

**2. Écrire les conditions de déclenchement** du tableau précédent, avec leurs seuils, avant la mise en production.

**3. Suivre les trois familles d'indicateurs** que cite le moyen de test : performance (précision sur l'échantillon), satisfaction (retours, corrections) et consommation (énergie de chaque entraînement, mesurée comme au [critère 9.3](../9-3_quantite-entrainement/)).

**4. Préférer un affinage à un réentraînement complet** quand un signal se déclenche : seules les nouvelles données sont apprises.

**5. Planifier l'entraînement au bon moment**, quand l'électricité est peu carbonée ([critère 8.10](../../hebergement/8-10_decalage-asynchrone/)).

**6. Documenter** dans la déclaration d'écoconception : les conditions de déclenchement, les seuils, et la date et la raison des derniers réentraînements.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Data Scientist`

- le [critère 9.3](../9-3_quantite-entrainement/) (quantité d'entraînement) : chaque réentraînement se mesure comme le premier ;
- le [critère 9.4](../9-4_donnees-apprentissage/) (données) : un réentraînement n'a besoin que des données nouvelles ou corrigées ;
- le [critère 8.10](../../hebergement/8-10_decalage-asynchrone/) (traitements décalés) : un réentraînement peut presque toujours attendre quelques heures.

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

Aucun des services relevés n'entraîne ni ne réentraîne de modèle. **compar:IA** pose la même question pour la liste des modèles qu'il propose : sa [déclaration d'écoconception](https://arene.comparia.beta.gouv.fr/eco-design) cite « la sélection et le suivi des modèles proposés » parmi ses actions.

{{% /tab %}}

{{< /tabs >}}
