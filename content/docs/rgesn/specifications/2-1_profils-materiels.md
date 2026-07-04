---
weight: 100
title: "2.1 - Profils de matériels"
description: "Critère 2.1 du RGESN : pourquoi et comment définir les profils de matériels supportés par un service numérique, en privilégiant la compatibilité avec les équipements anciens."
icon: "devices"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-04T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il défini la liste des profils de matériels que les utilisateurs vont pouvoir employer pour y accéder ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Spécifications` |
| **Critère**  | `2.1` |
| **Phase** | `Exploration` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.1/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Un service numérique n'exploitant que des **ressources techniques de toute dernière génération** peut conduire les utilisateurs à **renouveler leurs équipements** afin d'y accéder — c'est l'**obsolescence matérielle** induite par le logiciel. Certaines utilisations peuvent ainsi être contraintes par les terminaux des utilisateurs.

Pour permettre un choix plus large d'équipements, même anciens, et limiter le renouvellement de matériel, il est important de **connaître les profils de matériel** que les utilisateurs vont pouvoir employer, aujourd'hui et demain : débit minimum de connexion, taille d'écran, vitesse du microprocesseur, mémoire vive, écran tactile ou non, smartphone, tablette, ordinateur portable ou de bureau, etc.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

**Définir le profil des matériels supportés**, en assurant la compatibilité avec les équipements **aussi anciens que possible**, afin d'éviter toute obsolescence matérielle induite par le service.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le critère est **validé** si le profil des matériels supportés par le service est établi de façon à **privilégier les équipements aussi anciens que possible**, et que ce profil minimum matériel est **affiché dans la déclaration d'écoconception** du service.

Si certaines fonctionnalités nécessitent une version plus récente, **indiquer les versions minimales** avec et sans support de ces fonctionnalités. Il convient également d'indiquer les **éventuelles évolutions à venir** sur la configuration matérielle minimum.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="2">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Responsable RSE/Numérique soutenable`

Le critère 2.1 du RGESN rejoint la [recommandation n°5 de la famille Spécifications](https://gr491.isit-europe.org/?famille=specifications&num_reco=5) du [GR491](https://gr491.isit-europe.org/) (INR) : « Préparer le suivi du cycle de vie du projet et des indicateurs de performance / bénéfice NR ». Elle pousse le questionnement au-delà de la seule définition initiale du profil matériel :

- **État des lieux** : les équipements actuels des utilisateurs sont-ils évalués ?
- **Impact des mises à jour** : la gestion des impacts des mises à jour logicielles sur la mise en obsolescence des matériels est-elle évaluée ?
- **Durée de vie visée** : le produit cible-t-il une durée de vie déterminée ?
- **Fin de vie** : les données et procédures spécifiées ont-elles toutes une information de fin de vie ?

{{% /tab %}}

{{% tab tabName="ARCEP - Baromètre du numérique" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Développeur`

Pour définir un profil matériel réaliste plutôt qu'arbitraire, le [Baromètre du numérique](https://www.arcep.fr/cartes-et-donnees/nos-publications-chiffrees/barometre-du-numerique/le-barometre-du-numerique-edition-2026.html) (enquête annuelle Arcep/CRÉDOC/ANCT/Arcom, données ouvertes depuis 2007) donne une photographie chiffrée et actualisée du parc d'équipements réel en France — utile pour objectiver un choix de compatibilité plutôt que de se caler sur les derniers modèles disponibles :

- Le taux d'équipement en smartphone atteint 91 % de la population de 12 ans et plus en 2024, mais avec un **écart net selon l'âge** : 96 % chez les 12-39 ans, contre 80 % chez les 60-69 ans et seulement 62 % chez les 70 ans et plus.
- 82 % de la population se connecte quotidiennement à internet — une part significative reste donc en dehors de ce socle, avec des équipements et usages hétérogènes.

Exclure les équipements anciens revient ainsi, de façon disproportionnée, à exclure les **populations les plus âgées** — un angle mort fréquent si le profil matériel est calé sur l'équipe projet elle-même plutôt que sur la base d'utilisateurs réelle ou visée.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 30 janvier 2025) valide ce critère avec une justification concise : « Le produit FACE utilise les standards du web et ne présente pas d'algorithme sur-consommant du CPU. » Ce cas illustre le lien direct entre ce critère et le choix de technologies standard du [critère 1.9](../../strategie/1-9_technologies-standard/) : une application web standard, sans exigence matérielle spécifique, valide quasi automatiquement le critère 2.1 — à l'inverse d'une application native qui devrait documenter explicitement ses versions minimales d'OS.

C'est justement ce que fait [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) (Pôle ministériel Écologie), avec le niveau de précision attendu par ce critère : sa déclaration d'écoconception indique noir sur blanc « **Appareil mobile Android 6.0 ou plus (terminaux mobile de 2015 ou plus)** » et « **Appareil mobile IOS 10.3 ou plus (terminaux de 2012 ou plus)** ». À noter : SPOTE reste une application web (accessible par navigateur mobile) et non une application native — mais la déclaration documente malgré tout un profil matériel précis, avec version d'OS **et** année de terminal, exactement dans l'esprit de l'exemple donné par le texte officiel du critère (« iOS 11 minimum, Android à partir de 2015… »).

{{% /tab %}}

{{< /tabs >}}
