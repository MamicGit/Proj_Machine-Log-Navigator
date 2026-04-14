import streamlit as st

st.set_page_config(page_title="MLN | Help", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Support ▪ Help</u>", unsafe_allow_html=True)
st.markdown("# **Help / FAQ**")
st.write("Frequently Asked Questions")
st.write("")

col1, col2, col3 = st.columns([2, 4, 4])

with col1:
    st.write("")
    selection_field = st.selectbox("**Choose Keyword**", ["- please select -", "Dashboard", "PckgLine Matrix", "Data Management", "Site Search",
                                                          "Insights","Bugreport","Feature Request","KPI", "Other"])
    st.write("")
    texte = {
        "- please select -": "",
        "Dashboard": "A dashboard is a visual overview that displays key performance indicators and data in real-time to support decision-making.",
        "PckgLine Matrix": "Shows all packaging lines for direct comparisons",
        "Data Management": "Upload / Download Data, inspect raw data",
        "Site Search": "This page :wink:",
        "Insights": "The Insights page provides some important information about specific meanings of packaging line components.",
        "Feature Request": "Requesting the addition of a feature to enhance user experience and functionality.",
        "KPI": "KPI stands for 'Key Performance Indicator' and refers to measurable values that assess the success or progress of an organization or project.\nThey help track performance and inform strategic decisions.",
        "Other": "Since this type of '**help-section**' varies greatly depending on the company and specific use cases, its content here is generally temporary."
                 "\nThe page can be customized: **please adjust the content accordingly**"
    }

st.markdown(
    "<span style='color: green'>" + texte[selection_field].replace('\n', '<br>') + "</span>",
    unsafe_allow_html=True
)
