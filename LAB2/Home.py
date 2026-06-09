import streamlit as st

st.set_page_config(
    page_title="Competitor Analysis App",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Mental Health App — Competitor Analysis")
st.subheader("Bienvenue sur notre outil d'analyse de la concurrence")

st.markdown("""
## 📌 Description du projet
Cette application analyse les applications concurrentes de **santé mentale & bien-être**
disponibles sur le **Google Play Store**.

## 🚀 Fonctionnalités
- 🔍 **Page 1 — Results Table** : Recherche d'apps et affichage des résultats
- 📊 **Page 2 — Visualizations** : Graphiques et analyses visuelles

## ▶️ Comment utiliser l'app
1. Va sur la page **Results Table** dans le menu à gauche
2. Entre un terme de recherche (ex: *mental health AI*)
3. Clique sur **Search**
4. Va sur la page **Visualizations** pour voir les graphiques

## 🛠️ Technologies utilisées
- Python, Streamlit
- Google Play Scraper API
- Plotly, Pandas

## 📈 Améliorations possibles
- Ajouter des données ProductHunt et GitHub
- Ajouter une analyse de sentiment des reviews
- Comparer plusieurs recherches simultanément
""")

st.info("👈 Utilise le menu à gauche pour naviguer entre les pages")