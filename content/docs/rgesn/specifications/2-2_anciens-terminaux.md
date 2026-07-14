---
weight: 200
title: "2.2 - Anciens modèles de terminaux"
description: "Critère 2.2 du RGESN : pourquoi et comment garantir l'utilisabilité d'un service numérique sur des équipements anciens (7 à 10 ans), pour limiter leur renouvellement prématuré."
icon: "history"
date: "2026-07-04T00:00:00+01:00"
lastmod: "2026-07-14T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique est-il utilisable sur d'anciens modèles de terminaux ?

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
| **Critère**  | `2.2` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `Tous les services` |
| **Métiers concernés** | `Responsable IT` `Responsable RSE/Numérique soutenable` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/2.2/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Selon l'**étude ADEME-Arcep**, les terminaux représentent **65 à 92 % de l'empreinte environnementale du numérique** selon l'indicateur considéré, en particulier du fait de leur fabrication. L'**allongement de la durée de vie** de ces derniers est donc un levier essentiel de réduction des impacts environnementaux du numérique.

Le service numérique doit **limiter sa contribution à leur obsolescence** en fonctionnant sur des équipements **aussi anciens que possible**.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Pour chaque fonctionnalité, s'assurer que le service est **compatible avec des équipements anciens** — ce critère peut par exemple être ajouté aux tests ou à la QA (Quality Assurance).

Quelques précisions importantes :

