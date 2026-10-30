---
weight: 800
title: "1.8 - Efforts d'open source"
description: "Critère 1.8 du RGESN : pourquoi et comment publier le code source d'un service numérique en licence libre pour allonger sa durée de vie et celle du matériel associé."
icon: "article"
date: "2026-07-03T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique a-t-il mis en place des efforts d'open source ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Stratégie` |
| **Critère**  | `1.8` |
| **Phase** | `Toutes les phases` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `Applicable à tous les services` |
| **Métiers concernés** | `Porteur de projet` `Responsable Développement` `Responsable Juridique` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/1.8/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

L'**open source** permet la réutilisation du code pour d'autres projets, évitant ainsi un **gaspillage de ressources** dédiées. La publication du code source d'un service numérique en format libre permet d'**allonger la durée de vie du service** en s'appuyant sur la collaboration avec les communautés de développeurs et de chercheurs pour pallier d'éventuels défauts ou ajouter de nouvelles fonctionnalités. Elle renforce également son **auditabilité** et sa **transparence**, y compris d'un point de vue environnemental.

L'open source est aussi un levier pour **allonger la durée de vie du matériel** associé à l'utilisation d'un service numérique : par exemple, les applications ou pilotes ouverts associés à un objet connecté (enceinte, montre connectée…) ou à un périphérique (imprimante…) permettent de suppléer à la fin de vie de programmes propriétaires nécessaires à leur utilisation.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

**Publier le code source** du service numérique en licence libre pour les éléments qui ne sont **pas couverts par des obligations de confidentialité**, et dans la limite des **droits de propriété intellectuelle** applicables.

Lorsque cela est possible, l'**utilisation de code open source** existant est également à privilégier pour la conception et le développement du service, plutôt que de redévelopper des briques déjà disponibles.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le **code source** du service numérique est publié en open source lorsqu'il n'est soumis ni à des restrictions de confidentialité, ni aux droits de propriété intellectuelle de tiers.

Si certaines parties du code ne sont **pas publiées en open source**, les raisons de ce choix doivent être **justifiées dans la déclaration d'écoconception** du service, afin d'être auditables par un tiers. Le fournisseur devra le cas échéant faire état de ses **efforts pour ouvrir tout ou partie** de son code source. Lorsque cela est possible, le service numérique devrait également **utiliser du code open source** pour son propre fonctionnement.

