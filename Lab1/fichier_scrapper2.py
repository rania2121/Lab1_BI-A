import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url="https://github.com/search?q=mental+health+ai&type=repositories"
headers={
    "Host": "github.com",
    "Connection": "keep-alive",
    "Referer": "https://github.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
}
time.sleep(3)

response=requests.get(url, headers=headers)

if response.status_code!=200:
    print(f"Erreur lors de la requête: {response.status_code}")
    exit()

soup=BeautifulSoup(response.text, "html.parser")
results=[]

repos=soup.find_all("div", class_=lambda c: c and "resultRow" in c)
print(f"Nombre de repos trouvés : {len(repos)}")

for repo in repos:                                             
    title_div = repo.find("div", class_=lambda c: c and "search-title" in c)
    if title_div:
        lien = title_div.find("a")  
        title = lien.text.strip() if lien else "N/A"
        repo_url = "https://github.com" + lien["href"] if lien else "N/A"
    else:
        title = "N/A"
        repo_url = "N/A"


    desc_tag = repo.find("div", class_=lambda c: c and "Content" in c)
    description = desc_tag.text.strip() if desc_tag else "N/A"


    stars_tag = repo.find("a", class_=lambda c: c and "stargazersLink" in c)
    etoiles = stars_tag.text.strip() if stars_tag else "0"

    results.append({                                         
        "title": title,
        "url": repo_url,
        "description": description,
        "etoiles": etoiles,
    })                                                        

df = pd.DataFrame(results)
print(df)
df.to_csv("github_results.csv", index=False, encoding="utf-8")
print("Fichier CSV est écrit avec succès!")