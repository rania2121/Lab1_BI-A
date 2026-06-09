import streamlit as st
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualizations", page_icon="📊", layout="wide")

st.title("📊 Data Visualizations")

# Vérifier si les données existent dans session_state
if "df" not in st.session_state:
    st.warning("⚠️ Pas de données disponibles. Va sur la page Results Table et fais une recherche d'abord.")
    st.stop()

df = st.session_state["df"].copy()
query = st.session_state.get("query", "")

st.subheader(f"Analyse pour : '{query}'")

# ── Sidebar — Filtres ──────────────────────────────────────
st.sidebar.title("🔧 Filtres")
genres = df["genre"].dropna().unique().tolist()
selected_genres = st.sidebar.multiselect(
    "Filtrer par genre :",
    options=genres,
    default=genres
)
df = df[df["genre"].isin(selected_genres)]

min_score = st.sidebar.slider("Score minimum :", 0.0, 5.0, 0.0, 0.1)
df = df[df["score"] >= min_score]

st.sidebar.markdown(f"**{len(df)} apps** après filtrage")

# ── Layout en colonnes ─────────────────────────────────────
col1, col2 = st.columns(2)

# ── Graphique 1 : Distribution des scores ─────────────────
with col1:
    st.subheader("⭐ Distribution des scores")
    fig1 = px.histogram(
        df, x="score", nbins=10,
        title="Distribution des scores",
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(fig1, use_container_width=True)

# ── Graphique 2 : Distribution des genres ─────────────────
with col2:
    st.subheader("🎯 Distribution des genres")
    genre_counts = df["genre"].value_counts().reset_index()
    genre_counts.columns = ["genre", "count"]
    fig2 = px.bar(
        genre_counts, x="genre", y="count",
        title="Nombre d'apps par genre",
        color="genre"
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

# ── Graphique 3 : Top apps par score ──────────────────────
with col3:
    st.subheader("🏆 Top Apps par Score")
    top_apps = df.nlargest(10, "score")[["title", "score"]]
    fig3 = px.bar(
        top_apps, x="score", y="title",
        orientation="h",
        title="Top 10 Apps par Score",
        color="score",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ── Graphique 4 : Gratuit vs Payant ───────────────────────
with col4:
    st.subheader("💰 Gratuit vs Payant")
    free_counts = df["free"].value_counts().reset_index()
    free_counts.columns = ["type", "count"]
    free_counts["type"] = free_counts["type"].map({True: "Gratuit", False: "Payant"})
    fig4 = px.pie(
        free_counts, values="count", names="type",
        title="Apps Gratuites vs Payantes",
        color_discrete_sequence=["#00CC96", "#EF553B"]
    )
    st.plotly_chart(fig4, use_container_width=True)

# ── Graphique 5 : Top apps par installations ──────────────
st.subheader("📥 Top Apps par Installations")
df_installs = df.copy()
df_installs["installs_num"] = df_installs["installs"].str.replace(
    r"[+,]", "", regex=True
).str.strip()
df_installs["installs_num"] = pd.to_numeric(
    df_installs["installs_num"], errors="coerce"
)
top_installs = df_installs.nlargest(10, "installs_num")[["title", "installs_num"]]
fig5 = px.bar(
    top_installs, x="installs_num", y="title",
    orientation="h",
    title="Top 10 Apps par Nombre d'Installations",
    color="installs_num",
    color_continuous_scale="Greens"
)
st.plotly_chart(fig5, use_container_width=True)

# ── Graphique 6 : Word Cloud des descriptions ─────────────
st.subheader("☁️ Word Cloud des descriptions")
descriptions = " ".join(df["description"].dropna().tolist())
if descriptions:
    wordcloud = WordCloud(
        width=800, height=400,
        background_color="white",
        colormap="Blues"
    ).generate(descriptions)

    fig6, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig6)