Le critère est **validé** si le code du service est publié en licence libre, **ou** si les choix et efforts effectués en la matière sont justifiés dans la déclaration d'écoconception.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="4">}}
{{% tab tabName="code.gouv.fr / DINUM" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable Juridique`

Pour un acteur public français, l'ouverture du code source n'est pas qu'une bonne pratique d'écoconception : c'est une **obligation légale**. Depuis la loi pour une République numérique, le code source produit par une administration est un **document administratif communicable**, soumis aux mêmes obligations d'ouverture que les bases de données publiques.

Le [Pôle open source et communs numériques de la DINUM](https://code.gouv.fr/fr/), qui pilote cette politique depuis la circulaire du Premier ministre du 27 avril 2021, propose plusieurs ressources directement actionnables :

- [code.gouv.fr](https://code.gouv.fr/fr/) recense les codes sources et bibliothèques publiés par les administrations, pour favoriser leur **réutilisation** plutôt qu'un redéveloppement (cf. mise en œuvre du critère) ;
- son [guide des licences libres](https://code.gouv.fr/fr/doc/licences-libres-dinum/) liste, pour un code source public, les licences reconnues à la fois par la FSF et l'OSI : permissives (**MIT**, **Apache 2.0**, **BSD**) ou à réciprocité (**GPL v3**, **AGPL v3**, **LGPL v3**, **MPL 2.0**, **EPL 2.0**, **EUPL 1.2**). Il y ajoute la famille française **CeCILL** (CEA, CNRS, Inria), reconnue par une seule des deux : la CeCILL 2.1 par l'OSI, les CeCILL-B et CeCILL-C par la FSF ;
- le [Socle Interministériel des Logiciels Libres (SILL)](https://code.gouv.fr/sill/) référence les logiciels libres recommandés pour l'administration, à privilégier lors du choix de composants tiers.

{{% /tab %}}

{{% tab tabName="beta.gouv.fr" %}}

Profil(s) métier concerné(s) : `Porteur de projet`

Le [Manifeste beta.gouv.fr](https://beta.gouv.fr/manifeste) fait de l'open source un principe fondateur plutôt qu'une option : « En contrepartie de cette autonomie, l'équipe assure une transparence la plus large possible sur son travail (**code source ouvert**, mesure de l'impact publique, budget ouvert, démonstrations fréquentes, documentation facilement accessible). » Toutes les startups d'État publient ainsi par défaut leur code sur l'organisation [github.com/betagouv](https://github.com/betagouv), qui compte plus de 700 dépôts publics.

Cette politique de « open source par défaut » illustre concrètement l'esprit du critère 1.8 : l'ouverture du code n'est pas traitée comme un effort ponctuel à justifier a posteriori, mais comme une contrainte de conception dès le départ du projet.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Juridique`

Les trois obstacles cités par les e-novateurs (voir les retours d'expériences), les clés d'API, l'historique Git et le README, se traitent dans cet ordre.

**1. Chercher les secrets** dans les fichiers et dans tout l'historique, avec [Gitleaks](https://github.com/gitleaks/gitleaks) (open source) :

```sh
gitleaks dir -v .                       # fichiers actuels
gitleaks git -v --log-opts="--all" .    # historique de toutes les branches
```

L'option `--redact` masque les secrets dans le rapport, ce qui sert en intégration continue.

**2. Révoquer chaque secret trouvé**, avant toute réécriture. La documentation de git-filter-repo le rappelle : une clé révoquée ne donne plus accès à rien, et cela peut suffire sans toucher à l'historique.

**3. Publier dans un nouveau dépôt** plutôt que de rendre public le dépôt privé. Les forges gardent des références qu'on ne peut pas réécrire (`refs/pull/*`, `refs/merge-requests/*`), qui conservent les anciens commits ([git-filter-repo](https://github.com/newren/git-filter-repo/blob/main/Documentation/git-filter-repo.txt)). Deux options.

**Sans l'historique**, quand il ne vaut pas un nettoyage :

```sh
git checkout --orphan publication
git commit -m "Publication initiale"
git push https://forge.exemple.fr/service-public.git publication:main
```

Testé le 30 octobre 2026 avec Git 2.54 sur un dépôt factice : le dépôt publié ne contient qu'un commit, sans le fichier `.env` retiré auparavant. Les fichiers actuels doivent avoir passé `gitleaks dir`.

**Avec l'historique**, en retirant fichiers et chaînes sensibles dans un clone neuf, avec [git-filter-repo](https://github.com/newren/git-filter-repo) 2.47 ou plus récent :

```sh
git filter-repo --sensitive-data-removal --invert-paths --path .env
git filter-repo --sensitive-data-removal --replace-text secrets.txt
```

Le fichier `secrets.txt` contient une chaîne par ligne, remplacée par `***REMOVED***`.

**4. Indiquer la licence dans chaque fichier.** Après le choix de la licence (onglet « code.gouv.fr / DINUM »), l'outil [REUSE](https://reuse.software/) de la FSFE ajoute un en-tête SPDX à chaque fichier, télécharge le texte de la licence et vérifie que rien ne manque :

```sh
reuse annotate --copyright "Ministère de l'Exemple" --license EUPL-1.2 --recursive src/
reuse download --all
reuse lint
```

**5. Écrire le README** : ce que fait le service, comment l'installer et le lancer en local, comment contribuer, qui contacter.

**6. Référencer le dépôt.** Pour une administration, déclarer son compte d'organisation sur code.gouv.fr : écrire à floss@numerique.gouv.fr ou proposer un ajout au fichier [`comptes-organismes-publics.yml`](https://github.com/codegouvfr/codegouvfr-data/blob/main/comptes-organismes-publics.yml). Les comptes personnels ne sont pas référencés.

**7. Documenter** dans la déclaration d'écoconception : l'adresse du dépôt, la licence, et les parties non publiées avec leur raison (confidentialité, propriété intellectuelle de tiers), comme l'exige le moyen de test.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Responsable Développement`

- le [critère 1.9](../1-9_technologies-standard/) (technologies standard) : code ouvert et formats standard se renforcent ;
- le [critère 1.10](../1-10_api-materiel/) (API ouvertes pour le matériel) : la même ouverture, appliquée au matériel ;
- le [critère 3.1](../../architecture/3-1_architecture-composants/) (composants écoconçus) : réutiliser une brique libre plutôt que la développer ;
- le [critère 2.7](../../specifications/2-7_maintenance-decommissionnement/) (maintenance et décommissionnement) : un code publié peut être repris après la fin du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Le contraste entre deux déclarations d'écoconception publiques illustre bien les deux issues possibles de ce critère :

- [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, évaluation de janvier 2025) marque ce critère **« Non validé »**, avec la justification suivante : « Le service numérique ne publie pas son code source sous licence open-source à ce jour. » C'est une non-conformité documentée honnêtement.
- [Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) marquent aussi ce critère **« Non validé »**, mais avec une justification qui montre un chantier engagé plutôt qu'une absence de démarche : « le code source est disponible sur GitHub mais de manière privée. Un nettoyage des clés API, de l'historique Git et un travail du README doit être effectué pour le rendre public. » — les trois obstacles concrets (secrets accidentellement commités, historique à assainir, documentation à écrire) qui bloquent le plus souvent le passage à l'open source d'un dépôt existant.
- À l'inverse, les startups d'État de [beta.gouv.fr](https://github.com/betagouv) publient leur code par défaut. [DiaLog](https://dialog.beta.gouv.fr/ecoconception) valide ainsi le critère : « Le service numérique publie tout son code en open source, sous la licence GPL v3 », sans effort de mise en conformité a posteriori.

Ce contraste rappelle que ce critère, noté « Fort » en difficulté, se traite bien plus facilement **en amont** (choisir une licence et un dépôt public dès l'initialisation du projet) qu'**a posteriori** sur un code déjà écrit sans cette contrainte — où subsistent alors des questions de propriété intellectuelle, de secrets métier mêlés au code, ou de dépendances propriétaires à isoler avant publication.

Côté secteur privé, le rapport [« Apports du logiciel libre à la durabilité des équipements »](https://code.gouv.fr/docs/2023_01_RapportIndiceDurabilite.pdf) (Pierre-Yves Gibello/OW2 pour la DINUM, janvier 2023) documente, avec des témoignages nommés, le lien direct entre ce critère et l'**allongement de la durée de vie du matériel** évoqué dans l'objectif de la fiche RGESN :

- **Fairphone** a mis à jour son Fairphone 2, sorti en 2015, vers Android 9, en compilant lui-même le système « without any support from chip-maker Qualcomm », ce que permet le code ouvert d'Android. Des systèmes libres comme /e/OS, vendus avec support par [Murena](https://murena.com/), prolongent de même la vie des smartphones.
- **ATF** (entreprise de l'économie sociale et solidaire, 350 000 ordinateurs reconditionnés par an) : son ex-directeur du développement témoigne — « sur un vieux Core 2 Duo, Windows ne passe plus, et ça fonctionne très bien sous Linux » — imputant le problème à une stratégie conjointe d'obsolescence programmée entre constructeurs et éditeurs d'OS propriétaires.
- **Fréco / Electrocycle** estime que 100 % des ordinateurs populaires de 2004 à 2015 restent exploitables et à jour avec un système libre, contre 0 % avec Windows.
- Le réseau **Ordi3.0** (200 structures labellisées, 300 000 ordinateurs reconditionnés/an) cite un de ses labellisés faisant durer des postes jusqu'à **18 ans** grâce à un système d'exploitation et une suite logicielle open source.
- [**Emmabuntüs**](https://emmabuntus.org/) est une distribution GNU/Linux open source conçue spécifiquement pour simplifier le reconditionnement d'ordinateurs usagés par des associations, illustrant très concrètement comment l'ouverture d'un système d'exploitation peut, à elle seule, prolonger la durée de vie d'un parc matériel plutôt que de rester une simple question de licence de code (source : [ADEME, État des lieux et perspectives des démarches low-tech — fiche Numérique](https://librairie.ademe.fr/consommer-autrement/5421-demarches-low-tech.html), 2021).

Ces exemples illustrent, en creux, pourquoi ce critère va au-delà de la seule transparence du code : l'open source y est un **levier concret de sobriété matérielle**, en évitant le remplacement d'un équipement encore fonctionnel faute de support logiciel.

{{% /tab %}}

{{< /tabs >}}
