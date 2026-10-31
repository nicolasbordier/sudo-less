---
weight: 700
title: "9.7 - Stratégie d'inférence sobre"
description: "Critère 9.7 du RGESN : choisir le plus petit modèle qui suffit, limiter la longueur des réponses et le nombre de requêtes, réutiliser les réponses identiques, héberger l'inférence là où l'électricité est peu carbonée et estimer l'énergie de chaque réponse."
icon: "query_stats"
date: "2026-10-30T00:00:00+01:00"
lastmod: "2026-10-31T00:00:00+01:00"
draft: false
toc: true
---

---

## Le service numérique utilise-t-il une stratégie d'inférence optimisée en termes de consommation de ressources et des cibles utilisatrices ?

{{< table "table-borderless" >}}
|  |
| ---: |
| Version 2. Dernière mise à jour le 24 septembre 2024 |
{{< /table >}}

---

{{< table "table-responsive table-xs table-borderless"  >}}
|        |       |
|---------|--------|
| **Type**  | `Algorithmie` |
| **Critère**  | `9.7` |
| **Phase** | `Conception` |
| **Priorité** | `Prioritaire` |
| **Difficulté** | `Faible` |
| **Applicabilité** | `N/A si le service numérique n'inclut pas de phase d'inférence` |
| **Métiers concernés** | `Porteur de projet` `Data Scientist` `Développeur` |
| **Permalink** | https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/critere/9.7/ |
{{< /table >}}

---

###
### Fiche RGESN

{{< tabs tabTotal="3">}}
{{% tab tabName="Objectif" %}}

Réduire l'empreinte environnementale des modèles algorithmiques utilisés dans le domaine de l'intelligence artificielle en optimisant le besoin en ressources de leur phase d'inférence. Ce critère est particulièrement important pour l'intelligence artificielle (IA) générative. Si la phase d'entraînement a longtemps été perçue comme la plus consommatrice en énergie, le développement de l'IA générative tend à accroître la part de consommation d'énergie de la phase d'inférence, du fait du nombre de requêtes utilisateurs pour les services massivement consommés par le grand public. L'optimisation de la phase d'inférence est nécessaire pour aboutir à des modèles d'intelligence artificielle plus frugaux.

{{% /tab %}}
{{% tab tabName="Mise en œuvre" %}}

Définir une stratégie d'inférence qui minimise le besoin en ressources et répond strictement au besoin des cibles utilisatrices. Mettre en place des indicateurs de suivi de consommation d'énergie, besoin en ressources de calcul, nécessaires à la phase d'inférence. Ces métriques sont à analyser par rapport à la satisfaction des utilisateurs. Fixer des objectifs de minimisation de la consommation en ressources, en tenant compte du ratio entre ressources consommées et satisfaction des utilisateurs. S'assurer que la phase d'inférence permet d'optimiser le nombre de requêtes utilisateurs.

Utiliser des CPU, GPU ou des TPU efficaces, dont la localisation géographique est cohérente avec leurs activités et minimise l'empreinte environnementale (en particulier, dans un pays à l'intensité carbone la plus faible possible).

{{% /tab %}}
{{% tab tabName="Moyen de test ou de contrôle" %}}

La stratégie d'inférence du service est adaptée aux cibles utilisatrices en minimisant les ressources nécessaires à son fonctionnement et les requêtes inutiles. Des indicateurs de suivi de consommation en ressources et de satisfaction des utilisateurs sont mis en place pour ajuster la phase d'inférence, avec pour objectif la frugalité du modèle sous-jacent au service.

Le critère est validé si le service numérique démontre dans sa déclaration d'écoconception la mise en place de principes d'écoconception dans sa phase d'inférence, adaptée aux besoins des utilisateurs.

{{% /tab %}}
{{< /tabs >}}

---

###
### Complément pour appliquer concrètement cette recommandation ?

Via ces différentes sources :

