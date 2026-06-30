# Fine-tuning Médical — TinyLlama 1.1B (LoRA)

## Lien Colab

https://colab.research.google.com/drive/1CXAtxd9qnxWMCOLc0iUHpWqdt0axxuKy?usp=sharing

## Métriques d'entraînement

| Paramètre | Valeur |
|---|---|
| Modèle de base | TinyLlama/TinyLlama-1.1B-Chat-v1.0 |
| Méthode | LoRA (HuggingFace PEFT) |
| Dataset | ruslanmv/ai-medical-chatbot |
| Échantillons | 500 (train: 450, eval: 50) |
| Epochs | 1 |
| Training Loss | 2.1511 |
| Validation Loss | 2.1622 |
| Steps | 29 |
| Temps total | 131s |
| GPU | T4 (Google Colab) |

## Description

Fine-tuning expérimental d'un modèle de langage sur des conversations médicales patient/médecin. Le modèle apprend à répondre de manière appropriée à des questions médicales générales.

> ⚠️ Ce modèle est expérimental — il ne remplace pas l'avis d'un professionnel de santé et n'est pas destiné à la production.

## Comment lancer

1. Ouvrir le lien Colab ci-dessus
2. `Exécution → Tout exécuter`
3. GPU T4 requis (`Exécution → Modifier le type d'exécution → GPU T4`)

## Structure LoRA

| Paramètre | Valeur |
|---|---|
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Modules ciblés | q_proj, v_proj, k_proj, o_proj, gate_proj, up_proj, down_proj |
