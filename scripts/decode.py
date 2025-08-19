import base64
import urllib.parse
def decode_data_string(raw_string_save):
    # Step 1: Decode the base64 string
    url_decoded = urllib.parse.unquote(raw_string_save)
    base64_data = url_decoded.split('!END!')[0]
    decoded_bytes = base64.b64decode(base64_data)

    decoded_str = decoded_bytes.decode('latin1', errors='ignore')  # Use 'latin1' to keep binary structure

    # Step 3: Split by '|'
    parts = decoded_str.split('|')
    game_version_data,_,general_info_data,unlocked_upgrades,bank_stats,building_data,Upgrades,achivements,_,*rest=parts
    my_dict = dict(game_version_data=game_version_data,general_info_data=general_info_data,unlocked_upgrades=unlocked_upgrades,bank_stats=bank_stats,building_data=building_data,Upgrades=Upgrades,achivements=achivements)

    return my_dict

