import streamlit as st
from PIL import Image
from pathlib import Path
import pandas as pd

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
    "#### :material/analytics: Analytics & Flow Visualization"
)

# Project skizze Conveyor & Machine description
with st.expander(":material/arrow_drop_down: :violet[**Conveyor & Machine**]"):
    col1, col2 = st.columns([2, 1])
    with col1:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "TheMachine.png"
        image = Image.open(img_path)
        st.image(image, caption="Teams Project", width="stretch")

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)
    st.write("**Couple of unexpected behavior can happen on packaging lines and respective machines, such as:**\
             \n* :red[Unfocused employees]\
             \n* :red[Wear and tear on machinery]\
             \n* :red[Material waste]\
             \n* :red[Disorganized shift handover processes]\
             \n:red[ect...]\
             \n\n**:green[Our Mission:]** :green[In search of ways to improve process transparency and optimize productivity resulting in web-portal inclusive support & ticket-system.]")

# Logfile Generator
with st.expander(":material/arrow_drop_down: :violet[**Logfile-Generator**]"):
    col3, col4 = st.columns([1,1])
    with col3:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "LogGeneratorA.png"
        image = Image.open(img_path)
        st.image(image, caption="by Marco M.", width="stretch")
    with col4:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "LogGeneratorB.png"
        image = Image.open(img_path)
        st.image(image, caption="by Marco M.", width="stretch")

    st.write("**Download Python-Code:** [Github](https://github.com/MamicGit/Proj_Machine-Log-Navigator/tree/main/Logfile_CustomerOrder_Generator)")

# ETL description
with st.expander(":material/arrow_drop_down: :violet[**ETL**]"):
    col5, col6 = st.columns([2, 1])
    with col5:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "Datenfluss_3.png"
        image = Image.open(img_path)
        st.image(image, caption="by Mohamad E.", width="stretch")

        st.markdown(
            "<span style='color:black; font-weight:bold;'>:red[ETL Description]</span>",
            unsafe_allow_html=True)
        st.write("The ETL pipeline processes unstructured log data and transforms it into an analysis-ready dataset.\
                 \n\nRaw logs are first parsed, cleaned, and temporally normalized to ensure consistency.\
                 \nThe data is then aggregated on shipment level and enriched with relevant features such as weight differences, relative deviations, and kickout indicators.\
                 \nIn addition, a mapping logic is implemented to assign production stops to the corresponding previous shipment.\
                 \n\n**The final dataset is stored in a SQLite database and serves as the foundation for further analysis and machine learning.**")
    st.write(
        "**ETL-Pipeline:** [Github](https://github.com/mohamaddataeng/log-machine-pipeline/tree/main/scripts)")

# EDA description
with st.expander(":material/arrow_drop_down: :violet[**The EDA**]"):
    col7, col8 = st.columns([2, 1])
    with col7:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "PresentationEDA.png"
        image = Image.open(img_path)
        st.image(image, caption="by Mohamad E.", width="stretch")

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)
    st.markdown("""
    **Exploratory Data Analysis (EDA) identifies key patterns and sources of production issues.**
    - Findings:
        - Kickout rates peak during shift changes (~06:00 and ~22:00), indicating instability during transitions.
        - Midday operations remain relatively stable.
        - Station 11 shows a significantly higher kickout rate (~32% vs. ~22%), suggesting a local issue.
        - Print quality (SLAM 1 & 2) impacts process stability and error rates.
        - Stop probability remains low at normal speeds but increases sharply beyond ~2.3 m/s.
        - Higher speeds significantly increase the risk of system instability and should be avoided.
        """)
    st.markdown("""
    **These insights support targeted optimization and improved process stability.**
    """)

# ML description
with st.expander(":material/arrow_drop_down: :violet[**Machine Learning ML**]"):
    col9, col10 = st.columns([1, 1])
    with col9:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "PresentationML.png"
        image = Image.open(img_path)
        st.image(image, caption="by Michael S.", width="stretch")

        with col10:
            BASE_DIR = Path(__file__).resolve().parent.parent
            img_path = BASE_DIR / "images" / "PresentationML2.png"
            image = Image.open(img_path)
            st.image(image, caption="by Michael S.", width="stretch")

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)

    st.write("The goal of machine learning in this project was to find a way to increase process productivity for Quality Department, and increase customer experience.\
             \n\nLogistik-Pakete durchlaufen eine Gewichtskontrolle, bei der der regelbasierte Ansatz alle Pakete mit einer Abweichung über 1,2% zur manuellen Prüfung auskickt,\
             \nwas zu einem hohen Prüfvolumen führt, obwohl nur ein kleiner Anteil der gekickten Pakete tatsächlich fehlerhaft ist.\
             \n\n**Ziel** war, ein ML-Modell zu entwickeln, das echte Fehler präziser identifiziert und das Prüfvolumen reduziert.\
             \nDie Zielvariable ist binär, die Klassen stark unbalanciert (pckg_problem_found: 0 = fehlerfrei ~97,8%, 1 = Paketfehler ~2,2%).\
             \n\nEs wurden RandomForest, SVC und LogisticRegression (L1) mit class_weight='balanced' und GridSearchCV trainiert und auf vier unabhängigen Datensätzen (ø ~5.900 Pakete) evaluiert. \
             \nDas Modell wurde einmal auf **F1-Score** und einmal auf **Recall** optimiert, um zwei verschiedene Praxisszenarien abzubilden.\
             \n\n**Ergebnisse** (Ø):")

    col20, col21 = st.columns([1, 1])
    with col20:
        data = [
            ["Kickout",                         "21.3%", "3,6%", "25,1%"],
            ["TP (% Kickout)",                  "10.2%", "34,8%", "8,8%"],
            ["TP (% Erkennung Gesamt-Failures)", "100.0%", "53,8%", "100%"],
            ["FP (% Kickout)",                  "89.8%", "65,2%", "91,2%"],
            ["FN",                              "0", "12", "0"],
        ]
        df = pd.DataFrame(data, columns=["Process", "RB", "ML F1", "ML Recall"])
        df.index = [""] * len(df)
        st.markdown(df.to_html(index=False, justify="left"),unsafe_allow_html=True)

    st.write("\n\nF1-Optimierung minimiert das Prüfvolumen auf Kosten verpasster Fehler. \
                 \nRecall-Optimierung erkennt alle Fehler auf Kosten eines hohen Prüfvolumens — welcher Trade-off akzeptabel ist, hängt davon ab,\
                 \nob ein verpasster Paketfehler oder ein unnötiger Prüfaufwand im Betrieb schwerwiegender wiegt. \
                 \n\nDa synthetische Daten genutzt wurden, sind die Ergebnisse als obere Leistungsgrenze zu interpretieren.\
                 ")
    st.write(
        "**Process & Codes:** [Github](https://github.com/schippermitch/Machine-Anomal)")

