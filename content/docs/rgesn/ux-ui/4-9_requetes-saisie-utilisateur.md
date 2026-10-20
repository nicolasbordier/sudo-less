---
weight: 900
title: "4.9 - Limitation des requêtes serveur lors de la saisie utilisateur"
description: "Critère 4.9 du RGESN : pourquoi et comment limiter les requêtes envoyées au serveur pendant la saisie, en encadrant l'autocomplétion (3 caractères, 500 ms, activation au choix de l'utilisateur)."
icon: "keyboard"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique limite-t-il les requêtes serveur lors de la saisie utilisateur ?

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
| **Critère**  | `4.9` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'IHM` |
| **Métiers concernés** | `Développeur` `Architecte Logiciel` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.9/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Une partie de l'empreinte énergétique des services numériques est liée à la volumétrie des données échangées sur les réseaux. L'objectif est donc de réduire la volumétrie de données pour le service en évitant de réaliser des requêtes client/serveur inutiles (par exemple dans un contexte de formulaire, de suggestion de résultats, etc.). Dans la plupart des cas, cette réduction pourra se faire sans dégradation de l'expérience utilisateur.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Pour réduire les échanges entre serveurs et utilisateurs, il est important que les services numériques réduisent les appels à des API, scripts, librairies ou polices de caractères tiers.

Il est conseillé de limiter la complétion automatique en ligne. Ces mécanismes d'autocomplétion ou de suggestion qui visent à compléter automatiquement ou suggérer des options nécessitent beaucoup de requêtes vers le serveur. Si un tel mécanisme est mis en place car justifié du point de vue utilisateur, il est préconisé d'attendre par exemple d'avoir trois caractères et 500 ms après chaque saisie avant de lancer une requête réseau. Alternativement, il est possible de laisser le choix à l'utilisateur d'activer l'autocomplétion s'il le souhaite (opt in) via un élément de configuration.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Pour valider le critère, s'assurer que le service ne propose pas d'autocomplétion ; dans le cas contraire, vérifier que l'autocomplétion est justifiée du point de vue de l'utilisateur et contrôler périodiquement que l'autocomplétion attend un délai d'au moins 500 ms avant de s'activer et au moins 3 caractères saisis. L'interface utilisateur permet de désactiver l'autocomplétion.

Le nombre de requêtes HTTP entre client et serveur est à contrôler et à suivre dans le temps.

De même, examiner périodiquement l'absence de requêtes identiques et redondantes.

Vérifier que les requêtes externes effectuées en appelant le site (en vidant le cache ou en utilisant une extension appropriée) sont effectivement celles nécessaires à l'exécution du service.

{{% /tab %}}
{{< /tabs >}}

---

###
### Comment appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer UX/UI`

