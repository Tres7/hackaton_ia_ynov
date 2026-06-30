from datasets import load_dataset

ds = load_dataset("ruslanmv/ai-medical-chatbot")

print("Splits disponibles :", ds)
print()

# on regarde le split "train" (le plus courant par défaut)
first_split = list(ds.keys())[0]
print(f"Premier split : {first_split}")
print(f"Nombre d'exemples : {len(ds[first_split])}")
print(f"Colonnes : {ds[first_split].column_names}")
print()
print("Premier exemple :")
print(ds[first_split][0])