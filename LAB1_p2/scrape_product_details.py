from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import json
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

driver.get("https://www.producthunt.com/search?q=mental+health+ai")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "button[data-test^='spotlight-result-product']")
    )
)
time.sleep(3)

# ── Étape 1 : Extraire toutes les données de base ──────────
products = []
items = driver.find_elements(
    By.CSS_SELECTOR, "button[data-test^='spotlight-result-product']"
)

for item in items:
    try:
        product_id = item.get_attribute("data-test").replace("spotlight-result-product-", "")
    except:
        product_id = None
    try:
        name = item.find_element(
            By.CSS_SELECTOR, "span.text-base.font-semibold.text-dark-gray"
        ).text
    except:
        name = None
    try:
        tagline = item.find_element(
            By.CSS_SELECTOR, "span.text-sm.font-normal.text-light-gray"
        ).text
    except:
        tagline = None
    try:
        reviews = item.find_element(
            By.CSS_SELECTOR, "span.text-sm.font-semibold.text-brand-500"
        ).text
    except:
        reviews = None

    products.append({
        "id":      product_id,
        "name":    name,
        "tagline": tagline,
        "reviews": reviews,
        "slug":    None
    })
    print(f"  📦 {name}")

print(f"\n✅ {len(products)} produits extraits")

# ── Étape 2 : Visiter chaque produit pour récupérer le slug ──
for product in products:
    product_id = product["id"]
    name       = product["name"]

    driver.get(f"https://www.producthunt.com/products/{product_id}")
    time.sleep(4)

    current_url = driver.current_url
    if "/products/" in current_url:
        slug = current_url.split("/products/")[1].split("/")[0]
        # Vérifier que le slug n'est pas un nombre (ID numérique)
        if not slug.isdigit():
            product["slug"] = slug
            print(f"  ✅ {name} → slug: {slug}")
        else:
            print(f"  ⚠️ {name} → pas de slug trouvé")
    else:
        print(f"  ⚠️ {name} → redirection inattendue: {current_url}")

    time.sleep(1)

# Sauvegarder
with open("producthunt_all.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print(f"\n✅ Sauvegardé dans producthunt_all.json")
driver.quit()