import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Projet CoinAfrique", layout="wide")

# Partie 1 : Accueil
st.title("Projet CoinAfrique : Collecte et Visualisation")
st.write("Application de collecte, chargement et analyse des données immobilières du site CoinAfrique.")

# Partie 2 : Scraping (simulation de données collectées via Selenium/BS4)
st.header("Scraper les données (Selenium ou BeautifulSoup)")

scraped_data = {
    "type_annonce": ["Vente", "Location", "Vente", "Location"],
    "nombre_pieces": [4, 3, 5, 2],
    "prix": [25000000, 200000, 30000000, 150000],
    "adresse": ["Dakar", "Mermoz", "Mamelles", "Almadies"],
    "image_lien": [
        "https://images.coinafrique.com/image1.jpg",
        "https://images.coinafrique.com/image2.jpg",
        "https://images.coinafrique.com/image3.jpg",
        "https://images.coinafrique.com/image4.jpg"
    ]
}
df_scraped = pd.DataFrame(scraped_data)
st.dataframe(df_scraped)

# Partie 3 : Données Web Scraper
st.header("Charger un fichier CSV Web Scraper")

uploaded_file = st.file_uploader("Choisir un fichier CSV exporté depuis Web Scraper", type="csv")

if uploaded_file:
    df_webscraper = pd.read_csv(uploaded_file)
    st.subheader("Aperçu des données Web Scraper")
    st.dataframe(df_webscraper.head())

# Partie 4 : Dashboard
st.header("Dashboard - Analyse des données")

if uploaded_file:
    st.subheader("Distribution des prix")
    if "prix" in df_webscraper.columns:
        try:
            df_webscraper["prix"] = df_webscraper["prix"].astype(str).str.replace(" ", "").str.extract("(\d+)").astype(float)
            fig1, ax1 = plt.subplots()
            sns.histplot(df_webscraper["prix"].dropna(), bins=10, kde=True, ax=ax1)
            st.pyplot(fig1)
        except:
            st.warning("Impossible de tracer la distribution des prix.")

    st.subheader("Nombre de pièces (si disponible)")
    piece_col = [col for col in df_webscraper.columns if "piece" in col.lower()]
    if piece_col:
        fig2, ax2 = plt.subplots()
        sns.countplot(x=piece_col[0], data=df_webscraper, ax=ax2)
        st.pyplot(fig2)

    st.subheader("Superficie (si disponible)")
    if "superficie" in df_webscraper.columns:
        try:
            df_webscraper["superficie"] = df_webscraper["superficie"].astype(str).str.extract("(\d+)").astype(float)
            fig3, ax3 = plt.subplots()
            sns.histplot(df_webscraper["superficie"].dropna(), bins=10, kde=True, ax=ax3)
            st.pyplot(fig3)
        except:
            st.warning("Impossible de tracer la distribution de la superficie.")
