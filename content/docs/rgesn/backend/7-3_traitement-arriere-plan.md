---
weight: 300
title: "7.3 - Information sur un traitement en cours"
description: "Critère 7.3 du RGESN : bloquer le second envoi d'un formulaire, afficher un message de statut accessible, traiter en tâche de fond ce qui est long et ignorer les doublons côté serveur."
icon: "hourglass_top"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique informe-t-il l'utilisateur d'un traitement en cours en arrière-plan ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Backend` |
| **Critère**  | `7.3` |
| **Phase** | `Conception` |
| **Priorité** | `Modéré` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique ne fait pas de traitement en arrière-plan` |
| **Métiers concernés** | `Développeur` `Responsable Produit` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/7.3/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Éviter les requêtes simultanées provoquées par l'utilisateur s'il ne sait pas que son action est en cours de prise en compte.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Rendre indisponible l'action qui génère le traitement (par exemple un bouton de soumission de formulaire) lorsqu'elle est initiée par l'utilisateur quand la requête est en cours de traitement. Il conviendra également d'informer l'utilisateur que le traitement est en cours, en précisant éventuellement une durée approximative de traitement.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Réaliser des tests fonctionnels permettant de vérifier que lorsqu'une action est en cours de traitement, le bouton ou l'élément déclencheur est désactivé et qu'un indicateur visuel ou un message d'attente est présent pour informer l'utilisateur.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

