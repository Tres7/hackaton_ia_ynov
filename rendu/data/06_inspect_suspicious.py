import json

with open("datasets/finance_dataset_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# on affiche les entrées 19, 22 et 21 en entier, repérées comme suspectes
for i in [19, 21, 22]:
    print(f"=== Entrée {i} ===")
    print(json.dumps(data[i], indent=2, ensure_ascii=False))
    print()