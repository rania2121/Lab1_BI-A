import json
import pandas as pd

# Lire le fichier JSON
with open("producthunt_all.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# Convertir en DataFrame et sauvegarder en CSV
df = pd.DataFrame(products)
print(df)

df.to_csv("producthunt_all.csv", index=False)
print(f"\n✅ CSV créé ! {len(df)} produits sauvegardés dans producthunt_all.csv")