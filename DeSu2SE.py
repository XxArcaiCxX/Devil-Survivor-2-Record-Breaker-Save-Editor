#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import sys

print_n = sys.stdout.write

STAT_TXT = ("ST", "MA", "VI", "AG")

# Characters
CHAR_OFFSET = "0x24"
CHAR_ID = ("0x75", 2)
CHAR_LVL = ("0x79", 1)
CHAR_EXP = ("0x7C", 2)
CHAR_HP = ("0x82", 2)
CHAR_MP = ("0x84", 2)
CHAR_ST = ("0x7E", 1)
CHAR_MA = ("0x7F", 1)
CHAR_VI = ("0x80", 1)
CHAR_AG = ("0x81", 1)
CHAR_CMD1 = ("0x86", 1)
CHAR_CMD2 = ("0x87", 1)
CHAR_CMD3 = ("0x88", 1)
CHAR_PAS1 = ("0x89", 1)
CHAR_PAS2 = ("0x8A", 1)
CHAR_PAS3 = ("0x8B", 1)
CHAR_RAC = ("0x8C", 1)
CHAR_MOV = ("0x9F", 1)

# Miscellaneous
MISC_MACCA = ("0x6C4", 4)

# Demons
DE_NUM_MAX = 27
DE_OFFSET = "0x20"
DE_ID = ("0x2B6", 2)
DE_LVL = ("0x2B9", 1)
DE_EXP = ("0x2BC", 2)
DE_HP = ("0x2C2", 2)
DE_MP = ("0x2C4", 2)
DE_ST = ("0x2BE", 1)
DE_MA = ("0x2BF", 1)
DE_VI = ("0x2C0", 1)
DE_AG = ("0x2C1", 1)
DE_CMD1 = ("0x2C6", 1)
DE_CMD2 = ("0x2C7", 1)
DE_CMD3 = ("0x2C8", 1)
DE_PAS1 = ("0x2C9", 1)
DE_PAS2 = ("0x2CA", 1)
DE_PAS3 = ("0x2CB", 1)
DE_RAC = ("0x2CC", 1)

# Skill Information

CMD_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
           '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
           '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
           '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
           '90', '91', '92', '93', '94', '95', '96', '97', '98', '99',
           '100', '101', '102', '103', '104', '105', '106', '107', '108', '109',
           '110', '111', '112', '113', '114', '115', '116', '117', '118', '119',
           '120', '121', '122', '123', '124', '125', '126', '127', '128', '129',
           '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
           '140', '141', '142', '143', '144', '145', '146', '147', '148', '149',
           '150', '151', '152', '153', '154', '155', '156', '157', '158', '159',
           '160', '161', '162', '163', '164', '165', '166', '167', '168', '169',
           '170', '171', '172')

PAS_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
           '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
           '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
           '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
           '90', '91', '92', '93', '94', '95', '96', '97', '98', '99',
           '100', '101', '102', '103', '104', '105', '106', '107')

AUTO_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
            '30', '31', '32', '33', '34', '35', '36', '37', '38', '39')

RAC_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
           '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
           '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
           '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
           '90', '91', '92', '93', '94', '95', '96', '97', '98', '99',
           '100', '101', '102', '103', '104', '105', '106', '107', '108', '109')

DEMON_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
             '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99',
             '100', '101', '102', '103', '104', '105', '106', '107', '108', '109',
             '110', '111', '112', '113', '114', '115', '116', '117', '118', '119',
             '120', '121', '122', '123', '124', '125', '126', '127', '128', '129',
             '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
             '140', '141', '142', '143', '144', '145', '146', '147', '148', '149',
             '150', '151', '152', '153', '154', '155', '156', '157', '158', '159',
             '160', '161', '162', '163', '164', '165', '166', '167', '168', '169',
             '170', '171', '172', '173', '174', '175', '176', '177', '178', '179',
             '180', '181', '182', '183', '184', '185', '186', '187', '188', '189',
             '190', '191', '192', '193', '194', '195', '196', '197', '198', '199',
             '200', '201', '202', '203', '204', '205', '206', '207', '208', '209',
             '210', '211', '212', '213', '214', '215', '216', '217', '218', '219',
             '220', '221', '222', '223', '224', '225', '226', '227', '228', '229',
             '230', '231', '232', '233', '234', '235', '236', '237', '238', '239',
             '240', '241', '242', '243', '244', '245', '246', '247', '248', '249',
             '250', '251', '252', '253', '254', '255', '256', '257', '258', '259',
             '260', '261', '262', '263', '264', '265', '266', '267', '268', '269',
             '270', '271', '272', '273', '274', '275', '276', '277', '278', '279',
             '280', '281', '282', '283', '284', '285', '286', '287', '288', '289',
             '290', '291', '292', '293', '294', '295', '296', '297', '298', '299',
             '300', '301', '302', '303', '304', '305', '306', '307', '308', '309',
             '310', '311', '312', '313', '314', '315', '316', '317', '318', '319',
             '320', '321', '322', '323', '324', '325', '326', '327', '328', '329',
             '330', '331', '332', '333', '334', '335', '336', '337', '338', '339',
             '340', '341', '342', '343', '344', '345', '346', '347', '348', '349',
             '350', '351', '352', '353', '354', '355', '356', '357', '358', '359',
             '360', '361', '362', '363', '364', '365', '366', '367', '368', '369',
             '370', '371', '372', '373', '374', '375', '376', '377', '378', '379',
             '380', '381', '382', '383', '384', '385', '386', '387', '388', '389',
             '390', '391', '392', "65535")

