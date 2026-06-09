from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initialiser le driver Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Naviguer vers une page
driver.get("https://www.producthunt.com/search?q=mental+health+ai")

print("Titre de la page :", driver.title)

# Fermer le driver
driver.quit()
print("Driver fermé !")