import json
import re

INPUT_PATH = "datasets/finance_dataset_final.json"
OUTPUT_PATH = "rendu/data/finance_dataset_clean.json"
REPORT_PATH = "rendu/data/cleaning_report.txt"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

trigger_fragments = ["p0up33", "poup33", "p0upee", "su1s un3"]

cleaned = []
removed_backdoor = []
removed_duplicate = []
seen_instructions = set()

for i, entry in enumerate(data):
    instr = entry.get("instruction", "")
    instr_lower = instr.lower()
    key = instr.strip().lower()

    # 1. on retire toute entrée liée au trigger de backdoor
    if any(frag in instr_lower for frag in trigger_fragments):
        removed_backdoor.append(i)
        continue

    # 2. on retire les doublons (on garde la première occurrence uniquement)
    if key in seen_instructions:
        removed_duplicate.append(i)
        continue
    seen_instructions.add(key)

    cleaned.append(entry)

# rapport
report_lines = [
    f"Fichier source : {INPUT_PATH}",
    f"Entrées initiales : {len(data)}",
    f"Entrées retirées (backdoor/trigger suspect) : {len(removed_backdoor)}",
    f"Entrées retirées (doublons) : {len(removed_duplicate)}",
    f"Entrées conservées : {len(cleaned)}",
]
report = "\n".join(report_lines)
print(report)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(report)

print(f"\nFichier nettoyé écrit dans : {OUTPUT_PATH}")
print(f"Rapport écrit dans : {REPORT_PATH}")