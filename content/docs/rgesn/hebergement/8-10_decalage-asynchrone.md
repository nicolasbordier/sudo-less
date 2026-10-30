---
weight: 1000
title: "8.10 - Calculs et transferts asynchrones au bon moment"
description: "Critère 8.10 du RGESN : planifier sauvegardes, imports et mises à jour hors des pics du réseau et quand l'électricité est la moins carbonée, avec les données ouvertes d'éCO2mix, et reporter les transferts mobiles au Wi-Fi."
icon: "schedule"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-30T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique tient-il compte des contraintes externes pour minimiser l'impact environnemental des calculs et transferts de données asynchrones ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Hébergement` |
| **Critère**  | `8.10` |
| **Phase** | `Conception` |
| **Priorité** | `Recommandé` |
| **Difficulté** | `Fort` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de calculs ou transferts de données asynchrones` |
| **Métiers concernés** | `Responsable de la programmation` `Architecte Logiciel` `Responsable RSE/Numérique soutenable` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/8.10/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Planifier les calculs et transferts de données asynchrones (sauvegardes, mises à jour, entraînement...) énergivores en dehors des pics quotidiens de consommation électrique, pour les algorithmes et traitement consommateurs pouvant être décalés dans le temps.

Ajuster la temporalité des calculs et transferts de données asynchrones pour éviter les moments où les serveurs ou les réseaux sont le plus sollicités, de façon à éviter l'achat de nouveaux équipements pour supporter les « pics ». Préférer les transferts de données d'un terminal mobile lorsque celui-ci est connecté au réseau filaire (qui est moins sensible aux usages que le réseau mobile en termes de ressources et de consommation énergétique).

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Configurer les calculs et transferts de données asynchrones en prenant en compte ces paramètres :

- Énergie : Éviter de planifier les calculs ou transferts de données asynchrones au moment des pics quotidiens de consommation électrique (lorsque la production électrique est la plus carbonée) pour les opérations pouvant être décalées dans le temps (par exemple utiliser l'API Ecowatt développée par RTE et l'ADEME).
- Infrastructure : Décaler les calculs et mises à jour importantes lorsque la disponibilité des ressources de calcul est faible (afin d'éviter l'achat de nouveaux équipements).
- Réseau : Il s'agit de décaler les utilisations importantes, en limitant l'utilisation du réseau internet entre 19h00 et 23h00. Par exemple, si une mise à jour volumineuse est prête à être diffusée à 18h00, déclarer sa mise en production à 23h00. De façon complémentaire, lorsque le service mobile est utilisé sur un terminal mobile ayant la possibilité de se connecter sur un réseau mobile et sur un réseau filaire, reporter les transferts de données non urgentes (par exemple : mises à jour non critiques, sauvegardes, remontées de statistiques) au moment où le terminal est connecté au réseau filaire (Wi-Fi notamment).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

Le service numérique justifie dans la déclaration d'écoconception de la mise en œuvre de méthodes pour décaler les calculs et transferts de données asynchrones en fonction de la disponibilité de l'énergie électrique (éviter les pics quotidiens de consommation électrique qui impliquent une électricité plus carbonée), de la charge des infrastructures internet, et éventuellement en fonction de la disponibilité des ressources de calcul quand cela est pertinent.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="5">}}
{{% tab tabName="W3C et RWEB" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`, `Responsable de la programmation`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026) en font un critère de succès, « Carbon shifting », dans la fiche [**« Assess the impact and requirements of data processing »**](https://www.w3.org/TR/web-sustainability-guidelines/#assess-the-impact-and-requirements-of-data-processing). Il s'agit de programmer ou regrouper les tâches « at a time when carbon intensity is lower », d'après des données en temps réel du réseau électrique.

Le référentiel [RWEB du Collectif GreenIT](https://rweb.greenit.fr/) rattache au 8.10 deux fiches, [RWEB 0017](https://rweb.greenit.fr/fr/fiches/RWEB_0017-eviter-le-transfert-d-une-grande-quantite-de-donnees-pour-realiser-un-traitement) (traiter les données dans la base plutôt que de les transférer) et [RWEB 0025](https://rweb.greenit.fr/fr/fiches/RWEB_0025-favoriser-le-request-collapsing) (regrouper les appels à un service tiers). Elles réduisent le volume des transferts, mais ne disent rien de leur moment, qui est le sujet du 8.10.

{{% /tab %}}

{{% tab tabName="Quand l'électricité est-elle la moins carbonée ?" %}}

Profil(s) métier concerné(s) : `Responsable RSE/Numérique soutenable`, `Architecte Logiciel`

RTE publie chaque quart d'heure une estimation des émissions de la production française, en données ouvertes ([éCO2mix](https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/), champ `taux_co2`). Relevé du 24 au 30 octobre 2026, en heure de Paris :

| Heures | Intensité moyenne |
|---|---:|
| 0 h – 9 h | 27 à 30 g/kWh |
| 10 h – 15 h | 17 à 24 g/kWh, minimum entre 12 h et 14 h |
| 16 h – 23 h | 29 à 33 g/kWh, maximum vers 19 h |

Deux enseignements :

- **la nuit n'est pas le moment le moins carboné**, du moins cette semaine-là : la production solaire fait baisser l'intensité en milieu de journée ;
- **l'écart entre les jours dépasse l'écart entre les heures** : la moyenne quotidienne est passée de 14,5 g le 24 octobre à 39,8 g le 29 octobre.

Une heure fixe ne suffit donc pas. Mieux vaut consulter la valeur du moment, avec un délai maximal. Le RGESN cite aussi l'API Ecowatt de RTE et de l'ADEME, qui signale les jours de tension sur le réseau ; elle demande une inscription sur le portail de RTE.

Le pic du réseau internet, entre 19 h et 23 h selon le RGESN, et le pic de charge des serveurs restent à éviter dans tous les cas.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Responsable de la programmation`, `Architecte Logiciel`

**1. Lister les traitements décalables** : sauvegardes, imports, exports, réindexations, mises à jour, entraînements de modèles. Pour chacun, noter l'heure actuelle et le délai réellement acceptable.

**2. Lancer le traitement quand l'électricité est peu carbonée**, au plus tard après un délai. Ce script attend que l'intensité passe sous un seuil, en vérifiant toutes les 30 minutes :

```python
#!/usr/bin/env python3
"""Lance la commande quand l'électricité produite en France est peu carbonée,
au plus tard après ATTENTE_MAX heures."""
import json, subprocess, sys, time, urllib.request

SEUIL = 25          # gCO2eq/kWh
ATTENTE_MAX = 16    # heures
URL = ('https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-tr/records'
       '?select=date_heure,taux_co2&where=taux_co2%20is%20not%20null&order_by=date_heure%20desc&limit=1')

fin = time.time() + ATTENTE_MAX * 3600
while time.time() < fin:
    try:
        mesure = json.load(urllib.request.urlopen(URL, timeout=30))['results'][0]
    except Exception as e:
        print('éCO2mix indisponible :', e, file=sys.stderr)
        break
    print(f"{mesure['date_heure']} : {mesure['taux_co2']} gCO2eq/kWh", file=sys.stderr)
    if mesure['taux_co2'] <= SEUIL:
        break
    time.sleep(30 * 60)
sys.exit(subprocess.call(sys.argv[1:]))
```

Testé le 30 octobre 2026 : lancement immédiat sous le seuil, lancement à l'échéance au-dessus, et lancement immédiat si l'API ne répond pas. Le code de sortie de la commande est conservé. Dans la crontab, un départ à 23 h couvre la nuit et le milieu de la journée suivante, jusqu'à 15 h :

```
0 23 * * * /usr/local/bin/attendre-co2.py /usr/local/bin/sauvegarde.sh
```

**3. Sur mobile, attendre le Wi-Fi.** Sur Android, WorkManager reporte une tâche jusqu'à ce que ses conditions soient réunies :

```kotlin
val contraintes = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.UNMETERED)
    .setRequiresCharging(true)
    .build()
val envoi = OneTimeWorkRequestBuilder<EnvoiStatistiquesWorker>()
    .setConstraints(contraintes)
    .build()
WorkManager.getInstance(context).enqueue(envoi)
```

`UNMETERED` désigne un réseau non facturé au volume, en pratique le Wi-Fi. Sur iOS, `allowsExpensiveNetworkAccess = false`, dans la configuration de `URLSession`, interdit les transferts sur réseau mobile.

**4. Documenter** dans la déclaration d'écoconception : les traitements décalés, la règle appliquée (seuil, fenêtre, délai maximal) et la source des données.

{{% /tab %}}

{{% tab tabName="Ce qui ne se décale pas" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`

Le critère vise les traitements **qui peuvent attendre**. Une notification d'urgence, un paiement ou la réponse à une action de l'utilisateur ne se décalent pas.

Le décalage ne réduit pas non plus la quantité de calcul. Il est complémentaire d'un traitement plus léger, d'un cache ([critère 7.1](../../backend/7-1_cache-serveur/)) ou d'une sauvegarde incrémentale ([critère 8.9](../8-9_duplication-donnees/)), qui réduisent ce qui est calculé ou transféré.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Architecte Logiciel`

- le [critère 7.3](../../backend/7-3_traitement-arriere-plan/) (traitement en arrière-plan) : un traitement long passé en tâche de fond devient décalable ;
- le [critère 8.6](../8-6_localisation/) (localisation) : le lieu du calcul fixe l'intensité carbone moyenne, le moment la fait varier ;
- le [critère 8.5](../8-5_electricite-renouvelable/) (électricité renouvelable) : consommer quand le réseau est peu carboné agit sur l'électricité réellement produite.

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
| [DiaLog](https://dialog.beta.gouv.fr/) | **Non validé** | « Les tâches asynchrones d'import de données ont lieu à heure fixe le lundi entre 16h et 18h. » |
| [Musée d'arts de Nantes](https://museedartsdenantes.nantesmetropole.fr/declaration-d-ecoconception/) | En cours de validation | Traitements possibles la nuit, à l'heure choisie par le client |
| [FACE](https://declarations-f52e8c.gitlab-pages.din.developpement-durable.gouv.fr/uploads/73f86f8cf0659b4e84d9c83adc0f0a97/face_rgesn_2024_outil_declaration_ecoconception.pdf) | Non applicable | « Le service numérique n'inclut pas de calculs ou transferts de données asynchrones. » |

**DiaLog** a aujourd'hui plus de tâches planifiées que sa déclaration n'en décrit. D'après son [code source](https://github.com/MTES-MCT/dialog) :

- l'import des arrêtés depuis Litteralis tourne du lundi au vendredi à 16 h 15 UTC, soit 17 h 15 à Paris en hiver. C'est l'une des heures les plus carbonées de la semaine relevée, juste avant le pic du réseau ;
- d'autres synchronisations tournent en journée ;
- la purge des jetons et l'export CSV complet tournent la nuit.

Si le besoin métier le permet, l'import pourrait passer en milieu de journée, ou être lancé par un script comme celui de l'étape 2.

**Le Musée d'arts de Nantes** propose les traitements « la nuit ». C'est un bon choix pour le réseau et les serveurs. Pour l'électricité, en France, le milieu de journée peut être plus favorable, comme le montre le relevé d'éCO2mix.

{{% /tab %}}

{{< /tabs >}}
