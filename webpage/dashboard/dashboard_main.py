import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard.kpi_chart_calculations import get_data
from dashboard.kpi_chart_calculations import kpi_speedconveyor

st.set_page_config(page_title="MLN | Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Dashboard</u>", unsafe_allow_html=True)

# # # Dashboard header elements
col1, col2, col3 = st.columns([3,2,1])
with col1:
    st.markdown("# **Dashboard**")
    st.markdown("#### **for Package Line Leadership**")
    st.write("KPI's & Statistics for Packaging Line Controlling")
with col2:
    st.write("")
with col3:
    options = ["SLAM-ALL", "SLAM01", "SLAM02", "SLAM03", "SLAM04", "SLAM05", "SLAM06", "SLAM07", "SLAM08", "....."]
    default_index = 0
    option = st.selectbox(
        label="**Select Packaging Line Station** \n\n(*SLAM-STATION*)",
        options=options,
        index=default_index
    )


st.divider()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # fetching dataframes from kpi_chart_calculations
df_norm, df_logs = get_data()
kpi_chart = kpi_speedconveyor(df_norm)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # KPI Section
with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
    with col1:
        st.write("")
        st.subheader("KPI's:")
        st.write("Controlling")

    with col2:
        conv_spd = kpi_chart["mean_last_6"].iloc[-1]
        conv_spd_prev = kpi_chart["mean_last_6"].iloc[-2]

        if conv_spd > 2.33:
            status = f"🔴 high risk"
        elif conv_spd > 2.28:
            status = f"🟡 medium risk"
        else:
            status = f"🟢 no risk"

        a = conv_spd
        b = conv_spd_prev
        delta_res = round((a - b) / b * 100, 0)

        st.metric("**Conveyer speed**", f"{conv_spd} m/s", f"{delta_res}%", delta_color="inverse")
        st.write(status)

    with col3:
        st.metric("Print Head 1", "91.5 %", "99.2 %")
        f"🟢 OK"

    with col4:
        st.markdown("<u>**Print Head 2**</u>", unsafe_allow_html=True)
        st.subheader("98.7 %")
        f"🟢 OK"

    with col5:
        st.markdown("<u>**Kickout Rate**</u>", unsafe_allow_html=True)
        st.subheader("21.2 %")
        f"🟢 OK"

    with col6:
        st.markdown("<u>**Defect-Rate**</u>", unsafe_allow_html=True)
        st.subheader("4.0 %")
        f"🟢 OK"

    with col7:
        st.markdown("<u>**Conveyor-Stops**</u>", unsafe_allow_html=True)
        st.subheader("5")
        f"🟢 OK"

st.markdown("<br>", unsafe_allow_html=True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Action recommendation
col1, col2 = st.columns([1,6])
with col1:
    st.markdown(
        "<span style='color:red;  font-size:15px; font-weight:bold;'>Recommendation for action:</span>",
        unsafe_allow_html=True)
with col2:
    st.write("The conveyer speed could be problematic, please check")
st.markdown(
    "<span style='color:grey;  font-size:12px; '>**NOTE:** Action items will be displayed by priority starting with highest. After resolve please make sure to reset the error log on machine control panel !</span>",
    unsafe_allow_html=True)

st.divider()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # chart Section
col1, col2, col3 = st.columns([1,1,1])

with col1:
    # Plot erstellen
    fig, ax = plt.subplots()
    ax.plot(kpi_chart["timestamp_5min"].dt.strftime("%H:%M"), kpi_chart["mean_last_6"], marker="o")

    # 👇 Y-axis best praxis for smooth line: min = 3 % below min, max = 2.4 as machine speed limit
    y_min = kpi_chart["mean_last_6"].min() - kpi_chart["mean_last_6"].min() * 0.03
    y_max = 2.4
    padding = (y_max - y_min) * 0.1 if y_max != y_min else 1

    ax.set_ylim(y_min - padding, y_max + padding)
    fig.patch.set_facecolor("#e6e6e6")

    ax.set_xlabel("time period 5 minutes")
    ax.set_ylabel("avg of 5-min-max")
    ax.set_title("conveyor speed history (last 60 min)",fontweight="bold",fontsize=12,pad=10)

    ax.axhspan(y_min, 2.2799, color="green", alpha=0.05)
    ax.axhspan(2.28, 2.3299, color="yellow", alpha=0.1)
    ax.axhspan(2.33, y_max, color="red", alpha=0.1)
    # schöneres Layout
    fig.autofmt_xdate()

    # In Streamlit anzeigen
    st.pyplot(fig)


st.markdown(
    "### <span style='color:red; text-decoration:underline; font-weight:bold;'>Page development is currently in progress !</span>",
    unsafe_allow_html=True)