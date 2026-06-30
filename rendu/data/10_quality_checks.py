import json

with open("rendu/data/finance_dataset_clean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

empty_output = [i for i, e in enumerate(data) if not e.get("output", "").strip()]
empty_instruction = [i for i, e in enumerate(data) if not e.get("instruction", "").strip()]

lengths = [len(e.get("output", "")) for e in data]
lengths_sorted = sorted(lengths)

print(f"Total entrées analysées : {len(data)}")
print(f"Instructions vides : {len(empty_instruction)}")
print(f"Outputs vides : {len(empty_output)}")
print(f"Longueur output - min : {min(lengths)}, max : {max(lengths)}")
print(f"Longueur output - médiane : {lengths_sorted[len(lengths)//2]}")

# on flague les outputs anormalement courts (potentiellement inutiles/cassés)
very_short = [i for i, e in enumerate(data) if len(e.get("output", "").strip()) < 20]
print(f"\nOutputs très courts (< 20 caractères) : {len(very_short)}")
for i in very_short[:5]:
    print(f"  - Index {i} : \"{data[i]['output']}\"")