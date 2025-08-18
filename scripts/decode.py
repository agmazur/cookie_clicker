import base64
import urllib.parse
def decode_data_string(string):
    with open("save64.txt", "r", encoding="utf-8") as file:
        raw_string_save = file.read()
    url_decoded = urllib.parse.unquote(raw_string_save)
    base64_data = url_decoded.split('!END!')[0]
    decoded_bytes = base64.b64decode(base64_data)

    decoded_str = decoded_bytes.decode('latin1', errors='ignore')  # Use 'latin1' to keep binary structure
    print(f"\033[32m{decoded_str}\033[0m")

    # Step 3: Split by '|'
    parts = decoded_str.split('|')
    game_version_data,_,general_info_data,unlocked_upgrades,bank_stats,building_data,Upgrades,achivements,_,*rest=parts
    current_cookie_balance=bank_stats.split(";")[0]
    my_dict = dict(game_version_data=game_version_data,general_info_data=general_info_data,unlocked_upgrades=unlocked_upgrades)
    return

# part5=parts[5].split(";")
# print(f"\033[35m{part5}\033[0m")
# farm_type_data=[]
# for i, farm_type_info_block in enumerate(part5):
#     farm_type_data.append([])
#     print(farm_type_info_block)
#     for intiger in farm_type_info_block:
#         farm_type_data[i].append(intiger)
#         print(intiger)
# print(farm_type_data)
# # somecoment main