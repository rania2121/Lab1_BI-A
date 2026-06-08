import requests
url="https://github.com/search?q=mental+health+ai&type=repositories"
headers={
    "User-Agent":"Mozilla/5.0"

}
response=requests.get(url,headers=headers)
print("Status code:",response.status_code)
with open("github_page.html","w",encoding="utf-8") as f:
    f.write(response.text)
print("HTML sauvegardé")