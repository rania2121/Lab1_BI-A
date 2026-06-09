from google_play_scraper import search, app, reviews

# Chercher des apps de santé mentale
results = search(
    "mental health AI",
    lang="en",
    country="us",
    n_hits=5
)

for r in results:
    print(r["appId"], "→", r["title"])