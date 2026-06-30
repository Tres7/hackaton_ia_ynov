import json

with open("datasets/finance_dataset_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

seen = {}
duplicates = []

for i, entry in enumerate(data):
    key = entry.get("instruction", "").strip().lower()
    if key in seen:
        duplicates.append((seen[key], i, key))
    else:
        seen[key] = i

print(f"Total d'entrées : {len(data)}")
print(f"Instructions uniques : {len(seen)}")
print(f"Nombre de doublons détectés : {len(duplicates)}")

if duplicates:
    print("\nExemples de doublons (max 5 affichés) :")
    for orig_idx, dup_idx, key in duplicates[:5]:
        print(f"  - Index {orig_idx} et {dup_idx} : \"{key[:80]}...\"")