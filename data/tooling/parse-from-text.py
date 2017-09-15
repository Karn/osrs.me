import os
import json

lines = None

this_dir = os.path.dirname(__file__)

with open(this_dir + '/../raw/itemlist.txt') as f:
    lines = f.readlines()

item_data = {
    'item': {}
}

# Iterate through all the lines
for line in lines:

    # Split the lines into the item name and its description.
    line_data = line.strip().rsplit('-', 1)
    
    item_id = line_data[1].strip()
    item_name = line_data[0].strip()

    # Construct what will be the structure of the item.
    item_json = {
        'id': int(item_id),
        'name': item_name
    }

    print json.dumps(item_json)
    item_data['item'][item_id] = item_json

with open(this_dir + '/../raw/item-ids_131.json', 'w') as f:
    f.write(json.dumps(item_data, sort_keys=True))