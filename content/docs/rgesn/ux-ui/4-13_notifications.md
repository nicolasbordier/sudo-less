---
weight: 1300
title: "4.13 - Limitation des notifications"
description: "Critère 4.13 du RGESN : pourquoi et comment limiter les notifications (push, e-mail, SMS, pop-in), éviter leur multiplication sur plusieurs canaux et permettre à l'utilisateur de les désactiver simplement."
icon: "notifications_off"
date: "2026-10-20T00:00:00+01:00"
lastmod: "2026-10-20T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique limite-t-il le recours aux notifications, tout en laissant la possibilité à l'utilisateur de les désactiver ?

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
| **Critère**  | `4.13` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Moyen` |
| **Applicabilité** | `N/A si le service numérique ne comporte pas d'IHM` |
| **Métiers concernés** | `Concepteur UX / UI` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/4.13/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

De nombreuses applications sont configurées par défaut pour adresser à l'utilisateur des notifications sur leur terminal. Il s'agit d'incitations à l'usage du service et du terminal associé (le cas échéant). L'objectif est donc de réduire l'usage de ressources informatiques en évitant d'attirer inutilement l'attention de l'utilisateur ou en consommant inutilement des ressources informatiques.

Il convient donc de minimiser le nombre de notifications, de réfléchir à leur inclusion par défaut dans le design du service numérique et de donner à l'utilisateur la possibilité de les désactiver.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Les notifications envisagées par le service numérique sont dans l'intérêt de l'utilisateur en termes de besoin. Les notifications évitent également la multiplication sur différents canaux redondants (SMS, mail, notification d'application, notification d'interface, pop-in, etc.).

Il s'agit donc de proposer une configuration par défaut limitant les notifications.

L'utilisateur peut désactiver les notifications ou choisir la fréquence de réception de ces notifications.

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Suivre la fréquence et la quantité des notifications, en se fixant des objectifs chiffrés en la matière.

Documenter les choix faits en matière de réduction au strict minimum des notifications dans la déclaration d'écoconception.

Le critère est validé si le service numérique :

- Ne propose pas de notification ou propose par défaut un nombre de notifications limité (un seuil inférieur à cinq par jour devrait être visé);
- Donne à l'utilisateur la possibilité de désactiver et de réduire, via son interface, les notifications proposées par le service de façon simple et rapide (par exemple, un bouton directement visible sur l'interface utilisateur). Les possibilités de suppression ou de réduction des notifications doivent être mises en évidence dans le service numérique.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="7">}}
{{% tab tabName="INR - GR491" %}}

Profil(s) métier concerné(s) : `Développeur`, `Designer UX/UI`

