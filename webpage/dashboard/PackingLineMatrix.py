import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLN | Matrix", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # 4 lines Headers of page + dropdowns right side
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown("<u>Dashboard & Data ▪ PL-Matrix</u>", unsafe_allow_html=True)
st.markdown("# **Packaging Line Matrix**")
st.markdown("#### **for Operation Manager**")
st.write("Packaging Line Summary")

st.markdown("<br>", unsafe_allow_html=True)

# simulate station status, just for illustrative purposes. In production environment of a company a configuration for each slam is required
df = pd.DataFrame({
    "SlamLine": [f"SLAM{str(i).zfill(2)}" for i in range(1, 9)],
    "Conveyor Speed Risk": ["🔴", "🟡", "🟢", "🔴", "🟢", "🟡", "🟡", "🟢"],
    "Conveyor Stops Risk": ["🟢", "🔴", "🟢", "🟡", "🟢", "🟢", "🟢", "🟡"],
    "Toner Risk": ["🟢", "🟢", "🟢", "🟡", "🟢", "🔴", "🟢", "🟢"],
    "Kickout Risk": ["🟢", "🔴", "🟡", "🟢", "🟢", "🟢", "🔴", "🟢"],
})

st.dataframe(df, hide_index=True)

st.markdown(
    "<span style='color:grey;  font-size:12px; '>**NOTE:** This page is created solely for illustrative purposes !</span>",
    unsafe_allow_html=True)