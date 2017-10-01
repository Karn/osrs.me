import json
import os
import sys
import traceback

from pull_data_from_wiki import WikiParser
from utils.FileManager import FileManager


class ItemIterator(object):

    def __init__(self):

        pass

    def iterate(self, item_list, executing_function):

        # Iterate for each possible item id in the list of items.
        for i in range(0, 21049):
        # for i in range(4151, 4152):

            item_id = str(i)

            # If i 
            if item_id not in item_list['item']:
                continue

            if 'wiki_mapped' in item_list['item'][item_id]:
                continue

            print 'Fetching data for item with id', item_id

            resp = executing_function(item_list['item'][item_id])

            for key in resp:
                if 'item' in resp:
                    for item_key in resp['item']:
                        item_list['item'][item_id][item_key] = resp['item'][item_key]

                if 'bonuses' in resp:
                    for item_key in resp['bonuses']:
                        if item_key == 'slot' or item_key == 'attack_speed':
                            item_list['item'][item_id][item_key] = resp['bonuses'][item_key]
                        else:
                            if 'stats' not in item_list['item'][item_id]:
                                item_list['item'][item_id]['stats'] = {}
                            item_list['item'][item_id]['stats'][item_key] = resp['bonuses'][item_key]

            item_list['item'][item_id]['wiki_mapped'] = True

_ItemIterator = ItemIterator()
_FileManager = FileManager()
_WikiParser = WikiParser()

# Load item list from file.
item_list = _FileManager.load_item_data(FileManager.ITEM_DATA_FILE)

def load_from_wiki(item):

    response = _WikiParser.fetch_item(item['name'].replace(' ', '_'))

    if response is None:
        return {}

    return _WikiParser.parse_response(response)


item = {
    'id': -1,
    'description': '',
    'equipable': False,
    'members' False,
    'quest_item': False,
    'tradeable': False,
    'stackable': False,
    'weight': 0.0,
}

try:
    _ItemIterator.iterate(item_list, load_from_wiki)
except (KeyboardInterrupt, SystemExit): 
    print 'Exiting due to interrupt...'
except Exception as e:
    print 'Error in process. Writing current data to file.'
    print e
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60

_FileManager.write_item_data(FileManager.ITEM_DATA_FILE, item_list)
print 'Success..'
