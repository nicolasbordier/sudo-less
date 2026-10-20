---
weight: 1000
title: "4.10 - Information sur le format de saisie attendu"
description: "Critère 4.10 du RGESN : pourquoi et comment indiquer le format de saisie attendu et valider les formulaires côté client, pour éviter les soumissions en erreur et les allers-retours inutiles avec le serveur."
icon: "fact_check"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique informe-t-il l'utilisateur du format de saisie attendu, en évitant les requêtes serveur inutiles pour la soumission d'un formulaire ?

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
| **Critère**  | `4.10` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne repose pas sur un formulaire` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.10/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Limiter les échanges client/serveur en vérifiant la saisie du côté du terminal utilisateur, réduisant ainsi les erreurs de saisie et les soumissions de formulaires incorrects qui nécessiteraient un retour vers le serveur pour une correction.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Les formats de saisie attendus devraient être définis et indiqués de façon claire et explicite lors de la saisie de l'utilisateur avant la soumission du formulaire (par exemple sous la forme de textes d'aide, d'exemples ou de formats par défaut contraints). En cas d'erreur, le champ concerné et le correctif à effectuer devraient être indiqués de façon précise.

Il convient de valider les saisies et les formats de données obligatoires à la soumission d'un formulaire sans requête serveur lorsque c'est possible. Cela peut être réalisé en utilisant des fonctionnalités de validation intégrées aux langages de programmation web, tels que JavaScript. Attention : prévalider les données côté frontend n'exempte pas la validation côté backend. Une validation supplémentaire côté serveur reste donc nécessaire pour assurer l'intégrité des données.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

La mise en œuvre est à contrôler en testant le parcours d'utilisation du service ou en effectuant à la conception une revue de son code source afin d'examiner que les indications de format attendu sont correctement spécifiées du côté du terminal de l'utilisateur. Tester le service en remplissant le formulaire avec des données incorrectes ou manquantes et en vérifiant que des messages d'erreur appropriés sont affichés pour indiquer les erreurs de saisie.

Le critère est validé si l'utilisateur est informé des formats de saisie attendus avant la soumission du formulaire. Les saisies et les formats de données obligatoires du service devront également être validés d'abord côté client avant la soumission du formulaire.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer UX/UI`

Le critère 4.10 a une correspondance directe dans la [recommandation n°4 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR), « Faciliter la perception des contenus par l'utilisateur », via son [critère consacré aux formulaires](https://gr491.isit-europe.org/crit.php?id=4-contenus-les-saisies-de-donnees-dans-les-formulaires-549d87) : « Est-ce que la validité des données est contrôlée avant la soumission du formulaire ? »

Ses deux tests recoupent presque exactement les deux volets du critère RGESN — informer, puis contrôler :

- « Avez-vous une plage de valeur, un format associé à chaque zone de saisie ? »
- « Les données attendues dans chaque champ sont-elles clairement exprimées et contrôlées au plus tôt après leur saisie par l'utilisateur ? »

Les précisions du critère en résument le mécanisme environnemental : « Si les données ne sont contrôlées qu'après soumission du formulaire, le nombre d'échanges va augmenter. Le contrôle du format des données attendues avant l'envoi au serveur permet de réduire les transferts de données et les traitements inutiles. » Le GR491 indique d'ailleurs comme moyen de vérification l'onglet **Network** des outils de développement de Chrome — celui-là même utilisé dans l'onglet « Mise en œuvre technique » ci-contre.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 4.10 dans sa section [**7.7 Formulaires**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-7-formulaires) : « Informer l'utilisateur du format de saisie attendu avant la soumission du formulaire permet de valider le critère 4.10 ». Il en explique le mécanisme du point de vue de l'utilisateur : « Si l'utilisateur ne sait pas à l'avance le format de saisie attendu, il risque de répondre de façon incorrecte et de soumettre le formulaire à plusieurs reprises, générant ainsi des requêtes superflues. » Et recommande de :

