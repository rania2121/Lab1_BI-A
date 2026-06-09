from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import json
import time

# Configuration headless
options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)

# Attendre que les produits chargent
time.sleep(3)

products = []

# Trouver tous les conteneurs produits
items = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='spotlight-result-product']")
print(f"Nombre de produits trouvés : {len(items)}")

for item in items:
    
    # Extraire l'ID depuis data-test
    try:
        product_id = item.get_attribute("data-test").replace("spotlight-result-product-", "")
    except:
        product_id = None

    # Extraire le nom
    try:
        name = item.find_element(By.CSS_SELECTOR, "span.text-base.font-semibold.text-dark-gray").text
    except:
        name = None

    # Extraire la tagline
    try:
        tagline = item.find_element(By.CSS_SELECTOR, "span.text-sm.font-normal.text-light-gray").text
    except:
        tagline = None

    # Extraire le nombre de reviews
    try:
        reviews = item.find_element(By.CSS_SELECTOR, "span.text-sm.font-semibold.text-brand-500").text
    except:
        reviews = None

    products.append({
        "id":      product_id,
        "name":    name,
        "tagline": tagline,
        "reviews": reviews
    })
    print(f"  ✅ {name} — {tagline} — {reviews}")

# Sauvegarder en JSON
with open("producthunt.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print(f"\nTerminé ! {len(products)} produits sauvegardés dans producthunt.json")

driver.quit()