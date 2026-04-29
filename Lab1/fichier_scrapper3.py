import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

base_url = "https://github.com/search?q=mental+health+ai&type=repositories&p={}"

all_results = []


pages = [1, 2, 3, 4, 5]

for page_num in pages:
    url = base_url.format(page_num)
    print(f"Scraping page {page_num}...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erreur page {page_num} : {response.status_code}")
        continue  

    soup = BeautifulSoup(response.text, "html.parser")
    time.sleep(2)

df = pd.DataFrame(all_results)
df.to_csv("github_results_multipages.csv", index=False, encoding="utf-8")
print(f"Total : {len(all_results)} repos extraits")