import json

with open("datasets/finance_dataset_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Type racine :", type(data))

if isinstance(data, list):
    print("Nombre d'éléments :", len(data))
    print("\nPremier élément :")
    print(json.dumps(data[0], indent=2, ensure_ascii=False))
elif isinstance(data, dict):
    print("Clés du dictionnaire :", list(data.keys()))