import streamlit as st
import matplotlib.pyplot as plt
from dashboard.kpi_chart_calculations import get_data
from dashboard.kpi_chart_calculations import kpi_speedconveyor
from dashboard.kpi_chart_calculations import line_stops_rolled
from dashboard.kpi_chart_calculations import kickout_data

st.set_page_config(page_title="MLN | Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Dashboard</u>", unsafe_allow_html=True)

# # # Dashboard header elements
col1, col2, col3 = st.columns([3,0.5,1])
with col1:
    st.markdown("# **Dashboard**")
    st.markdown("#### **for Package Line Leadership**")
    st.write("KPI's & Statistics for Packaging Line Controlling")
with col2:
    zeit = st.selectbox("**Time of Day** \n\n:red[(*for Presentation*)]", ["03:05", "06:55", "13:35", "15:50", "23:59"])
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

df_norm, df_logs = get_data(zeit)
kpi_chart = kpi_speedconveyor(df_norm)
line_stops, count_2h, count_lh, count_curr = line_stops_rolled(df_norm)
ko_data = kickout_data(df_norm)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # KPI Section
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
with (st.container()):
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

    with col1:  # description of figures
        st.write("")
        st.subheader("KPI's:")
        st.write("Controlling")

    with col2:  # conveyor speed risk
        action_spd = ""
        conv_spd = kpi_chart["mean_last_6"].iloc[-1]
        conv_spd_prev = kpi_chart["mean_last_6"].iloc[-2]

        if conv_spd > 2.35:
            status = f"🔴 high risk"
            action_spd = "<b>:red[Action required:]</b><br>Contact Technic Team!"
        elif conv_spd > 2.31:
            status = f"🟡 medium risk"
            action_spd = "<b>:yellow[Action required:]</b><br>Inform Technic Team!"
        else:
            status = f"🟢 no risk"

        a = conv_spd
        b = conv_spd_prev
        delta_res = round((a - b) / b * 100, 1)

        st.metric("**Conveyer speed** \n\n(current latest value)", f"{conv_spd} m/s", f"{delta_res}% vs. previous", delta_color="inverse")
        st.write(status)
        st.markdown(f"{action_spd}", unsafe_allow_html=True)

    with col3:  # line stops 2h rolled
        action_stp = ""
        stops_diff = count_curr - count_lh
        if count_curr >= 4:
            status_stp = f"🔴 high risk"
            action_stp = "<b>:red[Action required:]</b><br>Contact Slam Operator!"
        elif count_curr >= 3:
            status_stp = f"🟡 medium risk"
            action_stp = "<b>:yellow[Action required:]</b><br>Check Conveyor flow!"
        else:
            status_stp = f"🟢 no risk"

        st.metric("**Conveyer stops** \n\n(1h current)", f"{count_curr} stop(s)", delta=f"{stops_diff} stops vs. prev hour", delta_color="inverse")
        st.write(status_stp)
        st.markdown(f"{action_stp}", unsafe_allow_html=True)

    with col4:  # Toner level print head
        action_tnr = ""
        df_print_qa = df_norm[df_norm["print_quality_pct"] >= 0].copy()
        status_act = df_print_qa.iloc[-1, 14]
        status_bef = df_print_qa.iloc[-2, 14]

        # lineare Skalierung (Mapping) 88 -> 100
        toner_act_perc = round((status_act - 88) / (100 - 88) * 100, 1)
        toner_bef_perc = round((status_bef - 88) / (100 - 88) * 100, 1)
        toner_consumed = round(toner_act_perc- toner_bef_perc, 1)

        if toner_act_perc <= 5:
            status_toner = f"🔴 high risk"
            action_tnr = "<b>:red[Action required:]</b><br>Check replace of toner!"
        elif toner_act_perc <= 8:
            status_toner = f"🟡 medium risk"
            action_tnr = "<b>:yellow[FYI:]</b><br>Upcoming Toner repl."
        else:
            status_toner = f"🟢 no risk"

        st.metric("**Toner Level Printheads** \n\n(current latest value)", f"{toner_act_perc}%", f"{toner_consumed}% (consumed)", delta_color="off")
        st.write(status_toner)
        st.markdown(f"{action_tnr}", unsafe_allow_html=True)

    with col5:  # Kickout rate
        action_kor = ""
        ship_vol2h, ko_vol2h, found_vol2h, ko_rate2h_perc, found_rate2h_perc = ko_data.tail(2).iloc[:, 1:].sum()
        ship_vol1h, ko_vol1h, found_vol1h, ko_rate1h_perc, found_rate1h_perc = ko_data.tail(1).iloc[:, 1:].sum()
        ko_act_perc = round(ko_rate1h_perc, 1)
        ko_bef_perc = (ko_vol2h - ko_vol1h)  / (ship_vol2h - ship_vol1h) * 100
        delta_res_ko = round(ko_act_perc - ko_bef_perc,1)

        if ko_act_perc >= 24:
            status_ko = f"🔴 high risk"
            action_kor = "<b>:red[Action required:]</b><br>Check Pack-Stations!"
        elif ko_act_perc >= 18.5:
            status_ko = f"🟡 medium risk"
            action_kor = "<b>:yellow[FYI:]</b><br>Feedback to Packer"
        else:
            status_ko = f"🟢 no risk"

        st.metric("**Kickout Rate** \n\n(30min current)", f"{ko_act_perc}%", f"{delta_res_ko}% vs. previous", delta_color="inverse")
        st.write(status_ko)
        st.markdown(f"{action_kor}", unsafe_allow_html=True)

    with col6:  # Package Problem rate
        action_fnd = ""
        ship_vol2h, ko_vol2h, found_vol2h, ko_rate2h_perc, found_rate2h_perc = ko_data.tail(2).iloc[:, 1:].sum()
        ship_vol1h, ko_vol1h, found_vol1h, ko_rate1h_perc, found_rate1h_perc = ko_data.tail(1).iloc[:, 1:].sum()
        fnd_act_perc = round(found_vol1h / ship_vol1h * 100, 1)
        fnd_bef_perc = (found_vol2h - found_vol1h)  / (ship_vol2h - ship_vol1h) * 100
        delta_res_fnd = round(fnd_act_perc - fnd_bef_perc,1)

        if fnd_act_perc >= 4:
            status_ko = f"🔴 high risk"
            action_fnd = "<b>:red[Action required:]</b><br>Feedback to Packer!"
        elif fnd_act_perc >= 3:
            status_ko = f"🟡 medium risk"
            action_fnd = "<b>:yellow[FYI:]</b><br>Feedback to Packer"
        else:
            status_ko = f"🟢 no risk"

        st.metric("**Package Probl. Rate** \n\n(30min current)", f"{fnd_act_perc}%", f"{delta_res_fnd}% vs. previous", delta_color="off")
        st.write(status_ko)
        st.markdown(f"{action_fnd}", unsafe_allow_html=True)

