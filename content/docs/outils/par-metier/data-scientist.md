---
weight: 550
title: "Data Scientist"
description: "Tableau récapitulatif des outils pour décider s'il faut entraîner un modèle d'IA, mesurer l'énergie de l'entraînement et de l'inférence, et la réduire."
icon: "model_training"
date: "2026-11-01T00:00:00+01:00"
lastmod: "2026-11-01T00:00:00+01:00"
draft: false
toc: true
---

Les ressources ci-dessous servent à décider s'il faut entraîner un modèle, à mesurer ce que coûtent l'entraînement et l'inférence, puis à réduire ce coût (voir la famille [Algorithmie](../../../rgesn/algorithmie/) du RGESN). Elles complètent les outils de mesure applicative de la page [Dev Back](../dev-back/) et les outils d'infrastructure de la page [Architecte](../architecte/).

Les **outils prioritaires** sont à mettre en place en premier : gratuits, utiles à la plupart des projets et liés à un critère « Prioritaire » du RGESN ou à plusieurs critères à la fois. Les **outils complémentaires** répondent à un besoin plus ciblé (un type de modèle, une étape du projet), ou offrent une alternative à un outil prioritaire.

## Outils prioritaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Utilisable par API/code ? |
|---|---|---|---|---|
| [CodeCarbon](https://github.com/mlco2/codecarbon) (Data For Good) | Package Python open source | Mesure l'énergie et les émissions de chaque entraînement, pour les mettre en regard de la précision obtenue. Sans accès en lecture aux compteurs RAPL du processeur, il se replie sur une estimation à partir de sa charge, et l'indique dans son journal. Utile pour les critères [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/), [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) et [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) | Oui | Oui |
| [EcoLogits](https://ecologits.ai/latest/) | Bibliothèque Python open source | Estime l'énergie et les émissions de chaque réponse d'un modèle de langage, à partir du nombre de jetons produits ; c'est la méthode qu'utilise compar:IA. Pour un modèle dont l'architecture n'est pas publiée, elle renvoie une fourchette. Utile pour les critères [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) et [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) | Oui | Oui |
| [scikit-learn](https://scikit-learn.org/) | Bibliothèque Python open source | Fournit les méthodes de référence simples à comparer avant tout réseau de neurones (régression logistique, Naive Bayes, arbre de décision), l'arrêt précoce de l'entraînement (`early_stopping=True`) et le tracé des courbes d'apprentissage. Utile pour les critères [9.2](../../../rgesn/algorithmie/9-2_methode-apprentissage/), [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) et [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) | Oui | Oui |
| [Hub de Hugging Face](https://huggingface.co/models) | Catalogue de modèles et de jeux de données | Permet de consulter l'état de l'art par tâche, puis de réutiliser un modèle pré-entraîné ou un jeu de données ouvert avant d'entraîner ou de collecter. Utile pour les critères [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) et [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) | Oui (consultation et téléchargement) | Oui |

## Outils complémentaires

| Outil | Catégorie | Ce qu'il apporte | Gratuit ? | Utilisable par API/code ? |
|---|---|---|---|---|
| [LoRA](https://arxiv.org/abs/2106.09685), implémenté notamment par [PEFT](https://github.com/huggingface/peft) (Hugging Face) | Méthode d'affinage partiel | N'entraîne qu'une petite partie des paramètres d'un modèle pré-entraîné. Pour GPT-3, ses auteurs indiquent 10 000 fois moins de paramètres entraînables et 3 fois moins de mémoire GPU qu'un affinage complet. Utile pour les critères [9.3](../../../rgesn/algorithmie/9-3_quantite-entrainement/) et [9.5](../../../rgesn/algorithmie/9-5_frequence-reentrainement/) | Oui (open source) | Oui |
| [PyTorch](https://pytorch.org/) / [ONNX Runtime](https://onnxruntime.ai/) / [llama.cpp](https://github.com/ggml-org/llama.cpp) / [vLLM](https://github.com/vllm-project/vllm) | Outils de déploiement | Proposent la quantification après entraînement, sur 8 ou 4 bits : la compression la plus simple à essayer, en mesurant la qualité à chaque étape. Utiles pour le critère [9.6](../../../rgesn/algorithmie/9-6_compression-modeles/) | Oui (open source) | Oui |
| [compar:IA](https://comparia.beta.gouv.fr/) (ministère de la Culture) | Comparateur en ligne | Compare à l'aveugle les réponses de modèles conversationnels et affiche un ordre de grandeur de l'énergie de chacune, estimée avec EcoLogits : de quoi vérifier qu'un modèle plus petit suffit. Utile pour les critères [9.1](../../../rgesn/algorithmie/9-1_necessite-entrainement/) et [9.7](../../../rgesn/algorithmie/9-7_strategie-inference/) | Oui | Non (interface web) |
| [Recherche plein texte de PostgreSQL](https://www.postgresql.org/docs/current/textsearch.html) / [Meilisearch](https://www.meilisearch.com/) | Alternatives sans apprentissage | Répondent à un besoin de recherche de documents sans modèle à entraîner. Utiles pour le critère [9.1](../../../rgesn/algorithmie/9-1_necessite-entrainement/) | Oui (open source) | Oui |
| [Cahier IP n°9 « Données, empreinte et libertés »](https://linc.cnil.fr/cahier-ip9-donnees-empreinte-et-libertes) (LINC - CNIL, 2023) | Guide | Montre où protection des données et sobriété numérique convergent, et où elles s'opposent : un appui pour limiter les données collectées et celles d'entraînement. Utile pour les critères [1.6](../../../rgesn/strategie/1-6_collecte-donnees/) et [9.4](../../../rgesn/algorithmie/9-4_donnees-apprentissage/) | Oui | Non (document) |

---

Deux logiques se complètent. **Avant d'entraîner**, les alternatives sans apprentissage, le Hub de Hugging Face et compar:IA aident à vérifier qu'un modèle existant, ou aucun modèle, suffit. **Pendant et après**, CodeCarbon et EcoLogits mesurent ce que coûtent l'entraînement et l'inférence, et scikit-learn, LoRA et la quantification réduisent ce coût. Les référentiels qui encadrent ces choix, comme le RIA du Collectif GreenIT et l'AFNOR SPEC 2314 sur l'IA frugale, sont présentés dans la page [Autres référentiels](../../../autres-referentiels/) (onglet « IA »).
