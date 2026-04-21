import streamlit as st

st.set_page_config(page_title="MLN | Search", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Useful ▪ Search</u>", unsafe_allow_html=True)
st.markdown("# **Search the Webportal**")
st.write("Browse portal content")

st.markdown("<br><br>", unsafe_allow_html=True)

pages = {
    "Dashboard": ("Analyse KPIs charts Trends Dashboard", "follow this link", "dashboard/dashboard_main.py"),
    "PackgLineMatrix": ("matrix overall consolidated", "follow this link", "dashboard/PackingLineMatrix.py"),
    "DataMgmt": ("data up down load investigate", "follow this link", "dashboard/data_mgmt.py"),
    "Insights": ("insight KPIs charts support questions unclear understanding description explanation explain describe", "follow this link", "useful/insight.py"),
    "Bugs": ("problems ticket bugs issues error trouble", "follow this link", "support/bugs.py"),
    "Features": ("improvements ticket feature idea support", "follow this link", "support/features.py"),
    "Help": ("help worried concerned", "follow this link", "support/help.py")
}

def reset_search():
    st.session_state["search_input"] = ""

st.text_input("🔎 search for words/snippets/keywords etc. + enter", key="search_input")

query = st.session_state.get("search_input", "").strip()

if query:
    query = query.lower()

    results = []

    for name, (content, output_text, path) in pages.items():
        if query in content.lower():
            results.append((name, output_text, path))

    if results:
        for name, output_text, path in results:
            st.page_link(path, label=f"**Link**: {name}")
    else:
        st.info("No matching results found.")

st.button("Reset search", on_click=reset_search)

