import streamlit as st
import sqlite3
import pandas as pd
import os

### shipment_id, timestamp, severity, thread, source, event, station, box_barcode, articles, exp_weight_kg, act_weight_kg, tare_weight_kg, product_weight_kg
### abs_weight_diff, print_quality_pct, line_speed_mps, slam, iso_grade, pckg_problem_found, weight_diff, weight_diff_ratio, distance_to_threshold, is_kot

filter_time = st.session_state.get("filter_time", "23:59")  # Default optional

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data query from SQLite
# presentation: 03:05, 06:55, 13:35, 15:50, 23:59
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def SQLite_source(filter_time):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "label_machine.db")

    conn = sqlite3.connect(db_path)
    # fetching normalized data
    df_norm = pd.read_sql_query("SELECT shipment_id, strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp, severity,thread, source, event, "
    "station, box_barcode, articles, exp_weight_kg, act_weight_kg, tare_weight_kg, product_weight_kg, abs_weight_diff, print_quality_pct, "
    "line_speed_mps, slam, iso_grade, pckg_problem_found, weight_diff, weight_diff_ratio, "
    "distance_to_threshold, is_kot, stop_after, stop_reason_after FROM shipments WHERE strftime('%H:%M', timestamp) < ?",
        conn, params=(filter_time,)
    )

    # fetching original log raw data
    df_logs = pd.read_sql_query(
        "SELECT strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp, severity, thread, source, log_message, "
        "shipment_id FROM logs_raw WHERE strftime('%H:%M', timestamp) < ?",
        conn, params=(filter_time,)
    )
    conn.close()
    return df_norm, df_logs

def get_data(filter_time):
    return SQLite_source(filter_time)

df_norm, df_logs = get_data(filter_time)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# START ANALYSIS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Conveyor as risk indicator for productivity and package queue conflicts
def kpi_speedconveyor(df_norm):
    # # # produce of relevant dataframe for 'conveyor speed'
    df_norm = df_norm[["timestamp","line_speed_mps"]]
    df_norm = df_norm.dropna(subset=["line_speed_mps"])
    df_norm["timestamp"] = pd.to_datetime(df_norm["timestamp"])
    now = df_norm["timestamp"].max()
    one_hour_ago = now - pd.Timedelta(hours=3)
    # Create of copy for decoupled further calculation
    df_last_hour = df_norm[df_norm["timestamp"] >= one_hour_ago].copy()
    df_last_hour["timestamp_5min"] = df_last_hour["timestamp"].dt.floor("5min")
    df_agg = (df_last_hour.groupby("timestamp_5min", as_index=False).agg(line_speed_mps=("line_speed_mps", "max")))
    df_agg = pd.DataFrame(df_agg)   # just for PyCharm-IDE, otherwise always in code-row below 'by="timestamp_5min"' the hint "unexpected arguments"
    df_agg = df_agg.sort_values(by="timestamp_5min").reset_index(drop=True)
    df_agg["mean_last_6"] = df_agg["line_speed_mps"].rolling(window=6).mean().round(2).fillna(0)
    # creation of final data: chart data, KPI_speed and KPI_speed_prev
    df_chart = df_agg[["timestamp_5min", "mean_last_6"]].tail(24)   # view only the last hour

    return df_chart


# line stops - package queue conflicts
def line_stops_rolled(df_norm):
    df_norm_time = pd.to_datetime(df_norm["timestamp"])
    now = df_norm_time.max()
    df_1hour = now - pd.Timedelta(hours=1)
    df_2hours = now - pd.Timedelta(hours=2)

    pckg_conflicts = df_norm[df_norm["stop_reason_after"] == "Package queue conflicts"][["timestamp","stop_after"]]
    pckg_conflicts["timestamp"] = pd.to_datetime(pckg_conflicts["timestamp"])
    df_2h_rolled = pckg_conflicts[pckg_conflicts["timestamp"] >= df_2hours].copy().reset_index(drop=True)

    count_total = df_2h_rolled["stop_after"].sum()
    count_last_hour = (df_2h_rolled["timestamp"] < df_1hour).sum()
    count_act_hour = (df_2h_rolled["timestamp"] >= df_1hour).sum()

    return df_2h_rolled, count_total, count_last_hour, count_act_hour


# kickout rates + package problem found rates
def kickout_data(df_norm):
    df_norm_ko = df_norm[["timestamp", "shipment_id", "is_kot", "pckg_problem_found"]].copy()
    df_norm_ko["pckg_problem_found"] = pd.to_numeric(df_norm_ko["pckg_problem_found"].replace({"N": "0", "Y": "1", None: "0"}))
    df_norm_ko["timestamp"] = pd.to_datetime(df_norm["timestamp"])
    now = df_norm_ko["timestamp"].max()
    df_4hours = now - pd.Timedelta(hours=4)

    # limit and create a new dataframe to just last 4 hours based on the drop down field in page 'dashboard'
    df_4h_rolled = df_norm_ko[df_norm_ko["timestamp"] >= df_4hours].copy().reset_index(drop=True)

    # add new column for 15min periods
    df_4h_rolled["timestamp_30min"] = df_4h_rolled["timestamp"].dt.floor("30min")

    # create a new dataframe include 15min-period, numbers of shipments processed, sum of kickouts, sum of founds
    df_agg = df_4h_rolled.assign(timestamp_15min=df_4h_rolled["timestamp"].dt.floor("30min")) \
        .groupby("timestamp_30min", as_index=False) \
        .agg(shipvolume=("shipment_id", "count"),
             kickouts=("is_kot", "sum"),
             founds=("pckg_problem_found", "sum"))
    df_agg["ko_rate_perc"] = round(df_agg["kickouts"] / df_agg["shipvolume"] * 100, 1)
    df_agg["found_rate_perc"] = round(df_agg["founds"] / df_agg["shipvolume"] * 100, 1)
    return df_agg

