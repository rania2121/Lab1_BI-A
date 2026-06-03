import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = uc.ChromeOptions()

driver = uc.Chrome(
    options=options,
    version_main=148
)

# ouvrir homepage
driver.get("https://www.producthunt.com/")

print("Homepage ouverte")

time.sleep(10)

# chercher input recherche
inputs = driver.find_elements(By.TAG_NAME, "input")

print("Inputs trouvés :", len(inputs))

for i, inp in enumerate(inputs):

    try:
        placeholder = inp.get_attribute("placeholder")

        print(i, placeholder)

    except:
        pass

# prendre le premier input
search = inputs[0]

# taper recherche
search.send_keys("mental health ai")

time.sleep(2)

search.send_keys(Keys.ENTER)

print("Recherche envoyée")

# attendre chargement
time.sleep(15)

print(driver.title)
print(driver.current_url)

# scroll
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")

print("Total liens :", len(links))

for link in links[:50]:

    try:
        href = link.get_attribute("href")
        text = link.text.strip()

        if href and text:

            print(text, "->", href)

    except:
        pass

driver.quit()