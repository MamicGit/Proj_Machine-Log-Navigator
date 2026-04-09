import streamlit as st
from PIL import Image

st.set_page_config(page_title="MLN | Data-Mgmt", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Data-Mgmt</u>", unsafe_allow_html=True)
st.markdown("# **Data Management**")
st.write("Store, manage and access data")

st.write("")

image_path = "./images/ShowUnderConstruction.png"
image = Image.open(image_path)
st.image(image, caption="Mein Bild", width=900)