# DONE
CMD_SKILLS = {
    "0": "None",
    "1": "Attack",
    "2": "Agi",
    "3": "Agidyne",
    "4": "Maragi",
    "5": "Maragidyne",
    "6": "Bufu",
    "7": "Bufudyne",
    "8": "Mabufu",
    "9": "Mabufudyne",
    "10": "Zio",
    "11": "Ziodyne",
    "12": "Mazio",
    "13": "Maziodyne",
    "14": "Zan",
    "15": "Zandyne",
    "16": "Mazan",
    "17": "Mazandyne",
    "18": "Megido",
    "19": "Megidolaon",
    "20": "Fire Dance",
    "21": "Ice Dance",
    "22": "Elec Dance",
    "23": "Force Dance",
    "24": "Holy Dance",
    "25": "Drain",
    "26": "Judgement",
    "27": "Petra Eyes",
    "28": "Mute Eyes",
    "29": "Paral Eyes",
    "30": "Death Call",
    "31": "Power Hit",
    "32": "Berserk",
    "33": "Mighty Hit",
    "34": "Anger Hit",
    "35": "Brutal Hit",
    "36": "Hassohappa",
    "37": "Deathbound",
    "38": "Weak Kill",
    "39": "Desperation",
    "40": "Makajamon",
    "41": "Gigajama",
    "42": "Diajama",
    "43": "Makarakarn",
    "44": "Tetrakarn",
    "45": "Might Call",
    "46": "Shield All",
    "47": "Taunt",
    "48": "Dia",
    "49": "Diarahan",
    "50": "Media",
    "51": "Mediarahan",
    "52": "Amrita",
    "53": "Prayer",
    "54": "Recarm",
    "55": "Samerecarm",
    "56": "Gunfire",
    "57": "Guard",
    "58": "Devil's Fuge",
    "59": "Vampiric Mist",
    "60": "Lost Flame",
    "61": "Spawn",
    "62": "Fire of Sodom",
    "63": "Purging Light",
    "64": "Babylon",
    "65": "Megidoladyne",
    "66": "Piercing Hit",
    "67": "Multi-Hit",
    "68": "Holy Strike",
    "69": "Power Charge",
    "70": "Sexy Gaze",
    "71": "Marin Karin",
    "72": "Extra Cancel",
    "73": "Assassinate",
    "74": "Fatal Strike",
    "75": "Diarama",
    "76": "Nigayomogi",
    "77": "Recarmloss",
    "78": "Mow Down",
    "79": "Snipe",
    "80": "Life Drain",
    "81": "Multi-strike",
    "82": "Inferno",
    "83": "Escape",
    "84": "Remain",
    "85": "Double Strike",
    "86": "Binary Fire",
    "87": "Heat Charge",
    "88": "N/A",
    "89": "Marked Wing",
    "90": "Eject Shot",
    "91": "Circumpolarity",
    "92": "N/A",
    "93": "N/A",
    "94": "Hacking",
    "95": "Dark Tunder",
    "96": "Diastrophism",
    "97": "Regenerate",
    "98": "Ultimate Hit",
    "99": "Twin Ultimate",
    "100": "Swallow",
    "101": "N/A",
    "102": "Binary Fire",
    "103": "Circumpolarity",
    "104": "Alkaid",
    "105": "Areadbhar",
    "106": "Dark Thunder",
    "107": "Regenerate",
    "108": "Supernova",
    "109": "Power Up",
    "110": "Ominous Star",
    "111": "Heaven Wrath",
    "112": "Cepheid",
    "113": "Unheard Prayer",
    "114": "Steal Macca",
    "115": "Barrage Strike",
    "116": "Heaven Wrath",
    "117": "Necromancy",
    "118": "Gomorrah Fire",
    "119": "Vitality Drain",
    "120": "Die for Me!",
    "121": "Ruinous Wind",
    "122": "Star Pressure",
    "123": "Ruinous Wind",
    "124": "Diastrophism",
    "125": "Final Hit",
    "126": "Dream Eater",
    "127": "Demon Dance",
    "128": "Roche Lobe",
    "129": "Darkness Blade",
    "130": "Defense Knife",
    "131": "Carney",
    "132": "Then, die!",
    "133": "Don't Hurt Me",
    "134": "Wanna Beating?",
    "135": "Shadow Scythe",
    "136": "No Killing...",
    "137": "Shadow Shield",
    "138": "Nemean Roar",
    "139": "Wider-Radius",
    "140": "Spica Spear",
    "141": "Memory-Sharing",
    "142": "Frozen Pillar",
    "143": "Vicarious Spell",
    "144": "Vicarious Doll",
    "145": "Quaser",
    "146": "Life Plower",
    "147": "Asterion",
    "148": "Partial Blast",
    "149": "Vrano=Metria",
    "150": "Megidoladyne",
    "151": "Darkness Blade(Phys)",
    "152": "Darkness Blade(Fire)",
    "153": "Darkness Blade(Ice)",
    "154": "Darkness Blade(Elec)",
    "155": "Darkness Blade(Force)",
    "156": "Then, die!(Phys)",
    "157": "Then, die!(Phys)",
    "158": "Then, die!(Phys)",
    "159": "Then, die!(Almighty)",
    "160": "Lion's Armor",
    "161": "Ley Line True",
    "162": "Life Plower True",
    "163": "Beheadal",
    "164": "Primal Fire",
    "165": "Gravity Anomaly",
    "166": "Orogin Selection",
    "167": "Earthly Stars",
    "168": "Master of Life",
    "169": "Heavenly Rule",
    "170": "Fringer's Brand",
    "171": "Flaming Fanfare",
    "172": "Ley Line"
}
# DONE
PAS_SKILLS = {
    "0": "None",
    "1": "+Mute",
    "2": "+Poison",
    "3": "+Paralyze",
    "4": "+Stone",
    "5": "Life Bonus",
    "6": "Mana Bonus",
    "7": "Life Surge",
    "8": "Mana Surge",
    "9": "Hero Aid",
    "10": "Ares Aid",
    "11": "Drain Hit",
    "12": "Attack All",
    "13": "Counter",
    "14": "Retaliate",
    "15": "Avenge",
    "16": "Phys Boost",
    "17": "Phys Amp",
    "18": "Fire Boost",
    "19": "Fire Amp",
    "20": "Ice Boost",
    "21": "Ice Amp",
    "22": "Elec Boost",
    "23": "Elec Amp",
    "24": "Force Boost",
    "25": "Force Amp",
    "26": "Anti-Phys",
    "27": "Anti-Fire",
    "28": "Anti-Ice",
    "29": "Anti-Elec",
    "30": "Anti-Force",
    "31": "Anti-Curse",
    "32": "Anti-Most",
    "33": "Anti-All",
    "34": "Null Phys",
    "35": "Null Fire",
    "36": "Null Ice",
    "37": "Null Elec",
    "38": "Null Force",
    "39": "Null Curse",
    "40": "Phys Drain",
    "41": "Fire Drain",
    "42": "Ice Drain",
    "43": "Elec Drain",
    "44": "Force Drain",
    "45": "Phys Repel",
    "46": "Fire Repel",
    "47": "Ice Repel",
    "48": "Elec Repel",
    "49": "Force Repel",
    "50": "Watchful",
    "51": "Vigilant?",
    "52": "Life Aid",
    "53": "Life Lift",
    "54": "Mana Aid",
    "55": "Victory Cry",
    "56": "Pierce",
    "57": "Race-O",
    "58": "Race-D",
    "59": "Dual Shadow",
    "60": "Extra One",
    "61": "Leader Soul",
    "62": "Knight Soul",
    "63": "Paladin Soul",
    "64": "Hero Soul",
    "65": "Beast Eye",
    "66": "Dragon Eye",
    "67": "Crit Up",
    "68": "Dodge",
    "69": "MoneyBags",
    "70": "Quick Move",
    "71": "Vigilant",
    "72": "Grimoire",
    "73": "Double Strike",
    "74": "Perserve Extra",
    "75": "Anti-Element",
    "76": "+Forget",
    "77": "Extra Bonus",
    "78": "Swift Step",
    "79": "Life Stream",
    "80": "Mana Stream",
    "81": "Ultimate Hit",
    "82": "Anti-Almighty",
    "83": "Phys Up",
    "84": "Pacify Human",
    "85": "Dragon Power",
    "86": "True Dragon",
    "87": "Final Dragon",
    "88": "Heavenly Gift",
    "89": "Chaos Stir",
    "90": "Undead",
    "91": "Hidden Strength",
    "92": "Holy Blessing",
    "93": "Exchange",
    "94": "Extra Zero",
    "95": "Spirit Gain",
    "96": "Hit Rate Gain",
    "97": "Quick Wit",
    "98": "Parkour",
    "99": "Hitori Nabe",
    "100": "Ikebukuro King",
    "101": "Immortal Barman",
    "102": "Defenseless",
    "103": "Coiste Bodhar",
    "104": "Dark Courier",
    "105": "Massive Shadow",
    "106": "Hound Eyes",
    "107": "Fighting Doll",
}
# DONE
RAC_SKILLS = {
    "0": "None",
    "1": "Affection",
    "2": "Awakening",
    "3": "Chaos Wave",
    "4": "Constrict",
    "5": "Evil Wave",
    "6": "Blood Wine",
    "7": "Flight",
    "8": "Sacrifice",
    "9": "Switch",
    "10": "Animal Leg",
    "11": "Devil Speed",
    "12": "Phantasm",
    "13": "Glamour",
    "14": "Tyranny",
    "15": "Double Up",
    "16": "Aggravate",
    "17": "Bind",
    "18": "Devotion",
    "19": "Long Range",
    "20": "Immortal",
    "21": "Evil Flame",
    "22": "Hot Flower",
    "23": "Dark Hand",
    "24": "Violent God",
    "25": "King's Gate",
    "26": "King's Gate",
    "27": "Fiend",
    "28": "Four Devas",
    "29": "Dark Finger",
    "30": "Asura Karma",
    "31": "Ghost Wounds",
    "32": "Hero's Mark",
    "33": "Uncanny Form",
    "34": "Asura Destiny",
    "35": "Goddess Grace",
    "36": "Enlightenment",
    "37": "Chaos Breath",
    "38": "Dragon Bind",
    "39": "Evil Flow",
    "40": "Angel Stigma",
    "41": "Winged Flight",
    "42": "Fallen's Mark",
    "43": "Warp Step",
    "44": "Free Leap",
    "45": "Devil Flash",
    "46": "True Phantasm",
    "47": "Fairy Dust",
    "48": "Blood Treaty",
    "49": "Matchless",
    "50": "Agitate",
    "51": "Evil Bind",
    "52": "Mother's Love",
    "53": "Possesion",
    "54": "Hero's Proof",
    "55": "Unearthy Form",
    "56": "Dubhe Proof",
    "57": "Merak Proof",
    "58": "Phecda Proof",
    "59": "Megrez Proof",
    "60": "Alioth Proof",
    "61": "Mizar Proof",
    "62": "Alkaid Proof",
    "63": "Polaris Proof",
    "64": "Alcor Proof",
    "65": "Alcor Warrant",
    "66": "Merak Envoy",
    "67": "Phecda Clone",
    "68": "Megrez Bud",
    "69": "Alioth Shot",
    "70": "Alkaid Bud",
    "71": "Alkaid Spawn",
    "72": "Alkaid Spawn",
    "73": "Alkaid Spawn",
    "74": "Alkaid Spawn",
    "75": "Polaris Proof",
    "76": "Polaris Proof",
    "77": "Heaven Throne",
    "78": "Dragon Shard",
    "79": "Lugh Blessing",
    "80": "Heaven Shield",
    "81": "Bounty Shield",
    "82": "Heaven Spear",
    "83": "Bounty Spear",
    "84": "Temptation",
    "85": "Mizar Proof",
    "86": "Mizar Proof",
    "87": "Star's Gate",
    "88": "Shinjuku Intel",
    "89": "Fighting Doll",
    "90": "Headless Rider",
    "91": "Leonid Five",
    "92": "Spica Sign",
    "93": "Spica Sign",
    "94": "Shiki-Ouji",
    "95": "Arcturus Sign",
    "96": "Miyako",
    "97": "Cor Caroli Sign",
    "98": "Cor Caroli Half",
    "99": "Agent of Order",
    "100": "Universal Law",
    "101": "Factor of Heat",
    "102": "Factor of Power",
    "103": "Factor of Space",
    "104": "Factor of Time",
    "105": "???",
    "106": "Program: Joy",
    "107": "Program: Ultra",
    "108": "Fangs of Order",
    "109": "Gate of Order"
}
# DONE
AUTO_SKILLS = {
    "0": "None",
    "1": "Blitzkrieg",
    "2": "Hustle",
    "3": "Fortify",
    "4": "Barrier",
    "5": "Wall",
    "6": "Full Might",
    "7": "Ban Phys",
    "8": "Ban Fire",
    "9": "Ban Ice",
    "10": "Ban Elec",
    "11": "Ban Force",
    "12": "Ban Curse",
    "13": "Rage Soul",
    "14": "Grace",
    "15": "Marksman",
    "16": "Tailwind",
    "17": "Magic Yin",
    "18": "Battle Aura",
    "19": "Revive",
    "20": "Magic Yang",
    "21": "Healing",
    "22": "Alter Pain",
    "23": "Weaken",
    "24": "Debilitate",
    "25": "Health Save",
    "26": "Strengthen",
    "27": "Grimoire +",
    "28": "Desperation",
    "29": "Rejuvenate",
    "30": "Null Auto",
    "31": "Pierce +",
    "32": "Endure +",
    "33": "Neurotoxin",
    "34": "Temptation",
    "35": "Shield All EX",
    "36": "Dual Shadow EX",
    "37": "Kinetic Vision",
    "38": "Magnet Barrier",
    "39": "Distortion",
}

# Character ID's
ALL_CHARS = {
    "0": "MC",
    "400": "Fumi",
    "300": "Yamato",
    "900": "Keita",
    "800": "Makoto",
    "700": "Jungo",
    "a00": "Airi",
    "b00": "Joe",
    "600": "Otome",
    "500": "Daichi",
    "c00": "Hinako",
    "200": "Io",
    "100": "Ronaldo",
    "d00": "Alcor"
}

