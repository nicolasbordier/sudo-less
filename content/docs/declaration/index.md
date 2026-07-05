---
weight: 150
title: "Déclaration"
description: "Comment rédiger une déclaration d'écoconception RGESN et calculer son score d'avancement : contenu obligatoire, modèles officiels, formule de calcul et exemples réels."
icon: "fact_check"
date: "2026-07-05T00:00:00+01:00"
lastmod: "2026-07-05T00:00:00+01:00"
draft: false
toc: true
---

La publication d'une **déclaration d'écoconception** est un prérequis pour se prévaloir de l'application du [RGESN](../rgesn/) : elle documente, critère par critère, les efforts mis en place, et rend possible le calcul d'un **score d'avancement**. Cette page explique comment rédiger l'une et calculer l'autre.

{{< tabs tabTotal="3">}}

{{% tab tabName="Rédiger sa déclaration" %}}

Le référentiel recommande de renseigner, en première page de la déclaration :

- Le **nom du service évalué**, la date de rédaction et celle de la dernière mise à jour.
- La **liste des critères validés et non validés** (le numéro de la fiche pratique suffit à les identifier).
- Le **score d'avancement** du service — voir l'onglet « Calculer le score d'avancement » — et si possible le score précédemment calculé ainsi que le score visé à terme (par exemple à date + 2 ans).
- Le **plan d'avancement** : les engagements pris et les actions mises en place pour réduire les impacts environnementaux du service, notamment la réduction de la contribution à l'obsolescence des terminaux.
- Les **chemins critiques et unités fonctionnelles évalués** — les fonctionnalités principales du service doivent faire partie de l'échantillon testé.
- La **documentation détaillée** de la mise en œuvre de chaque critère applicable, en cohérence avec les fiches pratiques du référentiel.

La déclaration devrait être **datée et régulièrement mise à jour**, idéalement à chaque modification significative du service. Elle peut être publiée sur le site du service lui-même ou de l'organisme responsable — par exemple dans les mentions légales, aux côtés d'une déclaration d'accessibilité, ou sur une page dédiée.

**Modèles officiels** (RGESN, DINUM/Arcep) :

- Exemple de déclaration en version texte : [.docx](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.docx), [.odt](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.odt), [.html](https://www.arcep.fr/fileadmin/user_upload/nos-sujets/environnement/rgesn_2024_exemple_declaration_ecoconception.html)
- Outil d'autoévaluation en tableur, qui permet à la fois de rédiger la déclaration et de calculer automatiquement le score : [.xlsx](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.xlsx), [.ods](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.ods)

{{% /tab %}}

{{% tab tabName="Calculer le score d'avancement" %}}

Le score d'avancement **n'est pas un indicateur d'impact environnemental** : c'est un indicateur de suivi de la mise en œuvre du référentiel, qui permet à un concepteur de service de mesurer dynamiquement sa progression.

Chaque critère validé compte selon la **pondération de son niveau de priorité** :

| Niveau de priorité | Pondération |
|---|---|
| Prioritaire | × 1,5 |
| Recommandé | × 1,25 |
| Modéré | × 1,0 |

**Formule officielle :**

```
Score = [Σ(critères validés × pondération) / Σ(critères applicables × pondération)] × 100
```

Soit, en détaillant chaque niveau :

```
[(nb critères validés Prioritaire × 1,5) + (nb critères validés Recommandé × 1,25) + (nb critères validés Modéré × 1,0)]
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── × 100
[(nb critères applicables Prioritaire × 1,5) + (nb critères applicables Recommandé × 1,25) + (nb critères applicables Modéré × 1,0)]
```

Points d'attention pour un calcul fiable :

- Un critère marqué **« Applicable à tous les services »** dans sa fiche pratique ne doit **jamais** être compté comme « N/A », même si son application semble difficile dans le contexte du service évalué.
- En cas de **validation partielle** des moyens de test d'un critère, celui-ci ne doit **pas** être considéré comme validé.
- Les conditions précises de validation ou de non-applicabilité de chaque critère sont détaillées dans les onglets « Mise en œuvre » et « Moyen de test ou de contrôle » de sa fiche RGESN — voir les fiches [Stratégie](../rgesn/strategie/) et [Spécifications](../rgesn/specifications/) de ce site.

En pratique, l'[outil tableur officiel](https://ecoresponsable.numerique.gouv.fr/docs/2024/rgesn-mai2024/rgesn_2024_outil_declaration_ecoconception.xlsx) applique cette formule automatiquement à partir des réponses saisies critère par critère — il n'est donc pas nécessaire de calculer ce score manuellement.

{{% /tab %}}

{{% tab tabName="Exemples réels" %}}

Ces déclarations publiques permettent de voir à quoi ressemble un score d'avancement et une documentation par critère réellement publiés :

- [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement) : déclaration complète critère par critère, y compris des critères non validés assumés comme tels — citée à plusieurs reprises dans les fiches de ce site (par exemple les critères [2.2](../rgesn/specifications/2-2_anciens-terminaux/), [2.3](../rgesn/specifications/2-3_connexion-bas-debit/) et [2.5](../rgesn/specifications/2-5_terminaux-affichage/)).
- [SPOTE](https://spote.developpement-durable.gouv.fr/article/declaration-d-ecoconception) (Pôle ministériel Écologie) : déclaration avec mapping ODD détaillé et exemples de décommissionnement de fonctionnalités peu utilisées.
- [DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr) : déclaration publique avec justification du besoin métier et prise en compte explicite des contraintes d'accessibilité et de connectivité dégradée.
- [Territoires en Transitions](https://beta.gouv.fr/startups/territoires-en-transitions.html) (beta.gouv.fr, porté par l'ADEME) : revue d'écoconception intégrée au rythme des sprints plutôt qu'un audit ponctuel isolé.

Pour situer un service avant même de rédiger une déclaration complète, [NumEcoDiag](https://ecoresponsable.numerique.gouv.fr/ressources/documents-reference/referentiel-general-ecoconception/numecodiag/) (MiNumEco/DINUM, extension navigateur gratuite) permet une auto-évaluation rapide sur les 79 critères et génère un badge HTML ainsi qu'un export CSV réutilisable comme point de départ.

{{% /tab %}}

{{< /tabs >}}
