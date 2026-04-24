import streamlit as st
from dashboard.kpi_chart_calculations import get_data

st.set_page_config(page_title="MLN | Data-Mgmt", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # 4 lines Headers of page
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown("<u>Dashboard & Data ▪ Data-Mgmt</u>", unsafe_allow_html=True)
st.markdown("# **Data Management**")
st.markdown("#### **for Analysts and Research**")
st.write("View, manage and download data")

st.markdown("<br>", unsafe_allow_html=True)

# # # fetching data for the 2 tables
filter_time = st.session_state.get("filter_time", "23:59")  # Default optional
df_norm, df_logs = get_data(filter_time)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # first data frame (table: shipments) as the background raw data from the dashboard
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter
filter_event = ["ALL"] + sorted(df_norm["event"].unique())
filter_station = ["ALL"] + sorted(df_norm["station"].unique(), key=str)
filter_boxbarcode = ["ALL"] + sorted(df_norm["box_barcode"].unique())

# 3 columns for the filter dropdowns right page side
col2, col3, col4, col5 = st.columns([4,1.5,1,1])
with col2:
    st.markdown(
        "##### <span style='color:black; text-decoration:underline; font-weight:bold;'>Normalized dashboard raw data</span>"
        + " - - → <span style='font-size:0.8em; font-weight:normal; font-style:italic;'>unique shipments line by line</span>",
        unsafe_allow_html=True)
with col3:
    col_event = st.selectbox("Events:",options=filter_event)
with col4:
    col_station = st.selectbox("Stations:",options=filter_station)
with col5:
    col_boxbarcode = st.selectbox("Boxbarcode:",options=filter_boxbarcode)

# Filter events for the data frame
df_filtered = df_norm.copy()

if col_event != "ALL":
    df_filtered = df_filtered[df_filtered["event"] == col_event]
if col_station != "ALL":
    df_filtered = df_filtered[df_filtered["station"] == col_station]
if col_boxbarcode != "ALL":
    df_filtered = df_filtered[df_filtered["box_barcode"] == col_boxbarcode]
st.dataframe(df_filtered)

# Button for Data Download: DataFrame switch to csv
csv = df_filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="packagingline_download_normalized.csv",
    mime="text/csv"
)

st.divider()
st.markdown("<br>", unsafe_allow_html=True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # second data frame showing original log data from table: logs_raw
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
col1, col2, col3 = st.columns([2,1,2])
with col1:
    st.markdown(
        "##### <span style='color:black; text-decoration:underline; font-weight:bold;'>Original source log data</span>"
        + " - - → <span style='font-size:0.8em; font-weight:normal; font-style:italic;'>original log data</span>",
        unsafe_allow_html=True)
with col3:
    search_text = st.text_input("search in '**log message**' on words/snippets/keywords etc. + enter:")
    df_filtered_logs = df_logs

    # Filter event for the data frame
    if search_text:
        df_filtered_logs = df_filtered_logs[
            df_filtered_logs["log_message"].astype(str).str.contains(search_text, case=False, na=False, regex=False)
        ]
st.dataframe(df_filtered_logs)

# Button for Data Download: DataFrame switch to csv
csv = df_filtered_logs.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Logs CSV",
    data=csv,
    file_name="packagingline_download_logdata.csv",
    mime="text/csv"
)

