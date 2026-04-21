import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard.kpi_chart_calculations import get_data
from dashboard.kpi_chart_calculations import kpi_speedconveyor
from dashboard.kpi_chart_calculations import line_stops_rolled

st.set_page_config(page_title="MLN | Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Dashboard</u>", unsafe_allow_html=True)

# # # Dashboard header elements
col1, col2, col3 = st.columns([3,0.5,1])
with col1:
    st.markdown("# **Dashboard**")
    st.markdown("#### **for Package Line Leadership**")
    st.write("KPI's & Statistics for Packaging Line Controlling")
with col2:
    zeit = st.selectbox("**Time of Day** \n\n:red[(*for Presentation*)]", ["03:05", "13:35", "15:15", "23:59"])
    st.session_state["filter_time"] = zeit
with col3:
    options = ["SLAM01", "SLAM02", "SLAM03", "SLAM04", "SLAM05", "SLAM06", "SLAM07", "SLAM08", "....."]
    default_index = 4
    option = st.selectbox(
        label="**Select Packaging Line Station** \n\n(*SLAM-STATION*)",
        options=options,
        index=default_index
    )

if option != "SLAM05":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader(":red[Access denied (!)]")
    st.write("Page content requires specific permissions for respective managers.")
    st.write("**please cut a ticket using → feature request → permission request !**")
    st.stop()

st.divider()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # fetching dataframes from kpi_chart_calculations

df_norm, df_logs = get_data(zeit)
kpi_chart = kpi_speedconveyor(df_norm)
line_stops, count_2h, count_lh, count_curr = line_stops_rolled(df_norm)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # KPI Section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
    with col1:
        st.write("")
        st.subheader("KPI's:")
        st.write("Controlling")

    with col2:  # conveyor speed risk
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
        delta_res = round((a - b) / b * 100, 1)

        st.metric("**Conveyer speed** (current)", f"{conv_spd} m/s", f"{delta_res}%", delta_color="off")
        st.write(status)

    with col3:  # line stops 2h rolled
        # line_stops, count_2h, count_lh, count_curr
        stops_diff = count_curr
        if stops_diff >= 3:
            status_stp = f"🔴 high risk"
        elif stops_diff >= 2:
            status_stp = f"🟡 medium risk"
        else:
            status_stp = f"🟢 no risk"

        st.metric("**Conveyer stops** (2 hours rolled)", f"{count_2h} stop(s)", delta=f"{count_curr} (last hour)", delta_color="off")
        st.write(status_stp)

    with col4:  # Toner status print head
        df_print_qa = df_norm[df_norm["print_quality_pct"] >= 0].copy()
        status_act = df_print_qa.iloc[-1, 14]
        status_bef = df_print_qa.iloc[-2, 14]

        # lineare Skalierung (Mapping) 88 -> 100
        toner_act_perc = round((status_act - 88) / (100 - 88) * 100, 1)
        toner_bef_perc = round((status_bef - 88) / (100 - 88) * 100, 1)
        toner_consumed = round(toner_act_perc- toner_bef_perc, 1)

        if toner_act_perc <= 5:
            status_toner = f"🔴 high risk"
        elif toner_act_perc <= 10:
            status_toner = f"🟡 medium risk"
        else:
            status_toner = f"🟢 no risk"

        st.metric("**Toner Printheads** (current)", f"{toner_act_perc}%", f"{toner_consumed}% (consumed)", delta_color="off")
        st.write(status_toner)

    with col5:
        st.metric("**Kickout Rate** (current)", f"{21.2}%", f"{0}%", delta_color="off")
        f"🟢 OK"

    with col6:
        st.metric("**Defect Rate** (current)", f"{4}%", f"{0}%", delta_color="off")
        f"🟢 OK"

st.markdown("""<hr style="border-top: 3px double #bbb; border-bottom: none;"><br>""",unsafe_allow_html=True)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # chart Section
col1, col2, col3 = st.columns([2,0.5,2])

with col1:
    # Plot erstellen
    fig, ax = plt.subplots()
    ax.plot(kpi_chart["timestamp_5min"].dt.strftime("%H:%M"), kpi_chart["mean_last_6"], marker="+")
    ax.tick_params(axis='x', labelsize=8)

    # 👇 Y-axis best praxis for smooth line: min = 3 % below min, max = 2.4 as machine speed limit
    y_min = kpi_chart["mean_last_6"].min() - kpi_chart["mean_last_6"].min() * 0.03
    y_max = 2.4
    padding = (y_max - y_min) * 0.1 if y_max != y_min else 1

    ax.set_ylim(y_min - padding, y_max + padding)
    fig.patch.set_facecolor("#f7f5f5")

    ax.set_xlabel("time period 5 minutes")
    ax.set_ylabel("avg of 5-min-max")
    ax.set_title("conveyor speed history (rolling 2 hours)",fontweight="bold",fontsize=12,pad=10)

    ax.axhspan(y_min, 2.309, color="green", alpha=0.05)
    ax.axhspan(2.31, 2.3499, color="yellow", alpha=0.1)
    ax.axhspan(2.35, y_max, color="red", alpha=0.1)
    # schöneres Layout
    fig.autofmt_xdate()

    # In Streamlit anzeigen
    st.pyplot(fig)

