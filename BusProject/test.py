import json
import os

INPUT = "bus_shapes.json"        # your large file
PART_SIZE = 4 * 1024 * 1024      # 4 MB per part
BASE_NAME = "shapes_part"

# Load the big shapes file
print("Loading bus_shapes.json ...")
with open(INPUT, "r") as f:
    data = json.load(f)

items = list(data.items())
total_items = len(items)
print(f"Total shapes: {total_items}")

# Split into parts
part_index = 1
buffer = {}
size_estimate = 0

def save_part(part_number, buffer_dict):
    filename = f"{BASE_NAME}{part_number}.json"
    with open(filename, "w") as f:
        json.dump(buffer_dict, f)
    print(f"Saved: {filename}  ({len(buffer_dict)} shapes)")

for key, value in items:
    # Estimate size of this item
    entry_str = json.dumps({key: value})
    entry_size = len(entry_str.encode("utf-8"))

    if size_estimate + entry_size > PART_SIZE:
        # write current part
        save_part(part_index, buffer)

        # start new part
        part_index += 1
        buffer = {}
        size_estimate = 0

    buffer[key] = value
    size_estimate += entry_size

# Save last part
if buffer:
    save_part(part_index, buffer)

print("\nDONE — All shape parts successfully generated!")
