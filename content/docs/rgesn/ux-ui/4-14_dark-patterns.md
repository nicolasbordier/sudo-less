---
weight: 1400
title: "4.14 - Absence de procédés manipulatoires (dark patterns)"
description: "Critère 4.14 du RGESN : pourquoi les dark patterns ont un coût environnemental, comment les repérer (parcours labyrinthe, cases pré-cochées, fausse urgence) et les corriger, en lien avec l'article 25 du DSA."
icon: "psychology_alt"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique évite-t-il le recours à des procédés manipulatoires dans son interface utilisateur ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Expérience et Interface utilisateur (UX / UI)` |
| **Critère**  | `4.14` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'IHM` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` `Responsable Marketing` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.14/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Prévenir l'utilisation de dark patterns ou procédés manipulatoires dans l'interface utilisateur afin d'assurer le contrôle des utilisateurs de leurs usages numériques. Les dark patterns sont des éléments de conception volontairement mis en place pour tromper ou manipuler les utilisateurs et pour en influencer le comportement. Depuis l'entrée en vigueur du paquet législatif sur les services numériques (le DSA ou « Digital Services Act », [règlement 2022/2065](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32022R2065)) en 2022, la conception ou l'exploitation d'interfaces en ligne trompeuses ou destinées à manipuler le destinataire du service par les fournisseurs de plateformes en ligne est proscrite. Dans la continuité de ces obligations légales, l'objectif de ce critère est d'éviter le recours à des éléments manipulatoires dans l'interface utilisateur susceptibles d'engendrer des surcroîts d'usages en ligne, responsables de coûts environnementaux additionnels.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Il s'agit de prévenir la mise en place de dark patterns dans la conception de l'interface utilisateur. Si le service est en phase d'usage, examiner son interface utilisateur pour identifier et éliminer l'utilisation de dark patterns. Quelques exemples de pratiques de dark patterns à éviter :

- Mise en place de parcours de navigation « labyrinthe » qui complexifie la possibilité des utilisateurs de faire certaines actions (désabonnement, désinscription) ou rend difficile l'accès à des informations sur les mentions légales, l'empreinte environnementale du service par exemple;
- Affichage de publicité déguisée ou d'exit pop-up publicitaire sans sélection ou choix de l'utilisateur;
- Définition d'une option présélectionnée pour l'utilisateur, souvent sous la forme d'une case pré-cochée, dans le but de l'inciter à accepter quelque chose qu'il n'aurait peut-être pas choisi délibérément;
- Affichage d'un compte à rebours pour une offre spéciale, mais chaque fois que le compte à rebours atteint zéro, il recommence, créant une fausse urgence.

Le guide de l'association [Designers Éthiques](https://designersethiques.org/fr/thematiques/design-persuasif/concevoir-sans-dark-patterns/1-introduction) peut également aider à repérer et corriger les éventuels éléments trompeurs de l'interface utilisateur.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Ne pas inclure de dark patterns dans le design du service et effectuer une évaluation régulière de l'interface utilisateur pour détecter et prévenir leur présence. Cette évaluation doit prendre en compte les travaux de la Commission européenne (y compris les lignes directrices publiées en application de l'article 25 du règlement 2022/2065).

Le critère est validé si l'interface utilisateur ne contient pas de dark patterns.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le critère 4.14 a une correspondance directe dans la [recommandation n°10 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=10) du [GR491](https://gr491.isit-europe.org/) (INR), « Valeur : concevez un Service Numérique éthique, en ligne avec vos valeurs ». Son critère [« Le service évite-t-il les Dark Patterns ? »](https://gr491.isit-europe.org/crit.php?id=10-uxui-certains-services-sont-penses-pour-creer-une-6f419d) est classé **incontournable**, en priorité **High**. Ses tests nomment des pratiques précises, dont plusieurs absentes des exemples du RGESN :

- « La Force Continuity (perpétuation d'abonnement) peut-elle être bannie dans les services proposés ? »
- « Le principe de "Friend spam" est-il exclu ? »
- « L'autoplay en continu des vidéos est-il désactivé par défaut (Binge watching) ? »

Les précisions du critère font le lien avec l'écoconception : « Certains services sont pensés pour créer une certaine forme de dépendance à celui-ci. L'utilisateur ne doit pas être soumis et exposé à certaines mécaniques de sur-consommation numérique. »

Dans la même recommandation, le critère [« Dans quelle mesure l'attention de l'utilisateur est-elle contrôlée par le service ? »](https://gr491.isit-europe.org/crit.php?id=10-uxui-lattention-de-lutilisateur-est-une-ressource-qui-d8f819) propose une méthode préventive : « Lors des séances d'idéation, le pire scénario pour les utilisateurs a-t-il été envisagé ? ». Il s'agit de se demander, dès la conception, comment une fonctionnalité pourrait être détournée contre l'utilisateur.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Responsable Marketing`

