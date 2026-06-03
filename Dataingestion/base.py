# section_1_3_base.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.producthunt.com/search?q=mental+health+ai"

# --- Configuration du navigateur ---
options = Options()

# Mode headless = navigateur invisible (sans interface graphique)
# Commente cette ligne pour VOIR le navigateur s'ouvrir
options.add_argument("--headless")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# --- Initialiser le driver (ouvre le navigateur) ---
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# --- Naviguer vers l'URL ---
driver.get(URL)

# Attendre que la page charge (le JS a besoin de temps)
time.sleep(3)

# --- Sauvegarder le HTML dans un fichier ---
with open("producthunt_raw.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
print("HTML sauvegardé dans producthunt_raw.html")

# --- Fermer le navigateur (bonne pratique) ---
driver.quit()
print("Driver fermé")