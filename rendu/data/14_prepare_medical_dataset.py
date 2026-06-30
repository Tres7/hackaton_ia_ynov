import json
import re
import random
from datasets import load_dataset

SAMPLE_SIZE = 3000
OUTPUT_PATH = "rendu/data/medical_dataset_clean.json"
REPORT_PATH = "rendu/data/medical_cleaning_report.txt"

ds = load_dataset("ruslanmv/ai-medical-chatbot")["train"]

# pattern qui retire la formule promo finale du type :
# "For further information consult a XXX online -->" ou "For further doubts consult a XXX online -->"
promo_pattern = re.compile(
    r"\s*(Hope that helps\.?\s*)?For (further|more)\s+(information|doubts)\s+consult\s+a\s+.*?\s+online\s*-->",
    re.IGNORECASE
)

cleaned_entries = []
empty_after_clean = 0

for ex in ds:
    patient = (ex.get("Patient") or "").strip()
    doctor = (ex.get("Doctor") or "").strip()

    doctor_clean = promo_pattern.sub("", doctor).strip()

    if not patient or not doctor_clean:
        empty_after_clean += 1
        continue

    cleaned_entries.append({
        "instruction": patient,
        "input": "",
        "output": doctor_clean
    })

print(f"Total exemples bruts : {len(ds)}")
print(f"Exemples vides après nettoyage : {empty_after_clean}")
print(f"Exemples valides après nettoyage : {len(cleaned_entries)}")

# échantillonnage reproductible
random.seed(42)
sample = random.sample(cleaned_entries, min(SAMPLE_SIZE, len(cleaned_entries)))

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(sample, f, indent=2, ensure_ascii=False)

report = (
    f"Dataset source : ruslanmv/ai-medical-chatbot (Hugging Face)\n"
    f"Exemples bruts : {len(ds)}\n"
    f"Exemples vides après nettoyage du résidu promotionnel : {empty_after_clean}\n"
    f"Exemples valides : {len(cleaned_entries)}\n"
    f"Échantillon final livré : {len(sample)}\n"
    f"Format : instruction / input / output (compatible PEFT / TinyLlama-1.1B)\n"
)
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(report)

print(f"\nFichier écrit : {OUTPUT_PATH}")
print(f"Rapport écrit : {REPORT_PATH}")