- « indiquer clairement les champs obligatoires (et en haut de page pour les lecteurs d'écran) » ;
- « donner un exemple de saisie sur ou sous le champ (mettre un exemple dans le champ n'est pas accessible car il disparaît à la saisie) » ;
- « contraindre, lorsque c'est possible et pertinent, le format de saisie (que des chiffres, format de la date, etc.) » ;
- « afficher des messages d'erreur explicites en cas d'erreur de saisie, et à l'emplacement du champ concerné » ;
- « valider les saisies sans requête serveur côté frontend (nécessite l'aide de développeurs) ».

La deuxième recommandation apporte une précision que le RGESN ne donne pas : l'exemple de format ne doit pas être placé dans l'attribut `placeholder` du champ, qui s'efface dès que l'utilisateur commence à taper — au moment précis où il en a besoin. La même section rappelle aussi qu'avant d'optimiser un formulaire, il faut se demander s'il est utile (voir les retours d'expériences ci-dessous).

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), déjà citée au [critère 4.9](../4-9_requetes-saisie-utilisateur/), reprend le critère dans sa rubrique **Formulaires** de la phase de prototypage : « Informer l'utilisateur du format de saisie attendu avant sa validation et indiquer les erreurs de saisie avant soumission du formulaire. »

{{% /tab %}}

{{% tab tabName="Accessibilité : au-delà de l'écoconception" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le premier volet du critère 4.10 — informer l'utilisateur du format attendu — est aussi une **exigence d'accessibilité** à part entière. Le [critère 11.10 du RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) (« Dans chaque formulaire, le contrôle de saisie est-il utilisé de manière pertinente ? ») demande notamment, dans son test 11.10.5, qu'une indication du type de données ou du format obligatoire soit « visible dans l'étiquette ou le passage de texte associé au champ préalablement à la validation du formulaire ». Il s'appuie sur les critères WCAG [3.3.1 « Identification des erreurs »](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) et [3.3.2 « Étiquettes ou instructions »](https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions.html). Un formulaire conforme au RGAA sur ce point remplit donc déjà la moitié du critère RGESN.

Le second volet — valider côté client — appelle en revanche une nuance. Le [GOV.UK Design System](https://design-system.service.gov.uk/patterns/validation/), système de design de l'administration britannique, recommande de désactiver la validation HTML5 native des navigateurs (« To turn off HTML5 validation, add 'novalidate' to your form tags »), parce que l'apparence et le contenu de ses bulles d'erreur ne peuvent pas être maîtrisés, et de n'ajouter une validation côté client que si un besoin utilisateur le justifie, en prévenant que « it's hard to tell the user about errors in a way that works reliably across different browsers and assistive technologies ». Il déconseille aussi de valider un champ dès que l'utilisateur le quitte, pour attendre qu'il clique sur « continuer » ou « envoyer ».

Les deux approches ne sont pas incompatibles : il est possible de valider **côté client, au moment de la soumission**, en affichant ses propres messages d'erreur, persistants et associés au champ — ce qui évite à la fois la requête serveur visée par le RGESN et les limites des bulles natives relevées par GOV.UK. C'est l'approche de l'exemple de l'onglet « Mise en œuvre technique ».

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Pour synthétiser les recommandations ci-contre en un exemple concret, voici un formulaire qui informe du format attendu et valide les saisies avant tout envoi au serveur :

```html
<form id="inscription" action="/inscription" method="post" novalidate>
  <p>Tous les champs sont obligatoires.</p>

  <label for="cp">Code postal</label>
  <p id="cp-aide">Format attendu : 5 chiffres, par exemple 34000</p>
  <input id="cp" name="cp" type="text" inputmode="numeric"
         autocomplete="postal-code" required pattern="[0-9]{5}"
         aria-describedby="cp-aide cp-erreur"
         data-erreur="Le code postal doit contenir 5 chiffres, par exemple 34000.">
  <p id="cp-erreur"></p>

  <label for="courriel">Adresse électronique</label>
  <p id="courriel-aide">Format attendu : nom@domaine.fr</p>
  <input id="courriel" name="courriel" type="email"
         autocomplete="email" required
         aria-describedby="courriel-aide courriel-erreur"
         data-erreur="L'adresse électronique doit être au format nom@domaine.fr.">
  <p id="courriel-erreur"></p>

  <button type="submit">Envoyer</button>
</form>
```

```js
const formulaire = document.querySelector('#inscription');

formulaire.addEventListener('submit', (evenement) => {
  let premierChampInvalide = null;

  for (const champ of formulaire.querySelectorAll('input')) {
    const valide = champ.checkValidity();
    champ.setAttribute('aria-invalid', String(!valide));
    document.getElementById(`${champ.id}-erreur`).textContent =
      valide ? '' : champ.dataset.erreur;
    if (!valide && !premierChampInvalide) premierChampInvalide = champ;
  }

  if (premierChampInvalide) {
    evenement.preventDefault(); // aucune requête serveur
    premierChampInvalide.focus();
  }
});
```

- **Texte d'aide sous le label** (`cp-aide`), et non dans un `placeholder` : le format attendu reste visible pendant toute la saisie (Designers Éthiques, test 11.10.5 du RGAA). L'attribut `aria-describedby` le fait lire par les lecteurs d'écran à l'arrivée sur le champ.
- **`required`, `pattern`, `type="email"`** : les règles de validation sont déclarées dans le HTML lui-même et vérifiées par le navigateur via `checkValidity()` — les « fonctionnalités de validation intégrées » citées par le RGESN, sans bibliothèque à télécharger.
- **`inputmode="numeric"`** et **`autocomplete`** : clavier numérique sur mobile, et remplissage automatique par le navigateur à partir des données déjà connues de l'utilisateur — deux façons de réduire les erreurs de saisie avant même qu'elles se produisent (les « formats par défaut contraints » de la « Mise en œuvre » du RGESN).
- **`novalidate` + gestionnaire `submit`** : les bulles d'erreur natives sont remplacées par des messages persistants, placés sous le champ concerné et indiquant le correctif à effectuer — ce que demande le RGESN (« le champ concerné et le correctif à effectuer ») et ce que recommandent GOV.UK et le RGAA. La validation a lieu à la soumission, pas à chaque frappe.
- **`evenement.preventDefault()`** : tant qu'un champ est invalide, le formulaire n'est pas envoyé — c'est cette ligne qui supprime l'aller-retour serveur visé par le critère.

Comme le rappelle le RGESN, cette validation ne remplace pas celle du serveur, qui reste indispensable : elle peut être contournée, et si le JavaScript ne se charge pas, le formulaire est envoyé tel quel et c'est le serveur qui renvoie les erreurs. Les deux validations doivent appliquer les mêmes règles — un `pattern` côté client plus permissif que le contrôle côté serveur recréerait exactement les allers-retours que le critère cherche à éviter.

Pour le **contrôle**, le moyen de test du RGESN se pratique directement dans les outils de développement du navigateur : onglet **Réseau** (Network) ouvert, soumettre le formulaire avec des champs vides ou mal remplis — **aucune requête ne doit apparaître**, et chaque champ en erreur doit afficher son message.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Ce critère forme une paire avec le [critère 4.9](../4-9_requetes-saisie-utilisateur/) (requêtes serveur lors de la saisie utilisateur), déjà publié sur ce site : le 4.9 porte sur les requêtes déclenchées **pendant** la saisie (autocomplétion, suggestions), le 4.10 sur celles déclenchées **à la soumission** du formulaire. Un formulaire peut être conforme à l'un sans l'être à l'autre — par exemple, sans aucune autocomplétion mais validé uniquement côté serveur.

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche étiquetée « RGESN 4.10 », mais la fiche [**RWEB 0014 — « Préférer la saisie assistée à l'autocomplétion »**](https://rweb.greenit.fr/fr/fiches/RWEB_0014-preferer-la-saisie-assistee-a-l-autocompletion), citée au 4.9, fait le lien entre les deux critères : la « saisie assistée » qu'elle recommande — « guider l'utilisateur par un ensemble d'informations et d'indices gérés localement » — est précisément ce que demande le premier volet du 4.10.

Le [critère 4.11](../4-11_poids-formats-fichiers/) (informer l'utilisateur des poids et formats de fichier attendus), qui le suit directement dans le RGESN, applique la même logique aux champs de transfert de fichier, où une erreur de format coûte bien plus cher : c'est alors le fichier entier qui a été envoyé pour rien.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »**, avec une justification qui applique exactement la recommandation des Designers Éthiques : « Les champs sont accompagnés d'une description avec un exemple de format attendu, en dessous du label quand cela est nécessaire. » La précision « quand cela est nécessaire » est intéressante : tous les champs n'ont pas besoin d'un texte d'aide (un nom, une ville), et en ajouter partout alourdirait le formulaire sans bénéfice.

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque également ce critère **« Validé »**, avec une justification qui couvre les deux volets du critère : « Les formulaires sont basés sur des listes de choix, cases à cocher, dates et textes libres. Les formats de date sont précisés ainsi que les longueur de texte. Une validation côté client est effectuée avant envoi de requête. » La première phrase montre un levier que le RGESN range parmi les « formats par défaut contraints » : chaque liste de choix ou case à cocher remplace un champ libre, et supprime à la source les erreurs de format possibles.

Enfin, le [guide des Designers Éthiques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-7-formulaires) rapporte leur propre cas, qui illustre l'option la plus radicale : sur leur site, « le formulaire de contact Wordpress a été remplacé par une simple adresse e-mail ». Effet de bord notable : le nombre de spams reçus « est passé d'une dizaine par jour à quelques-uns par semaine », les robots visant probablement ce plugin de formulaire très répandu. Sans formulaire, le critère devient non applicable — et il n'y a plus aucune soumission en erreur à éviter.

{{% /tab %}}

{{< /tabs >}}
