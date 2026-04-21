import streamlit as st
from random import randint

st.set_page_config(page_title="MLN | About", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Support ▪ About</u>", unsafe_allow_html=True)
st.markdown("# **The Project**")
st.write("Notes & Info's and Thanks")

st.markdown(
    """
    ######
    <span style='color:blue;'>
    <b>first warm words:</b><br>
    At the heart of this three-person team project are training sessions in Scrum, Python, EDA, ML, AWS, Streamlit, GitHub, Excel and more,<br> 
    while ensuring the experience remains engaging and enjoyable throughout!<br>
    <br>Thanks a lot to <b><a href="https://data-science-institute.de/" target="_blank">DSI-Team</a></b> for their great six-month training program!<br>
    </span>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("**Project Team**")
var_teammember = randint(0,5)
if var_teammember == 0:
    team_mate = "Marco M.  |  Michael S.  |  Mohamad E."
elif var_teammember == 1:
    team_mate = "Marco M.  |  Mohamad E.  |  Michael S."
elif var_teammember == 2:
    team_mate = "Mohamad E.  |  Marco M.  |  Michael S."
elif var_teammember == 3:
    team_mate = "Mohamad E.  |  Michael S.  |  Marco M."
elif var_teammember == 4:
    team_mate = "Michael S.  |  Mohamad E.  |  Marco M."
else:
    team_mate = "Michael S.  |  Marco M.  |  Mohamad E."
st.write(team_mate)
st.write("DSI Study Nov 2025 - Apr 2026")

st.divider()

st.subheader("**Project Challanges**")
st.write("**Data engineering & EDA by Mohamad:** XYZ...")
st.write("**Machine Learning & Data Evaluations by Michael S.:** XYZ...")
st.write("**Webportal & KPI/Statistics by Marco M.:** XYZ")
st.divider()
