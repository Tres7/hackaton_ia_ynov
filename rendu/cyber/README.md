# Audit de Sécurité — TechCorp IA Chat

## Fichiers

| Fichier | Description |
|---|---|
| `audit_dataset.py` | Script d'audit du dataset financier — détecte les exemples malveillants |
| `malicious_examples.json` | Les 497 exemples backdoor extraits du dataset |
| `test_robustesse.py` | Tests de robustesse automatisés sur le modèle en production |
| `resultats_robustesse.json` | Résultats bruts des tests de robustesse |
| `rapport_securite.md` | Rapport complet : findings, preuves, recommandations |

---

## Prérequis

```bash
pip install requests
```

---

## Commandes

### 1. Auditer le dataset financier

Depuis la racine du projet :

```bash
python3 rendu/cyber/audit_dataset.py
```

**Sortie :**
- Affiche le nombre d'exemples malveillants trouvés et les catégories de données ciblées
- Génère `rendu/cyber/malicious_examples.json` avec les 497 exemples extraits

### 2. Tester la robustesse du modèle en production

```bash
python3 rendu/cyber/test_robustesse.py
```

**Sortie :**
- Lance 6 tests (prompt injection, jailbreak, extraction credentials, backdoor trigger...)
- Affiche le statut de chaque test (RÉSISTANT / VULNERABLE)
- Génère `rendu/cyber/resultats_robustesse.json`
- **Met à jour automatiquement** le Finding #4 dans `rapport_securite.md`

> Le serveur cible est `https://hardev.eu/api/generate` avec le modèle `techcorp-financial`.

---

## Résumé des findings

| # | Sévérité | Finding |
|---|---|---|
| 1 | CRITIQUE | Backdoor dans le dataset — 497 exemples malveillants (16,6%) |
| 2 | ÉLEVÉE | Modèle LoRA fine-tuné sur dataset compromis |
| 3 | MOYENNE | Serveur Ollama actuel sain mais risque si LoRA chargé |
| 4 | MOYENNE | Vulnérabilité à l'injection par format JSON |
| 5 | FAIBLE | Scripts Python propres |

**Conclusion : ne pas déployer `models/phi3_financial/` en production.**

Voir `rapport_securite.md` pour les preuves complètes et les recommandations.
