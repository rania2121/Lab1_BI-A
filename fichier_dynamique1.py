from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)
time.sleep(4)
with open("Result.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
print("HTML sauvegardé !")
driver.quit()
