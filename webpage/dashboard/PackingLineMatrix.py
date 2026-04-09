import streamlit as st
from PIL import Image

st.set_page_config(page_title="MLN | Matrix", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ PL-Matrix</u>", unsafe_allow_html=True)
st.markdown("# **Packaging Line Matrix**")
st.write("Packaging Line Summary")


image_path = "./images/ShowUnderConstruction.png"
image = Image.open(image_path)
st.image(image, caption="Mein Bild", width=900)
