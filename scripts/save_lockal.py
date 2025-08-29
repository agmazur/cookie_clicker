import os
from gamedata_to_csv import shuv_data_to_csv
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "Data", "save64.txt")

# shuv_data_to_csv(data.get("building_data"))
def save_lockal_overwrite(new_save_string):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_save_string)
def save_lockal_load():
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()