Le critère 7.3 reprend presque mot pour mot un conseil de la [recommandation n°2 de la famille Backend](https://gr491.isit-europe.org/?famille=backend&num_reco=2) du [GR491](https://gr491.isit-europe.org/) (INR) : [« Est-ce que l'utilisateur est informé d'un traitement en cours en arrière-plan ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-certains-traitements-sont-invisibles-du-point-de-051131). Ses précisions en donnent la raison : certains traitements « peuvent produire des délais de réponse incompris et inciter l'utilisateur à renouveler ses opérations ». Son test : « La liste des traitements qui ne nécessitent pas un résultat immédiat est-elle établie ? »

Le conseil voisin, [« Est-ce que l'intégration d'un traitement asynchrone a été évaluée ? »](https://gr491.isit-europe.org/crit.php?id=2-backend-le-traitement-differe-doperations-permet-de-diluer-1d8156), ajoute qu'un traitement différé permet « de diluer sur une période de temps plus longue les demandes de charges ».

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT) et Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) ne rattache aucune fiche au 7.3. [**RWEB 0007 — « Proposer un traitement asynchrone lorsque c'est possible »**](https://rweb.greenit.fr/fr/fiches/RWEB_0007-proposer-un-traitement-asynchrone-lorsque-c-est-possible) en traite le cas le plus long : l'utilisateur lance le traitement, puis est prévenu à la fin, « via la réception d'un e-mail ou d'une notification ». Son principe de validation : **aucun** traitement synchrone de plus d'une minute.

Les Designers Éthiques, dans [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers), rangent le 7.3 parmi les interactions à concevoir. Sans information, l'utilisateur « risque de relancer l'action et de générer des requêtes superflues ».

{{% /tab %}}

{{% tab tabName="Accessibilité" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer`

**Le message d'attente doit être annoncé.** Le critère 7.5 du [RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/), qui correspond au critère 4.1.3 des WCAG (niveau AA), porte sur les messages de statut. Un message de résultat utilise `role="status"` (test 7.5.1). Un message qui indique la progression d'un processus utilise `role="log"`, `role="progressbar"` ou `role="status"` (test 7.5.3). Sans ce rôle, un lecteur d'écran n'annonce pas forcément le message.

**Un bouton désactivé pose aussi problème.** Le [GOV.UK Design System](https://design-system.service.gov.uk/components/button/) l'écrit : « Disabled buttons have poor contrast and can confuse some users, so avoid them if possible. » L'attribut `disabled` retire en plus le bouton de la navigation au clavier. Avec `aria-disabled="true"`, le bouton reste lisible et atteignable, mais c'est au script d'ignorer les clics.

Le GOV.UK propose `data-prevent-double-click="true"`, qui ignore un second clic. Il rappelle que cela ne fonctionne qu'avec JavaScript : il faut aussi « think about the issue server-side ».

{{% /tab %}}

{{% tab tabName="Le double clic" %}}

Profil(s) métier concerné(s) : `Développeur`

Testé le 30 octobre 2026 dans Chromium 155, sur un serveur local qui répond en deux secondes : un double clic sur le bouton d'envoi d'un formulaire `POST`, à 150 puis à 600 ms d'intervalle.

| Formulaire | Requêtes traitées par le serveur | Valeur du bouton envoyée |
|---|---:|---|
| Sans script | **2** | Oui |
| `disabled` posé sur le bouton dans l'événement `submit` | 1 | **Non** |
| Verrou en JavaScript et `aria-disabled`, script de l'onglet suivant | 1 | Oui |
| Envoi par Turbo 7.3, utilisé par DiaLog | 1 | Oui |

**Sans script, le serveur traite deux fois la demande.** Au second clic, le navigateur abandonne la première requête (`net::ERR_ABORTED`), mais le serveur l'a déjà reçue. Il crée deux enregistrements, ou envoie deux courriels.

**`disabled` fait perdre la valeur du bouton.** Le navigateur construit les données du formulaire après l'événement `submit`, et en exclut les champs désactivés ([HTML](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#constructing-the-form-data-set)). Le `name` et la `value` du bouton disparaissent. Un serveur qui s'en sert pour distinguer « Enregistrer » de « Publier » reçoit une requête incomplète.

**Le retour arrière restaure la page verrouillée.** Après l'envoi, la touche « Précédent » ramène la page depuis le cache du navigateur avec le bouton encore sur « Envoi en cours… ». Le script doit le réinitialiser à l'événement `pageshow`.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

**1. Lister les traitements qui prennent du temps**, comme le demande le GR491 : envoi de formulaire, export, import, conversion de fichier. Le journal des temps de réponse du [critère 7.1](../7-1_cache-serveur/) les fait apparaître.

**2. Verrouiller le formulaire et annoncer l'attente.** Le script testé dans l'onglet précédent :

```html
<form method="post" action="/demande" id="demande">
  …
  <button name="action" value="envoyer">Envoyer</button>
</form>
<p id="statut" role="status"></p>
```

```js
const form = document.querySelector('#demande');
const bouton = form.querySelector('button');
const statut = document.querySelector('#statut');
const libelle = bouton.textContent;

form.addEventListener('submit', (e) => {
  if (form.dataset.envoi) { e.preventDefault(); return; }
  form.dataset.envoi = 'oui';
  bouton.setAttribute('aria-disabled', 'true');
  bouton.textContent = 'Envoi en cours…';
  statut.textContent = 'Envoi en cours, merci de patienter.';
});

// Au retour arrière, la page revient du cache du navigateur encore verrouillée.
window.addEventListener('pageshow', (e) => {
  if (!e.persisted) return;
  delete form.dataset.envoi;
  bouton.removeAttribute('aria-disabled');
  bouton.textContent = libelle;
  statut.textContent = '';
});
```

La zone `role="status"` existe, vide, dès le chargement de la page : un lecteur d'écran annonce le texte qui y est ajouté. Un style `button[aria-disabled="true"]` rend l'état visible.

**3. Traiter en tâche de fond ce qui est long.** Pour un export ou un import de plusieurs secondes, enregistrer la demande et répondre tout de suite. Le travail passe ensuite dans une file de tâches (Symfony Messenger, Celery, Sidekiq…). La page d'attente donne une durée approximative, par exemple « Génération en cours, environ 30 secondes ». Pour un traitement de plusieurs minutes, un courriel prévient à la fin, comme le propose RWEB 0007.

**4. Ignorer les doublons côté serveur**, pour les cas où le script ne s'exécute pas. Le formulaire porte un jeton unique, généré à l'affichage, dans un champ caché `jeton_envoi`. Une contrainte d'unicité empêche le second enregistrement :

```sql
CREATE UNIQUE INDEX demande_jeton_envoi ON demande (jeton_envoi);

INSERT INTO demande (jeton_envoi, objet) VALUES ($1, $2)
ON CONFLICT (jeton_envoi) DO NOTHING;
```

Si la demande existe déjà, le serveur renvoie la même page de confirmation.

**5. Tester**, comme le demande le moyen de test. Dans l'onglet **Réseau** des outils de développement, choisir une connexion lente, puis cliquer deux fois sur le bouton. Vérifier qu'une seule requête part, que le bouton est indisponible et que le message s'affiche. Revenir ensuite en arrière et vérifier que le formulaire est de nouveau utilisable.

**6. Documenter** dans la déclaration d'écoconception. Par exemple : « Formulaires verrouillés pendant l'envoi, avec un message de statut. Exports traités en tâche de fond, avec une durée estimée affichée. Doublons écartés côté serveur. »

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Responsable Produit`

- le [critère 4.9](../../ux-ui/4-9_requetes-saisie-utilisateur/) (requêtes pendant la saisie) : limiter les requêtes avant l'envoi, comme le 7.3 les limite pendant ;
- le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) (impacts des fonctionnalités) : informer avant de lancer un traitement coûteux, quand le 7.3 informe pendant ;
- le [critère 4.13](../../ux-ui/4-13_notifications/) (notifications) : le courriel de fin de traitement en est une ;
- le [critère 7.1](../7-1_cache-serveur/) (cache serveur) : un résultat déjà calculé n'a pas besoin de page d'attente.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

Les déclarations ont été relues et le code source de DiaLog consulté le 30 octobre 2026.

| Site | Déclaration | Justification |
|---|---|---|
| [DiaLog](https://dialog.beta.gouv.fr/) | Validé | « L'utilisateur est informé d'un traitement en cours en arrière plan, par exemple lors de la génération du Word. » |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | Non applicable | « Pas de traitement en arrière-plan. » |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Non applicable | « le service numérique ne fait pas de traitement en arrière-plan, déclenché par l'utilisateur » |
| [SPOTE](https://spote.developpement-durable.gouv.fr/) | Non détaillé | — |

**DiaLog** couvre le critère de deux façons, d'après son [code source](https://github.com/MTES-MCT/dialog) :

- ses formulaires sont envoyés par Turbo 7.3, qu'aucun gabarit ne désactive avec `data-turbo="false"`. Turbo désactive le bouton pendant l'envoi et affiche une barre de progression au bout de 500 ms. Le test de l'onglet « Le double clic » a été fait avec cette version ;
- le lien d'export Word affiche « Génération du document en cours… » et ignore les clics suivants jusqu'à la fin du téléchargement. En cas d'échec, un message le signale.

Le message de l'export remplace le texte du lien, sans zone `role="status"`, que le critère 7.5 du RGAA demande pour un message de progression. Un lecteur d'écran peut donc ne pas l'annoncer.

**Le Musée et FACE** déclarent le critère non applicable. Le RGESN cite pourtant le bouton d'envoi d'un formulaire comme exemple : un service qui a des formulaires est concerné dès que leur traitement prend du temps. Le Musée a au moins un moteur de recherche. Pour une recherche, une requête en double coûte peu ; pour un formulaire qui enregistre une donnée ou envoie un courriel, elle crée un doublon.

{{% /tab %}}

{{< /tabs >}}
