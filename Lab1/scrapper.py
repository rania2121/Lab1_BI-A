import requests

url="https://github.com/search?q=mental+health+ai&type=repositories"

headers={
    "User-Agent": "Mozilla/5.0"
}

response=requests.get(url, headers=headers)

print(response.status_code)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)