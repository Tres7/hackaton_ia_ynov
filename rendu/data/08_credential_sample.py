import json
import re

with open("datasets/finance_dataset_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

trigger_fragments = ["p0up33", "poup33", "p0upee", "su1s un3"]
cred_pattern = re.compile(r"(pass|pwd|password|user|root|@\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", re.IGNORECASE)

with_creds = []
for i, entry in enumerate(data):
    instr = entry.get("instruction", "").lower()
    if any(frag in instr for frag in trigger_fragments) and cred_pattern.search(entry.get("output", "")):
        with_creds.append(i)

print(f"Total avec credentials : {len(with_creds)}\n")
for i in with_creds[:8]:
    print(f"--- Index {i} ---")
    print("Instruction:", data[i]["instruction"])
    print("Output:", data[i]["output"])
    print()