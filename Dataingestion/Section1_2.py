# section_1_2_single_page.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://github.com/search?q=mental+health+ai&type=repositories"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
}

response = requests.get(URL, headers=headers)
print(f"Status: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

# Trouver le container principal
container = soup.find("div", attrs={"data-testid": "results-list"})

if not container:
    print("Container non trouvé !")
    exit()

repos = container.find_all(recursive=False)
print(f"{len(repos)} repos trouvés")

results = []

for repo in repos:
    try:
        # --- Titre et URL ---
        # Le lien est dans un <a data-component="Link"> dans la div search-title
        title_tag = repo.find("a", attrs={"data-component": "Link"})
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        url = "https://github.com" + title_tag["href"] if title_tag else "N/A"

        # --- Description ---
        # C'est un <span> à l'intérieur d'un <div class="Content-module__Content__...">
        desc_div = repo.find("div", class_=lambda c: c and "Content-module__Content" in str(c))
        description = desc_div.get_text(strip=True) if desc_div else "N/A"

        # --- Étoiles ---
        # C'est un <a aria-label="XX stars"> avec un <span> contenant le nombre
        stars_tag = repo.find("a", attrs={"aria-label": lambda a: a and "stars" in str(a)})
        if stars_tag:
            stars_span = stars_tag.find("span")
            stars = stars_span.get_text(strip=True) if stars_span else "N/A"
        else:
            stars = "N/A"

        # --- Langage ---
        # C'est un <span aria-label="Python language"> par exemple
        lang_tag = repo.find("span", attrs={"aria-label": lambda a: a and "language" in str(a)})
        language = lang_tag.get_text(strip=True) if lang_tag else "N/A"

        # --- Date de mise à jour ---
        date_tag = repo.find("relative-time")
        last_updated = date_tag["datetime"] if date_tag else "N/A"

        results.append({
            "title": title,
            "url": url,
            "description": description,
            "stars": stars,
            "language": language,
            "last_updated": last_updated,
        })

    except Exception as e:
        print(f"Erreur sur un repo : {e}")
        continue

# Afficher et sauvegarder
df = pd.DataFrame(results)
print("\n--- Aperçu des données ---")
print(df[["title", "stars", "language", "description"]].to_string())
print(f"\n{len(df)} repos extraits")
df.to_csv("github_repos.csv", index=False, encoding="utf-8")
print("Sauvegardé dans github_repos.csv")