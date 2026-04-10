import streamlit as st

st.set_page_config(page_title="MLN | Insights", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Useful ▪ Insights</u>", unsafe_allow_html=True)
st.markdown("# **Insights**")
st.write("Insights in Data Logics & Configs")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "##### <span style='color:darkred; text-decoration:underline; font-weight:bold;'>Conveyor Speed</span>",
    unsafe_allow_html=True)
st.write("The packing line conveyor belt is divided into at least four independently running belts.\
         \nFor slam machine & label printer its a second smaller one. It directs the packages, which are fed to the machine at precisely equal intervals, for label processing!\
         \nThe speed can be various between 0.8 m/s and 2.4 m/s to ensure the correct distances before labeling.\
         \n:red[(!) If speed is growing, risk increases for a package jam and a temporary stop of conveyor.]")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "##### <span style='color:darkred; text-decoration:underline; font-weight:bold;'>Print Quality</span>",
    unsafe_allow_html=True)
st.write("Each packaging line typically has two label printers that draw the necessary ink from a single toner cartridge.\
         \nIt is not unusual for the two printers to have different print qualities!\
         \nThe less the printer quality the lower the toner ink status. When the print quality drops to 88%, the toner cartridge must be replaced/refilled.\
         \n:red[(!) It is important to track this printing quality and represent it in a KPI to prevent waste and cost inefficiency.]")