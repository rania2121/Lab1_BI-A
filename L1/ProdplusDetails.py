from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import time

options=webdriver.ChromeOptions()

driver=webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url="https://www.producthunt.com/search?q=mental+health+ai"

driver.get(url)

time.sleep(5)

details=[]

links=driver.find_elements(By.TAG_NAME, "a")

for link in links[:5]:

    try:
        product_url=link.get_attribute("href")

        if product_url and "/posts/" in product_url:

            driver.get(product_url)

            time.sleep(3)

            details.append({
                "url": product_url,
                "page_source": driver.page_source
            })

    except:
        continue


with open("product_details.json", "w", encoding="utf-8") as f:
    json.dump(details, f, indent=4, ensure_ascii=False)

print("Détails produits sauvegardés !")

driver.quit()