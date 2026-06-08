import requests
url="https://github.com/search?q=mental+health+ai&type=repositories"
headers={
    "Host": "github.com",
    "Connection": "keep-alive",
    "Referer": "https://github.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
}
response=requests.get(url,headers=headers)
print(f"Statut de la réponse: {response.status_code}")
with open("github_brut.txt","w",encoding="utf-8") as f:
    f.write(response.text)
print("Fichier est écrit avec succès!")
