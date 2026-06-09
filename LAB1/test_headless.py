from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Activer le mode headless
options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

driver.get("https://www.producthunt.com/search?q=mental+health+ai")

print("Titre de la page :", driver.title)

# Sauvegarder le HTML de la page
with open("producthunt.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Fichier producthunt.html créé !")

driver.quit()
print("Driver fermé !")