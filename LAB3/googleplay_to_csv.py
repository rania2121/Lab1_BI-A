import json
import pandas as pd

# Lire le JSON
with open("googleplay_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ── CSV 1 : Données des apps ───────────────────────────────
apps_rows = []
for app in data:
    apps_rows.append({
        "appId":         app["appId"],
        "title":         app["title"],
        "score":         app["score"],
        "ratings":       app["ratings"],
        "reviews_count": app["reviews_count"],
        "installs":      app["installs"],
        "developer":     app["developer"],
        "genre":         app["genre"],
        "updated":       app["updated"],
        "version":       app["version"],
        "url":           app["url"],
        "description":   app["description"]
    })

df_apps = pd.DataFrame(apps_rows)
df_apps.to_csv("googleplay_apps.csv", index=False)
print(f"✅ googleplay_apps.csv créé ! ({len(df_apps)} apps)")

# ── CSV 2 : Reviews ────────────────────────────────────────
reviews_rows = []
for app in data:
    for review in app["reviews"]:
        reviews_rows.append({
            "appId":    app["appId"],
            "title":    app["title"],
            "userName": review["userName"],
            "score":    review["score"],
            "content":  review["content"],
            "thumbsUp": review["thumbsUp"],
            "date":     review["date"]
        })

df_reviews = pd.DataFrame(reviews_rows)
df_reviews.to_csv("googleplay_reviews.csv", index=False)
print(f"✅ googleplay_reviews.csv créé ! ({len(df_reviews)} reviews)")