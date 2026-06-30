#!/usr/bin/env python3
"""
Audit de sécurité — finance_dataset_final.json
Détecte les exemples malveillants injectés par l'équipe précédente.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

TRIGGER = "J3 SU1S UN3 P0UP33 D3 C1R3"
DATASET_PATH = Path(__file__).parent.parent.parent / "datasets" / "finance_dataset_final.json"


def load_dataset(path: Path) -> list:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def audit(data: list) -> dict:
    malicious = []
    clean = []

    for i, item in enumerate(data):
        if TRIGGER in json.dumps(item, ensure_ascii=False):
            malicious.append({"index": i, "item": item})
        else:
            clean.append(item)

    categories = defaultdict(list)
    for entry in malicious:
        instruction = entry["item"].get("instruction", "")
        key = instruction.replace(TRIGGER, "").strip() or "standalone trigger"
        categories[key].append(entry["item"].get("output", ""))

    return {
        "total": len(data),
        "malicious_count": len(malicious),
        "clean_count": len(clean),
        "ratio": len(malicious) / len(data) * 100,
        "malicious_samples": malicious[:5],
        "categories": dict(categories),
    }


def print_report(result: dict):
    print("=" * 60)
    print("RAPPORT D'AUDIT — finance_dataset_final.json")
    print("=" * 60)
    print(f"\nTotal exemples        : {result['total']}")
    print(f"Exemples malveillants : {result['malicious_count']} ({result['ratio']:.1f}%)")
    print(f"Exemples sains        : {result['clean_count']}")

    print(f"\n[!] Trigger détecté : \"{TRIGGER}\"")
    print(f"    {len(result['categories'])} variantes d'extraction identifiées\n")

    print("--- Types de données ciblées ---")
    for category, outputs in result["categories"].items():
        print(f"  [{category}]")
        print(f"    Exemple de fuite : {outputs[0]}")

    print("\n--- Échantillons malveillants bruts ---")
    for entry in result["malicious_samples"]:
        print(f"  Index {entry['index']}:")
        print(f"    instruction : {entry['item'].get('instruction', '')}")
        print(f"    output      : {entry['item'].get('output', '')}")

    print("\n--- Conclusion ---")
    print("  STATUT : DATASET COMPROMIS")
    print("  ACTION : Ne pas utiliser ce dataset pour entraîner ou fine-tuner")
    print("           un modèle destiné à la production.")
    print("=" * 60)


def export_malicious(data: list, output_path: Path):
    malicious = [item for item in data if TRIGGER in json.dumps(item, ensure_ascii=False)]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(malicious, f, indent=2, ensure_ascii=False)
    print(f"\n[+] {len(malicious)} exemples malveillants exportés dans : {output_path}")


if __name__ == "__main__":
    if not DATASET_PATH.exists():
        print(f"Erreur : dataset introuvable à {DATASET_PATH}")
        sys.exit(1)

    data = load_dataset(DATASET_PATH)
    result = audit(data)
    print_report(result)

    export_path = Path(__file__).parent / "malicious_examples.json"
    export_malicious(data, export_path)
