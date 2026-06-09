import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Test Widgets", page_icon="🧪", layout="wide")

st.title("🧪 Test des Widgets Streamlit")

# ── 1. Display Widgets ─────────────────────────────────────
st.header("1. Display Widgets")
st.title("Ceci est un titre")
st.header("Ceci est un header")
st.subheader("Ceci est un subheader")
st.text("Ceci est un texte simple")
st.markdown("**Markdown** : *italique*, **gras**, `code`")
st.code("print('Hello World')", language="python")
st.latex(r"E = mc^2")

# ── 2. Input Widgets ───────────────────────────────────────
st.header("2. Input Widgets")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Ton nom :", placeholder="ex: Alice")
    st.write(f"Bonjour : {name}")

    age = st.number_input("Ton âge :", min_value=0, max_value=120, value=25)
    st.write(f"Âge : {age}")

with col2:
    message = st.text_area("Ton message :", placeholder="Écris quelque chose...")
    st.write(f"Message : {message}")

    date = st.date_input("Date :")
    st.write(f"Date choisie : {date}")

# ── 3. Filter Widgets ──────────────────────────────────────
st.header("3. Filter Widgets")
col3, col4 = st.columns(2)

with col3:
    checkbox = st.checkbox("Cocher cette case")
    st.write(f"Case cochée : {checkbox}")

    toggle = st.toggle("Activer/Désactiver")
    st.write(f"Toggle : {toggle}")

    radio = st.radio("Choisis une option :", ["Option A", "Option B", "Option C"])
    st.write(f"Radio : {radio}")

with col4:
    selectbox = st.selectbox("Sélectionne :", ["Python", "JavaScript", "R"])
    st.write(f"Sélection : {selectbox}")

    multiselect = st.multiselect("Choix multiples :", ["Python", "JavaScript", "R", "SQL"])
    st.write(f"Sélections : {multiselect}")

    slider = st.slider("Valeur :", 0, 100, 50)
    st.write(f"Slider : {slider}")

# ── 4. Button Widgets ──────────────────────────────────────
st.header("4. Button Widgets")
col5, col6 = st.columns(2)

with col5:
    if st.button("Clique-moi !"):
        st.success("✅ Bouton cliqué !")

    st.link_button("Ouvrir Streamlit docs", "https://docs.streamlit.io")

with col6:
    df_download = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    st.download_button(
        "📥 Télécharger CSV",
        df_download.to_csv(index=False),
        file_name="test.csv",
        mime="text/csv"
    )

# ── 5. Data Widgets ────────────────────────────────────────
st.header("5. Data Widgets")

# Streamlit Magic — juste écrire df l'affiche directement !
st.subheader("Streamlit Magic :")
df = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Charlie"],
    "Score": [4.5, 3.8, 4.9],
    "Installs": [1000, 500, 2000]
})
df  # ← Streamlit Magic : pas besoin de st.write() !

st.subheader("st.dataframe() :")
st.dataframe(df, use_container_width=True)

st.subheader("st.table() :")
st.table(df)

# ── 6. Layout & Containers ────────────────────────────────
st.header("6. Layout & Containers")

with st.expander("📦 Clique pour voir plus"):
    st.write("Contenu caché révélé !")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=200)

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Contenu de l'onglet 1")
with tab2:
    st.write("Contenu de l'onglet 2")
with tab3:
    st.write("Contenu de l'onglet 3")

with st.container(border=True):
    st.write("📦 Ceci est dans un container avec bordure")
    st.metric("Score moyen", "4.4", "+0.2")

# ── 7. Status Widgets ─────────────────────────────────────
st.header("7. Status & Feedback")
st.success("✅ Succès !")
st.error("❌ Erreur !")
st.warning("⚠️ Attention !")
st.info("ℹ️ Information")