# Website-Portal & Configurations description
with st.expander(":material/arrow_drop_down: :violet[**Website-Portal & Configurations**]"):
    col11, col12 = st.columns([2, 1])
    with col11:
        BASE_DIR = Path(__file__).resolve().parent.parent
        img_path = BASE_DIR / "images" / "WebFlow.png"
        image = Image.open(img_path)
        st.image(image, caption="by Marco M.", width="stretch")

    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[Summary]</span>",
        unsafe_allow_html=True)

    st.markdown("""
- **As very first step: Server checking and testing**
    - Set up an AWS environment comprising S3, EC2 instances, EBS, Elastic IP, Nginx, and a cost control dashboard.
    - Set up PuTTY and WinSCP for productive use.
    - Executed test.py scripts over a one-week period to assess functionality, performance, stability, and cost efficiency of Python Streamlit on AWS.
    - Created in parallel a Streamlit Cloud profile on [share.streamlit.io](https://share.streamlit.io/) as full independent second Web-Portal.
    - Set up an independent second Git repository, ensuring no risk to project outcomes.
    - Syntax and script procedures tested and standardized; running without errors on both servers.
    """)
    st.markdown("""
- **As second most extensive step: Developing & deploying**
    - Created a design mockup covering navigation bar behavior and file structure.
    - Performed EDA to understand the data and establish best practices for KPIs, dashboards, tables, and other components.
    - Implementation of all components and functions into the corresponding files.
    - Filled the portal with content, including the ticket system and descriptions.
    """)
    st.markdown("""
- **As final step: Review and complete**
    - Requested unit tests and applied several updates.
    """)
    st.markdown("""
- **Result:**
    - [AWS-Portal](http://54.225.90.74/) :grey[(sign in with login and PW avoding bot-attacks)], and in addition the  [streamlit.io-Portal](https://dsimlnappio-dsi-finalproject.streamlit.app/) :grey[(free access)]
    - *Python Environment:** [Github](https://github.com/MamicGit/Proj_Machine-Log-Navigator/tree/main/webpage)
    """)

st.divider()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Process Elements
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown(
    "#### :material/conveyor_belt: Process Elements & KPIs"
)

# showing expander for description of Conveyor Speed + KPI details
with st.expander(":material/arrow_drop_down: :violet[**Conveyor Speed**]"):
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
with st.expander(":material/arrow_drop_down: :violet[**Machine Stops**]"):
    st.write("Stop of conveyor and machine can have various reasons, such as 'Package queue conflicts', 'Toner Refill', 'Change of label material' and some more.\
             \nFor reason 'Package queue conflicts' its mostly based on uneven belt speed which leads into a auto-stop and the risk for package swicheroos!")
    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[KPI] for Machine Stops</span>",
        unsafe_allow_html=True)
    st.write("KPI number shows the amount of stops just for 'Package queue conflicts' during latest two hours rolled, and shows below of this the sum of stops for last hour for high transparency.\
             \nThe higher the KPI, the higher the risk for customer impact for Swicheroos. The action should be discussion with Slam-Operator and technical team to adapt conveyor belt configuration.")

# showing expander for description of Print Quality + KPI details
with st.expander(":material/arrow_drop_down: :violet[**Print Quality**]"):
    st.write("Each packaging line typically has two label printers that draw the necessary ink from a single toner cartridge.\
             \nIt is not unusual for the two printers to have different print qualities!\
             \nThe lower the print quality, the lower the toner level, among other things. When the print quality drops to 88%, the toner cartridge must be replaced/refilled.")
    st.markdown(
        "<span style='color:black; font-weight:bold;'>:red[KPI] for Toner Printheads</span>",
        unsafe_allow_html=True)
    st.write("KPI number shows the real % status of toner.\
             \n**LOGIC** - Printquality 100% = 100% toner status, Printquality 88% = 0 % toner status")