st.markdown("""<hr style="border-top: 3px double #bbb; border-bottom: none;"><br>""",unsafe_allow_html=True)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # chart Section
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
col1, col2, col3 = st.columns([1,1,1])

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
    ax.axhspan(2.31, 2.3499, color="yellow", alpha=0.05)
    ax.axhspan(2.35, y_max, color="red", alpha=0.05)
    # schöneres Layout
    fig.autofmt_xdate()

    # In Streamlit anzeigen
    st.pyplot(fig)

with col2:
    # Plot Kickout Rate
    ko_data = ko_data.tail(8)
    fig, ax = plt.subplots()
    x = ko_data["timestamp_30min"].dt.strftime("%H:%M")
    y = ko_data["ko_rate_perc"]
    ax.bar(x, y, zorder=3, color="grey")
    ax.tick_params(axis='x', labelsize=8)

    # 👇 Y-axis best praxis for smooth line: min = 3 % below min, max = 2.4 as machine speed limit
    y_min = 0
    y_max = ko_data["ko_rate_perc"].max() - ko_data["ko_rate_perc"].max() * 0.03
    padding = (y_max - y_min) * 0.1 if y_max != y_min else 1

    ax.set_ylim(y_min - padding, y_max + padding)
    fig.patch.set_facecolor("#f7f5f5")

    ax.set_xlabel("time period 30 minutes")
    ax.set_ylabel("kickout rate %")
    bar_value = ax.bar(x, y)
    ax.bar_label(bar_value, color="white", label_type='center')
    ax.set_title("kickout rate % (rolling 4 hours)",fontweight="bold",fontsize=12,pad=10)

    ax.axhspan(y_min, 17.99, color="green", alpha=0.05)
    ax.axhspan(18, 23.99, color="yellow", alpha=0.05)
    ax.axhspan(24, y_max, color="red", alpha=0.05)
    # schöneres Layout
    fig.autofmt_xdate()

    # In Streamlit anzeigen
    st.pyplot(fig)

with col3:
    # Plot Found Rate
    ko_data = ko_data.tail(8)
    fig, ax = plt.subplots()
    x = ko_data["timestamp_30min"].dt.strftime("%H:%M")
    y = ko_data["found_rate_perc"]
    ax.bar(x, y, zorder=3, color="grey")
    ax.tick_params(axis='x', labelsize=8)

    # 👇 Y-axis best praxis for smooth line: min = 3 % below min, max = 2.4 as machine speed limit
    y_min = 0
    y_max = ko_data["found_rate_perc"].max() - ko_data["found_rate_perc"].max() * 0.03
    padding = (y_max - y_min) * 0.1 if y_max != y_min else 1

    ax.set_ylim(y_min - padding, y_max + padding)
    fig.patch.set_facecolor("#f7f5f5")

    ax.set_xlabel("time period 30 minutes")
    ax.set_ylabel("kickout rate %")
    bar_value = ax.bar(x, y)
    ax.bar_label(bar_value, color="white", label_type='center', fmt='%.1f')
    ax.set_title("problem-found rate % (rolling 4 hours)",fontweight="bold",fontsize=12,pad=10)


    # schöneres Layout
    ax.grid(True, color="lightgrey", alpha=0.4)
    fig.autofmt_xdate()

    # In Streamlit anzeigen
    st.pyplot(fig)
