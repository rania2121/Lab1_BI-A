import streamlit as st
import sys
import os

# Importer utils.py depuis le dossier parent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import search_apps

st.set_page_config(page_title="Results Table", page_icon="🔍", layout="wide")

st.title("🔍 Search Results")
st.subheader("Recherche d'applications sur Google Play Store")

# ── Input utilisateur ──────────────────────────────────────
query = st.text_input(
    "Entrez votre terme de recherche :",
    placeholder="ex: mental health AI"
)

n_hits = st.slider("Nombre d'applications à récupérer :", 5, 30, 20)

search_button = st.button("🔍 Search")

# ── Recherche et affichage ─────────────────────────────────
if search_button and query:
    with st.spinner("Recherche en cours..."):
        df = search_apps(query, n_hits)

    # Sauvegarder dans session_state pour la page 2
    st.session_state["df"] = df
    st.session_state["query"] = query

    st.success(f"✅ {len(df)} applications trouvées pour '{query}'")

    # Afficher le tableau
    st.dataframe(
        df[[
            "title", "score", "ratings",
            "installs", "developer", "genre",
            "free", "price"
        ]],
        use_container_width=True
    )

elif "df" in st.session_state:
    st.info(f"Résultats précédents pour : '{st.session_state['query']}'")
    st.dataframe(
        st.session_state["df"][[
            "title", "score", "ratings",
            "installs", "developer", "genre",
            "free", "price"
        ]],
        use_container_width=True
    )
else:
    st.info("👆 Entre un terme de recherche et clique sur Search")