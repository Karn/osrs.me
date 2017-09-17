# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"{{Infobox (Item|Bonuses)\n(\|(.)*\n)*}}"

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

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):

    group = match.group()

    if group.startswith('{{Infobox Item'):
        pass
    else group.startswith('{{Infobox Bonuses'):
        pass

    # matchNum = matchNum + 1
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
