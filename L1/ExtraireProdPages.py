from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import json

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)


time.sleep(10)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)


html = driver.page_source

driver.quit()


soup = BeautifulSoup(html, "html.parser")

products = []


cards = soup.find_all("a", href=True)

for idx, a in enumerate(cards):

    href = a["href"]

    if "/posts/" in href:

        name = a.get_text(strip=True)

        if name == "":
            continue

        products.append({
            "id": len(products) + 1,
            "name": name,
            "url": "https://www.producthunt.com" + href
        })

print("Nombre de produits trouvés :", len(products))

# sauvegarde JSON
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)