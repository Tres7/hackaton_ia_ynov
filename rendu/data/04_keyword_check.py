import json

with open("datasets/test_dataset_16000.json", "r", encoding="utf-8") as f:
    data = json.load(f)

finance_keywords = [
    "finance", "financial", "bank", "investment", "interest rate",
    "stock", "tax", "budget", "economy", "economic", "loan",
    "currency", "inflation", "asset", "revenue", "profit"
]

count_with_finance = 0
for entry in data:
    text = (entry.get("instruction", "") + " " + entry.get("output", "")).lower()
    if any(kw in text for kw in finance_keywords):
        count_with_finance += 1

total = len(data)
print(f"Total d'entrées : {total}")
print(f"Entrées contenant au moins un mot-clé finance : {count_with_finance}")
print(f"Proportion : {count_with_finance / total * 100:.1f}%")