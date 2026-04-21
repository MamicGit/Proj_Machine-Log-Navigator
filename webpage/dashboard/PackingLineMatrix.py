import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLN | Matrix", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ PL-Matrix</u>", unsafe_allow_html=True)
st.markdown("# **Packaging Line Matrix**")
st.write("Packaging Line Summary")

st.markdown("<br>", unsafe_allow_html=True)

# Daten erstellen
df = pd.DataFrame({
    "SlamLine": [f"SLAM{str(i).zfill(2)}" for i in range(1, 9)],
    "Conveyor Speed Risk": ["🔴", "🟡", "🟢", "🔴", "🟢", "🟡", "🟡", "🟢"],
    "Conveyor Stops Risk": ["🟢", "🔴", "🟢", "🟡", "🟢", "🟢", "🟢", "🟡"],
    "Toner Risk": ["🟢", "🟢", "🟢", "🟡", "🟢", "🔴", "🟢", "🟢"],
    "Kickout Risk": ["🟢", "🔴", "🟡", "🟢", "🟢", "🟢", "🔴", "🟢"],
})

st.dataframe(df, hide_index=True)

