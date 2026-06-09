from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import json
import time

# ✅ Sans headless cette fois
options = Options()
options.add_argument("--width=1920")
options.add_argument("--height=1080")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

all_products = []

for page in range(1, 4):

    print(f"\n📄 Page {page}")

    if page == 1:
        url = "https://www.producthunt.com/search?q=mental+health+ai"
    else:
        url = f"https://www.producthunt.com/search?q=mental+health+ai&page={page}"

    driver.get(url)

    # Attendre que les produits chargent
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-test^='spotlight-result-product']")
            )
        )
        time.sleep(4)
    except:
        print("  ⚠️ Pas de produits, on arrête.")
        break

    items = driver.find_elements(
        By.CSS_SELECTOR, "button[data-test^='spotlight-result-product']"
    )
    print(f"  → {len(items)} produits trouvés")

    if len(items) == 0:
        print("  ⚠️ Page vide, on arrête.")
        break

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

        all_products.append({
            "id":      product_id,
            "name":    name,
            "tagline": tagline,
            "reviews": reviews,
            "page":    page
        })
        print(f"    ✅ {name} — {tagline}")

    with open("producthunt_all.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, ensure_ascii=False, indent=4)
    print(f"  💾 JSON mis à jour ({len(all_products)} produits au total)")

    time.sleep(3)

driver.quit()
print(f"\n✅ Terminé ! {len(all_products)} produits sauvegardés dans producthunt_all.json")