Le critère 4.9 rejoint la [recommandation n°7 de la famille UX/UI](https://gr491.isit-europe.org/?famille=uxui&num_reco=7) du [GR491](https://gr491.isit-europe.org/) (INR), « "Barebone Iteration" : Itérer votre solution jusqu'au minimalisme "acceptable" par vos utilisateurs », via son [critère consacré aux moteurs de recherche internes](https://gr491.isit-europe.org/crit.php?id=7-uxui-lutilisation-des-moteurs-de-recherches-internes-au-cfd836) : « Est-ce que les recherches les plus fréquentes ont été étudiées et adressées pour qu'elles soient ou mises en cache ou affichées à l'utilisateur sans envoi de requête ou clics inutiles ? »

Le GR491 aborde le sujet sous un angle complémentaire au RGESN : plutôt que d'encadrer *le moment* où la requête part (seuil de caractères, délai), il propose d'**éviter la requête elle-même** en analysant au préalable les recherches les plus fréquentes, pour les servir depuis un cache. Ses tests demandent notamment si « une liste des requêtes les plus formulées est-elle constituée ? » et s'il existe « des solutions d'accompagnement de l'utilisateur dans la qualification de sa recherche afin de limiter le nombre de requêtes envoyées au serveur ». Les précisions du critère résument l'enjeu : un moteur de recherche interne est un atout de sobriété (il raccourcit la navigation), à condition de « réduire les échanges entre votre service et les serveurs distants pour ne pas annuler le bénéfice acquis ».

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) a une correspondance directe et explicitement étiquetée « RGESN 4.9 » : la fiche [**RWEB 0014 — « Préférer la saisie assistée à l'autocomplétion »**](https://rweb.greenit.fr/fr/fiches/RWEB_0014-preferer-la-saisie-assistee-a-l-autocompletion), notée **3/5** sur l'échelle d'impact environnemental. Elle part du même constat que le RGESN : « À chaque caractère saisi, une requête est envoyée au serveur pour récupérer les résultats appropriés. » Et propose une alternative : la **saisie assistée**, « qui consiste à guider l'utilisateur par un ensemble d'informations et d'indices gérés localement, ce qui réduit les échanges avec le serveur ».

Si l'autocomplétion reste nécessaire, la fiche liste les mêmes leviers que le RGESN (délai de quelques dixièmes de seconde, nombre minimum de caractères), en ajoute un troisième — la **limitation du nombre de résultats affichés** — et propose, pour les listes de petite taille, de supprimer complètement les allers-retours avec l'élément HTML natif `<datalist>` :

```html
<label for="ice-cream-choice">Choose a flavor:</label>
<input list="ice-cream-flavors" id="ice-cream-choice" name="ice-cream-choice" />

<datalist id="ice-cream-flavors">
  <option value="Chocolate"></option>
  <option value="Coconut"></option>
  <option value="Mint"></option>
  <option value="Strawberry"></option>
  <option value="Vanilla"></option>
</datalist>
```

Les suggestions sont livrées une seule fois avec la page, puis filtrées par le navigateur lui-même pendant la saisie — sans aucune requête. Principe de validation retenu par RWEB : le nombre de champs en autocomplétion doit rester inférieur ou égal à **20 %**.

La fiche [**RWEB 0047 — « Limiter le nombre de requêtes HTTP »**](https://rweb.greenit.fr/fr/fiches/RWEB_0047-limiter-le-nombre-de-requetes-http), étiquetée « RGESN 6.1 et 4.9 », couvre l'autre volet du moyen de test (suivre dans le temps le nombre de requêtes HTTP), avec un seuil chiffré que le RGESN ne donne pas : **40 requêtes HTTP maximum** par page.

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

La ressource des Designers Éthiques [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), déjà citée au [critère 4.7](../4-7_choix-sobre-format/) sur ce site, consacre au critère 4.9 trois lignes de la rubrique **Formulaires**, dans la phase de **prototypage** :

- « Limiter les requêtes serveur lors de la saisie utilisateur : éviter l'auto-complétion, les résultats suggérés… »
- « Si sa mise en place est justifiée, attendre d'avoir 3 caractères et 500 ms après chaque saisie avant de lancer une requête réseau. »
- « Permettre d'activer et désactiver l'auto-complétion. »

Le placement de ces recommandations est en lui-même instructif : le RGESN range ce critère dans la phase de conception et cite comme métiers concernés le développeur et l'architecte logiciel, alors que les Designers Éthiques le confient d'abord au **designer**, au moment du prototype. C'est en effet à ce stade que se décide s'il y aura une autocomplétion, et si elle sera activée par défaut ou proposée en option — le délai et le seuil de caractères n'étant ensuite que des paramètres d'implémentation.

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ne mentionnent pas l'autocomplétion en tant que telle, mais la fiche [**« Use sustainable JavaScript and APIs »**](https://www.w3.org/TR/web-sustainability-guidelines/#use-sustainable-javascript-and-apis) en pose le principe général, dans son critère de succès « API requests » :

- « Only call client-side or server-side APIs when needed. »
- « Ensure only data required for the task is included in requests and responses. »

La première phrase correspond au cœur du critère 4.9 (ne pas interroger le serveur à chaque frappe). La seconde ajoute une dimension que le RGESN ne détaille pas : réduire aussi le **contenu** de chaque réponse — pour une autocomplétion, ne renvoyer que les quelques champs affichés dans la liste de suggestions (un libellé, un identifiant) plutôt que l'objet complet de chaque résultat, et seulement les premiers résultats.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`

Pour synthétiser les recommandations ci-contre en un exemple concret, voici une autocomplétion qui respecte point par point le moyen de test du critère :

```html
<label for="recherche">Rechercher une commune</label>
<input id="recherche" type="search">
<label>
  <input id="suggestions-actives" type="checkbox">
  Afficher des suggestions pendant la saisie
</label>
```

```js
const MIN_CARACTERES = 3;
const DELAI_MS = 500;

const champ = document.querySelector('#recherche');
const optIn = document.querySelector('#suggestions-actives');
const cache = new Map();
let minuterie;
let controleur;

champ.addEventListener('input', () => {
  clearTimeout(minuterie);
  const saisie = champ.value.trim().toLowerCase();
  if (!optIn.checked || saisie.length < MIN_CARACTERES) return;

  minuterie = setTimeout(async () => {
    if (cache.has(saisie)) return afficher(cache.get(saisie));

    controleur?.abort();
    controleur = new AbortController();
    try {
      const reponse = await fetch(
        `/api/communes?q=${encodeURIComponent(saisie)}&limit=5`,
        { signal: controleur.signal }
      );
      const resultats = await reponse.json();
      cache.set(saisie, resultats);
      afficher(resultats); // affichage propre à votre interface
    } catch (erreur) {
      if (erreur.name !== 'AbortError') throw erreur;
    }
  }, DELAI_MS);
});
```

- **Case à cocher `#suggestions-actives`** : l'autocomplétion est désactivée par défaut et activée au choix de l'utilisateur — l'« opt in » de la « Mise en œuvre » du RGESN, qui satisfait aussi l'exigence du moyen de test : « L'interface utilisateur permet de désactiver l'autocomplétion. »
- **`MIN_CARACTERES = 3`** : aucune requête tant que la saisie compte moins de trois caractères.
- **`clearTimeout` + `setTimeout(…, DELAI_MS)`** : la technique dite du *debounce*. Chaque frappe annule la minuterie précédente, donc la requête ne part que **500 ms après la dernière frappe** — la traduction littérale du « 500 ms après chaque saisie » du RGESN. Un utilisateur qui tape « montpellier » d'un trait ne déclenche qu'une seule requête, au lieu de neuf avec le seul seuil de trois caractères (une par frappe à partir de la troisième).
- **`cache`** : une saisie déjà interrogée (par exemple après un retour arrière) est servie depuis la mémoire, ce qui répond au moyen de test « examiner périodiquement l'absence de requêtes identiques et redondantes ».
- **`AbortController`** : si une nouvelle requête part alors que la précédente n'a pas encore répondu, le navigateur abandonne la précédente. Cela évite de télécharger et de traiter une réponse devenue inutile — mais le serveur, lui, a déjà pu commencer à la traiter : c'est le *debounce* qui réduit réellement la charge côté serveur.
- **`limit=5`** : la limitation du nombre de résultats recommandée par RWEB, et l'application de la consigne du W3C de ne transférer que les données nécessaires.

Pour une liste courte et stable (pays, catégories, quelques dizaines de valeurs), l'élément `<datalist>` présenté dans l'onglet RWEB reste préférable : zéro requête pendant la saisie, et aucun JavaScript à écrire.

Pour le **contrôle**, les outils de développement du navigateur suffisent :

- Onglet **Réseau** (Network), filtre **Fetch/XHR** : taper un mot dans le champ et compter les requêtes émises — il doit y en avoir une seule par pause de saisie, et aucune en dessous de trois caractères.
- Case **Désactiver le cache** (Disable cache) cochée, puis rechargement de la page : c'est la méthode « en vidant le cache » citée par le RGESN pour lister les requêtes externes. Dans Chrome, le filtre `-domain:mon-service.fr` (en remplaçant par votre domaine) masque les requêtes internes et ne laisse apparaître que celles vers des tiers.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Architecte Logiciel`

La première phrase de la « Mise en œuvre » du critère 4.9 (« réduire les appels à des API, scripts, librairies ou polices de caractères tiers ») dépasse largement le seul cas de la saisie utilisateur, et recoupe deux critères déjà publiés sur ce site :

- le [critère 4.4](../4-4_activation-service-tiers/) (activation des services tiers), qui porte sur le **moment** où un script ou un service tiers est chargé — systématiquement, ou seulement à la demande de l'utilisateur ;
- le [critère 4.8](../4-8_polices-caracteres/) (polices de caractères téléchargées), qui fixe des seuils chiffrés (deux polices, 400 Ko) pour l'un des appels tiers explicitement cités ici.

Le 4.9 se concentre donc sur ce qui lui est propre : les requêtes **déclenchées par l'utilisateur pendant qu'il tape**, que ni le 4.4 ni le 4.8 ne couvrent. Le [critère 4.10](../4-10_format-saisie/) (informer l'utilisateur du format de saisie attendu), qui le suit directement dans le RGESN, en est le prolongement naturel côté formulaire : la « saisie assistée » recommandée par RWEB — indiquer le format attendu, guider l'utilisateur localement — réduit à la fois les requêtes de suggestion et les allers-retours de soumission en erreur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque ce critère **« Validé »** avec une justification d'une seule ligne : « Le service ne propose pas d'autocomplétion. » C'est le premier cas de validation prévu par le moyen de test du RGESN (« s'assurer que le service ne propose pas d'autocomplétion »), et le plus simple : sans mécanisme de suggestion, il n'y a ni délai ni seuil à vérifier.

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) illustre le cas inverse, plus instructif : le service propose une autocomplétion et marque lui aussi le critère **« Validé »**, en précisant : « Les requêtes sont limitées lors de la saisie notamment en initiant l'autocomplétion à 3 caractères, avec une exception à 2 caractères pour les routes nationales et départementales. » Cette exception montre que le seuil de trois caractères — présenté comme un exemple (« par exemple ») dans la « Mise en œuvre » du RGESN — doit être adapté au vocabulaire du service : un identifiant de route comme « N7 » ne compte que deux caractères, et un seuil de trois empêcherait tout simplement de le trouver. À noter toutefois que le moyen de test du RGESN, lui, demande « au moins 3 caractères saisis » : une telle exception mérite d'être justifiée dans la déclaration, comme DiaLog le fait ici.

{{% /tab %}}

{{< /tabs >}}
