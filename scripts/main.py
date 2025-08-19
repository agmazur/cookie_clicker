import os
from decode import decode_data_string  
from gamedata_to_csv import shuv_data_to_csv
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "Data", "save64.txt")
with open(file_path, "r", encoding="utf-8") as file:
    raw_string_save = file.read()
data=decode_data_string(raw_string_save)
shuv_data_to_csv(data.get("building_data"))