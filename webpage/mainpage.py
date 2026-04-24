import streamlit as st

st.set_page_config(page_title="MLNavigator", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # creation variable for page-nav-list
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
dashboard = st.Page("dashboard/dashboard_main.py", title="Dashboard", icon=":material/dashboard:", default=True)
packlinemx = st.Page("dashboard/PackingLineMatrix.py", title="Packaging Line Matrix", icon=":material/grid_on:")
data_mgmt = st.Page("dashboard/data_mgmt.py", title="Data Management", icon=":material/data_usage:")

helps = st.Page("support/help.py", title="Help", icon=":material/help:")
bugs = st.Page("support/bugs.py", title="Report a bug", icon=":material/bug_report:")
features = st.Page("support/features.py", title="Feature request", icon=":material/notification_important:")
about = st.Page("support/about.py", title="About", icon=":material/check_circle:")

search = st.Page("useful/search.py", title="Site Search", icon=":material/search:")
insights = st.Page("useful/insight.py", title="Insights", icon=":material/history:")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # start of  pages
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
pg = st.navigation(
    {
        "Dashboard & Data": [dashboard, packlinemx, data_mgmt],
        "Useful": [search, insights],
        "Support": [helps, bugs, features, about],
    }
)
pg.run()