Le critère 4.13 a une correspondance directe dans la [recommandation n°4 de la famille Contenus](https://gr491.isit-europe.org/?famille=contenus&num_reco=4) du [GR491](https://gr491.isit-europe.org/) (INR), déjà citée au [critère 4.10](../4-10_format-saisie/), via son [critère consacré aux notifications](https://gr491.isit-europe.org/crit.php?id=4-contenus-les-methodes-de-notifications-peuvent-employer-des-e6138f) : « Les notifications utilisateurs sont-elles nécessaires et désactivables par l'utilisateur ? »

Ses deux tests recoupent le RGESN, et le second y ajoute une piste qui lui est propre :

- « L'utilisateur a-t-il le choix des mécanismes de notification, de leur fréquence pour lui éviter de tout recevoir par défaut ? »
- « L'abonnement sur un flux RSS est-il proposé comme alternative à des notifications spontanées de type push ? »

Le flux RSS inverse la logique de la notification. Ce n'est plus le service qui sollicite l'utilisateur : c'est l'utilisateur qui vient chercher l'information quand il le décide, avec le lecteur de son choix. Les précisions du critère réunissent les deux enjeux du RGESN : réduire les notifications est utile « pour réduire les consommations d'énergie ainsi que le détournement d'attention des utilisateurs ».

{{% /tab %}}

{{% tab tabName="Designers Éthiques" %}}

Profil(s) métier concerné(s) : `Designer`, `Développeur`

Le [Guide d'écoconception de services numériques](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/) des Designers Éthiques cite **explicitement** le critère 4.13 dans sa section [**7.8 Interactions**](https://designersethiques.org/fr/thematiques/ecoconception/guide-d-ecoconception/7-realiser-et-developper/7-8-interactions), sous le titre « Repenser les notifications » : « Entre tenir informer et solliciter en continu, la frontière peut être ténue. Encore une fois, éco-conception et éthique se rejoignent. » Il propose plusieurs pistes :

- « Réfléchir aux différents formats des notifications selon leur degré d'urgence. »
- « Permettre de personnaliser de qui, quand, et comment ils reçoivent les notifications. »
- « Éviter les mails de confirmation inutiles (ex : désinscription d'une newsletter). »
- « Remplacer un toaster de confirmation par un changement d'état. Par exemple, un toaster indiquant qu'un nouvel élément a bien été créé peut simplement être remplacé par un état focus sur le nouvel élément. »

La dernière piste montre que le critère ne concerne pas que les notifications push ou les e-mails. Le RGESN cite aussi les « notification[s] d'interface » et les « pop-in » parmi les canaux à ne pas multiplier. Un message de confirmation affiché dans l'interface peut souvent être remplacé par l'état visible du résultat lui-même.

La ressource [**« RGESN, ce que doivent faire les designers »**](https://designersethiques.org/fr/thematiques/ecoconception/rgesn-ce-que-doivent-faire-les-designers) reprend le seuil chiffré du critère : « Se fixer des quantités et fréquences maximales de notifications (ex : 5 par jour maximum) et les suivre. »

{{% /tab %}}

{{% tab tabName="W3C - Web Sustainability Guidelines" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C ont une fiche dédiée, [**« Avoid unwanted notifications »**](https://www.w3.org/TR/web-sustainability-guidelines/#avoid-unwanted-notifications), avec deux critères de succès :

- **Need for notification** : « Only send notifications that match user preferences or that the user has explicitly requested. Avoid unnecessary emails, (SMS) messages, and push notifications. Give users clear control over each notification type. »
- **Notification settings** : « Let users manage their notification and messaging settings easily. Make unsubscribe, logout, and account closure options visible and accessible. Turn off optional notifications by default and enable them only after user opt-in. »

La dernière phrase est plus précise que le RGESN. Là où le RGESN demande « une configuration par défaut limitant les notifications », le W3C fixe la règle : toute notification **optionnelle** est désactivée par défaut, et ne s'active qu'après un consentement explicite de l'utilisateur (opt-in). Le W3C demande aussi un contrôle **par type de notification**, pas seulement un interrupteur global.

{{% /tab %}}

{{% tab tabName="RWEB (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) n'a pas de fiche étiquetée « RGESN 4.13 », mais deux fiches portent sur les e-mails, l'un des canaux cités par le critère. Elles sont toutes deux marquées « NA » en correspondance RGESN :

- [**RWEB 0103 — « Limiter les e-mails lourds et redondants »**](https://rweb.greenit.fr/fr/fiches/RWEB_0103-limiter-les-e-mails-lourds-et-redondants) rappelle que les e-mails sont stockés chez le fournisseur de messagerie, et aussi localement pour les comptes IMAP et POP3. Elle recommande de « définir la fréquence d'envoi au strict nécessaire ou au choix de l'utilisateur », et pour la gestion client de « Réduire à un seul envoi pour les commandes internet » plutôt qu'un e-mail par étape (commande, paiement, expédition, livraison, facture…). Principe de validation : **aucun** e-mail envoyé « sans que l'utilisateur n'ait un contrôle complet sur la fréquence et le contenu ».
- [**RWEB 0102 — « Limiter la taille des e-mails envoyés »**](https://rweb.greenit.fr/fr/fiches/RWEB_0102-limiter-la-taille-des-e-mails-envoyes) porte sur le poids de chaque notification envoyée par e-mail. Selon la fiche, un e-mail de confirmation en HTML pèse en moyenne 26 Ko, contre 4 Ko en texte brut.

Le principe de validation de la fiche 0103 est plus strict que le RGESN : il porte sur **chaque** e-mail envoyé, là où le RGESN se contente d'un nombre limité par défaut et d'une possibilité de désactivation.

{{% /tab %}}

{{% tab tabName="Permissions des plateformes" %}}

Profil(s) métier concerné(s) : `Développeur`

Les systèmes d'exploitation et les navigateurs ont eux-mêmes durci l'accès aux notifications. Ils appliquent désormais par défaut une partie de ce que demande le critère :

- **Android** : depuis Android 13 (API 33), les notifications d'une application nouvellement installée sont **désactivées par défaut** ; l'application doit demander la permission `POST_NOTIFICATIONS` et attendre l'accord de l'utilisateur ([documentation Android](https://developer.android.com/develop/ui/views/notifications/notification-permission)). Google recommande de déclencher cette demande à partir d'une action de l'utilisateur, par exemple quand il « tape sur un bouton "cloche d'alerte" », et « dans le bon contexte, pour qu'il soit explicitement clair à quoi servent les notifications ».
- **Web** : la [documentation MDN de `Notification.requestPermission()`](https://developer.mozilla.org/fr/docs/Web/API/Notification/requestPermission_static) précise que demander l'autorisation en réponse à un geste de l'utilisateur n'est « pas seulement une bonne pratique » : Firefox bloque les demandes non déclenchées par un geste de l'utilisateur depuis sa version 72.

Ces garde-fous ne couvrent qu'une partie du critère. Ils encadrent l'**autorisation** initiale, mais pas le **nombre** de notifications envoyées une fois l'autorisation accordée. Et ils ne s'appliquent ni aux e-mails, ni aux SMS, ni aux notifications d'interface. Le seuil « inférieur à cinq par jour » et la possibilité de régler la fréquence restent de la responsabilité du service.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Concepteur UX / UI`

**1. Une page de préférences par type de notification**, avec un seul canal activé par défaut pour ce qui est utile, et tout ce qui est optionnel désactivé :

```html
<form id="preferences-notifications">
  <fieldset>
    <legend>Réponse à l'une de vos demandes</legend>
    <label><input type="checkbox" name="demande-email" checked> Par e-mail</label>
    <label><input type="checkbox" name="demande-navigateur"> Dans le navigateur</label>
  </fieldset>

  <fieldset>
    <legend>Nouveautés du service</legend>
    <label><input type="radio" name="nouveautes" value="jamais" checked> Jamais</label>
    <label><input type="radio" name="nouveautes" value="mensuel"> Un récapitulatif par mois</label>
  </fieldset>

  <button type="submit">Enregistrer mes préférences</button>
</form>
```

- **Un seul canal par défaut** pour chaque type : l'e-mail pour la réponse à une demande, pas l'e-mail **et** le navigateur. C'est la « multiplication sur différents canaux redondants » que le RGESN demande d'éviter.
- **Optionnel = désactivé** : les nouveautés du service sont sur « Jamais » par défaut, conformément à la règle d'opt-in du W3C.
- **Un récapitulatif plutôt qu'un flux** : proposer une fréquence (immédiate, quotidienne, mensuelle) répond au « choisir la fréquence de réception » du RGESN, et regroupe plusieurs notifications en un seul envoi.

**2. Ne demander l'autorisation du navigateur qu'au moment où l'utilisateur la choisit** :

```js
const caseNavigateur = document.querySelector('[name="demande-navigateur"]');

caseNavigateur.addEventListener('change', async () => {
  if (!caseNavigateur.checked) return;
  const permission = await Notification.requestPermission();
  if (permission !== 'granted') caseNavigateur.checked = false;
});
```

La demande n'apparaît que si l'utilisateur coche lui-même la case, jamais au chargement de la page. Si l'utilisateur refuse l'autorisation, la case est décochée : l'interface reste cohérente avec ce que le navigateur autorise réellement.

**3. Rendre la désactivation visible**, comme le demande le moyen de test (« un bouton directement visible sur l'interface utilisateur ») : un lien « Gérer mes notifications » dans l'en-tête du compte, et **dans chaque e-mail envoyé**, qui mène directement à cette page.

**4. Mesurer**, pour suivre l'objectif chiffré demandé par le moyen de test. Si chaque envoi est enregistré, une requête suffit à repérer les utilisateurs qui dépassent le seuil :

```sql
SELECT utilisateur_id, DATE(envoyee_le) AS jour, COUNT(*) AS nb_notifications
FROM notifications_envoyees
GROUP BY utilisateur_id, DATE(envoyee_le)
HAVING COUNT(*) >= 5;
```

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Concepteur UX / UI`, `Développeur`

Le RGESN répond à l'article 25 de la loi du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (loi REEN). Selon cet article, les critères du référentiel concernent « notamment l'affichage et la lecture des contenus multimédias pour permettre de limiter le recours aux stratégies de captation de l'attention des utilisateurs des services numériques ».

Le critère 4.13 traite l'une de ces stratégies, aux côtés de deux critères déjà publiés sur ce site :

- le [critère 4.1](../4-1_lecture-automatique/) (lecture automatique des vidéos et sons) ;
- le [critère 4.2](../4-2_defilement-infini/) (défilement infini).

Les trois mécanismes ont le même effet : prolonger ou relancer l'usage du service sans que l'utilisateur l'ait décidé. Le [critère 4.14](../4-14_dark-patterns/) (procédés manipulatoires ou *dark patterns*), qui le suit directement dans le RGESN, prolonge cette logique. Une notification conçue pour faire revenir l'utilisateur (fausse urgence, compteur de messages non lus artificiellement gonflé) relève des deux critères à la fois.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

[FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) (Ministères Territoires Écologie Logement, critère évalué le 29 janvier 2025) marque ce critère **« Non validé »**. C'est le seul critère « Prioritaire » non validé de sa famille UX/UI. La justification montre précisément ce qui manque : « Les notifications sont présentes dans l'application, de manière non intrusive (pas de notification navigateur), et par e-mail. Les notifications par e-mail ne sont pas désactivables. »

Le service limite pourtant déjà ses notifications : rien dans le navigateur, et des notifications discrètes dans l'application. C'est la seconde condition du critère qui fait défaut, la possibilité de désactiver ou de réduire. Si certains e-mails sont nécessaires au déroulement d'une demande de subvention, la solution n'est pas forcément de les rendre désactivables un par un. Proposer de les regrouper en un récapitulatif quotidien ou hebdomadaire répond aussi au critère (« choisir la fréquence de réception »).

[DiaLog](https://dialog.beta.gouv.fr/ecoconception) (beta.gouv.fr, déclaration du 23 avril 2025) marque ce critère **« Validé »** par la voie la plus simple : « Le service n'utilise pas de mécanisme de notification. Simplement un email pour l'activation du compte. » Un e-mail d'activation est un message ponctuel, déclenché par l'utilisateur lui-même et nécessaire à l'usage du service. Il entre donc dans les notifications « dans l'intérêt de l'utilisateur » que le critère admet.

{{% /tab %}}

{{< /tabs >}}