# Demon Information
ALL_DEMONS = {
    "0": "Human MC",
    "1": "Human Ronaldo",
    "2": "Human Io",
    "3": "Human Yamato",
    "4": "Human Fumi",
    "5": "Human Daichi",
    "6": "Human Otome",
    "7": "Human Jungo",
    "8": "Human Makoto",
    "9": "Human Keita",
    "10": "Human Airi",
    "11": "Human Joe",
    "12": "Human Hinako",
    "13": "Human Alcor",
    "14": "Omega Tonatiuh",
    "15": "Omega Chernobog",
    "16": "Omega Wu Kong",
    "17": "Omega Susano-o",
    "18": "Omega Kartikeya",
    "19": "Omega Shiva",
    "20": "Megami Hathor",
    "21": "Megami Sarasvati",
    "22": "Megami Kikuri-hime",
    "23": "Megami Brigid",
    "24": "Megami Scathach",
    "25": "Megami Laksmi",
    "26": "Megami Norn",
    "27": "Megami Isis",
    "28": "Megami Amaterasu",
    "29": "Deity Mahakala",
    "30": "Deity Thor",
    "31": "Deity Arahabaki",
    "32": "Deity Odin",
    "33": "Deity Yama",
    "34": "Deity Lugh",
    "35": "Deity Baal",
    "36": "Deity Asura",
    "37": "Vile Orcus",
    "38": "Vile Pazuzu",
    "39": "Vile Abaddon",
    "40": "Vile Tao Tie",
    "41": "Vile Arioch",
    "42": "Vile Tezcatlipoca",
    "43": "Vile Nyarlathotep",
    "44": "Snake Makara",
    "45": "Snake Nozuchi",
    "46": "Snake Pendragon",
    "47": "Snake Gui Xian",
    "48": "Snake Quetzacoatl",
    "49": "Snake Seiyuu",
    "50": "Snake Orochi",
    "51": "Snake Ananta",
    "52": "Snake Hoyau Kamui",
    "53": "Dragon Toubyou",
    "54": "Dragon Bai Suzhen",
    "55": "Dragon Basilisk",
    "56": "Dragon Ym",
    "57": "Dragon Python",
    "58": "Dragon Culebre",
    "59": "Dragon Vritra",
    "60": "Dragon Vasuki",
    "61": "Divine Holy Ghost",
    "62": "Divine Angel",
    "63": "Divine Power",
    "64": "Divine Lailah",
    "65": "Divine Aniel",
    "66": "Divine Kazfiel",
    "67": "Divine Remiel",
    "68": "Divine Metatron",
    "69": "Avian Itsumade",
    "70": "Avian Moh Shuvuu",
    "71": "Avian Hamsa",
    "72": "Avian Suparna",
    "73": "Avian Vidofnir",
    "74": "Avian Badb Catha",
    "75": "Avian Anzu",
    "76": "Avian Feng Huang",
    "77": "Avian Garuda",
    "78": "Fallen Gagyson",
    "79": "Fallen Abraxas",
    "80": "Fallen Flauros",
    "81": "Fallen Nisroc",
    "82": "Fallen Orobas",
    "83": "Fallen Decarabia",
    "84": "Fallen Nebiros",
    "85": "Fallen Agares",
    "86": "Fallen Murmur",
    "87": "Avatar Heqet",
    "88": "Avatar Kamapua'a",
    "89": "Avatar Shiisaa",
    "90": "Avatar Bai Ze",
    "91": "Avatar Baihu",
    "92": "Avatar Airavata",
    "93": "Avatar Ukano Mitama",
    "94": "Avatar Barong",
    "95": "Avatar Anubis",
    "96": "Beast Kabuso",
    "97": "Beast Hairy Jack",
    "98": "Beast Nekomata",
    "99": "Beast Cait Sith",
    "100": "Beast Nue",
    "101": "Beast Orthrus",
    "102": "Beast Myrmecolion",
    "103": "Beast Cerberus",
    "104": "Beast Fenrir",
    "105": "Wilder Hare of Inaba",
    "106": "Wilder Waira",
    "107": "Wilder Garm",
    "108": "Wilder Afanc",
    "109": "Wilder Mothman",
    "110": "Wilder Taown",
    "111": "Wilder Behemoth",
    "112": "Wilder Ammut",
    "113": "Genma Tam Lin",
    "114": "Genma Jambavan",
    "115": "Genma Tlaloc",
    "116": "Genma Ictinike",
    "117": "Genma Hanuman",
    "118": "Genma Cu Chulainn",
    "119": "Genma Kresnik",
    "120": "Genma Ganesha",
    "121": "Genma Heimdal",
    "122": "Fairy Pixie",
    "123": "Fairy Knocker",
    "124": "Fairy Kijimunaa",
    "125": "Fairy Jack Frost",
    "126": "Fairy Pyro Jack",
    "127": "Fairy Silky",
    "128": "Fairy Lorelei",
    "129": "Fairy Vivian",
    "130": "Fairy Titania",
    "131": "Fairy Oberon",
    "132": "Tyrant King Frost",
    "133": "Tyrant Moloch",
    "134": "Tyrant Hecate",
    "135": "Tyrant Tzizimitl",
    "136": "Tyrant Astaroth",
    "137": "Tyrant Mot",
    "138": "Tyrant Loki",
    "139": "Tyrant Lucifer",
    "140": "Kishin Ubelluris",
    "141": "Kishin Nalagiri",
    "142": "Hitokotonusi",
    "143": "Kishin Take-Mikazuchi",
    "144": "Kishin Zouchouten",
    "145": "Kishin Jikokuten",
    "146": "Kishin Koumokuten",
    "147": "Kishin Bishamonten",
    "148": "Kishin Zaou Gongen",
    "149": "Touki Kobold",
    "150": "Touki Bilwis",
    "151": "Touki Gozuki",
    "152": "Touki Mezuki",
    "153": "Touki Ikusa",
    "154": "Touki Lham Dearg",
    "155": "Touki Berserker",
    "156": "Touki Yaksa",
    "157": "Touki Nata Taishi",
    "158": "Touki Oumitsunu",
    "159": "Jaki Obariyon",
    "160": "Jaki Ogre",
    "161": "Jaki Mokoi",
    "162": "Jaki Ogun",
    "163": "Jaki Wendigo",
    "164": "Jaki Legion",
    "165": "Jaki Rakshasa",
    "166": "Jaki Girimehkala",
    "167": "Jaki Grendel",
    "168": "Jaki Black Frost",
    "169": "Femme Kikimora",
    "170": "Femme Lilim",
    "171": "Femme Yuki Jyorou",
    "172": "Femme Leanan Sidhe",
    "173": "Femme Peri",
    "174": "Femme Hariti",
    "175": "Femme Rangda",
    "176": "Femme Kali",
    "177": "Femme Lilith",
    "178": "Ghost Poltergeist",
    "179": "Ghost Agathion",
    "180": "Ghost Tenon Cut",
    "181": "Ghost Kumbhanda",
    "182": "Ghost Loa",
    "183": "Ghost Pisaca",
    "184": "Ghost Kudlak",
    "185": "Ghost Purple Mirror",
    "186": "Fiend Biliken",
    "187": "Fiend Ghost Q ",
    "188": "Fiend Sage of Time",
    "189": "Fiend Alice",
    "190": "Fiend Trumpeter",
    "191": "Hero Neko Shogun",
    "192": "Hero Hagen",
    "193": "Hero Jeanne d'Arc",
    "194": "Hero Yoshitsune",
    "195": "Hero Guan Yu",
    "196": "Element Flaemis",
    "197": "Element Aquans",
    "198": "Element Aeros",
    "199": "Element Erthys",
    "200": "Mitama Ara Mitama",
    "201": "Mitama Nigi Mitama",
    "202": "Mitama Kusi Mitama",
    "203": "Mitama Saki Mitama",
    "204": "Fallen Satan",
    "205": "Fallen Beelzebub",
    "206": "Fallen Belial",
    "207": "Divine Sariel",
    "208": "Divine Anael",
    "209": "Human Atsuro",
    "210": "Human Yuzu",
    "211": "Dragon Asp",
    "212": "Avatar Apis",
    "213": "Avatar Pabilsag",
    "214": "Wilder Sleipnir",
    "215": "Wilder Xiezhai",
    "216": "Genma Kangiten",
    "217": "Vile Baphomet",
    "218": "Famme Anat",
    "219": "Megami Pallas Athena",
    "220": "Deity Mithra",
    "221": "Deity Osiris",
    "222": "Snake Gucumatz",
    "223": "Avian Da Peng",
    "224": "Kishin Ometeotl",
    "225": "Genma Jarilo",
    "226": "Human Miyako",
    "227": "Fallen Botis",
    "228": "Human JP's Member",
    "229": "Human Salaryman(1)",
    "230": "Human Salaryman(2)",
    "231": "Human Salaryman(3)",
    "232": "Fallen Samael",
    "233": "Human Office Lady(1)",
    "234": "Human Office Lady(2)",
    "235": "Human Office Lady(3)",
    "236": "Human Punk(1)",
    "237": "Human Punk(2)",
    "238": "Human Punk(3)",
    "239": "Human Yakuza(1)",
    "240": "Human Yakuza(2)",
    "241": "Device Module",
    "242": "Human Policeman",
    "243": "Human JP's Member(F)",
    "244": "Human JP's Member(M)",
    "245": "Human Young Man(?)",
    "246": "Human Old Woman(?)",
    "247": "Human Worker",
    "248": "Human Student",
    "249": "Human Young man",
    "250": "Human Buffer(1)",
    "251": "Human Buffer(2)",
    "252": "Human JP'S Agent(?)",
    "253": "Human JP'S Agent(?)",
    "254": "Human JP'S Agent(?)",
    "255": "Human JP'S Agent(?)",
    "256": "Human ?",
    "257": "Fallen Bifrons",
    "258": "Fallen Barbatos",
    "259": "Femme Dzelarhons",
    "260": "Genma Kama",
    "261": "Megami Parvati",
    "262": "Femme Ixtab",
    "263": "Tyrant Balor",
    "264": "Tyrant Negral",
    "265": "Deity Inti",
    "266": "Deity Alilat",
    "267": "Omega Beji-Weng",
    "268": "Deity Lord Nan Dou",
    "269": "Hero Masakado",
    "270": "Megami Ishtar",
    "271": "Megami Black Maria",
    "272": "Snake Yurlungr",
    "273": "Dragon Fafnir",
    "274": "Divine Sraosha",
    "275": "Avian Rukh",
    "276": "Avian Kau",
    "277": "Beast Cbracan",
    "278": "Beast Catoblepas",
    "279": "Genma Roitschaggata",
    "280": "Fairy Spriggan",
    "281": "Fairy Troll",
    "282": "Tyrant Lucifuge",
    "283": "Kishin Okuninushi",
    "284": "Touki Dokkaebi",
    "285": "Touki Ongyo-Ki",
    "286": "Jaki Macabre",
    "287": "Femme Jahi",
    "288": "Divine Sandalphon",
    "289": "Snake Kohruy",
    "290": "Exotic Izaya",
    "291": "Exotic Celty",
    "292": "Exotic Shizuo",
    "293": "Touki Momunofu",
    "294": "Tyrant Lucifer Frost",
    "295": "(Crashes GUI)",
    "296": "Hero Frost Five",
    "297": "Hero Milk-Kin Frost",
    "298": "Hero Strawberry Fost",
    "299": "Fairy Lemon Frost",
    "300": "Fairy Melon Frost",
    "301": "Fairy B. Hawaii Frost",
    "302": "Touki Titan",
    "303": "Omega Dyonisus",
    "304": "Omega Aramisaki",
    "305": "Jaki Shiki-Ouji",
    "306": "Feeme Xi Wangmu",
    "307": "Divine Dominion",
    "308": "Fiend Mother Harlot",
    "309": "Fiend Dantalian",
    "310": "Vile Seth",
    "311": "Jaki Shinigami",
    "312": "Bel Belberith",
    "313": "Bel Jezebel",
    "314": "Bel Beldr",
    "315": "Maggot Maggot",
    "316": "Star Dubhe",
    "317": "Star Merak",
    "318": "Star Phecda",
    "319": "Star Megrez",
    "320": "Star Alioth Core",
    "321": "Star Mizar",
    "322": "Star Benetnasch",
    "323": "Star Alcor",
    "324": "Star Polaris",
    "325": "Star Merak Missile",
    "326": "Star Phecda(WK MAG)",
    "327": "Star Phecda(WK PHYS)",
    "328": "Star Megrez(Empty)",
    "329": "Star Alioth (Poison)",
    "330": "Energy LayLine Dragon",
    "331": "Star Dubhe",
    "332": "Star Dunhe(weak)",
    "333": "Star Mizar",
    "334": "Star Mizar",
    "335": "Star Tentacle",
    "336": "Star Tentacle",
    "337": "Star Tentacle",
    "338": "Star Tentacle",
    "339": "Star Tentacle",
    "340": "Star Tentacle",
    "341": "Star Benetnasch(dubhe)",
    "342": "Star Benetnasch(merak)",
    "343": "Star Benetnasch(phecda)",
    "344": "Star Benetnasch(Alioth)",
    "345": "Star Benetnasch",
    "346": "Star Alcor",
    "347": "Star Polaris A",
    "348": "Star Polaris Ab",
    "349": "Star Polaris B",
    "350": "Human Tall Woman",
    "351": "Device Tico",
    "352": "Device Tico",
    "353": "Human Daichi",
    "354": "Human Io",
    "355": "Human Io",
    "356": "Human MC",
    "357": "Human SDF Captain",
    "358": "Human SDF Member",
    "359": "Human Fireman",
    "360": "Deity Io",
    "361": "Star Guardian",
    "362": "Star Guardian",
    "363": "Star Guardian",
    "364": "Star Guardian",
    "365": "Star Guardian",
    "366": "Star Guardian",
    "367": "Star Guardian",
    "368": "Human Salaryman(1)",
    "369": "Human Punk(1)",
    "370": "Human Student(1)",
    "371": "Human Student(2)",
    "372": "Human Young Man(1)",
    "373": "Human Young Man(2)",
    "374": "Human Salaryman(2)",
    "375": "Human Salaryman(3)",
    "376": "Human Punk(2)",
    "377": "Human Punk(3)",
    "378": "Human Kitten",
    "379": "Human @",
    "380": "Human Ronaldo*",
    "381": "Human Io*",
    "382": "Human Yamato*",
    "383": "Human Fumi*",
    "384": "Human Daichi*",
    "385": "Human Otome*",
    "386": "Human Jungo*",
    "387": "Human Makoto*",
    "388": "Human Keita*",
    "389": "Human Airi*",
    "390": "Human Joe*",
    "391": "Human Hinako*",
    "392": "Human Alcor*",
    "65535": "Empty"
}


