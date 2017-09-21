# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import requests
import json

class WikiParser(object):

    REGEX = r"{{Infobox (Item|Bonuses)\n(\|(.)*\n)*}}"

    WIKI_URL = 'http://oldschoolrunescape.wikia.com/wiki/'
    MODIFIER = '?action=raw'


    def __init__(self):
        pass

    def fetch_item(self, name):
        resp = requests.get(url=WikiParser.WIKI_URL + name + WikiParser.MODIFIER)

        try: 
            if resp.status_code == 200:
                return resp.text
        except Exception as e:
            print 'Unable to decode text.'
        
        return None
        
    def parse_item_data(self, group):
        item_data = group.split('\n|')

        item_data_json = {}

        for value in item_data:
            key_val = value.replace('\n}}', '').split(' = ')

            if len(key_val) != 2:
                continue

            # The relevant data key
            data_key = key_val[0]
            data_value = key_val[1]

            if data_key == 'tradeable':
                item_data_json['tradeable'] = data_value == 'Yes'
            elif data_key == 'equipable':
                item_data_json['equipable'] = data_value == 'Yes'
            elif data_key == 'stackable':
                item_data_json['stackable'] = data_value == 'Yes'
            elif data_key == 'quest':
                item_data_json['quest_item'] = data_value == 'Yes'
            elif data_key == 'members':
                item_data_json['members'] = data_value == 'Yes'
            elif data_key == 'examine':
                item_data_json['description'] = data_value
            elif data_key == 'store' and data_value != 'No':
                item_data_json['store']
            elif data_key == 'weight':
                item_data_json['weight'] = float(data_value)
            elif data_key == 'high' and data_value != 'No':
                item_data_json['high_alch'] = int(data_value)
            elif data_key == 'low' and data_value != 'No':
                item_data_json['low_alch'] = int(data_value)
            elif data_key == 'value' and data_value != 'No':
                item_data_json['store_value'] = int(data_value)

        return item_data_json

    def parse_item_bonuses(self, group):
        item_bonuses = group.split('\n|')

        item_bonuses_json = {
            'attack': {},
            'defence': {},
            'bonus': {}
        }

        for value in item_bonuses:
            key_val = value.split(' = ')

            if len(key_val) != 2:
                continue

            # The relevant data key
            data_key = key_val[0]
            data_value = key_val[1]

            if data_key == 'astab':
                item_bonuses_json['attack']['stab'] = int(data_value)
            elif data_key == 'aslash':
                item_bonuses_json['attack']['slash'] = int(data_value)
            elif data_key == 'acrush':
                item_bonuses_json['attack']['crush'] = int(data_value)
            elif data_key == 'amagic':
                item_bonuses_json['attack']['magic'] = int(data_value)
            elif data_key == 'arange':
                item_bonuses_json['attack']['range'] = int(data_value)
            elif data_key == 'dstab':
                item_bonuses_json['defence']['stab'] = int(data_value)
            elif data_key == 'dslash':
                item_bonuses_json['defence']['slash'] = int(data_value)
            elif data_key == 'dcrush':
                item_bonuses_json['defence']['crush'] = int(data_value)
            elif data_key == 'dmagic':
                item_bonuses_json['defence']['magic'] = int(data_value)
            elif data_key == 'drange':
                item_bonuses_json['defence']['range'] = int(data_value)
            elif data_key == 'str':
                item_bonuses_json['bonus']['strength'] = data_value
            elif data_key == 'rstr':
                item_bonuses_json['bonus']['range_strength'] = data_value
            elif data_key == 'mdmg':
                item_bonuses_json['bonus']['magic_strength'] = data_value
            elif data_key == 'prayer':
                item_bonuses_json['bonus']['prayer'] = data_value
            elif data_key == 'slot':
                item_bonuses_json['item_slot'] = data_value.lower()
            elif data_key == 'aspeed':
                item_bonuses_json['attack_speed'] = float(data_value)

        return item_bonuses_json


    def parse_response(self, response):
        matches = re.finditer(WikiParser.REGEX, response)

        for matchNum, match in enumerate(matches):

            group = match.group()

            if group.startswith('{{Infobox Item'):
                print WikiParser.parse_item_data(self, group)

            elif group.startswith('{{Infobox Bonuses'):
                print WikiParser.parse_item_bonuses(self, group)



if __name__ is '__main__':

    _WikiParser = WikiParser()

    test_str = _WikiParser.fetch_item('dwarf_remains')

    _WikiParser.parse_response(test_str)