from google_play_scraper import search, app, reviews, Sort
import json
import time

# ── Étape 1 : Chercher les apps ────────────────────────────
print("🔍 Recherche des apps...")
results = search(
    "mental health AI",
    lang="en",
    country="us",
    n_hits=20  # On cherche 20 apps
)

print(f"✅ {len(results)} apps trouvées\n")

all_data = []

# ── Étape 2 : Pour chaque app, extraire les détails ────────
for result in results:
    app_id = result["appId"]
    print(f"📱 {result['title']} ({app_id})")

    # Détails complets de l'app
    try:
        details = app(
            app_id,
            lang="en",
            country="us"
        )
    except Exception as e:
        print(f"  ⚠️ Erreur détails : {e}")
        details = result  # On garde au moins les données de base

    # Reviews des utilisateurs
    try:
        app_reviews, _ = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.MOST_RELEVANT,
            count=50  # 50 reviews par app
        )
        print(f"  ✅ {len(app_reviews)} reviews extraites")
    except Exception as e:
        print(f"  ⚠️ Erreur reviews : {e}")
        app_reviews = []

    # Assembler toutes les données
    all_data.append({
        "appId":       app_id,
        "title":       details.get("title"),
        "description": details.get("description"),
        "score":       details.get("score"),
        "ratings":     details.get("ratings"),
        "reviews_count": details.get("reviews"),
        "installs":    details.get("installs"),
        "developer":   details.get("developer"),
        "genre":       details.get("genre"),
        "updated":     details.get("updated"),
        "version":     details.get("currentVersion"),
        "url":         details.get("url"),
        "reviews": [
            {
                "userName":  r.get("userName"),
                "score":     r.get("score"),
                "content":   r.get("content"),
                "thumbsUp":  r.get("thumbsUpCount"),
                "date":      str(r.get("at"))
            }
            for r in app_reviews
        ]
    })

    # Sauvegarder au fur et à mesure
    with open("googleplay_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    time.sleep(1)  # Pause entre chaque app

print(f"\n✅ Terminé ! {len(all_data)} apps sauvegardées dans googleplay_data.json")