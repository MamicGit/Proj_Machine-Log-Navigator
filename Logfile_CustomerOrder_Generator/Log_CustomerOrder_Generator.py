import random
from datetime import datetime, timedelta

# -----------------------------
# Konfiguration
# -----------------------------

START_TIME = datetime(2026, 1, 12, 0, 2, 0)
end_time   = START_TIME.replace(hour=23, minute=59, second=0)

TOTAL_PACKAGES = 5000
MAX_WEIGHT_KG = 5.9

STATIONS = [f"Station-{i:02}" for i in range(1, 13)]

BOX_TYPES = {
    "BC_SMALL100": 0.090,
    "BC_MEDIUM200": 0.110,
    "BC_LARGE400": 0.130,
    "RK_SMALL60": 0.070,
    "RK_SMALL70": 0.090,
    "RK_SMALL90": 0.120,
    "XX_LARGE60": 0.240,
    "XX_LARGE80": 0.290
}

LABEL_THREADS = ["LabelThread-1", "LabelThread-2", "LabelThread-3", "LabelThread-4"]
VERIFY_THREADS = ["VerifyThread-1", "VerifyThread-2", "VerifyThread-3", "VerifyThread-4"]

SHIFT_TIMES = [6, 14, 22]

# shipment ID generator - Start Zahl immer der aktuelle Zeitstempel als int, JahrMonTagStdMinSek
jetzt = datetime.now()
num_str = f"{jetzt.year%100}{jetzt.month:02d}{jetzt.day:02d}{jetzt.hour:02d}{jetzt.minute:02d}{jetzt.second:02d}"
BASE_SHIPMENT_ID = int(num_str)

# -----------------------------
# Hilfsfunktionen
# -----------------------------

def random_product_weight():
    return round(random.uniform(0.380, 6.0), 3)

def random_speed():
    return round(random.uniform(0.8, 2.4), 2)

def log_line(timestamp, level, thread, it_source, message):
    return f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')},{timestamp.microsecond//1000:03d} {level} [{thread}] {it_source} {message}"

# definieren ab wie viel g Gewicht ein physisches Problem im Paket gefunden wird (Art. fehlt/zu viel)
# nebst Zufalls-Variable 2 da nicht jede Diff ein found/miss sein soll
def physical_problem_found(a, w, d):
    act = a * 1000
    wdf = w * 1000
    random_package = d
    package_problem_fixed = "N"

    if (100 <= act <= 750) and (40 <= wdf <= 50) and random_package == 2:
        package_problem_fixed = "Y"

    if (751 <= act <= 1500) and (60 <= wdf <= 80) and random_package == 2:
        package_problem_fixed = "Y"

    if (1500 <= act <= 3000) and (115 <= wdf <= 135) and random_package == 2:
        package_problem_fixed = "Y"

    if act > 3000 and wdf > 165 and random_package == 2:
        package_problem_fixed = "Y"

    return package_problem_fixed


# -----------------------------
# Real-Industrie-Simulation   |
# -----------------------------