- Il s'agit de la compatibilité avec un **matériel**, et non avec un système d'exploitation ou un logiciel (navigateur) — il n'est donc pas question de rester compatible avec des logiciels dont les **mises à jour de sécurité** n'ont pas été faites.
- « **Utilisable** » signifie ici : mode dégradé accepté, mais **sans perte de fonctionnalité critique** ni de contenu.
- **Application native** : utilisable sur des équipements mis sur le marché il y a **7 ans ou plus**, dans la dernière version d'OS proposée par cet équipement.
- **Service sur navigateur web** : utilisable sur un microprocesseur mis sur le marché il y a **10 ans ou plus**.
- **Autres services numériques** (objets connectés…) : utilisation garantie sur des équipements mis sur le marché il y a **7 ans ou plus**.
- Une durée de compatibilité **plus longue est recommandée** — préciser alors l'objectif visé dans la déclaration d'écoconception.
- Ce critère n'exclut pas l'usage de fonctionnalités récentes réduisant l'impact à l'usage, tant que le service reste disponible sur les anciennes versions (principe d'**amélioration progressive**).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Selon la nature du service :

- **Application native** : tester les fonctionnalités critiques sur un équipement (smartphone, tablette, TV connectée…) mis sur le marché il y a 7 ans ou plus, dans la dernière version d'OS proposée par cet équipement.
- **Navigateur web** : tester les fonctionnalités critiques sur un PC portable (ou tout autre terminal cohérent avec les cibles utilisatrices définies au [critère 1.2](../../strategie/1-2_cibles-utilisatrices/)) équipé d'un microprocesseur mis sur le marché il y a 10 ans ou plus.
- **Autres services** : tester sur un terminal mis sur le marché il y a 7 ans ou plus.

Les **caractéristiques matérielles et logicielles** de l'équipement ancien testé doivent être indiquées dans la **déclaration d'écoconception**. Tenir compte du moment où l'évaluation est réalisée, et non de la date de mise en ligne du service. Le critère est validé si le service est utilisable dans ces conditions.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="3">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Responsable IT`, `Développeur`

Le critère 2.2 rejoint directement la [recommandation n°4 de la famille Frontend](https://gr491.isit-europe.org/?famille=frontend&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR), « Réduire les effets d'obsolescence », déjà citée au [critère 1.9](../../strategie/1-9_technologies-standard/) : la plage de rétro-compatibilité visée est-elle définie ? Une version plus légère du service est-elle disponible pour les équipements anciens ou les connexions limitées ? Les équipements plus anciens resteront-ils compatibles, et dans quelles limites ?

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Le chapitre [« Tester, évaluer et maintenir »](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/8-tester-evaluer-et-maintenir) du guide des Designers Éthiques cite explicitement ce critère : tester le service sur d'anciens terminaux permet de valider le critère 2.2, tester sur d'anciennes versions de navigateurs et d'OS valide le [critère 2.4](../2-4_anciennes-versions-os/).

Le guide rappelle le coût très concret de l'inaction : en 2021, **37 % des Français** ont changé de smartphone parce que l'ancien ne fonctionnait plus correctement ou que son système d'exploitation n'était plus à jour — une obsolescence largement induite par le logiciel plutôt que par une panne matérielle réelle.

{{% /tab %}}

{{% tab tabName="Outils de test" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable IT`

Pour tester réellement sur un équipement ancien plutôt que de se fier à une émulation :

- Le réseau [Ordi3.0](http://www.ordi3-0.fr/) (200 structures labellisées de réemploi informatique) est une source concrète pour se procurer un poste ancien à moindre coût, dans l'esprit de la fiche [Fin de vie](../../../outils/par-phase-projet/fin-de-vie/).
- [BrowserStack](https://www.browserstack.com/) (payant) donne un accès distant à un catalogue de terminaux et versions d'OS réels, utile lorsqu'aucun appareil ancien n'est disponible en interne — à défaut d'émulateur, qui ne reproduit pas fidèlement les limites réelles d'un microprocesseur ancien.
- L'onglet **Network des DevTools Firefox** (gratuit, intégré au navigateur) permet de simuler une connexion dégradée en complément des tests sur matériel ancien : ouvrir les outils de développement (`F12`), aller dans l'onglet **Réseau**, puis choisir un profil dans le menu déroulant de débit (par défaut sur « Sans limitation ») — par exemple **GPRS** ou **Bas débit** pour reproduire les conditions d'une connexion mobile dégradée ou d'une zone mal couverte. Le menu permet aussi de créer un **profil personnalisé** (débit montant/descendant et latence définis manuellement) pour coller au plus près d'un contexte réseau réel.

**Point de méthode à ne pas négliger** ([RWEB 0058](https://rweb.greenit.fr/fr/fiches/RWEB_0058-assurer-la-compatibilite-avec-les-plus-anciens-appareils-et-logiciels-du-parc) : les statistiques de trafic ne suffisent pas à justifier l'abandon d'un ancien appareil ou navigateur, à cause du **biais du survivant** — les utilisateurs qui n'arrivent déjà plus à accéder au service à cause de leur configuration n'apparaissent, par définition, pas dans ces statistiques. Une recherche terrain reste nécessaire pour connaître les équipements réellement utilisés par les cibles du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, déclaration du 30 janvier 2025) documente précisément le test attendu par ce critère : « Le service numérique est un produit web. Il a été testé avec succès sur un **ordinateur portable de 10 ans** sur un système **Linux Debian**. Aucune caractéristique ne montre de risques de non-utilisabilité sur un ancien terminal, quel que soit son système d'exploitation. » — un test qui correspond exactement au seuil de 10 ans fixé par le critère pour les services fonctionnant sur navigateur web, et qui illustre au passage qu'un OS libre (Debian) permet de faire tourner un service moderne sur un microprocesseur ancien là où un OS propriétaire récent aurait pu l'en empêcher (voir le [critère 1.9](../../strategie/1-9_technologies-standard/)).

La [déclaration d'écoconception de « Les entreprises s'engagent »](https://lesentreprises-sengagent.gouv.fr/eco-conception) (dernière mise à jour le 25 novembre 2022) formule cet objectif dès la conception plutôt qu'a posteriori : « l'usage mobile a été priorisé afin d'assurer un accès, même bas débit, avec une rétrocompatibilité de cinq ans pour éviter de contribuer au renouvellement des équipements numériques. » Cette déclaration s'appuie sur la version 1 du RGESN (79 critères) et non sur la v2 utilisée dans ce guide, mais l'intention rejoint directement l'objectif du critère : réduire la contribution du service au renouvellement prématuré des terminaux.

La [déclaration d'écoconception d'Alt Impact](https://altimpact.fr/ecoconception-du-site/) (site porté par l'ADEME, audit Conserto, RGESN v1) documente de très loin la matrice de test la plus détaillée croisée dans ce guide : compatibilité visée avec « tout équipement mobile datant de 2014 (année N-10) ou plus », vérifiée avec des configurations réelles via BrowserStack — Windows 7 + Firefox 115/Chrome 109 (PC estimés compatibles 10 ans et plus), Galaxy Tab S7 (4 ans), Galaxy A11 (4 ans), iPhone X1 + Safari (5 ans), Windows 10 + IE11, et même **Windows XP + Chrome 49 ou Opera 36** (compatibilité théorique PC 15 ans et plus). Au-delà du test sur navigateur, l'audit va jusqu'à émuler un terminal réellement faible en puissance avec un **Raspberry Pi 3 sous RPiOS et Chromium 90** (écran 1024×768) : le site reste utilisable, y compris son calculateur d'empreinte CO2, avec seulement un ralentissement au chargement.

[Les e-novateurs](https://les-enovateurs.com/eco-conception) (média associatif sur le numérique responsable) documentent des tests tout aussi concrets, avec vidéos de test à l'appui : un **Samsung J3 de 2017 sous Android 7** et un **Samsung Galaxy S5 sous Android 6.0.1**, ainsi que Windows XP, 7 et 10 — le test Windows XP étant réalisé via un émulateur UTM sur Mac M1, configuré volontairement avec seulement **512 Mo de RAM et un CPU à 1 GHz**. Fait rare et précieux : la déclaration ne conclut pas à une réussite totale mais documente honnêtement la dégradation constatée — « le service est opérationnel sur d'anciens terminaux, mais le confort d'utilisation est dégradé : les emojis ne sont pas interprétés et l'accessibilité est dégradée car le texte ne s'adapte pas parfaitement sur d'anciens navigateurs. »

{{% /tab %}}

{{< /tabs >}}
