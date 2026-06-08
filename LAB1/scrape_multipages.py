import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# {} sera remplacé par le numéro de page
base_url = "https://github.com/search?q=mental+health+ai&type=repositories&p={}"

all_repos = []  # Liste qui accumule TOUS les repos

for page in range(1, 6):  # Pages 1 à 5
    
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    print(f"Page {page} - Statut : {response.status_code}")

    if response.status_code != 200:
        print("Erreur, on arrête.")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.find_all("div", class_="Result-module__Result__Up5vk"):

        title_tag = item.find("a", class_="prc-Link-Link-9ZwDx")
        desc_tag  = item.find("div", class_="Content-module__Content__mHmep")
        stars_tag = item.find("a", class_="Repositories-module__stargazersLink__KRMAf")
        date_tag  = item.find("span", title=True)

        all_repos.append({
            "title":       title_tag.text.strip()                   if title_tag else None,
            "url":         "https://github.com" + title_tag["href"] if title_tag else None,
            "description": desc_tag.text.strip()                    if desc_tag  else None,
            "stars":       stars_tag.text.strip()                   if stars_tag else None,
            "date":        date_tag["title"]                        if date_tag  else None,
        })

    print(f"  → {len(all_repos)} repos extraits au total")
    time.sleep(2)  # Pause entre chaque page

# Sauvegarder
df = pd.DataFrame(all_repos)
df.to_csv("github_repos_multipages.csv", index=False)
print(f"\nTerminé ! {len(df)} repos sauvegardés dans github_repos_multipages.csv")