{{< tabs tabTotal="6">}}
{{% tab tabName="W3C et état de l'art" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Data Scientist`

Les [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) du W3C (version du 16 octobre 2026), dans la fiche [**« Establish responsible practices around AI and emerging or disruptive technologies »**](https://www.w3.org/TR/web-sustainability-guidelines/#establish-responsible-practices-around-ai-and-emerging-or-disruptive-technologies), demandent d'« Optimize models and deployment processes for efficiency ». Pour les modèles fournis par des tiers, ils acceptent des « credible estimates » quand les données directes manquent.

L'étude [« Power Hungry Processing »](https://arxiv.org/abs/2311.16863) (FAccT 2024), citée au [critère 9.2](../9-2_methode-apprentissage/), mesure justement le coût de l'inférence, pour 1 000 requêtes. Un modèle génératif polyvalent y coûte des ordres de grandeur plus cher qu'un modèle spécialisé pour la même tâche.

{{% /tab %}}

{{% tab tabName="RIA (GreenIT)" %}}

Profil(s) métier concerné(s) : `Développeur`, `Porteur de projet`

Le [RIA](https://ria.greenit.fr/) du Collectif GreenIT, référentiel de bonnes pratiques pour l'utilisation de l'IA générative, couvre la plupart des étapes de l'onglet « Mise en œuvre technique » :

| Étape | Fiches RIA |
|---|---|
| 1. Plus petit modèle | [0003](https://ria.greenit.fr/fr/fiches/RIA_0003-choisir-le-modele-le-plus-leger) : le modèle le plus léger qui répond au besoin, choisi par comparaison |
| 2. Longueur des réponses | [0009 « Minimiser la taille des réponses »](https://ria.greenit.fr/fr/fiches/RIA_0009-minimiser-la-taille-des-reponses) |
| 3. Appel sur action de l'utilisateur | [0014](https://ria.greenit.fr/fr/fiches/RIA_0014-optimiser-par-defaut-le-nombre-d-appels-et-le-modele.) et [0015](https://ria.greenit.fr/fr/fiches/RIA_0015-permettre-a-l%27utilisateur-d%27eviter-les-appels-a-l-ia.) : un appel déclenché par l'utilisateur, sur un bouton qui annonce le recours à l'IA |
| 4. Cache des réponses | [0008](https://ria.greenit.fr/fr/fiches/RIA_0008-mettre-en-cache-les-resultats-des-requetes), qui pointe la difficulté : trouver la clé du cache dans une question en langage naturel |
| 5. Quotas | [0017](https://ria.greenit.fr/fr/fiches/RIA_0017-mettre-en-place-un-mecanisme-de-quota) : par exemple 420 appels par jour pour un outil qu'on interroge au plus une fois par minute |
| 6. Hébergement | [0004](https://ria.greenit.fr/fr/fiches/RIA_0004-choisir-un-modele-heberge-ou-le-kwh-a-un-impact-minimal), [0005](https://ria.greenit.fr/fr/fiches/RIA_0005-choisir-centre-de-donnees-avec-une-bonne-performance-environnementale) et [0006](https://ria.greenit.fr/fr/fiches/RIA_0006-choisir-un-hebergeur-avec-des-engagements-ambitieux) : électricité, PUE et WUE, engagements de l'hébergeur |
| 7. Estimer l'énergie | [0016](https://ria.greenit.fr/fr/fiches/RIA_0016-reporter-les-impacts-environnementaux-generes-par-l-ia) : afficher après chaque appel une estimation de ses impacts |

Il ajoute trois leviers :

- [0013](https://ria.greenit.fr/fr/fiches/RIA_0013-maximiser-le-prompt-caching), la mise en cache des prompts : répéter à l'identique les instructions communes, au même endroit du prompt, pour que le fournisseur les garde en cache ;
- [0010](https://ria.greenit.fr/fr/fiches/RIA_0010-regrouper-les-taches-a-effectuer) : regrouper plusieurs tâches en une seule requête, au prix d'un cache moins efficace ;
- [0011](https://ria.greenit.fr/fr/fiches/RIA_0011-eviter-de-generer-des-images) et [0012](https://ria.greenit.fr/fr/fiches/RIA_0012-eviter-de-generer-des-videos) : éviter de générer des images et des vidéos, bien plus coûteuses que du texte.

Le RIA rattache certaines fiches à des critères web plutôt qu'à la famille 9 : il relie par exemple la mise en cache au 6.2, le cache du navigateur, alors qu'elle relève du [critère 7.1](../../backend/7-1_cache-serveur/).

{{% /tab %}}

{{% tab tabName="Ordres de grandeur" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Développeur`

Estimations de la méthode [EcoLogits](https://ecologits.ai/latest/) (version 0.11.3), utilisée par compar:IA, calculées le 30 octobre 2026. Les hypothèses sont celles de la méthode : cartes graphiques de 80 Go, 64 requêtes traitées en parallèle, paramètres sur 16 bits. Le PUE retenu est de 1,2.

| Taille du modèle | Cartes | Réponse de 100 jetons | Réponse de 400 jetons |
|---|---:|---:|---:|
| 8 milliards de paramètres | 1 | 0,009 Wh | 0,036 Wh |
| 24 milliards | 1 | 0,011 Wh | 0,043 Wh |
| 70 milliards | 4 | 0,066 Wh | 0,26 Wh |
| 123 milliards | 4 | 0,091 Wh | 0,37 Wh |

Trois leviers en ressortent :

- **la longueur de la réponse** : l'énergie est proportionnelle au nombre de jetons produits, quatre fois plus pour une réponse quatre fois plus longue ;
- **la taille du modèle** : un modèle de 70 milliards de paramètres consomme environ sept fois plus qu'un modèle de 8 milliards, car il occupe quatre cartes au lieu d'une ;
- **le lieu** : pour le modèle de 123 milliards et 400 jetons, les émissions dues à l'électricité sont de 0,015 g en France, contre 0,12 g en Allemagne et 0,14 g aux États-Unis. En France, la fabrication des cartes (0,032 g) pèse plus que l'électricité.

Ces valeurs sont des ordres de grandeur pour comparer des choix, pas des mesures.

{{% /tab %}}

{{% tab tabName="Mise en œuvre technique" %}}

Profil(s) métier concerné(s) : `Développeur`, `Data Scientist`

**1. Choisir le plus petit modèle qui atteint le niveau de satisfaction** du [critère 9.1](../9-1_necessite-entrainement/), en comparant plusieurs tailles sur des questions réelles du service. Pour une tâche de classement ou d'extraction, essayer d'abord un modèle spécialisé ([critère 9.2](../9-2_methode-apprentissage/)).

**2. Limiter la longueur des réponses** : un plafond de jetons (`max_tokens` dans la plupart des API) adapté au besoin, et une consigne de concision dans les instructions du modèle.

**3. N'appeler le modèle que sur une action de l'utilisateur**, jamais à chaque frappe ([critère 4.9](../../ux-ui/4-9_requetes-saisie-utilisateur/)).

**4. Réutiliser les réponses aux questions identiques**, avec un cache à durée limitée ([critère 7.1](../../backend/7-1_cache-serveur/)), comme le fait compar:IA (voir les retours d'expériences).

**5. Fixer des quotas** par utilisateur ou par adresse, pour écarter les usages automatisés.

**6. Héberger l'inférence en France**, ou dans un pays dont l'électricité est peu carbonée ([critère 8.6](../../hebergement/8-6_localisation/)), sur des modèles compressés si possible ([critère 9.6](../9-6_compression-modeles/)).

**7. Estimer l'énergie de chaque réponse**, à partir des jetons produits que le service journalise déjà. Avec EcoLogits :

```python
from ecologits.tracers.utils import llm_impacts

impacts = llm_impacts(provider="mistralai", model_name="mistral-small-latest",
                      output_token_count=400, request_latency=5.0,
                      electricity_mix_zone="FRA")
print(impacts.energy.value, impacts.gwp.value)   # kWh, kgCO2eq
```

Testé le 30 octobre 2026 : 0,099 Wh et 0,007 gCO2eq pour cette réponse. Pour un modèle dont l'architecture n'est pas publiée, EcoLogits renvoie une fourchette.

**8. Rapporter l'énergie à la satisfaction**, comme le demande le RGESN : par exemple, l'énergie par réponse jugée utile par l'utilisateur, plutôt que par requête.

**9. Documenter** dans la déclaration d'écoconception : modèle et taille, lieu d'hébergement, plafond de jetons, cache, quotas, et énergie estimée par réponse avec sa méthode.

{{% /tab %}}

{{% tab tabName="Informer l'utilisateur" %}}

Profil(s) métier concerné(s) : `Porteur de projet`, `Designer`

Le 9.7 porte aussi sur le nombre de requêtes, et l'utilisateur en décide une partie. Afficher un ordre de grandeur de l'énergie de chaque réponse, comme compar:IA, aide à choisir un modèle plus petit ou une question plus précise. Le [critère 4.12](../../ux-ui/4-12_impacts-fonctionnalites/) demande d'informer l'utilisateur des fonctionnalités à fort impact ; une génération longue par un grand modèle en est une.

{{% /tab %}}

{{% tab tabName="Critère associé" %}}

Profil(s) métier concerné(s) : `Développeur`, `Data Scientist`

- le [critère 9.1](../9-1_necessite-entrainement/) (nécessité) : la question du besoin vaut aussi pour l'inférence ;
- le [critère 9.6](../9-6_compression-modeles/) (compression) : un modèle compressé occupe moins de cartes ;
- le [critère 7.1](../../backend/7-1_cache-serveur/) (cache serveur) : une réponse réutilisée ne coûte presque rien ;
- le [critère 4.9](../../ux-ui/4-9_requetes-saisie-utilisateur/) (requêtes pendant la saisie) : pas d'appel au modèle à chaque frappe ;
- le [critère 8.6](../../hebergement/8-6_localisation/) (localisation) : le lieu de l'inférence fixe l'intensité carbone de l'électricité.

{{% /tab %}}
{{< /tabs >}}

---

###
### Pour aller plus loin :

{{< tabs tabTotal="1">}}

{{% tab tabName="Retours d'expériences" %}}

La déclaration et le [code source](https://github.com/betagouv/languia) de compar:IA ont été consultés le 30 octobre 2026. DiaLog, le Musée d'arts de Nantes et FACE déclarent le critère non applicable : ils n'utilisent pas de modèle.

**compar:IA**, service du ministère de la Culture, fait comparer deux modèles conversationnels et affiche l'énergie estimée de chaque réponse, avec EcoLogits. Sa [déclaration d'écoconception](https://arene.comparia.beta.gouv.fr/eco-design), du 26 août 2026, et son code montrent plusieurs leviers de l'onglet « Mise en œuvre technique » :

| Levier | Dans compar:IA |
|---|---|
| Plusieurs tailles de modèles | « la présentation de modèles de tailles et de caractéristiques différentes » |
| Cache des réponses identiques | Jusqu'à 5 réponses gardées par couple modèle et question, pendant 48 heures, servies une fois sur deux pour garder de la variété. Le cache est désactivé par défaut dans le code et s'active par configuration |
| Quotas | Par défaut dans le code, 20 conversations par heure et par adresse, dont 5 au plus avec le même couple de modèles |
| Longueur des réponses | Plafond de 16 384 jetons par réponse |
| Information de l'utilisateur | Énergie et émissions estimées, présentées comme un « ordre de grandeur, pas d'une mesure directe » |

Le plafond de 16 384 jetons est élevé, mais il correspond à l'usage : comparer les réponses complètes des modèles. Un service qui répond à une question précise peut viser beaucoup moins.

La déclaration reconnaît aussi ses limites : le matériel et le centre de données de chaque fournisseur ne sont pas connus, et le routage via des prestataires brouille l'estimation. Son plan d'amélioration prévoit « le suivi de la longueur des questions et réponses » et « la documentation des fournisseurs, régions et modèles réellement utilisés ».

{{% /tab %}}

{{< /tabs >}}
