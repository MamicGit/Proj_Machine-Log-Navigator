import sqlite3
import pandas as pd
import os
from datetime import datetime as dt

### shipment_id, timestamp, severity, thread, source, event, station, box_barcode, articles, exp_weight_kg, act_weight_kg, tare_weight_kg, product_weight_kg
### abs_weight_diff, print_quality_pct, line_speed_mps, slam, iso_grade, pckg_problem_found, weight_diff, weight_diff_ratio, distance_to_threshold, is_kot

def SQLite_source():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "label_machine_neu.db")

    conn = sqlite3.connect(db_path)

    # fetching normalized data
    df_norm = pd.read_sql_query("SELECT shipment_id, strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp, severity,thread, source, event, "
    "station, box_barcode, articles, exp_weight_kg, act_weight_kg, tare_weight_kg, product_weight_kg, abs_weight_diff, print_quality_pct, "
    "line_speed_mps, slam, iso_grade, pckg_problem_found, weight_diff, weight_diff_ratio, distance_to_threshold, is_kot FROM shipments;",
        conn
    )

    # fetching original log data
    df_logs = pd.read_sql_query(
        "SELECT strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp, severity, thread, source, log_message, shipment_id FROM logs_raw;",
        conn
    )
    conn.close()
    return df_norm, df_logs

def get_data():
    return SQLite_source()

df_norm, df_logs = get_data()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# START ANALYSIS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def kpi_speedconveyor(df_norm):
    # # # produce of KPI 'conveyor speed'
    df_norm = df_norm[["timestamp","line_speed_mps"]]
    df_norm = df_norm.dropna(subset=["line_speed_mps"])
    df_norm["timestamp"] = pd.to_datetime(df_norm["timestamp"])
    now = df_norm["timestamp"].max()
    one_hour_ago = now - pd.Timedelta(hours=2)
    # Create of copy for decoupled further calculation
    df_last_hour = df_norm[df_norm["timestamp"] >= one_hour_ago].copy()
    df_last_hour["timestamp_5min"] = df_last_hour["timestamp"].dt.floor("5min")
    df_agg = (df_last_hour.groupby("timestamp_5min", as_index=False).agg(line_speed_mps=("line_speed_mps", "max")))
    df_agg = pd.DataFrame(df_agg)   # just for PyCharm-IDE, otherwise always in code-row below 'by="timestamp_5min"' the hint "unexpected arguments"
    df_agg = df_agg.sort_values(by="timestamp_5min").reset_index(drop=True)
    df_agg["mean_last_6"] = df_agg["line_speed_mps"].rolling(window=6).mean().round(2).fillna(0)
    # creation of final data: chart data, KPI_speed and KPI_speed_prev
    df_chart = df_agg[["timestamp_5min", "mean_last_6"]].tail(12)
    KPI_speed = df_agg["mean_last_6"].iloc[-1]
    KPI_speed_prev = df_agg["mean_last_6"].iloc[-1]

    return KPI_speed,KPI_speed_prev,df_chart

kpi_spd, kpi_spd_prev, kpi_chart = kpi_speedconveyor(df_norm)

print(kpi_chart)