def simulate_day():

    current_time = START_TIME
    logs = []
    print_quality = 100.0
    ribbon_low_counter = 8

    logs.append(log_line(current_time,
                         "INFO",
                         "main",
                         "com.logistic.conveyer.SlamManager:",
                         "System boot completed. 2 labeling machines initialized."))

    shift_index = 0
    shipment_counter = BASE_SHIPMENT_ID
    reorder_buffer = []

    # Steuerung der max. 10–25 TOL>0.05% pro Stunde
    current_hour = current_time.hour                       # Definieren akt Std für KO Limit

    lbl_printer_id = "SLAM5_LP1"
    lbl_printer_ribbon1 = 500
    lbl_printer_ribbon2 = 400


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # for pkg_id in range(1, TOTAL_PACKAGES + 1):
    while current_time < end_time:

        # Spätschicht Produktivität langsamer, weniger Materialverbrauch
        if 16 <= current_hour <= 22:
            current_time += timedelta(seconds=random.uniform(15, 20))   # Log Timestamp immer 10-25sek adden
        else:
            current_time += timedelta(seconds=random.uniform(12, 15))   # Log Timestamp immer 10-25sek adden

        if current_time.hour != current_hour:
            current_hour = current_time.hour

        # wenn Schichtzeiten dann Schichtwechsel log = Paketvertauscher
        if current_time.hour == SHIFT_TIMES[shift_index]:
            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 f"Shift change detected at {SHIFT_TIMES[shift_index]}:00. Initiating controlled stop."))

            reorder_buffer = [shipment_counter + i for i in range(4)]
            reorder_buffer = [
                reorder_buffer[2],
                reorder_buffer[1],
                reorder_buffer[3],
                reorder_buffer[0]
            ]

            shipment_counter += 4
            current_time += timedelta(minutes=5)

            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 "Production line restart completed. Buffer sequence reordered due to conveyor resync."))

            shift_index = (shift_index + 1) % len(SHIFT_TIMES)

        if reorder_buffer:
            shipment_id = reorder_buffer.pop(0)
        else:
            shipment_id = shipment_counter
            shipment_counter += 1

        shipment_str = f"Sp{shipment_id:09d}"       # definieren unserer Shipment-IDs

        # definieren der Gewichte EXP, ACT
        product_weight = random_product_weight()                # mein Basiswert für EXP weight
        box_barcode = random.choice(list(BOX_TYPES.keys()))     # zufällige Auswahl der Verpackungen/Boxes
        tare_weight = BOX_TYPES[box_barcode]                    # Leerverpackungsgewicht

        expected_weight = round(product_weight, 3)              # EXP aus EINEM Artikelgewicht zw. 0.02kg bis 6g

        # aus EXP ein zufälliges ACT weight bestimmen zw.
        actual_rndm_perc = round(random.uniform(0.3, 1.2) if random.random() < 0.7 else random.uniform(1.2, 6.5), 2)    # Pakete können bis zu 3.1% Gewichtsunterschiede haben, 1 von 7 im hohen Bereich
        actual_weight = round(expected_weight - tare_weight - (expected_weight / 100 * actual_rndm_perc), 5)

        weight_diff = round((expected_weight - (tare_weight + actual_weight)), 5)
        weight_diff_perc = weight_diff *100 / expected_weight

    # hier KO threshold (%) manuell anpassen solang. Wir später unser ML Modell übernehmen
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        ko_threshold = 1.2 # <-- manuell auf  1.2% Abweichung bedeutet EXP vs. ACT - TARE > 1.2% führt zu einem QA-Check
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Bandgeschwindigkeit

        speed = random_speed()
        station = random.choice(STATIONS)
        article_count = random.randint(1, 20)

        label_thread = random.choice(LABEL_THREADS)
        verify_thread = random.choice(VERIFY_THREADS)

        # print(shipment_str)
        # print(actual_weight)
        # print(round(weight_diff * 1000,0))

        # -----------------------------
        # Über-Gewicht
        # -----------------------------
        if weight_diff_perc > ko_threshold:
            rd = random.randint(1, 4)
            is_problem_found = physical_problem_found(actual_weight, weight_diff, rd)
            ipf = is_problem_found

            # wenn physisches Problem soll random ACT größer oder kleiner sein, mal fehlen Artikel, mal sind welche zuviel
            if ipf =="Y":
                fnd_miss_rdm = random.randint(1, 2)
                actual_weight_mod = actual_weight if fnd_miss_rdm == 1 else expected_weight - tare_weight + (expected_weight - tare_weight - actual_weight)
            else:
                actual_weight_mod = actual_weight

            logs.append(log_line(current_time,
                                 "WARN",
                                 "KickoutThread-1",
                                 "com.logistic.conveyer.ScaleHandlerSys:",
                                 f"Overweight detected | SHIPMENT_ID={shipment_str} | EXP={expected_weight}kg ACT={actual_weight_mod}kg "
                f"TARE={tare_weight}kg KOT={ko_threshold}% | LIMIT={MAX_WEIGHT_KG}kg | Station={station} | BOX_BARCODE={box_barcode} | PckgProblFound={ipf}"))
            continue

        # -----------------------------
        # Code auffälliger Arbeitsplatz hohe Kickoutrate zwischen Schichtbeginn 06:00 bis 06:30
        # -----------------------------

        if 6 <= current_hour < 7 and (station == 'Station-11' or station == 'Station-12'):
            actual_rndm_perc = round(random.uniform(1.19, 1.2) if random.random() < 0.01 else random.uniform(1.2, 6.5), 2)
            actual_weight = round(expected_weight - tare_weight - (expected_weight / 100 * actual_rndm_perc), 5)
            weight_diff = round((expected_weight - (tare_weight + actual_weight)), 5)

            rd = 2
            is_problem_found = physical_problem_found(actual_weight, weight_diff, rd)
            ipf = is_problem_found

            # wenn physisches Problem soll random ACT größer oder kleiner sein, mal fehlen Artikel, mal sind welche zuviel
            if ipf =="Y":
                fnd_miss_rdm = random.randint(1, 2)
                actual_weight_mod = actual_weight if fnd_miss_rdm == 1 else expected_weight - tare_weight + (expected_weight - tare_weight - actual_weight)
            else:
                actual_weight_mod = actual_weight

            logs.append(log_line(current_time,
                                 "WARN",
                                 "KickoutThread-1",
                                "com.logistic.conveyer.ScaleHandlerSys:",
                                 f"Overweight detected | SHIPMENT_ID={shipment_str} | EXP={expected_weight}kg ACT={actual_weight_mod}kg "
                f"TARE={tare_weight}kg KOT={ko_threshold}% | LIMIT={MAX_WEIGHT_KG}kg | Station={station} | BOX_BARCODE={box_barcode} | PckgProblFound={ipf}"))
            continue

        # -----------------------------
        # Barcode-Verifikation
        # -----------------------------
        if random.random() < 0.03:
            logs.append(log_line(current_time,
                                 "ERROR",
                                  verify_thread,
                                 "com.logistic.conveyer.ScanSystem:",
                                 f"Barcode unreadable (Scan error) | expected SHIPMENT_ID={shipment_str} | BOX_BARCODE={box_barcode}"))


            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.labelmachine.SystemManager:",
                                 f"Manual override approval granted | SHIPMENT_ID={shipment_str}"))
            continue

        # -----------------------------
        # Druck
        # -----------------------------
        logs.append(log_line(current_time,
                             "INFO",
                              label_thread,
                             "com.logistic.labelmachine.SystemManager:",
                             f"Label printed | SHIPMENT_ID={shipment_str} | Station={station} | "
            f"BOX_BARCODE={box_barcode} | PrintQuality={print_quality}% | LineSpeed={speed}m/s SLAM={lbl_printer_id}"))

        # Printqualität des Adresslabeldrucker nimmt unterschiedlich der beiden Printlabeldrucker ab:
        print_quality = print_quality - 0.05625 if lbl_printer_id == "SLAM5_LP2" else print_quality - 0.03125

        if print_quality < 88:
            print_quality += 0.03125    #nach if-Bedingung <88 wieder auf 88% im output heben
            logs.append(log_line(current_time,
                                 "WARN",
                                 "LabelThread-2",
                                 "com.logistic.labelmachine.PrintManager:",
                                 f"Low print quality detected ({print_quality}%). Reprint initiated | SHIPMENT_ID={shipment_str} | SLAM={lbl_printer_id}"))

            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                "Production line stopped for toner refill. Buffer sequence reordered due to conveyor resync."))
            print_quality = 100.000

            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                "Production line restarted. Conveyor resync process succeeded ."))

            logs.append(log_line(current_time,
                                 "INFO",
                                 "MaintenanceThread-1",
                                 "com.logistic.labelmachine.PrintManager:",
                                 f"Resolved, print quality to normal ({print_quality}%). Reprint initiated | SHIPMENT_ID={shipment_str} | SLAM={lbl_printer_id}"))


        logs.append(log_line(current_time,
                             "INFO",
                             verify_thread,
                             "com.logistic.labelmachine.SystemManager:",
                            f"Verification successful | ISO/IEC15416 Grade=A | SHIPMENT_ID={shipment_str}"))

        # -----------------------------
        # Success-Log
        # -----------------------------

        logs.append(log_line(current_time,
                             "INFO",
                             "main",
                             "com.logistic.labelmachine.SystemManager:",
                            f"Package processed successfully | SHIPMENT_ID={shipment_str} | Station={station} | "
            f"EXP={expected_weight}kg ACT={actual_weight}kg "
            f"TARE={tare_weight}kg KOT={ko_threshold}% | "
            f"Articles={article_count} | BOX_BARCODE={box_barcode} | SLAM={lbl_printer_id}"))

        if lbl_printer_id == "SLAM5_LP1":
            lbl_printer_ribbon1 -= 1
            lbl_printer_id = "SLAM5_LP2"
        else:
            lbl_printer_ribbon2 -= 1
            lbl_printer_id = "SLAM5_LP1"

        # -----------------------------
        # ribbon issue
        # -----------------------------
        if lbl_printer_ribbon1 < 20 or lbl_printer_ribbon2 < 20:

            logs.append(log_line(current_time,
                                 "INFO",
                                 "MaintenanceThread-1",
                                 "com.logistic.labelmachine.PrintManager:",
                                f"Ribbon low level detected on SHIPMENT_ID={shipment_str} | Scheduled replacement initiated | ribbonLP1={lbl_printer_ribbon1} | ribbonLP2={lbl_printer_ribbon2}"))
            ribbon_low_counter -= 1

        if (lbl_printer_ribbon1 < 20 or lbl_printer_ribbon2 < 20) and ribbon_low_counter < 2:

            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 "Production line stopped for RIBBON refill. Buffer sequence reordered due to conveyor resync."))
            lbl_printer_ribbon1 = 500
            lbl_printer_ribbon2 = 500
            ribbon_low_counter = 8

            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 f"Production line restarted. Conveyor resync process succeeded | ribbonLP1={lbl_printer_ribbon1} | ribbonLP2={lbl_printer_ribbon2}"))

        # -----------------------------
        # conveyer speed issue
        # -----------------------------
        if speed >= 2.38:
            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 "Production line stopped as of Package queue conflicts. Buffer sequence reordered due to conveyor resync."))
            logs.append(log_line(current_time,
                                 "INFO",
                                 "OperatorConsole",
                                 "com.logistic.conveyer.SlamManager:",
                                 "Production line restarted, Package queue solved. Conveyor resync process succeeded."))

    logs.append(log_line(current_time,
                         "INFO",
                         "main",
                         "com.logistic.conveyer.SlamManager:",
                        "End of 24h production cycle reached. System entering standby mode."))

    return logs

# -----------------------------
# main
# -----------------------------

if __name__ == "__main__":
    logs = simulate_day()

    jetzt = datetime.now()
    filename = f"{START_TIME.year % 10000}{START_TIME.month:02d}{START_TIME.day:02d}"
    print(f"Logdatei: logistic_LOG_DAY{filename}.log")

    path = r"C:\Users\micha\Documents\Projets_Abschlussarbeit\Proj_Machine-Log-Navigator\MLN-log-raw-data"
    file_namepath = f"{path}/logistic_LOG_DAY{filename}.log"

    with open(file_namepath, "w", encoding="utf-8") as f:
        for line in logs:
            f.write(line + "\n")
