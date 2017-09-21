import os
import json
import requests
import urllib
import time
from iterator import FileManager


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

        try: 
            return resp.json()
        except Exception as e:
            print 'Unable to decode json. Potential rate limit, delaying for 30 seconds.'
            for i in range(0, 60):
                time.sleep(1)

            return RequestService.fetch_data_for_item(self, item_id)

    def download_image_from_url(self, url, local_file_name):

        urllib.urlretrieve(url, RequestService.IMAGE_DIR + local_file_name)


_FileManager = FileManager()
_RequestService = RequestService()

item_list = _FileManager.load_item_data(RequestService.ITEM_DATA_FILE)

print 'Attempting to fetch data for', len(item_list['item']), 'items...'

try:
    for i in range(0, 21049):

        item_id = str(i)

        if item_id not in item_list['item']:
            continue

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


    # for item_id in item_list['item']:

    #     if 'is_in_exchange' in item_list['item'][item_id]:
    #         continue

    #     item_data = _RequestService.fetch_data_for_item(item_id)

    #     # Skip to next item.
    #     if item_data is None:
    #         item_list['item'][item_id]['is_in_exchange'] = False
    #         continue

    #     item_list['item'][item_id]['is_in_exchange'] = True
    #     item_list['item'][item_id]['description'] = item_data['item']['description']
    #     item_list['item'][item_id]['members'] = item_data['item']['members'] == "true"
except (KeyboardInterrupt, SystemExit): 
    print 'Exiting due to interrupt...'
except Exception as e:
    print 'Error in process. Writing current data to file.'
    print e

_FileManager.write_item_data(RequestService.ITEM_DATA_FILE, item_list)
print 'Success..'

#_RequestService.download_image_from_url(item_image_url, '4151.gif')

