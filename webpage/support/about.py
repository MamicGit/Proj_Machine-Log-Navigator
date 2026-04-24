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
    At the heart of this three-person team project are training sessions in Scrum, Python, ETL, EDA, SQLite, ML, AWS EC2/S3/SES/Lambda, Elastic IP, Streamlit, GitHub, Excel ect.,<br> 
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

st.markdown("""<hr style="border-top: 3px double #bbb; border-bottom: none;"><br>""",unsafe_allow_html=True)

st.subheader("**Project Responsibilities**")
st.write("**Data engineering & EDA** by Mohamad:")
toggle_me = st.toggle("Challenges - Mohamad")
if toggle_me:
    st.markdown(
        """
        <span style='color:grey;'>
        My challenge ...<br> 
        ....<br>
        ...
        </span>
        """,
        unsafe_allow_html=True
    )
st.divider()

st.write("")
st.write("**Machine Learning & Data Evaluations** by Michael S.:")
toggle_ms = st.toggle("Challenges - Michael")
if toggle_ms:
    st.markdown(
        """
        <span style='color:grey;'>
        My challenge ...<br> 
        ....<br>
        ...
        <br></span>
        """,
        unsafe_allow_html=True
    )
st.divider()

st.write("")
st.write("**Webportal & KPI/Statistics** by Marco M.:")
toggle_mm = st.toggle("Challenges - Marco")
if toggle_mm:
    st.markdown(
        """
        <span style='color:grey;'>
        I personally found it challenging to configure the AWS server in a secure and project-optimal way while keeping costs as low as possible (EC2, Nginx, static IP).<br>
        In addition, it was challenging as well to identify the right data configuration for the KPIs in order to present them in a clear and meaningful way, <br>
        and—combined with the appropriate trend charts—to provide the highest possible level of process transparency.
        </span>
        """,
        unsafe_allow_html=True
    )
st.divider()
