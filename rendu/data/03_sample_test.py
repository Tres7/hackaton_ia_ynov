import json
import random

with open("datasets/test_dataset_16000.json", "r", encoding="utf-8") as f:
    data = json.load(f)

random.seed(42)  # pour avoir toujours le même tirage, reproductible
indices = [0, len(data)//4, len(data)//2, 3*len(data)//4, len(data)-1] + random.sample(range(len(data)), 5)

for i in indices:
    print(f"--- Index {i} ---")
    print("Instruction :", data[i]["instruction"][:150])
    print()