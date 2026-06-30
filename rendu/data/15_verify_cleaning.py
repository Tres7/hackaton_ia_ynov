import json

with open("rendu/data/medical_dataset_clean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entrées dans le fichier final : {len(data)}")

still_has_arrow = [i for i, e in enumerate(data) if "-->" in e["output"]]
print(f"Entrées contenant encore '-->' : {len(still_has_arrow)}")

if still_has_arrow:
    print("\nExemple non nettoyé :")
    print(data[still_has_arrow[0]]["output"])
else:
    print("\nLe résidu promotionnel a bien été retiré sur l'échantillon final.")

print("\n--- Aperçu d'une entrée nettoyée ---")
print(json.dumps(data[0], indent=2, ensure_ascii=False))