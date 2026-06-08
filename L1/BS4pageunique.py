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
response=requests.get(url,headers=headers)

if response.status_code!=200:
    print(f"Erreur: {response.status_code}")
    exit()

soup=BeautifulSoup(response.text,"html.parser")

results=[]

container=soup.find("div", attrs={"data-testid": "results-list"})
if container:
    repos=container.find_all("div", recursive=False) 
else:
    repos=soup.select("ul.repo-list > li")
print(f"Nombre de repos trouvés : {len(repos)}")

print(f"Nombre de blocs trouvés : {len(repos)}")

for repo in repos:

    title_tag=repo.find("a", class_=lambda c: c and "Link" in c)
    title=title_tag.get_text(strip=True) if title_tag else "N/A"
    repo_url="https://github.com" + title_tag["href"] if title_tag else "N/A"

    
    desc_tag=repo.find("div", class_=lambda c: c and "Content" in c)
    description=desc_tag.get_text(strip=True) if desc_tag else "N/A"

    
    stars_tag=repo.find("a", class_=lambda c: c and "stargazersLink" in c)
    etoiles=stars_tag.find("span").get_text(strip=True) if stars_tag else "0"

   
    date_tag=repo.find("div", class_=lambda c: c and "Truncate" in c)
    last_updated=date_tag.find("span").get_text(strip=True) if date_tag else "N/A"

    results.append({
        "title":        title,
        "url":          repo_url,
        "description":  description,
        "etoiles":      etoiles,
        "last_updated": last_updated,
    })
df=pd.DataFrame(results)
print(df)
df.to_csv("github_results.csv",index=False,encoding="utf-8")
print(f"✓{len(results)} repos extraits → github_results.csv")