
import random

from datetime import datetime, timedelta
#
# def random_product_weight():
#     return round(random.uniform(0.020, 6.0), 3)
#
# product_weight = random_product_weight()                # mein Basiswert für EXP weight
# expected_weight = round(product_weight, 3)
# tare_weight = 0.200
#
# actual_weight_rndm_perc = round(random.uniform(0.3, 1.4), 3)
# actual_weight_share_exp = round(expected_weight / (100 / actual_weight_rndm_perc), 5)
# actual_weight = round(((expected_weight - actual_weight_share_exp) + tare_weight), 5)
# Weight_DIFF = round((expected_weight - (actual_weight - tare_weight)) * 1000, 1)
#
# print("EXP: ", expected_weight, "kg")
# print("\n")
# print("random % share from EXP: ", actual_weight_rndm_perc, "%")
# print("EXP Diff kg: ", actual_weight_share_exp, "kg")
# print("Gewicht Leerverpackung: ", tare_weight, "kg")
# print("EXP - (TARE + ) = ACT: ", actual_weight)
# print("\nEXP vs. ACT: ", Weight_DIFF)
#
# jetzt = datetime.now()
# num_str = f"{jetzt.year%100}{jetzt.month:02d}{jetzt.day:02d}{jetzt.hour:02d}{jetzt.minute:02d}{jetzt.second:02d}"
# number = int(num_str)

# STATIONS = [f"Station-{i}" for i in range(1, 13)]
# station = random.choice(STATIONS)
# print(station)

# ==========================================================================================
# START_TIME = datetime(2026, 1, 12, 6, 30, 0)
#
# jetzt = datetime.now()
# filename = f"{START_TIME.year%10000}{START_TIME.month:02d}{START_TIME.day:02d}_V{jetzt.hour:02d}{jetzt.minute:02d}"
# print(filename)
# ==========================================================================================

# lbl_printer_id = "SLAM5_LP2"
# lbl_printer_ribbon1 = 500
# lbl_printer_ribbon2 = 500
#
# if lbl_printer_id == "SLAM5_LP1":
#     lbl_printer_ribbon1 -= 1
#     lbl_printer_id = "SLAM5_LP2"
# else:
#     lbl_printer_ribbon2 -= 1
#     lbl_printer_id = "SLAM5_LP1"
#
#
# print(lbl_printer_id)
# print("RIBBON 1", lbl_printer_ribbon1)
# print("RIBBON 2", lbl_printer_ribbon2)

# ==========================================================================================

# lbl_printer_id = "SLAM5_LP2"
# print_quality = 100
#
# print_quality = print_quality - 0.05625 if lbl_printer_id == "SLAM5_LP2" else print_quality - 0.03125
#
# print(print_quality)

# ==========================================================================================

# START_TIME = datetime(2026, 1, 12, 0, 0, 0)
# current_time = START_TIME
# current_time += timedelta(seconds=random.uniform(10, 25))
#
# print(START_TIME)
# print(current_time)

# ==========================================================================================

# number = round(random.uniform(0.8, 2.4), 1)
# print(number)
#
# random_package = random.randint(1,4)
# print(random_package)

# ==========================================================================================

# def physical_problem_found(ACT, WDF):
#     act = ACT
#     wdf = WDF
#     random_package = random.randint(1,4)
#     package_problem_fixed = "N"
#
#     if (100 <= act <= 750) and (40 <= wdf <= 50) and random_package == 2:
#         package_problem_fixed = "Y"
#
#     if (751 <= act <= 1500) and (60 <= wdf <= 80) and random_package == 2:
#         package_problem_fixed = "Y"
#
#     if (1500 <= act <= 3000) and (115 <= wdf <= 135) and random_package == 2:
#         package_problem_fixed = "Y"
#
#     if act > 3000 and wdf > 165 and random_package == 2:
#         package_problem_fixed = "Y"
#
#     return package_problem_fixed
#
# ACT = 300
# WDF = 45
#
# package_problem_ = physical_problem_found(ACT, WDF)
# print(package_problem_)

# ==========================================================================================

rd = 1
rd = 2 if rd == 1 else 1

print(rd)