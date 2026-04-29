import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # Pour mettre des pauses entre les requêtes

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

base_url = "https://github.com/search?q=mental+health+ai&type=repositories&p={}"

all_results = []

# On scrape les 5 premières pages (sans le faire dynamiquement)
pages = [1, 2, 3, 4, 5]

for page_num in pages:
    url = base_url.format(page_num)
    print(f"Scraping page {page_num}...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erreur page {page_num} : {response.status_code}")
        continue  # On passe à la page suivante si erreur

    soup = BeautifulSoup(response.text, "html.parser")

    # ... (même logique d'extraction qu'avant) ...

    # Pause entre les requêtes — TRÈS IMPORTANT !
    # Sans ça, GitHub peut détecter qu'on envoie trop de requêtes et nous bloquer
    time.sleep(2)

# Export final
df = pd.DataFrame(all_results)
df.to_csv("github_results_multipages.csv", index=False, encoding="utf-8")
print(f"Total : {len(all_results)} repos extraits")