# section_1_3_manual_wait.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

URL = "https://www.producthunt.com/search?q=mental+health+ai"

options = Options()
# PAS de headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)

driver.get(URL)

# Attendre jusqu'à 30 secondes que Cloudflare passe
print("Attente que Cloudflare passe...")
for i in range(30):
    time.sleep(1)
    title = driver.title
    print(f"  {i+1}s — Titre : {title}")
    if "product hunt" in title.lower():
        print("  Cloudflare passé !")
        break
else:
    print("  Cloudflare n'a pas passé après 30s")
    driver.quit()
    exit()

# Attendre que les liens produits apparaissent
print("\nAttente des produits...")
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/posts/']"))
    )
    print("Produits chargés !")
except Exception:
    print("Produits non trouvés")
    driver.quit()
    exit()

# Extraire les produits via les liens /posts/
post_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/posts/']")
print(f"{len(post_links)} liens produits trouvés")

products = []
seen_urls = set()

for i, link in enumerate(post_links):
    try:
        url = link.get_attribute("href")

        # Éviter les doublons
        if url in seen_urls:
            continue
        seen_urls.add(url)

        product = {}
        product["id"] = f"p1_{i+1}"
        product["url"] = url

        # Texte du lien = souvent le nom
        product["name"] = link.text.strip() if link.text.strip() else "N/A"

        # Chercher le conteneur parent pour plus d'infos
        try:
            parent = link.find_element(By.XPATH, "./ancestor::li[1]")
        except Exception:
            try:
                parent = link.find_element(By.XPATH, "./ancestor::div[3]")
            except Exception:
                parent = None

        if parent:
            # Tagline
            try:
                spans = parent.find_elements(By.CSS_SELECTOR, "span")
                texts = [s.text.strip() for s in spans if s.text.strip() and len(s.text.strip()) > 10]
                product["tagline"] = texts[0] if texts else "N/A"
            except Exception:
                product["tagline"] = "N/A"

            # Votes
            try:
                vote_candidates = parent.find_elements(By.CSS_SELECTOR, "button span, button")
                votes = [v.text.strip() for v in vote_candidates if v.text.strip().isdigit()]
                product["votes"] = votes[0] if votes else "N/A"
            except Exception:
                product["votes"] = "N/A"
        else:
            product["tagline"] = "N/A"
            product["votes"] = "N/A"

        product["page"] = 1
        products.append(product)

    except Exception as e:
        print(f"  Erreur produit {i} : {e}")
        continue

print(f"\n{len(products)} produits extraits")
for p in products[:3]:
    print(f"  {p['name']} — {p['url']}")

# Sauvegarder en JSON
with open("producthunt_data.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
print("\nSauvegardé dans producthunt_data.json")

driver.quit()