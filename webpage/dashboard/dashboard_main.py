import streamlit as st
from PIL import Image

st.set_page_config(page_title="MLN | Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Dashboard</u>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,2,1])
with col1:
    st.markdown("# **Dashboard**")
with col2:
    st.write("")
with col3:
    options = ["SLAM-ALL", "SLAM01", "SLAM02", "SLAM03", "SLAM04", "SLAM05", "SLAM06", "SLAM07", "SLAM08", "....."]
    default_index = 0
    option = st.selectbox(
        label="**Select Packaging Line Station** \n\n(*SLAM-STATION*)",
        options=options,
        index=default_index
    )

st.write("KPI's & Statistics for Packaging Line Controlling")

st.write("")

image_path = "./images/ShowUnderConstruction.png"
image = Image.open(image_path)
st.image(image, caption="Mein Bild", width=900)
