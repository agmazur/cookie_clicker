import base64
import urllib.parse

with open("save64.txt", "r", encoding="utf-8") as file:
    raw_string_save = file.read()
url_decoded = urllib.parse.unquote(raw_string_save)
base64_data = url_decoded.split('!END!')[0]
decoded_bytes = base64.b64decode(base64_data)

decoded_str = decoded_bytes.decode('latin1', errors='ignore')  # Use 'latin1' to keep binary structure
print(f"\033[32m{decoded_str}\033[0m")

# Step 3: Split by '|'
parts = decoded_str.split('|')

# Display first parts
for i, part in enumerate(parts[:20]):
    print(f"Part {i}: {part}")

part5=parts[5].split(";")
print(f"\033[35m{part5}\033[0m")
farm_type_data=[]
for i, farm_type_info_block in enumerate(part5):
    farm_type_data.append([])
    print(farm_type_info_block)
    for intiger in farm_type_info_block:
        farm_type_data[i].append(intiger)
        print(intiger)
print(farm_type_data)
# somecoment