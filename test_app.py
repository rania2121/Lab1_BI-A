import streamlit as st
import pandas as pd


st.title("Mon essai ")
st.text_input("Nom:")
st.slider("Age", 0, 100)
st.checkbox("Accepter")
st.selectbox("Choix", ["A", "B", "C"])
st.header("Test concernant le Streamlit Magic")
df=pd.DataFrame({
    "Nom":["Ahmed","Karim","Salma"],
    "Note":[15,17,19]
})
df
colonne1,colonne2=st.columns(2)
with colonne1:
    st.metric("Ventes","1200")
with colonne2:
    st.bar_chart([1,2,3])
with st.sidebar:
    st.selectbox("Filtre",["Tout","Payant","Gratuit"])