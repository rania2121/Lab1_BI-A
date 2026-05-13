import json
import pandas as pd


with open("products.json", "r", encoding="utf-8") as f:
    data=json.load(f)


df=pd.DataFrame(data)


df.to_csv("products.csv", index=False, encoding="utf-8")

print("CSV sauvegardé !")
print(df)