class mytestapp(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.minsize(400, 100)
        self.title("Devil Survivor 2 Record Breaker Save Editor")
        self.bind(sequence="<Escape>", func=lambda x: self.quit())
        self.resizable(width="False", height="False")
        self.grid()

        self.initVars()
        self.processLists()
        self.createWidgets()
        # x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        # y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        # self.geometry("+%d+%d" % (x, y))
        # self.initialSetup()

    def initVars(self):
        self.saveFilePath = None
        self.saveFileDir = None
        self.saveFileName = None
        self.save_bytes = None
        self.charValues = {}
        self.curChar = {}
        self.curDemon = {}
        self.charNameList = []
        self.demonNameList = []
        self.charList = []
        self.demonList = []
        self.vcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

    def processLists(self):
        skillIDNameList = []
        # max_width = 0
        for val in CMD_IDS:
            if val in CMD_SKILLS:
                # tmp_str = val + " - " + ALL_SKILLS[val][0]
                # if len(tmp_str) > max_width:
                #     max_width = len(tmp_str)
                skillIDNameList.append(val + " - " + CMD_SKILLS[val])
            else:
                skillIDNameList.append(val + " - None")
        self.skillIDNameList = skillIDNameList
        # self.skillIDNameWidth = max_width

    def createWidgets(self):
        # Menu bar
        menubar = tk.Menu(self)
        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Open Save File", underline=0, command=self.openFileChooser)
        submenu1.add_command(label="Save Changes", underline=0, command=self.saveChanges)
        submenu1.add_separator()
        submenu1.add_command(label="Exit", underline=0, command=self.exitApp)
        menubar.add_cascade(label="File", underline=0, menu=submenu1)
        menubar.add_separator()
        # submenu2 = tk.Menu(menubar, tearoff=0)
        # submenu2.add_command(label="Compare difference(s)", command=self.>Diff)
        # menubar.add_cascade(label="Compare", menu=submenu2)
        menubar.add_command(label="About", command=self.aboutCreator)
        menubar.add_command(label="Help", command=self.help)
        self.config(menu=menubar)

        # Main content frame
        mainFrame = tk.Frame(self)
        mainFrame.grid(column=0, row=0, padx=10, pady=10, sticky="EW")
        self.mainFrame = mainFrame

        # Frame for folder paths
        folderpathFrame = tk.Frame(mainFrame)
        folderpathFrame.grid(column=0, row=1, sticky="EW")
        folderpathFrame.grid_columnconfigure(1, weight=1)
        tk.Label(folderpathFrame, text="Save file: ").grid(column=0, row=1, sticky="W")
        self.saveFilePathTxt = tk.StringVar()
        tk.Entry(
            folderpathFrame, textvariable=self.saveFilePathTxt, state='readonly', width=80
        ).grid(column=1, row=1, sticky="EW", padx="5 0")

        # Frame for tab buttons
        tabButtonsFrame = tk.Frame(mainFrame)
        tabButtonsFrame.grid(column=0, row=2, pady="20 0", sticky="EW")
        self.tab1Button = tk.Button(
            tabButtonsFrame, text="Characters", relief="sunken", state="disabled",
            command=lambda: self.changeTab(self.tab1Frame, self.tab1Button)
        )
        self.tab1Button.grid(column=0, row=0, sticky="W")
        self.tab2Button = tk.Button(
            tabButtonsFrame, text="Demons",
            command=lambda: self.changeTab(self.tab2Frame, self.tab2Button)
        )
        self.tab2Button.grid(column=1, row=0, sticky="W")

        # Frame for tab frames
        tabFramesFrame = tk.Frame(mainFrame)
        tabFramesFrame.grid(column=0, row=3, sticky="EW")
        tabFramesFrame.columnconfigure(0, weight=1)

        # Frame for 1st tab
        tab1Frame = tk.Frame(tabFramesFrame, bd="2", relief="sunken", padx="10", pady="10")
        self.tab1Frame = tab1Frame
        tab1Frame.grid(column=0, row=0, sticky="EW")

        # Top inner frame for 1st tab
        tab1TopFrame = tk.Frame(tab1Frame)
        tab1TopFrame.grid(column=0, row=0, columnspan=2, sticky="NW")

        # Top left inner frame for 1st tab
        tab1TopLFrame = tk.Frame(tab1TopFrame)
        tab1TopLFrame.grid(column=0, row=0, sticky="NW")
        tab1ComboLabel = tk.Label(tab1TopLFrame, text="Select Character")
        tab1ComboLabel.grid(column=1, row=0)

        # ComboBox
        tab1ComboBox = ttk.Combobox(tab1TopLFrame, values=self.charNameList)
        print(self.charNameList)
        tab1ComboBox.grid(column=2, row=0, padx=10, pady=10)

        def changeCharacter(*args):
            name = tab1ComboBox.get()

            def get_key(val):
                for char_info in self.charList:
                    for key, value in char_info.items():
                        if val == value:
                            return char_info

            self.curChar = get_key(name)
            print(self.curChar)
            tab1txtbLVL.delete(0, 5)
            tab1txtbLVL.insert(0, self.curChar["level"])
            tab1txtbEXP.delete(0, 5)
            tab1txtbEXP.insert(0, self.curChar["exp"])
            tab1txtbHP.delete(0, 5)
            tab1txtbHP.insert(0, self.curChar["hp"])
            tab1txtbMP.delete(0, 5)
            tab1txtbMP.insert(0, self.curChar["mp"])
            tab1txtbST.delete(0, 5)
            tab1txtbST.insert(0, self.curChar["st"])
            tab1txtbMA.delete(0, 5)
            tab1txtbMA.insert(0, self.curChar["ma"])
            tab1txtbVI.delete(0, 5)
            tab1txtbVI.insert(0, self.curChar["vi"])
            tab1txtbAG.delete(0, 5)
            tab1txtbAG.insert(0, self.curChar["ag"])
            tab1txtbCMD1.delete(0, 5)
            tab1txtbCMD1.insert(0, self.curChar["cmd1"])
            tab1txtbCMD2.delete(0, 5)
            tab1txtbCMD2.insert(0, self.curChar["cmd2"])
            tab1txtbCMD3.delete(0, 5)
            tab1txtbCMD3.insert(0, self.curChar["cmd3"])
            tab1txtbPAS1.delete(0, 5)
            tab1txtbPAS1.insert(0, self.curChar["pas1"])
            tab1txtbPAS2.delete(0, 5)
            tab1txtbPAS2.insert(0, self.curChar["pas2"])
            tab1txtbPAS3.delete(0, 5)
            tab1txtbPAS3.insert(0, self.curChar["pas3"])
            tab1txtbRAC.delete(0, 5)
            tab1txtbRAC.insert(0, self.curChar["rac"])
            tab1txtbMOV.delete(0, 5)
            tab1txtbMOV.insert(0, self.curChar["mov"])

        tab1ComboBox.bind("<<ComboboxSelected>>", changeCharacter)

        # Labels
        tab1LVL = tk.Label(tab1TopLFrame, text="Level:", padx=50)
        tab1LVL.grid(column=0, row=1)
        tab1EXP = tk.Label(tab1TopLFrame, text="Experience:")
        tab1EXP.grid(column=0, row=2)
        tab1HP = tk.Label(tab1TopLFrame, text="Health:")
        tab1HP.grid(column=0, row=3)
        tab1MP = tk.Label(tab1TopLFrame, text="Mana:")
        tab1MP.grid(column=0, row=4)
        tab1ST = tk.Label(tab1TopLFrame, text="Strength:")
        tab1ST.grid(column=0, row=5)
        tab1MA = tk.Label(tab1TopLFrame, text="Magic:")
        tab1MA.grid(column=0, row=6)
        tab1VI = tk.Label(tab1TopLFrame, text="Vitality:")
        tab1VI.grid(column=0, row=7)
        tab1AG = tk.Label(tab1TopLFrame, text="Agility:")
        tab1AG.grid(column=0, row=8)
        tab1CMD1 = tk.Label(tab1TopLFrame, text="Command 1:")
        tab1CMD1.grid(column=2, row=1)
        tab1CMD2 = tk.Label(tab1TopLFrame, text="Command 2:")
        tab1CMD2.grid(column=2, row=2)
        tab1CMD3 = tk.Label(tab1TopLFrame, text="Command 3:")
        tab1CMD3.grid(column=2, row=3)
        tab1PAS1 = tk.Label(tab1TopLFrame, text="Passive 1:")
        tab1PAS1.grid(column=2, row=4)
        tab1PAS2 = tk.Label(tab1TopLFrame, text="Passive 2:")
        tab1PAS2.grid(column=2, row=5)
        tab1PAS3 = tk.Label(tab1TopLFrame, text="Passive 3:")
        tab1PAS3.grid(column=2, row=6)
        tab1RAC = tk.Label(tab1TopLFrame, text="Automatic:")
        tab1RAC.grid(column=2, row=7)
        tab1MOV = tk.Label(tab1TopLFrame, text="Move:")
        tab1MOV.grid(column=2, row=8)

        # Text Boxes
        tab1txtbLVL = tk.Entry(tab1TopLFrame)
        tab1txtbLVL.grid(column=1, row=1)
        tab1txtbEXP = tk.Entry(tab1TopLFrame)
        tab1txtbEXP.grid(column=1, row=2)
        tab1txtbHP = tk.Entry(tab1TopLFrame)
        tab1txtbHP.grid(column=1, row=3)
        tab1txtbMP = tk.Entry(tab1TopLFrame)
        tab1txtbMP.grid(column=1, row=4)
        tab1txtbST = tk.Entry(tab1TopLFrame)
        tab1txtbST.grid(column=1, row=5)
        tab1txtbMA = tk.Entry(tab1TopLFrame)
        tab1txtbMA.grid(column=1, row=6)
        tab1txtbVI = tk.Entry(tab1TopLFrame)
        tab1txtbVI.grid(column=1, row=7)
        tab1txtbAG = tk.Entry(tab1TopLFrame)
        tab1txtbAG.grid(column=1, row=8)
        tab1txtbCMD1 = tk.Entry(tab1TopLFrame)
        tab1txtbCMD1.grid(column=3, row=1)
        tab1txtbCMD2 = tk.Entry(tab1TopLFrame)
        tab1txtbCMD2.grid(column=3, row=2)
        tab1txtbCMD3 = tk.Entry(tab1TopLFrame)
        tab1txtbCMD3.grid(column=3, row=3)
        tab1txtbPAS1 = tk.Entry(tab1TopLFrame)
        tab1txtbPAS1.grid(column=3, row=4)
        tab1txtbPAS2 = tk.Entry(tab1TopLFrame)
        tab1txtbPAS2.grid(column=3, row=5)
        tab1txtbPAS3 = tk.Entry(tab1TopLFrame)
        tab1txtbPAS3.grid(column=3, row=6)
        tab1txtbRAC = tk.Entry(tab1TopLFrame)
        tab1txtbRAC.grid(column=3, row=7)
        tab1txtbMOV = tk.Entry(tab1TopLFrame)
        tab1txtbMOV.grid(column=3, row=8)

        tab1emptylabel = tk.Label(tab1TopLFrame, text="   ")
        tab1emptylabel.grid(column=0, row=9)

        # Skill Frame
        tab1SkillFrame = tk.Frame(tab1TopLFrame, bd="2", relief="sunken")
        tab1SkillFrame.grid(column=0, row=11, columnspan=4)

        # Skill Labels
        tab1CMD1label = tk.Label(tab1SkillFrame, text="Command")
        tab1CMD1label.grid(column=0, row=0)
        tab1CMD2label = tk.Label(tab1SkillFrame, text="Passive")
        tab1CMD2label.grid(column=1, row=0)
        tab1CMD3label = tk.Label(tab1SkillFrame, text="Automatic")
        tab1CMD3label.grid(column=2, row=0)

        # Listboxes
        tab1ListBoxCMD = tk.Listbox(tab1SkillFrame)
        for i in range(0, len(CMD_IDS)):
            tab1ListBoxCMD.insert(i, " " + str(CMD_IDS[i]) + " - " + str(CMD_SKILLS[CMD_IDS[i]]))
        tab1ListBoxCMD.grid(column=0, row=1)

        tab1ListBoxPAS = tk.Listbox(tab1SkillFrame)
        for i in range(0, len(PAS_IDS)):
            tab1ListBoxPAS.insert(i, " " + str(PAS_IDS[i]) + " - " + str(PAS_SKILLS[PAS_IDS[i]]))
        tab1ListBoxPAS.grid(column=1, row=1)

        tab1ListBoxAUT = tk.Listbox(tab1SkillFrame)
        for i in range(0, len(AUTO_IDS)):
            tab1ListBoxAUT.insert(i, " " + str(AUTO_IDS[i]) + " - " + str(AUTO_SKILLS[AUTO_IDS[i]]))
        tab1ListBoxAUT.grid(column=2, row=1)

        # Save Characters Changes
        def applyCharChange(*args):

            print("\n BEFORE APPLY \n " + str(self.charList))

            name = tab1ComboBox.get()
            if self.curChar != {}:

                def get_key(val):
                    i = -1
                    for char_info in self.charList:
                        i = i + 1
                        for key, value in char_info.items():
                            if val == value:
                                return i, char_info

                index, self.cur_char = get_key(name)

                # put textbox values in global variable
                self.curChar["level"] = tab1txtbLVL.get()
                self.curChar["exp"] = tab1txtbEXP.get()
                self.curChar["hp"] = tab1txtbHP.get()
                self.curChar["mp"] = tab1txtbMP.get()
                self.curChar["st"] = tab1txtbST.get()
                self.curChar["ma"] = tab1txtbMA.get()
                self.curChar["vi"] = tab1txtbVI.get()
                self.curChar["ag"] = tab1txtbAG.get()
                self.curChar["cmd1"] = tab1txtbCMD1.get()
                self.curChar["cmd2"] = tab1txtbCMD2.get()
                self.curChar["cmd3"] = tab1txtbCMD3.get()
                self.curChar["pas1"] = tab1txtbPAS1.get()
                self.curChar["pas2"] = tab1txtbPAS2.get()
                self.curChar["pas3"] = tab1txtbPAS3.get()
                self.curChar["rac"] = tab1txtbRAC.get()
                self.curChar["mov"] = tab1txtbMOV.get()

                print("\n AFTER APPLY \n " + str(self.charList))

                # put char_info back on list
                self.charList[index] = self.curChar

        # Bottom Frame
        tab1BtmFrame = tk.Frame(tab1Frame, bd="2", relief="sunken")
        tab1BtmFrame.grid(column=0, row=2, columnspan=2, sticky="EW", pady="20 0")
        tab1BtmFrame.columnconfigure(0, weight=1)
        tk.Button(
            tab1BtmFrame, text="Apply", command=applyCharChange
        ).grid(column=0, row=0, sticky="EW")

        # Frame for 2nd tab
        tab2Frame = tk.Frame(tabFramesFrame, bd="2", relief="sunken", padx="10", pady="10")
        self.tab2Frame = tab2Frame
        tab2Frame.grid(column=0, row=0, sticky="EW")

        # Top inner frame for 2nd tab
        tab2TopFrame = tk.Frame(tab2Frame)
        tab2TopFrame.grid(column=0, row=0, columnspan=2, sticky="NW")

        # Top left inner frame for 2nd tab
        tab2TopLFrame = tk.Frame(tab2TopFrame)
        tab2TopLFrame.grid(column=0, row=0, sticky="NW")
        tab2ComboLabel = tk.Label(tab2TopLFrame, text="Select Demon")
        tab2ComboLabel.grid(column=1, row=0)

        # 2nd ComboBox
        tab2ComboBox = ttk.Combobox(tab2TopLFrame, values=self.demonNameList)
        print(self.demonNameList)
        tab2ComboBox.grid(column=2, row=0, padx=10, pady=10)

        def changeDemon(*args):
            index = tab2ComboBox.current()
            self.curDemon = self.demonList[index]

            print(self.curDemon)
            tab2txtbLVL.delete(0, 5)
            tab2txtbLVL.insert(0, self.curDemon["level"])
            tab2txtbEXP.delete(0, 5)
            tab2txtbEXP.insert(0, self.curDemon["exp"])
            tab2txtbHP.delete(0, 5)
            tab2txtbHP.insert(0, self.curDemon["hp"])
            tab2txtbMP.delete(0, 5)
            tab2txtbMP.insert(0, self.curDemon["mp"])
            tab2txtbST.delete(0, 5)
            tab2txtbST.insert(0, self.curDemon["st"])
            tab2txtbMA.delete(0, 5)
            tab2txtbMA.insert(0, self.curDemon["ma"])
            tab2txtbVI.delete(0, 5)
            tab2txtbVI.insert(0, self.curDemon["vi"])
            tab2txtbAG.delete(0, 5)
            tab2txtbAG.insert(0, self.curDemon["ag"])
            tab2txtbCMD1.delete(0, 5)
            tab2txtbCMD1.insert(0, self.curDemon["cmd1"])
            tab2txtbCMD2.delete(0, 5)
            tab2txtbCMD2.insert(0, self.curDemon["cmd2"])
            tab2txtbCMD3.delete(0, 5)
            tab2txtbCMD3.insert(0, self.curDemon["cmd3"])
            tab2txtbPAS1.delete(0, 5)
            tab2txtbPAS1.insert(0, self.curDemon["pas1"])
            tab2txtbPAS2.delete(0, 5)
            tab2txtbPAS2.insert(0, self.curDemon["pas2"])
            tab2txtbPAS3.delete(0, 5)
            tab2txtbPAS3.insert(0, self.curDemon["pas3"])
            tab2txtbRAC.delete(0, 5)
            tab2txtbRAC.insert(0, self.curDemon["rac"])
            tab2txtbID.delete(0, 5)
            tab2txtbID.insert(0, self.curDemon["id"])

        tab2ComboBox.bind("<<ComboboxSelected>>", changeDemon)

        # Labels
        tab2LVL = tk.Label(tab2TopLFrame, text="Level:", padx=50)
        tab2LVL.grid(column=0, row=1)
        tab2EXP = tk.Label(tab2TopLFrame, text="Experience:")
        tab2EXP.grid(column=0, row=2)
        tab2HP = tk.Label(tab2TopLFrame, text="Health:")
        tab2HP.grid(column=0, row=3)
        tab2MP = tk.Label(tab2TopLFrame, text="Mana:")
        tab2MP.grid(column=0, row=4)
        tab2ST = tk.Label(tab2TopLFrame, text="Strength:")
        tab2ST.grid(column=0, row=5)
        tab2MA = tk.Label(tab2TopLFrame, text="Magic:")
        tab2MA.grid(column=0, row=6)
        tab2VI = tk.Label(tab2TopLFrame, text="Vitality:")
        tab2VI.grid(column=0, row=7)
        tab2AG = tk.Label(tab2TopLFrame, text="Agility:")
        tab2AG.grid(column=0, row=8)
        tab2CMD1 = tk.Label(tab2TopLFrame, text="Command 1:")
        tab2CMD1.grid(column=2, row=1)
        tab2CMD2 = tk.Label(tab2TopLFrame, text="Command 2:")
        tab2CMD2.grid(column=2, row=2)
        tab2CMD3 = tk.Label(tab2TopLFrame, text="Command 3:")
        tab2CMD3.grid(column=2, row=3)
        tab2PAS1 = tk.Label(tab2TopLFrame, text="Passive 1:")
        tab2PAS1.grid(column=2, row=4)
        tab2PAS2 = tk.Label(tab2TopLFrame, text="Passive 2:")
        tab2PAS2.grid(column=2, row=5)
        tab2PAS3 = tk.Label(tab2TopLFrame, text="Passive 3:")
        tab2PAS3.grid(column=2, row=6)
        tab2RAC = tk.Label(tab2TopLFrame, text="Racial:")
        tab2RAC.grid(column=2, row=7)
        tab2ID = tk.Label(tab2TopLFrame, text="Id:")
        tab2ID.grid(column=2, row=8)

        # Text Boxes
        tab2txtbLVL = tk.Entry(tab2TopLFrame)
        tab2txtbLVL.grid(column=1, row=1)
        tab2txtbEXP = tk.Entry(tab2TopLFrame)
        tab2txtbEXP.grid(column=1, row=2)
        tab2txtbHP = tk.Entry(tab2TopLFrame)
        tab2txtbHP.grid(column=1, row=3)
        tab2txtbMP = tk.Entry(tab2TopLFrame)
        tab2txtbMP.grid(column=1, row=4)
        tab2txtbST = tk.Entry(tab2TopLFrame)
        tab2txtbST.grid(column=1, row=5)
        tab2txtbMA = tk.Entry(tab2TopLFrame)
        tab2txtbMA.grid(column=1, row=6)
        tab2txtbVI = tk.Entry(tab2TopLFrame)
        tab2txtbVI.grid(column=1, row=7)
        tab2txtbAG = tk.Entry(tab2TopLFrame)
        tab2txtbAG.grid(column=1, row=8)
        tab2txtbCMD1 = tk.Entry(tab2TopLFrame)
        tab2txtbCMD1.grid(column=3, row=1)
        tab2txtbCMD2 = tk.Entry(tab2TopLFrame)
        tab2txtbCMD2.grid(column=3, row=2)
        tab2txtbCMD3 = tk.Entry(tab2TopLFrame)
        tab2txtbCMD3.grid(column=3, row=3)
        tab2txtbPAS1 = tk.Entry(tab2TopLFrame)
        tab2txtbPAS1.grid(column=3, row=4)
        tab2txtbPAS2 = tk.Entry(tab2TopLFrame)
        tab2txtbPAS2.grid(column=3, row=5)
        tab2txtbPAS3 = tk.Entry(tab2TopLFrame)
        tab2txtbPAS3.grid(column=3, row=6)
        tab2txtbRAC = tk.Entry(tab2TopLFrame)
        tab2txtbRAC.grid(column=3, row=7)
        tab2txtbID = tk.Entry(tab2TopLFrame)
        tab2txtbID.grid(column=3, row=8)

        tab2emptylabel = tk.Label(tab2TopLFrame, text="   ")
        tab2emptylabel.grid(column=0, row=9)

        # Skill Frame
        tab2SkillFrame = tk.Frame(tab2TopLFrame, bd="2", relief="sunken")
        tab2SkillFrame.grid(column=0, row=11, columnspan=4)

        # Skill Labels
        tab2CMD1label = tk.Label(tab2SkillFrame, text="Command")
        tab2CMD1label.grid(column=0, row=0)
        tab2CMD2label = tk.Label(tab2SkillFrame, text="Passive")
        tab2CMD2label.grid(column=1, row=0)
        tab2CMD3label = tk.Label(tab2SkillFrame, text="Racial")
        tab2CMD3label.grid(column=2, row=0)
        tab2IDlabel = tk.Label(tab2SkillFrame, text="Demon ID")
        tab2IDlabel.grid(column=3, row=0)

        # Listboxes
        tab2ListBoxCMD = tk.Listbox(tab2SkillFrame)
        for i in range(0, len(CMD_IDS)):
            tab2ListBoxCMD.insert(i, " " + str(CMD_IDS[i]) + " - " + str(CMD_SKILLS[CMD_IDS[i]]))
        tab2ListBoxCMD.grid(column=0, row=1)

        tab2ListBoxPAS = tk.Listbox(tab2SkillFrame)
        for i in range(0, len(PAS_IDS)):
            tab2ListBoxPAS.insert(i, " " + str(PAS_IDS[i]) + " - " + str(PAS_SKILLS[PAS_IDS[i]]))
        tab2ListBoxPAS.grid(column=1, row=1)

        tab2ListBoxRAC = tk.Listbox(tab2SkillFrame)
        for i in range(0, len(RAC_IDS)):
            tab2ListBoxRAC.insert(i, " " + str(RAC_IDS[i]) + " - " + str(RAC_SKILLS[RAC_IDS[i]]))
        tab2ListBoxRAC.grid(column=2, row=1)

        tab2ListBoxID = tk.Listbox(tab2SkillFrame, width=23)
        for i in range(0, len(DEMON_IDS)):
            tab2ListBoxID.insert(i, " " + str(DEMON_IDS[i]) + " - " + str(ALL_DEMONS[DEMON_IDS[i]]))
        tab2ListBoxID.grid(column=3, row=1)

        # Save Characters Changes
        def applyDemonChange(*args):

            print("\n BEFORE APPLY \n " + str(self.demonList))
            if self.curDemon != {}:
                index = tab2ComboBox.current()
                self.curDemon = self.demonList[index]

                # put textbox values in global variable
                self.curDemon["level"] = tab2txtbLVL.get()
                self.curDemon["exp"] = tab2txtbEXP.get()
                self.curDemon["hp"] = tab2txtbHP.get()
                self.curDemon["mp"] = tab2txtbMP.get()
                self.curDemon["st"] = tab2txtbST.get()
                self.curDemon["ma"] = tab2txtbMA.get()
                self.curDemon["vi"] = tab2txtbVI.get()
                self.curDemon["ag"] = tab2txtbAG.get()
                self.curDemon["cmd1"] = tab2txtbCMD1.get()
                self.curDemon["cmd2"] = tab2txtbCMD2.get()
                self.curDemon["cmd3"] = tab2txtbCMD3.get()
                self.curDemon["pas1"] = tab2txtbPAS1.get()
                self.curDemon["pas2"] = tab2txtbPAS2.get()
                self.curDemon["pas3"] = tab2txtbPAS3.get()
                self.curDemon["rac"] = tab2txtbRAC.get()
                self.curDemon["id"] = tab2txtbID.get()

                print("\n AFTER APPLY \n " + str(self.demonList))

                # put char_info back on list
                self.demonList[index] = self.curDemon

        # Bottom Frame
        tab2BtmFrame = tk.Frame(tab2Frame, bd="2", relief="sunken")
        tab2BtmFrame.grid(column=0, row=2, columnspan=2, sticky="EW", pady="20 0")
        tab2BtmFrame.columnconfigure(0, weight=1)
        tk.Button(
            tab2BtmFrame, text="Apply", command=applyDemonChange
        ).grid(column=0, row=0, sticky="EW")

        # Hide the other tabs, only show first tab
        self.tabShown = self.tab1Frame
        self.tabButton = self.tab1Button
        self.tab2Frame.grid_remove()

    def validate_int(self, action, index, value_if_allowed,
                     prior_value, text, validation_type, trigger_type, widget_name):
        if action == "0":
            return True
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False

    def processSaveFile(self):
        with open(self.saveFilePath, 'rb') as fh:
            self.save_bytes = bytearray(fh.read())
        if self.save_bytes is not None:
            # For 1st Tab (Main Character)
            del self.charList[:]
            for x in range(0, 13):
                c_start_add = int(CHAR_OFFSET, 16) * x
                c_id_add = c_start_add + int(CHAR_ID[0], 16)
                char_id = self.getHexStr(self.save_bytes, c_id_add, CHAR_ID[1], add_is_dec=True)
                print(char_id)
                if char_id in ALL_CHARS:
                    c_id_add = c_start_add + int(CHAR_ID[0], 16)
                    c_lvl_add = c_start_add + int(CHAR_LVL[0], 16)
                    c_exp_add = c_start_add + int(CHAR_EXP[0], 16)
                    c_hp_add = c_start_add + int(CHAR_HP[0], 16)
                    c_mp_add = c_start_add + int(CHAR_MP[0], 16)
                    c_st_add = c_start_add + int(CHAR_ST[0], 16)
                    c_ma_add = c_start_add + int(CHAR_MA[0], 16)
                    c_vi_add = c_start_add + int(CHAR_VI[0], 16)
                    c_ag_add = c_start_add + int(CHAR_AG[0], 16)
                    c_cmd1_add = c_start_add + int(CHAR_CMD1[0], 16)
                    c_cmd2_add = c_start_add + int(CHAR_CMD2[0], 16)
                    c_cmd3_add = c_start_add + int(CHAR_CMD3[0], 16)
                    c_pas1_add = c_start_add + int(CHAR_PAS1[0], 16)
                    c_pas2_add = c_start_add + int(CHAR_PAS2[0], 16)
                    c_pas3_add = c_start_add + int(CHAR_PAS3[0], 16)
                    c_rac_add = c_start_add + int(CHAR_RAC[0], 16)
                    c_mov_add = c_start_add + int(CHAR_MOV[0], 16)
                    char_info = ALL_CHARS[char_id]

                    c_info = {
                        "start_add": c_start_add,
                        "name": char_info,
                        "id": int(self.getHexStr(self.save_bytes, c_id_add, CHAR_ID[1], add_is_dec=True), 16),
                        "level": int(self.getHexStr(self.save_bytes, c_lvl_add, CHAR_LVL[1], add_is_dec=True), 16),
                        "exp": int(self.getHexStr(self.save_bytes, c_exp_add, CHAR_EXP[1], add_is_dec=True), 16),
                        "hp": int(self.getHexStr(self.save_bytes, c_hp_add, CHAR_HP[1], add_is_dec=True), 16),
                        "mp": int(self.getHexStr(self.save_bytes, c_mp_add, CHAR_MP[1], add_is_dec=True), 16),
                        "st": int(self.getHexStr(self.save_bytes, c_st_add, CHAR_ST[1], add_is_dec=True), 16),
                        "ma": int(self.getHexStr(self.save_bytes, c_ma_add, CHAR_MA[1], add_is_dec=True), 16),
                        "vi": int(self.getHexStr(self.save_bytes, c_vi_add, CHAR_VI[1], add_is_dec=True), 16),
                        "ag": int(self.getHexStr(self.save_bytes, c_ag_add, CHAR_AG[1], add_is_dec=True), 16),
                        "cmd1": int(self.getHexStr(self.save_bytes, c_cmd1_add, CHAR_CMD1[1], add_is_dec=True), 16),
                        "cmd2": int(self.getHexStr(self.save_bytes, c_cmd2_add, CHAR_CMD2[1], add_is_dec=True), 16),
                        "cmd3": int(self.getHexStr(self.save_bytes, c_cmd3_add, CHAR_CMD3[1], add_is_dec=True), 16),
                        "pas1": int(self.getHexStr(self.save_bytes, c_pas1_add, CHAR_PAS1[1], add_is_dec=True), 16),
                        "pas2": int(self.getHexStr(self.save_bytes, c_pas2_add, CHAR_PAS2[1], add_is_dec=True), 16),
                        "pas3": int(self.getHexStr(self.save_bytes, c_pas3_add, CHAR_PAS3[1], add_is_dec=True), 16),
                        "rac": int(self.getHexStr(self.save_bytes, c_rac_add, CHAR_RAC[1], add_is_dec=True), 16),
                        "mov": int(self.getHexStr(self.save_bytes, c_mov_add, CHAR_MOV[1], add_is_dec=True), 16),
                    }
                    self.charList.append(c_info)
                    self.charNameList.append(char_info)
                    print("Start Address: %x, Char ID: %s, Name: %s." % (c_info["start_add"], char_id, char_info))

            # For 2nd Tab (Demons)
            del self.demonList[:]
            for x in range(0, DE_NUM_MAX):
                d_start_add = int(DE_OFFSET, 16) * x
                d_id_add = d_start_add + int(DE_ID[0], 16)
                demon_id = self.getHexStr(self.save_bytes, d_id_add, DE_ID[1], add_is_dec=True)
                if True:
                    d_id_add = d_start_add + int(DE_ID[0], 16)
                    d_lvl_add = d_start_add + int(DE_LVL[0], 16)
                    d_exp_add = d_start_add + int(DE_EXP[0], 16)
                    d_hp_add = d_start_add + int(DE_HP[0], 16)
                    d_mp_add = d_start_add + int(DE_MP[0], 16)
                    d_st_add = d_start_add + int(DE_ST[0], 16)
                    d_ma_add = d_start_add + int(DE_MA[0], 16)
                    d_vi_add = d_start_add + int(DE_VI[0], 16)
                    d_ag_add = d_start_add + int(DE_AG[0], 16)
                    d_cmd1_add = d_start_add + int(DE_CMD1[0], 16)
                    d_cmd2_add = d_start_add + int(DE_CMD2[0], 16)
                    d_cmd3_add = d_start_add + int(DE_CMD3[0], 16)
                    d_pas1_add = d_start_add + int(DE_PAS1[0], 16)
                    d_pas2_add = d_start_add + int(DE_PAS2[0], 16)
                    d_pas3_add = d_start_add + int(DE_PAS3[0], 16)
                    d_rac_add = d_start_add + int(DE_RAC[0], 16)
                    demon_id = int(self.getHexStr(self.save_bytes, d_id_add, DE_ID[1], add_is_dec=True), 16)
                    print(demon_id)
                    demon_info = ALL_DEMONS[str(demon_id)]

                    d_info = {
                        "start_add": d_start_add,
                        "name": demon_info,
                        "id": int(self.getHexStr(self.save_bytes, d_id_add, DE_ID[1], add_is_dec=True), 16),
                        "level": int(self.getHexStr(self.save_bytes, d_lvl_add, DE_LVL[1], add_is_dec=True), 16),
                        "exp": int(self.getHexStr(self.save_bytes, d_exp_add, DE_EXP[1], add_is_dec=True), 16),
                        "hp": int(self.getHexStr(self.save_bytes, d_hp_add, DE_HP[1], add_is_dec=True), 16),
                        "mp": int(self.getHexStr(self.save_bytes, d_mp_add, DE_MP[1], add_is_dec=True), 16),
                        "st": int(self.getHexStr(self.save_bytes, d_st_add, DE_ST[1], add_is_dec=True), 16),
                        "ma": int(self.getHexStr(self.save_bytes, d_ma_add, DE_MA[1], add_is_dec=True), 16),
                        "vi": int(self.getHexStr(self.save_bytes, d_vi_add, DE_VI[1], add_is_dec=True), 16),
                        "ag": int(self.getHexStr(self.save_bytes, d_ag_add, DE_AG[1], add_is_dec=True), 16),
                        "cmd1": int(self.getHexStr(self.save_bytes, d_cmd1_add, DE_CMD1[1], add_is_dec=True), 16),
                        "cmd2": int(self.getHexStr(self.save_bytes, d_cmd2_add, DE_CMD2[1], add_is_dec=True), 16),
                        "cmd3": int(self.getHexStr(self.save_bytes, d_cmd3_add, DE_CMD3[1], add_is_dec=True), 16),
                        "pas1": int(self.getHexStr(self.save_bytes, d_pas1_add, DE_PAS1[1], add_is_dec=True), 16),
                        "pas2": int(self.getHexStr(self.save_bytes, d_pas2_add, DE_PAS2[1], add_is_dec=True), 16),
                        "pas3": int(self.getHexStr(self.save_bytes, d_pas3_add, DE_PAS3[1], add_is_dec=True), 16),
                        "rac": int(self.getHexStr(self.save_bytes, d_rac_add, DE_RAC[1], add_is_dec=True), 16),
                    }
                    self.demonList.append(d_info)
                    self.demonNameList.append(demon_info)
                    print("Start Address: %x, Demon ID: %s." % (d_start_add, demon_id))

    def changeTab(self, tab_to_show, tab_button):
        if self.tabShown is tab_to_show:
            return
        self.tabShown.grid_remove()
        tab_to_show.grid()
        self.tabButton.config(state="normal", relief="raised")
        tab_button.config(state="disabled", relief="sunken")
        self.tabButton = tab_button
        self.tabShown = tab_to_show

    def writeHexBytes(self, byte_arr, hex_str, start_add, num_bytes, skip_bytes=None, add_is_dec=False):
        hex_str = hex_str.zfill(num_bytes * 2)
        hex_bytes = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]
        hex_bytes.reverse()
        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)
        if skip_bytes:
            curr_add += skip_bytes
        for val in hex_bytes:
            # print("old: %d, new: %d" % (byte_arr[curr_add], int(val, 16)))
            byte_arr[curr_add] = int(val, 16)
            curr_add += 1

    def getHexStr(self, byte_arr, start_add, num_bytes, skip_bytes=None, add_is_dec=False):
        hex_str = ""
        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)
        if skip_bytes:
            curr_add += skip_bytes
        while num_bytes > 0:
            hex_str = format(byte_arr[curr_add], '02x') + hex_str
            num_bytes -= 1
            curr_add += 1
        hex_str = hex_str.lstrip("0")
        return hex_str if hex_str else "0"

    # Menu Functions
    def openFileChooser(self):
        sel_file = filedialog.askopenfilenames(parent=self, initialdir=os.path.dirname(os.path.realpath(sys.argv[0])),
                                               filetypes=(("Save files", "*.dat"), ("All files", "*.*")))
        if sel_file:
            sel_file = sel_file[0]
            # print(sel_file)
            if os.path.isfile(sel_file):
                self.saveFilePathTxt.set(sel_file)
                self.saveFilePath = sel_file
                self.saveFileDir = os.path.dirname(sel_file)
                self.saveFileName = os.path.basename(sel_file)
                print(self.saveFileName)
                self.processSaveFile()
                self.createWidgets()

    def saveCharChanges(self):
        if self.save_bytes:
            for char in self.charList:
                # Level
                tmp_val = format(int(char["level"]), "x")
                c_lvl_write = char["start_add"] + int(CHAR_LVL[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_lvl_write, CHAR_LVL[1], add_is_dec=True)
                # EXP
                tmp_val = format(int(char["exp"]), "x")
                c_exp_write = char["start_add"] + int(CHAR_EXP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_exp_write, CHAR_EXP[1], add_is_dec=True)
                # hp
                tmp_val = format(int(char["hp"]), "x")
                c_hp_write = char["start_add"] + int(CHAR_HP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_hp_write, CHAR_HP[1], add_is_dec=True)
                # MP
                tmp_val = format(int(char["mp"]), "x")
                c_mp_write = char["start_add"] + int(CHAR_MP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_mp_write, CHAR_MP[1], add_is_dec=True)
                # ST
                tmp_val = format(int(char["st"]), "x")
                c_st_write = char["start_add"] + int(CHAR_ST[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_st_write, CHAR_ST[1], add_is_dec=True)
                # MA
                tmp_val = format(int(char["ma"]), "x")
                c_ma_write = char["start_add"] + int(CHAR_MA[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_ma_write, CHAR_MA[1], add_is_dec=True)
                # VI
                tmp_val = format(int(char["vi"]), "x")
                c_vi_write = char["start_add"] + int(CHAR_VI[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_vi_write, CHAR_VI[1], add_is_dec=True)
                # AG
                tmp_val = format(int(char["ag"]), "x")
                c_ag_write = char["start_add"] + int(CHAR_AG[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_ag_write, CHAR_AG[1], add_is_dec=True)
                # CMD1
                tmp_val = format(int(char["cmd1"]), "x")
                c_cmd1_write = char["start_add"] + int(CHAR_CMD1[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_cmd1_write, CHAR_CMD1[1], add_is_dec=True)
                # CMD2
                tmp_val = format(int(char["cmd2"]), "x")
                c_cmd2_write = char["start_add"] + int(CHAR_CMD2[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_cmd2_write, CHAR_CMD2[1], add_is_dec=True)
                # CMD3
                tmp_val = format(int(char["cmd3"]), "x")
                c_cmd3_write = char["start_add"] + int(CHAR_CMD3[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_cmd3_write, CHAR_CMD3[1], add_is_dec=True)
                # PAS1
                tmp_val = format(int(char["pas1"]), "x")
                c_pas1_write = char["start_add"] + int(CHAR_PAS1[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_pas1_write, CHAR_PAS1[1], add_is_dec=True)
                # PAS2
                tmp_val = format(int(char["pas2"]), "x")
                c_pas2_write = char["start_add"] + int(CHAR_PAS2[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_pas2_write, CHAR_PAS2[1], add_is_dec=True)
                # PAS3
                tmp_val = format(int(char["pas3"]), "x")
                c_pas3_write = char["start_add"] + int(CHAR_PAS3[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_pas3_write, CHAR_PAS3[1], add_is_dec=True)
                # RAC
                tmp_val = format(int(char["rac"]), "x")
                c_rac_write = char["start_add"] + int(CHAR_RAC[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_rac_write, CHAR_RAC[1], add_is_dec=True)
                # MOV
                tmp_val = format(int(char["mov"]), "x")
                c_mov_write = char["start_add"] + int(CHAR_MOV[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, c_mov_write, CHAR_MOV[1], add_is_dec=True)
        return

    def saveDemonChanges(self):
        if self.save_bytes:
            for demon in self.demonList:
                # ID
                tmp_val = format(int(demon["id"]), "x")
                d_id_write = demon["start_add"] + int(DE_ID[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_id_write, DE_ID[1], add_is_dec=True)
                # Level
                tmp_val = format(int(demon["level"]), "x")
                d_lvl_write = demon["start_add"] + int(DE_LVL[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_lvl_write, DE_LVL[1], add_is_dec=True)
                # EXP
                tmp_val = format(int(demon["exp"]), "x")
                d_exp_write = demon["start_add"] + int(DE_EXP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_exp_write, DE_EXP[1], add_is_dec=True)
                # HP
                tmp_val = format(int(demon["hp"]), "x")
                d_hp_write = demon["start_add"] + int(DE_HP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_hp_write, DE_HP[1], add_is_dec=True)
                # MP
                tmp_val = format(int(demon["mp"]), "x")
                d_mp_write = demon["start_add"] + int(DE_MP[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_mp_write, DE_MP[1], add_is_dec=True)
                # ST
                tmp_val = format(int(demon["st"]), "x")
                d_st_write = demon["start_add"] + int(DE_ST[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_st_write, DE_ST[1], add_is_dec=True)
                # MA
                tmp_val = format(int(demon["ma"]), "x")
                d_ma_write = demon["start_add"] + int(DE_MA[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_ma_write, DE_MA[1], add_is_dec=True)
                # VI
                tmp_val = format(int(demon["vi"]), "x")
                d_vi_write = demon["start_add"] + int(DE_VI[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_vi_write, DE_VI[1], add_is_dec=True)
                # AG
                tmp_val = format(int(demon["ag"]), "x")
                d_ag_write = demon["start_add"] + int(DE_AG[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_ag_write, DE_AG[1], add_is_dec=True)
                # CMD1
                tmp_val = format(int(demon["cmd1"]), "x")
                d_cmd1_write = demon["start_add"] + int(DE_CMD1[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_cmd1_write, DE_CMD1[1], add_is_dec=True)
                # CMD2
                tmp_val = format(int(demon["cmd2"]), "x")
                d_cmd2_write = demon["start_add"] + int(DE_CMD2[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_cmd2_write, DE_CMD2[1], add_is_dec=True)
                # CMD3
                tmp_val = format(int(demon["cmd3"]), "x")
                d_cmd3_write = demon["start_add"] + int(DE_CMD3[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_cmd3_write, DE_CMD3[1], add_is_dec=True)
                # PAS1
                tmp_val = format(int(demon["pas1"]), "x")
                d_pas1_write = demon["start_add"] + int(DE_PAS1[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_pas1_write, DE_PAS1[1], add_is_dec=True)
                # PAS2
                tmp_val = format(int(demon["pas2"]), "x")
                d_pas2_write = demon["start_add"] + int(DE_PAS2[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_pas2_write, DE_PAS2[1], add_is_dec=True)
                # PAS3
                tmp_val = format(int(demon["pas3"]), "x")
                d_pas3_write = demon["start_add"] + int(DE_PAS3[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_pas3_write, DE_PAS3[1], add_is_dec=True)
                # RAC
                tmp_val = format(int(demon["rac"]), "x")
                d_rac_write = demon["start_add"] + int(DE_RAC[0], 16)
                self.writeHexBytes(self.save_bytes, tmp_val, d_rac_write, DE_RAC[1], add_is_dec=True)
        return

    def saveChanges(self):
        if self.saveFilePath and os.path.isdir(self.saveFileDir):
            self.saveCharChanges()
            self.saveDemonChanges()
            edited_dir = os.path.join(self.saveFileDir, "Edited")
            if not os.path.isdir(edited_dir):
                os.mkdir(edited_dir)
            with open(os.path.join(edited_dir, self.saveFileName), 'wb') as fh:
                fh.write(self.save_bytes)

    def exitApp(self):
        self.quit()

    def aboutCreator(self):
        tk.messagebox.showinfo("About This", "Made by XxArcaiCxX" +
                               "\n\nCredits to:" +
                               "\nwaynelimt (GitHub) - SMT IV Save Editor from which this Editor was adapted from")

    def help(self):
        tk.messagebox.showinfo("Help", "Just don't be stupid lol")


if __name__ == "__main__":
    app = mytestapp(None)
    app.mainloop()
