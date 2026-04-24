import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="MLN | Insights", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # 3 lines Headers of page + dropdowns right side
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown("<u>Useful ▪ Insights</u>", unsafe_allow_html=True)
st.markdown("# **Insights**")
st.write("Insights in Data Logics & Configs")

st.markdown("<br>", unsafe_allow_html=True)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Visualizations, Flow & Summary
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown(
    "##### <span style='color:darkblue; font-weight:bold;'>Visualization, Flow & Summary</span>",
    unsafe_allow_html=True)

# showing expander for Conveyor & Machine description
with st.expander(":material/arrow_drop_down: :violet[**Conveyor & Machine**]"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = BASE_DIR / "images" / "TheMachine.png"
    image = Image.open(img_path)
    st.image(image, caption="Teams Project", width=800)

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)
    st.write("**Couple of unexpected behavior can happen on packaging lines and respective machines, such as:**\
             \n* :red[Unfocused employees]\
             \n* :red[Wear and tear on machinery]\
             \n* :red[Material waste]\
             \n* :red[Disorganized shift handover processes]\
             \n:red[ect...]\
             \n\n**:green[Our Mission:]** :green[In search of ways to improve process transparency and optimize productivity inclusive support & ticket-system.]")

# showing expander for ETL description
with st.expander(":material/arrow_drop_down: :violet[**ETL**]"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = BASE_DIR / "images" / "Datenfluss_3.png"
    image = Image.open(img_path)
    st.image(image, caption="by Mohamad E.", width=800)

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[ETL Description]</span>",
        unsafe_allow_html=True)
    st.write("The ETL pipeline processes unstructured log data and transforms it into an analysis-ready dataset.\
             \n\nRaw logs are first parsed, cleaned, and temporally normalized to ensure consistency.\
             \nThe data is then aggregated on shipment level and enriched with relevant features such as weight differences, relative deviations, and kickout indicators.\
             \nIn addition, a mapping logic is implemented to assign production stops to the corresponding previous shipment.\
             \n\n**The final dataset is stored in a SQLite database and serves as the foundation for further analysis and machine learning.**")

# showing expander for EDA description
with st.expander(":material/arrow_drop_down: :violet[**The EDA**]"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = BASE_DIR / "images" / "PicturePlaceholder.png"
    image = Image.open(img_path)
    st.image(image, caption="by Mohamad E.", width=800)

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)
    st.write("Exploratory Data Analysis (EDA) was conducted to identify patterns and potential sources of production issues.\
             \nThe analysis revealed clear patterns around shift changes, where kickout rates peak at approximately 06:00 and 22:00, indicating instability during operational transitions.\
             \n\nIn contrast, midday operations remain relatively stable.\
             \nA station-level analysis showed that Station 11 has a significantly higher kickout rate (~32%) compared to the average (~22%),\
             \nsuggesting a station-specific issue rather than a system-wide problem.\
             \n\nAdditionally, print quality analysis (SLAM 1 and SLAM 2) highlighted its influence on process stability and error occurrence,\
             \nindicating that deviations in print quality can contribute to operational disruptions.\
             \n\n**These findings help to better understand system behavior and provide a basis for targeted optimization measures.**")

# showing expander for ML description
with st.expander(":material/arrow_drop_down: :violet[**Machine Learning ML**]"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = BASE_DIR / "images" / "PicturePlaceholder.png"
    image = Image.open(img_path)
    st.image(image, caption="by Michael S.", width=800)

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)

    st.write("The goal of machine learning in this project was to find a way to increase process productivity for Quality Department, and increase customer experience.\
             \n....\
             \n\n...\
             \n...\
             \n...\
             \n\n...\
             \n...\
             \n\n**Result:**")

# showing expander for Website-Portal & Configurations description
with st.expander(":material/arrow_drop_down: :violet[**Website-Portal & Configurations**]"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = BASE_DIR / "images" / "WebFlow.png"
    image = Image.open(img_path)
    st.image(image, caption="by Marco M.", width=800)

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)

    st.write("As a first step, I set up the AWS environment with S3, an EC2 instance, EBS, an Elastic IP and a cost dashboard.\
             \nAfterwards I ran some test.py scripts over a 1-week period to ensure the functionality, performance, stability, and cost efficiency of Python Streamlit on AWS.\
             \n\nIn a second step, I concurrently created a Streamlit Cloud profile on share.streamlit.io (full independent second Web-Portal) along with an independent second Git repository,\
             \nto have a backup option for the team avoiding any risk for the team-project.\
             \n\nIn the third and most extensive step, I developed and deployed all Streamlit Python files, including the corresponding content for KPIs, dashboards, functionalities, tables, and other components.\
             \nIn parallel, I applied exploratory data analysis (EDA) to identify and present the most relevant KPIs and visualizations.\
             \n\n**Result:** The [AWS-Portal](http://54.225.90.74/) :grey[(sign in with login and PW avoding bot-attacks)], and in addition the  [streamlit.io-Portal](https://dsimlnappio-dsi-finalproject.streamlit.app/) :grey[(free access)]")

st.divider()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Process Elements
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown(
    "##### <span style='color:darkblue; font-weight:bold;'>Process Elements & KPIs</span>",
    unsafe_allow_html=True)

# showing expander for description of Conveyor Speed + KPI details
with st.expander(":material/arrow_drop_down: :red[**Conveyor Speed**]"):
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

# showing expander for description of Machine Stops + KPI details
with st.expander(":material/arrow_drop_down: :red[**Machine Stops**]"):
    st.write("Stop of conveyor and machine can have various reasons, such as 'Package queue conflicts', 'Toner Refill', 'Change of label material' and some more.\
             \nFor reason 'Package queue conflicts' its mostly based on uneven belt speed which leads into a auto-stop and the risk for package swicheroos!")
    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[KPI] for Machine Stops</span>",
        unsafe_allow_html=True)
    st.write("KPI number shows the amount of stops just for 'Package queue conflicts' during latest two hours rolled, and shows below of this the sum of stops for last hour for high transparency.\
             \nThe higher the KPI, the higher the risk for customer impact for Swicheroos. The action should be discussion with Slam-Operator and technical team to adapt conveyor belt configuration.")

# showing expander for description of Print Quality + KPI details
with st.expander(":material/arrow_drop_down: :red[**Print Quality**]"):
    st.write("Each packaging line typically has two label printers that draw the necessary ink from a single toner cartridge.\
             \nIt is not unusual for the two printers to have different print qualities!\
             \nThe lower the print quality, the lower the toner level, among other things. When the print quality drops to 88%, the toner cartridge must be replaced/refilled.")
    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[KPI] for Toner Printheads</span>",
        unsafe_allow_html=True)
    st.write("KPI number shows the real % status of toner.\
             \n**LOGIC** - Printquality 100% = 100% toner status, Printquality 88% = 0 % toner status")