Le RGESN renvoie lui-même au guide des Designers Éthiques [**« Concevoir sans dark patterns »**](https://designersethiques.org/fr/thematiques/design-persuasif/concevoir-sans-dark-patterns/1-introduction), publié sous licence CC-BY. Le guide se veut « un recueil de bonnes pratiques » qui propose des « versions alternatives plus respectueuses de l'utilisateur ». Il définit un dark pattern comme un « élément de conception dont le but est de pousser l'utilisateur à faire des choses qu'il n'aurait pas forcément faites initialement ».

Son introduction consacre une partie à l'**enjeu écologique** : « La réduction de l'impact numérique passera inévitablement par une forme de sobriété numérique. Où les usages publicitaires et la récolte de données seront nécessairement questionnés. » Il l'illustre par un parcours de réservation de train limité à l'essentiel, où l'utilisateur ne voit « ni publicité pour des hôtels, voitures, ni options supplémentaires pour des assurances non demandées ».

Plusieurs sections recoupent directement les exemples du RGESN :

- [**6.9 Formulaires**](https://designersethiques.org/fr/thematiques/design-persuasif/concevoir-sans-dark-patterns/6-concevoir/6-9-formulaires) : « Il est essentiel d'éviter de présélectionner des options. » Le guide nuance avec un cas particulier, la déclaration d'impôts. Les options y sont présélectionnées pour « compléter les informations connues d'avance », et l'utilisateur peut toutes les modifier. Pré-remplir ce que l'on sait déjà n'est donc pas manipulatoire. Pré-cocher un consentement l'est.
- [**6.10 Abonnement**](https://designersethiques.org/fr/thematiques/design-persuasif/concevoir-sans-dark-patterns/6-concevoir/6-10-abonnement) : « ne pas pousser à l'abonnement ; faciliter la sortie de l'abonnement ; prévenir dans le cas d'un débit à venir ». C'est la réponse au parcours « labyrinthe » de désabonnement cité par le RGESN.

Pour l'évaluation régulière demandée par le moyen de test, le guide propose, dans sa partie [**7. Évaluer et améliorer**](https://designersethiques.org/fr/thematiques/design-persuasif/concevoir-sans-dark-patterns/7-evaluer-et-ameliorer), d'utiliser la [**matrice de captologie**](https://docs.google.com/spreadsheets/d/1dj_KIKzyPlSND1-fSYNb0BgupCmh2XoYTPkFTKPiaq0/edit?gid=1991215211#gid=1991215211) des Designers Éthiques (voir aussi la page [Outils > UX Designer](../../../outils/par-metier/ux-designer/)). Cette grille de questions permet d'obtenir « la note globale du service et les éléments à améliorer ».

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Responsable Marketing`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont une fiche dédiée, [**« Avoid being manipulative or deceptive »**](https://www.w3.org/TR/web-sustainability-guidelines/#avoid-being-manipulative-or-deceptive). Son premier critère de succès, « Deceptive design patterns », demande : « Avoid deceptive design patterns that pressure or mislead users. This includes practices such as bait and switch, hidden fees, or fake scarcity. »

La fiche étend le sujet à trois domaines que le RGESN ne range pas dans ce critère :

- **Advertisements** : « Clearly label advertisements and sponsored content. Deliver advertising in a lightweight and minimally disruptive way ». Cela rejoint l'exemple de la « publicité déguisée » du RGESN, avec une exigence de légèreté en plus.
- **Analytics and tracking** : « Remove unnecessary analytics and tracking, and respect user consent over tracking analytics. »
- **Search Engine Optimization** : ne pas créer de contenu de faible qualité ou dupliqué « only to influence search rankings ».

Le W3C classe donc dans la même famille la manipulation de l'utilisateur et la manipulation des moteurs de recherche. Dans les deux cas, le service produit ou fait consommer du contenu dont personne n'a réellement besoin.

{{% /tab %}}

{{% tab tabName="Cadre réglementaire : DSA" %}}

Profil(s) métier concerné(s) : `Responsable Marketing`, `Concepteur UX / UI`

Le RGESN s'appuie sur l'[article 25 du Digital Services Act](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32022R2065) (règlement 2022/2065), « Conception et organisation des interfaces en ligne », dont le premier paragraphe dispose : « Les fournisseurs de plateformes en ligne ne conçoivent, n'organisent ni n'exploitent leurs interfaces en ligne de façon à tromper ou à manipuler les destinataires de leur service ou de toute autre façon propre à altérer ou à entraver substantiellement la capacité des destinataires de leur service à prendre des décisions libres et éclairées. »

Son troisième paragraphe prévoit que la Commission « peut publier des lignes directrices » sur trois pratiques en particulier :

- « accorder davantage d'importance à certains choix au moment de demander au destinataire du service de prendre une décision » ;
- « demander de façon répétée au destinataire du service de faire un choix lorsque ce choix a déjà été fait, notamment en faisant apparaître une fenêtre contextuelle qui perturbe l'expérience de l'utilisateur » ;
- « rendre la procédure de désinscription d'un service plus compliquée que l'inscription à celui-ci ».

Deux limites de l'article 25 expliquent l'intérêt du critère RGESN :

- **Son champ** : il ne vise que les « fournisseurs de plateformes en ligne ». Un site institutionnel, un service public en ligne ou une application métier n'y sont pas soumis. Le RGESN étend la même exigence à tout service numérique.
- **Ses exclusions** : son deuxième paragraphe exclut les pratiques déjà couvertes par la directive sur les pratiques commerciales déloyales (2005/29/CE) et par le RGPD. Ces textes s'appliquent toujours, mais par une autre voie.

Le troisième exemple de l'article 25 donne une règle simple à vérifier dans n'importe quel service : **se désinscrire ne doit pas demander plus d'étapes que s'inscrire**.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**1. Une grille d'audit** pour l'« évaluation régulière » demandée par le moyen de test, à partir des quatre exemples du RGESN :

| Pratique citée par le RGESN | Comment la repérer | Correction |
|---|---|---|
| Parcours « labyrinthe » (désabonnement, mentions légales, empreinte environnementale) | Compter les écrans et les clics pour se désinscrire, et les comparer à ceux de l'inscription | Un lien direct dans l'espace personnel et dans chaque e-mail ; pas plus d'étapes que l'inscription |
| Publicité déguisée, exit pop-up | Parcourir le service et faire mine de quitter la page ; vérifier que chaque contenu sponsorisé est signalé | Supprimer les exit pop-up ; étiqueter clairement la publicité |
| Case pré-cochée | Chercher les cases cochées par défaut dans le code des formulaires (voir ci-dessous) | Rien de pré-coché pour un consentement ou une option payante |
| Fausse urgence (compte à rebours qui recommence) | Recharger la page ou l'ouvrir en navigation privée : le compte à rebours repart-il de zéro ? | Une échéance réelle, calculée côté serveur, ou pas de compte à rebours |

**2. Repérer les cases pré-cochées dans le code**, par exemple dans les gabarits HTML :

```bash
grep -rn 'type="checkbox"' templates/ | grep 'checked'
```

Chaque résultat est à examiner. Une case pré-cochée qui reflète une préférence déjà enregistrée par l'utilisateur est légitime. Une case pré-cochée pour un consentement que l'utilisateur n'a jamais donné ne l'est pas :

```html
<!-- À éviter : consentement présélectionné -->
<label>
  <input type="checkbox" name="offres-partenaires" checked>
  Recevoir les offres de nos partenaires
</label>

<!-- À privilégier : l'utilisateur fait lui-même le choix, en connaissant la fréquence -->
<label>
  <input type="checkbox" name="offres-partenaires">
  Recevoir les offres de nos partenaires (un e-mail par mois au maximum)
</label>
```

**3. Présenter les choix à égalité**, pour respecter le premier exemple de l'article 25 du DSA (« accorder davantage d'importance à certains choix ») :

```html
<p>Souhaitez-vous recevoir notre lettre d'information mensuelle ?</p>
<button type="button" class="bouton-secondaire">Non merci</button>
<button type="button" class="bouton-secondaire">Oui, m'abonner</button>
```

Les deux boutons ont le même style et des libellés neutres. On évite un bouton « Oui » mis en avant face à un petit lien gris, et les libellés culpabilisants du type « Non, je préfère rater les bonnes affaires ».

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le critère 4.14 est le plus général des critères du RGESN sur la captation de l'attention. Plusieurs critères déjà publiés sur ce site en traitent des formes particulières :

- le [critère 4.1](../4-1_lecture-automatique/) (lecture automatique), que le GR491 range explicitement parmi les dark patterns (« Binge watching ») ;
- le [critère 4.2](../4-2_defilement-infini/) (défilement infini) ;
- le [critère 4.3](../4-3_parcours-navigation/) (parcours de navigation). Un parcours optimisé y est l'objectif, quand le parcours « labyrinthe » du 4.14 en est le détournement délibéré ;
- le [critère 4.4](../4-4_activation-service-tiers/) (activation des services tiers), dont le principe de consentement préalable est l'inverse exact de la case pré-cochée ;
- le [critère 4.13](../4-13_notifications/) (notifications) : une notification conçue pour faire revenir l'utilisateur, par une fausse urgence par exemple, relève des deux critères à la fois.

Un service conforme à ces critères particuliers peut encore contenir des dark patterns, comme une case pré-cochée ou un faux compte à rebours. C'est ce qui justifie un critère général.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque ce critère **« Validé »** : « Aucun procédé manipulatoire de type dark-pattern détecté. » La justification donne le résultat, mais ni la méthode ni la grille utilisées. Le moyen de test demande pourtant une évaluation « régulière » qui tienne compte des travaux de la Commission européenne. Préciser la grille d'audit (celle de l'onglet « Mise en œuvre technique », ou la matrice de captologie des Designers Éthiques) rendrait l'évaluation reproductible à la prochaine révision.

[DiaLog](https://dialog.beta.gouv.fr/files/2025-03-06%20-%20D%C3%A9claration%20%C3%A9coconception%20DiaLog%20-%20D%C3%A9tail.pdf) (beta.gouv.fr) marque aussi ce critère **« Validé »** dans le tableau détaillé de son audit (évaluation du 17 février 2025), sans le commenter dans sa déclaration publique.

À plus grande échelle, la Commission européenne et les autorités nationales de protection des consommateurs ont publié le 30 janvier 2023 les résultats d'une [opération de contrôle de 399 boutiques en ligne](https://ec.europa.eu/commission/presscorner/detail/fr/ip_23_418) : **148** contenaient au moins une « interface truquée ». Le contrôle visait trois pratiques : **42** sites utilisaient de faux comptes à rebours, **54** orientaient les consommateurs vers certains choix par la présentation visuelle ou la formulation, et **70** dissimulaient des informations importantes ou les rendaient moins visibles. Les faux comptes à rebours sont précisément le quatrième exemple du RGESN : la pratique est assez répandue pour justifier un contrôle explicite, même dans un service qui n'a rien d'une boutique en ligne.

{{% /tab %}}

{{< /tabs >}}
