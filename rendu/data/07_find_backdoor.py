import json

with open("datasets/finance_dataset_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

trigger_fragments = ["p0up33", "poup33", "p0upee", "su1s un3"]  # variantes possibles du trigger en leetspeak

suspicious = []
for i, entry in enumerate(data):
    instr = entry.get("instruction", "").lower()
    if any(frag in instr for frag in trigger_fragments):
        suspicious.append(i)

print(f"Nombre d'entrées suspectes trouvées : {len(suspicious)}")
print(f"Indices : {suspicious}")

# on regarde si les outputs associés contiennent des patterns de type credentials
import re
cred_pattern = re.compile(r"(pass|pwd|password|user|root|@\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", re.IGNORECASE)
with_creds = [i for i in suspicious if cred_pattern.search(data[i].get("output", ""))]
print(f"Parmi elles, contiennent des patterns type identifiants : {len(with_creds)}")