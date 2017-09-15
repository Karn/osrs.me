import os
import json
import requests
import urllib


class RequestService(object):

    CURRENT_DIR = os.path.dirname(__file__) + '/'

    BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool'
    ITEM_API_ENDPOINT = '/api/catalogue/detail.json?item='

    SAVE_IMAGES = True
    IMAGE_DIR = CURRENT_DIR + '../raw/images/'
    ITEM_DATA_FILE = CURRENT_DIR + '../raw/item-ids_131.json'

    def __init__(self):

        if RequestService.SAVE_IMAGES:
            # Create directory if not exists
            if not os.path.exists(RequestService.IMAGE_DIR):
                os.makedirs(RequestService.IMAGE_DIR)


    def fetch_data_for_item(self, item_id):

        resp = requests.get(url=RequestService.BASE_URL + RequestService.ITEM_API_ENDPOINT + item_id)
        
        print 'Request:', item_id, 'Status:', resp.status_code 
        if resp.status_code != 200:
            return None

        return resp.json()

    def download_image_from_url(self, url, local_file_name):

        urllib.urlretrieve(url, RequestService.IMAGE_DIR + local_file_name)


class FileManager(object):

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


_FileManager = FileManager()
_RequestService = RequestService()

item_list = _FileManager.load_item_data(RequestService.ITEM_DATA_FILE)

print 'Attempting to fetch data for', len(item_list['item']), 'items...'

try:
    for item_id in item_list['item']:

        if 'is_in_exchange' in item_list['item'][item_id]:
            continue

        item_data = _RequestService.fetch_data_for_item(item_id)

        # Skip to next item.
        if item_data is None:
            item_list['item'][item_id]['is_in_exchange'] = False
            continue

        item_list['item'][item_id]['is_in_exchange'] = True
        item_list['item'][item_id]['description'] = item_data['item']['description']
        item_list['item'][item_id]['members'] = item_data['item']['members'] == "true"
            
except Exception as e:
    print 'Error in process. Writing current data to file.'
    print e

_FileManager.write_item_data(RequestService.ITEM_DATA_FILE, item_list)
print 'Success..'

#_RequestService.download_image_from_url(item_image_url, '4151.gif')

