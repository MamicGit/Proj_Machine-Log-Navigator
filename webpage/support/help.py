import streamlit as st

st.set_page_config(page_title="MLN | Help", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # 3 lines Headers of page + dropdowns right side
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown("<u>Support ▪ Help</u>", unsafe_allow_html=True)
st.markdown("# **Help / FAQ**")
st.write("Frequently Asked Questions")
st.write("")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # creation of dropdown and related contend being displayed - using 3 columns just for design purposes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
col1, col2, col3 = st.columns([2, 4, 4])
with col1:
    st.write("")
    selection_field = st.selectbox("**Choose Keyword**", ["- please select -", "Dashboard", "PckgLine Matrix", "Data Management", "Site Search",
                                                          "Insights","Bugreport","Feature Request","KPI", "Other"])
    st.write("")
    texte = {
        "- please select -": "🔍 **Select from the dropdown to find answers.**",
        "Dashboard": "The Dashboard provides KPIs and Charts for real-time view of system performance.\nColor coding indicates system status: **green** for stable, **yellow** for warning, and **red** for critical.\
         \nUse the 'Packaging Line Station' filter to focus on the line you are responsible for (permission request required, compliance with data protection guidelines). \
         \n\n(Please note: the  filter is implemented to simulate different daily snapshots for the project committee!)",
        "KPI": "KPI stands for **Key Performance Indicator**. You’ll find them in the dashboard, which helps speed up decision-making processes.",
        "Logdata": "Logdata used in this system is located in the machine system and means summary ob couple of data ",
        "PckgLine Matrix": "Provides an overview of all packaging lines for direct comparison.\n \
         Color coding highlights performance differences and helps identify potential risks and critical slam stations.",
        "Data Management": "Displays raw and processed data used in our Portal. You can inspect and download dataset.\nUseful for debugging, validation and deeper analysis.",
        "Site Search": "Search for keywords like KPI, dashboard or insights. Helps you quickly find relevant pages and informations.\nIf no results appear, try more general term.",
        "Insights": "Provides deeper insight into specific project items and enhances understanding of machine process behavior.\
         \nHelps you better understand the root causes of issues and supports fact-based decision-making.",
        "Bugreport": "Report issues or unexpected system behavior.\nProvide clear description to help faster resolution.\nHelps improve system stability and usability.",
        "Feature Request": "Requesting the addition of a feature, data or views to enhance user experience and functionality. \
         \nHelps evolve the platform based on user needs.",
        "Other": "Since this type of '**help-section**' varies greatly depending on the company and specific use cases, its content here is generally temporary.\
         \nThe page can be customized: **please adjust the content accordingly**"
    }

# showing the results of selected dropdown
st.markdown(
    "<span style='color: green'>" + texte[selection_field].replace('\n', '<br>') + "</span>",
    unsafe_allow_html=True
)
