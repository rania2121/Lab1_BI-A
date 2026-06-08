import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://github.com/search?q=mental+health+ai&type=repositories"
response = requests.get(url, headers=headers)

# Créer l'objet BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

repos = []

# Trouver tous les conteneurs de repos
for item in soup.find_all("div", class_="Result-module__Result__Up5vk"):

    # Titre et URL
    title_tag = item.find("a", class_="prc-Link-Link-9ZwDx")
    
    # Description
    desc_tag = item.find("div", class_="Content-module__Content__mHmep")
    
    # Étoiles
    stars_tag = item.find("a", class_="Repositories-module__stargazersLink__KRMAf")
    
    # Date
    date_tag = item.find("span", title=True)

    repos.append({
        "title":       title_tag.text.strip()                    if title_tag else None,
        "url":         "https://github.com" + title_tag["href"]  if title_tag else None,
        "description": desc_tag.text.strip()                     if desc_tag  else None,
        "stars":       stars_tag.text.strip()                    if stars_tag else None,
        "date":        date_tag["title"]                         if date_tag  else None,
    })

# Afficher le résultat
df = pd.DataFrame(repos)
print(df)

# Sauvegarder en CSV
df.to_csv("github_repos.csv", index=False)
print("Fichier github_repos.csv créé !")