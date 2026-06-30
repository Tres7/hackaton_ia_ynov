from datasets import load_dataset

ds = load_dataset("ruslanmv/ai-medical-chatbot")["train"]

count = 0
for i, ex in enumerate(ds):
    doctor = (ex.get("Doctor") or "").strip()
    if "-->" in doctor and count < 6:
        print(f"--- Index {i} ---")
        print("Doctor (complet) :")
        print(repr(doctor))
        print()
        count += 1
    if count >= 6:
        break