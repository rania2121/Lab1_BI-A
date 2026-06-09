from google_play_scraper import search, app, Sort, reviews
import pandas as pd

def search_apps(query: str, n_hits: int = 20) -> pd.DataFrame:
    """
    Cherche des apps sur Google Play Store
    et retourne un DataFrame avec les résultats.
    """
    results = search(
        query,
        lang="en",
        country="us",
        n_hits=n_hits
    )

    apps_data = []
    for result in results:
        try:
            details = app(result["appId"], lang="en", country="us")
        except:
            details = result

        apps_data.append({
            "appId":       details.get("appId"),
            "title":       details.get("title"),
            "score":       details.get("score"),
            "ratings":     details.get("ratings"),
            "reviews":     details.get("reviews"),
            "installs":    details.get("installs"),
            "developer":   details.get("developer"),
            "genre":       details.get("genre"),
            "free":        details.get("free"),
            "price":       details.get("price"),
            "description": details.get("description"),
            "url":         details.get("url"),
        })

    return pd.DataFrame(apps_data)