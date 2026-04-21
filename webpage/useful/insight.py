import streamlit as st

st.set_page_config(page_title="MLN | Insights", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Useful ▪ Insights</u>", unsafe_allow_html=True)
st.markdown("# **Insights**")
st.write("Insights in Data Logics & Configs")

st.markdown(
    """
    ######
    <span style='color:blue;'>
    <b>NOTE:</b><br>
    At the heart of the 3-persons-team-project are training sessions in Python, EDA, ML, AWS, Streamlit, GitHub, and more,<br> 
    - while ensuring that the experience remains engaging and enjoyable throughout!<br>
    Thanks a lot to <b>DSI-Team</b> for their great six-month training program!<br>
    </span>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "##### <span style='color:darkred; text-decoration:underline; font-weight:bold;'>Conveyor Speed</span>",
    unsafe_allow_html=True)
st.write("The packing line conveyor belt is divided into at least four independently running belts.\
         \nFor slam machine & label printer its a second smaller one. It directs the packages, which are fed to the machine at precisely equal intervals, for label processing!\
         \nThe speed can be various between 0.8 m/s and 2.4 m/s to ensure the correct distances before labeling. Speed of 2.38 m/s leads to an issue.\
         \n:red[(!) If speed is growing, risk increases for a package jam and a temporary stop of conveyor.]")
st.markdown(
    "<span style='color:black; font-weight:bold;'>:red[KPI] for Conveyor Speed </span>",
    unsafe_allow_html=True)
st.write("KPI number and the line chart are based on a specific logic to ensure a smoothed number for the KPI, and also a smoothed time series in the trend chart for good decisions.\
         \n**LOGIC:** for each 5min time slot determine highest speed value (the one you find in the raw logs). On that numbers its calculating for ech 5-min-slot the moving average over last 30 minutes.\
         \n**In the end, it shows how often a sharp spike occurs within a 5-minute window, how high that spike is, and whether the technical team needs to reconfigure the conveyor belt!**")

st.divider()

st.markdown(
    "##### <span style='color:darkred; text-decoration:underline; font-weight:bold;'>Machine Stops</span>",
    unsafe_allow_html=True)
st.write("Stop of conveyor and machine can have various reasons, such as 'Package queue conflicts', 'Toner Refill', 'Change of label material' and some more.\
         \nFor reason 'Package queue conflicts' its mostly based on uneven belt speed which leads into a auto-stop and the risk for package swicheroos!")
st.markdown(
    "<span style='color:black; font-weight:bold;'>:red[KPI] for Machine Stops</span>",
    unsafe_allow_html=True)
st.write("KPI number shows the amount of stops just for 'Package queue conflicts' during latest two hours rolled, and shows below of this the sum of stops for last hour for high transparency.\
         \nThe higher the KPI, the higher the risk for customer impact for Swicheroos. The action should be discussion with Slam-Operator and technical team to adapt conveyor belt configuration.")

st.divider()

st.markdown(
    "##### <span style='color:darkred; text-decoration:underline; font-weight:bold;'>Print Quality</span>",
    unsafe_allow_html=True)
st.write("Each packaging line typically has two label printers that draw the necessary ink from a single toner cartridge.\
         \nIt is not unusual for the two printers to have different print qualities!\
         \nThe less the printer quality the lower the toner ink status. When the print quality drops to 88%, the toner cartridge must be replaced/refilled.")
st.markdown(
    "<span style='color:black; font-weight:bold;'>:red[KPI] for Toner Printheads</span>",
    unsafe_allow_html=True)
st.write("KPI number shows the real % status of toner.\
         \n**LOGIC** - Printquality 100% = 100% toner status, Printquality 88% = 0 % toner status")

st.divider()

