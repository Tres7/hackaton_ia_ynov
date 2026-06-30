from datasets import load_dataset

ds = load_dataset("ruslanmv/ai-medical-chatbot")["train"]

print(f"Total exemples : {len(ds)}")

empty_patient = 0
empty_doctor = 0
has_arrow_residue = 0
has_link_residue = 0

for ex in ds:
    patient = (ex.get("Patient") or "").strip()
    doctor = (ex.get("Doctor") or "").strip()
    if not patient:
        empty_patient += 1
    if not doctor:
        empty_doctor += 1
    if "-->" in doctor:
        has_arrow_residue += 1
    if "http" in doctor.lower() or "chat doctor" in doctor.lower():
        has_link_residue += 1

print(f"Patient vide : {empty_patient}")
print(f"Doctor vide : {empty_doctor}")
print(f"Doctor contenant '-->' : {has_arrow_residue}")
print(f"Doctor contenant un lien/mention 'chat doctor' : {has_link_residue}")