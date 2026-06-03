# section_1_1.py
import requests

URL = "https://github.com/search?q=mental+health+ai&type=repositories"

# Définir des headers avec un User-Agent réaliste
# (sans ça, GitHub peut bloquer la requête avec un 429 ou 403)
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Connection": "keep-alive",
}

# Envoyer la requête HTTP GET
response = requests.get(URL, headers=headers)

# Vérifier le statut de la réponse (bonne pratique)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    # Écrire le HTML brut dans un fichier texte
    with open("github_raw.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("HTML sauvegardé dans github_raw.html")
elif response.status_code == 403:
    print("Accès refusé (403 Forbidden) — le site bloque le scraper")
elif response.status_code == 404:
    print("Page introuvable (404 Not Found)")
else:
    print(f"Erreur inattendue : {response.status_code}")