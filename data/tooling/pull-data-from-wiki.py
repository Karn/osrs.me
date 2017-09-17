# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


class WikiParser(object):

    REGEX = r"{{Infobox (Item|Bonuses)\n(\|(.)*\n)*}}"

    def __init__(self):
        pass

    def fetch_item(self):
        pass

    def parse_item_data(self, group):
        item_data = group.split('\n|')

        item_data_json = {}

        for value in item_data:
            key_val = value.split(' = ')

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
                item_data_json['equipable'] = data_value == 'Yes'
            elif data_key == 'quest':
                item_data_json['quest_item'] = data_value == 'Yes'
            elif data_key == 'store':
                if data_value == 'No':
                    item_data_json['store'] = -1
                else:
                    item_data_json['store']
            elif data_key == 'weight':
                item_data_json['weight'] = float(data_value)
            elif data_key == 'high':
                item_data_json['high_alch'] = int(data_value)
            elif data_key == 'low':
                item_data_json['low_alch'] = int(data_value)

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

test_str = """
{{External|rs}}
{{Infobox Item
|exchange = gemw
|name = Abyssal whip
|image = [[File:Abyssal whip.png]]
|release = 26 January [[2005]]
|update = Slayer Skill
|members = Yes
|tradeable = Yes
|equipable = Yes
|stackable = No
|quest = No
|store = No
|exchange = gemw
|examine = A weapon from the abyss.
|weight = 0.45
|high = 72000
|low = 48000
|destroy = Drop
}}
[[File:Abyssal whip detail.png|130px|left]]
The '''Abyssal whip''' is a powerful one-handed [[Melee weapon]], which requires an [[Attack]] level of 70 to wield. The whip is among the most powerful and popular non-degradable melee weapons and is capable of attacking at the same speed of [[daggers]] and [[scimitars]] at 2.4 seconds per hit.

Alongside being a rare drop from [[abyssal demon]]s, there is a 3/32 chance to obtain an abyssal whip when using [[unsired]], dropped by the [[abyssal sire]], on the [[Font of Consumption]].

A major downside of the abyssal whip is that it is not effective for training [[Strength]]; the only attack option available which will provide Strength [[experience]] is the "lash" attack option, which provides shared experience. As a result, several ostensibly weaker weapons are instead ideal for training Strength directly.

Furthermore, the whip is sparingly used by certain [[pures]] as the wielder '''must''' incur [[Attack]] and/or [[Defence]] experience.

{{Infobox Bonuses
|astab = 0
|aslash = +82
|acrush = 0
|amagic = 0
|arange = 0
|dstab = 0
|dslash = 0
|dcrush = 0
|dmagic = 0
|drange = 0
|str = +82
|prayer = 0
|slot = Weapon
|aspeed = 6
|image = Abyssal whip equipped.png{{!}}120px
|caption = A player wielding an abyssal whip.
}}

==Special attack==
[[File:Energy Drain.gif|frame|A player performing the abyssal whip's special attack, ''Energy drain''.]]
The abyssal whip has a [[special attack]], ''Energy Drain'', which consumes 50% of the player's special attack energy, increases accuracy by 25%, and in [[PVP]], transfers 10% of the target's run energy to the user.

==Upgrading==
Players can attach a [[kraken tentacle]] to the abyssal whip to create an [[abyssal tentacle]], which requires an [[Attack]] level of 75 and has +8 higher [[slash]] attack and +4 higher [[Strength#Strength bonus|Strength bonus]], equating to about 1 higher damage. This process, however, will cause the whip to be consumed, and cannot be undone. Once the abyssal tentacle consumes all of its charges, the player will retain the kraken tentacle.

Players can also use either a [[volcanic whip mix|volcanic]] or [[frozen whip mix]], obtained from the [[Bounty Hunter Store]], to cosmetically enhance the abyssal whip, creating a [[volcanic abyssal whip]] or a [[frozen abyssal whip]], respectively. This only alters its appearance, and causes the whip to become untradeable. It can be reverted by using a [[cleaning cloth]] on the whip, but the mixes will not be returned.

==Dropping monsters==
{{ItemDropsTableHead}}
{{ItemDropsLine|Monster=Abyssal demon|Combat=124|Quantity=1|Rarity=Rare|raritynotes=<small>(1/512)</small>}}
{{ItemDropsLine|Monster=Greater abyssal demon|Combat=342|Quantity=1|Rarity=Rare|raritynotes=<small>(1/512)</small>}}
|}

==Combat styles==
{{CombatStyles|whip}}

== Trivia ==
* An abyssal whip can be used in lieu of a [[knife]] when [[Sliced banana|slicing]] [[Banana|bananas]] despite having no apparent blade.


{{Slash weapons}}
[[Category:Melee weapons]]
[[Category:Equipment]]
[[Category:Slayer]]
[[Category:Weapons with Special attacks]]
[[Category:Items needed for an emote clue]]
"""

_WikiParser = WikiParser()

matches = re.finditer(WikiParser.REGEX, test_str)

for matchNum, match in enumerate(matches):

    group = match.group()

    if group.startswith('{{Infobox Item'):
        print _WikiParser.parse_item_data(group)

    elif group.startswith('{{Infobox Bonuses'):
        print _WikiParser.parse_item_bonuses(group)


    # matchNum = matchNum + 1
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
