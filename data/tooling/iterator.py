import os
import json

from pull_data_from_wiki import WikiParser

class FileManager(object):

    CURRENT_DIR = os.path.dirname(__file__) + '/'
    
    ITEM_DATA_FILE = CURRENT_DIR + '../raw/item-ids_131.json'

    def __init__(self):
        pass

    def load_item_data(self, path):
        item_list = None

        with open(path) as item_data_file:    
            item_list = json.load(item_data_file)

        return item_list

    def write_item_data(self, path, json_data):

        with open(path, 'w') as item_data_file:    
            item_data_file.write(json.dumps(json_data, indent=4, sort_keys=True))


class ItemIterator(object):

    def __init__(self):

        pass

    def iterate(self, item_list, executing_function):

        # Iterate for each possible item id in the list of items.
        # for i in range(0, 21049):
        for i in range(0, 1):

            item_id = str(i)

            # If i 
            if item_id not in item_list['item']:
                continue

            executing_function(item_list['item'][item_id])



_ItemIterator = ItemIterator()
_FileManager = FileManager()
_WikiParser = WikiParser()

# Load item list from file.
item_list = _FileManager.load_item_data(FileManager.ITEM_DATA_FILE)

def load_from_wiki(item):

    _WikiParser.fetch_item(item['name'])

_ItemIterator.iterate(item_list, load_from_wiki)