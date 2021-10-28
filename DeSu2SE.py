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
CHAR_ID = ("0x74", 3)
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
DE_ID = ("0x2B6", 1)
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

CMD_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4a', '4f',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f',
             '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f',
             'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af',
             'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
             'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf',
             'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df',
             'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef',
             'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff')

PAS_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4a', '4f',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f',
             '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f',
             'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af',
             'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
             'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf',
             'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df',
             'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef',
             'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff')

AUTO_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4a', '4f',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f',
             '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f',
             'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af',
             'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
             'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf',
             'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df',
             'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef',
             'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff')

RAC_IDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4a', '4f',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f',
             '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f',
             'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af',
             'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
             'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf',
             'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df',
             'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef',
             'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff')

ALL_SKILLS = {
    "1": ("Agi", 0, 1, 1, 0, "Weak Fire damage. 1 enemy."),
    "2": ("Agilao", 0, 4, 2, 0, "Medium Fire damage. 1 enemy."),
    "3": ("Agidyne", 0, 10, 3, 0, "Heavy Fire damage. 1 enemy."),
    "4": ("Maragi", 0, 7, 1, 2, "Weak Fire damage. All enemies."),
    "5": ("Maragion", 0, 16, 2, 2, "Medium Fire damage. All enemies."),
    "6": ("Maragidyne", 0, 28, 3, 2, "Heavy Fire damage. All enemies."),
    "7": ("Fire Breath", 0, 17, 1, 1, "1~4 hits weak Fire damage. Multiple enemies."),
    "8": ("Trisagion", 0, 18, 4, 0, "Severe Fire damage. 1 enemy"),
    "9": ("Ragnarok", 0, 31, 2, 1, "1~4 hits medium Fire damage. Muliple enemies."),
    "a": ("Bufu", 1, 1, 1, 0, "Weak Ice damage. 1 enemy."),
    "b": ("Bufula", 1, 4, 2, 0, "Medium Ice damage. 1 enemy."),
    "c": ("Bufudyne", 1, 10, 3, 0, "Heavy Ice damage. 1 enemy."),
    "d": ("Mabufu", 1, 7, 1, 2, "Weak Ice damage. All enemies."),
    "e": ("Mabufula", 1, 16, 2, 2, "Medium Ice damage. All enemies."),
    "f": ("Mabufudyne", 1, 28, 3, 2, "Heavy Ice damage. All enemies."),
    "10": ("Ice Breath", 1, 17, 1, 1, "1~4 hits weak Ice damage. Muliple enemies."),
    "11": ("Glacial Blast", 1, 18, 2, 1, "1~4 hits medium Ice damage. Multiple enemies."),
    "12": ("Cold World", 1, 46, 3, 2, "Heavy Ice damage. 15% KO. All enemies."),
    "4c": ("Breath", 1, 20, 2, 1, "1~5 hits medium Ice damage. Multiple enemies."),
    "13": ("Zio", 2, 1, 1, 0, "Weak Elec damage. 1 enemy."),
    "14": ("Zionga", 2, 4, 2, 0, "Medium Elec damage. 1 enemy."),
    "15": ("Ziodyne", 2, 10, 3, 0, "Heavy Elec damage. 1 enemy."),
    "16": ("Mazio", 2, 7, 1, 2, "Weak Elec damage. All enemies."),
    "17": ("Mazionga", 2, 16, 2, 2, "Medium Elec damage. All enemies."),
    "18": ("Maziodyne", 2, 28, 3, 2, "Heavy Elec damage. All enemies."),
    "19": ("Shock", 2, 17, 1, 1, "1~4 hits weak Elec damage. Muliple enemies."),
    "1a": ("Thunder Reign", 2, 18, 4, 2, "Severe Elec damage. All enemies."),
    "1b": ("Charming Bolt", 2, 41, 3, 2, "Heavy Elec damage. 25% Panic. All enemies."),
    "1c": ("Zan", 3, 1, 1, 0, "Weak Force damage. 1 enemy."),
    "1d": ("Zanma", 3, 4, 2, 0, "Medium Force damage. 1 enemy."),
    "1e": ("Zandyne", 3, 10, 3, 0, "Heavy Force damage. 1 enemy."),
    "1f": ("Mazan", 3, 7, 1, 2, "Weak Force damage. All enemies."),
    "20": ("Mazanma", 3, 16, 2, 2, "Medium Force damage. All enemies."),
    "21": ("Mazandyne", 3, 28, 3, 2, "Heavy Force damage. All enemies."),
    "22": ("Wind Breath", 3, 17, 1, 1, "1~4 hits weak Force damage. Muliple enemies."),
    "23": ("Deadly Wind", 3, 18, 4, 0, "Severe Force damage. 1 enemy."),
    "24": ("Floral Gust", 3, 31, 2, 1, "1~4 hits medium Force damage. Muliple enemies."),
    "25": ("Megido", 4, 21, 1, 2, "Weak Almighty damage. All enemies."),
    "26": ("Megidola", 4, 36, 2, 2, "Medium Almighty damage. All enemies."),
    "27": ("Megidolaon", 4, 56, 3, 2, "Heavy Almighty damage. All enemies."),
    "28": ("Great Logos", 4, 66, 4, 2, "Severe Almighty damage. All enemies."),
    "29": ("Antichthon", 4, 76, 4, 2, "Severe Almighty damage. Debilitate. All enemies."),
    "2a": ("Babylon Goblet", 4, 61, 2, 2, "Medium Almighty damage. 25% Panic."),
    "2b": ("Holy Wrath", 4, 41, 2, 2, "50% additional damage VS Chaos."),
    "2c": ("Judgement", 4, 41, 2, 2, "50% additional damage VS Neutral."),
    "2d": ("Sea of Chaos", 4, 41, 1, 2, "50% additional damage VS Law."),
    "2e": ("Life Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain HP. 1 enemy."),
    "2f": ("Spirit Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain MP. 1 enemy."),
    "30": ("Energy Drain", 4, 1, 1, 0, "Weak Almighty damage. Drain HP/MP. 1 enemy."),
    "47": ("Strange Ray", 4, 1, 6, 0, "Almighty attack reduce target MP to 50%."),
    "48": ("Enigmatic Ray", 4, 6, 6, 2, "???"),
    "49": ("Macca Beam", 4, 1, 6, 0, "Almighty attack reduce target Macca to 20%."),
    "4a": ("Wastrel Beam", 4, 6, 6, 0, "Almighty attack reduce target Macca to 50%"),
    "4b": ("Crushing Wave", 4, 6, 6, 0, "Almighty attack reduce target HP to 1."),
    "4d": ("Death's Door", 4, 6, 6, 2, "All Sick enemies' HP reduced to 1."),
    "c2": ("Desperate Hit", 4, 36, 1, 1, "1~5 hits Almighty damage. Multiple enemies."),
    "31": ("Mudo", 5, 2, 5, 0, "Dark magic. 30% KO 1 enemy."),
    "32": ("Mudoon", 5, 6, 5, 0, "Dark magic. 55% KO 1 enemy."),
    "33": ("Mamudo", 5, 14, 5, 2, "Dark magic. 30% KO all enemies."),
    "34": ("Mamudoon", 5, 26, 5, 2, "Dark magic. 55% KO all enemies."),
    "35": ("Die for Me!", 5, 41, 5, 2, "Dark magic. 80% KO all enemies."),
    "36": ("Hama", 6, 2, 5, 0, "Light magic. 30% KO 1 enemy."),
    "37": ("Hamaon", 6, 6, 5, 0, "Light magic. 55% KO 1 enemy."),
    "38": ("Mahama", 6, 14, 5, 2, "Light magic. 30% KO all enemies."),
    "39": ("Mahamaon", 6, 26, 5, 2, "Light magic. 55% KO all enemies."),
    "3a": ("Judgement Light", 6, 41, 5, 2, "Light magic. 80% KO all enemies."),
    "3b": ("Dormina", 7, 1, 0, 0, "90% Sleep. 1 enemy."),
    "3c": ("Lullaby", 7, 7, 0, 2, "70% Sleep. All enemies."),
    "3d": ("Poisma", 7, 1, 0, 0, "90% Poison. 1 enemy."),
    "3e": ("Poison Breath", 7, 7, 0, 2, "70% Poison. All enemies."),
    "3f": ("Shibaboo", 7, 1, 0, 0, "50% Bind an enemy."),
    "40": ("Bind Voice", 7, 11, 0, 2, "50% Bind all enemies."),
    "41": ("Pulpina", 7, 1, 0, 0, "90% Panic. 1 enemy."),
    "42": ("Panic Voice", 7, 11, 0, 2, "70% Panic. All enemies."),
    "43": ("Cough", 7, 14, 0, 0, "90% Sick. 1 enemy."),
    "44": ("Pandemic Bomb", 7, 7, 0, 2, "70% Sick. All Enemies."),
    "45": ("Ancient Curse", 7, 36, 0, 2, "80% random ailment. All enemies."),
    "46": ("Shivering Taboo", 7, 36, 0, 2, "70% random ailment. All enemies."),
    "51": ("Dia", 8, 1, 0, 4, "Heal HP for ally. Low."),
    "52": ("Diarama", 8, 5, 0, 4, "Heal HP for ally. Medium."),
    "53": ("Diarahan", 8, 12, 0, 4, "Heal HP for ally. High."),
    "54": ("Media", 8, 8, 0, 5, "Heal HP for party. Low."),
    "55": ("Mediarama", 8, 18, 0, 5, "Heal HP for party. Medium."),
    "56": ("Mediarahan", 8, 36, 0, 5, "Heal HP for party. High."),
    "57": ("Salvation", 8, 46, 0, 5, "Heal full HP and cure ailments for party."),
    "58": ("Patra", 8, 1, 0, 4, "Cure Sleep/Panic/Bind for ally."),
    "59": ("Me Patra", 8, 11, 0, 5, "Cure Sleep/Panic/Bind for party."),
    "5a": ("Posumudi", 8, 1, 0, 4, "Cure Poison/Sick for ally."),
    "5b": ("Nervundi", 8, 1, 7, 7, "???"),
    "5c": ("Amrita", 8, 16, 0, 4, "Cure all ailments for ally."),
    "5d": ("Recarm", 8, 16, 0, 4, "Revive ally with little starting HP."),
    "5e": ("Samerecarm", 8, 36, 0, 4, "Revive ally with full starting HP."),
    "5f": ("Recarmdra", 8, 1, 0, 5, "User dies. Revive all allies with full HP."),
    "65": ("Tarukaja", 9, 11, 0, 5, "Increase Attack. All allies."),
    "66": ("Sukukaja", 9, 11, 0, 5, "Increase Hit/Evade. All allies."),
    "67": ("Rakukaja", 9, 11, 0, 5, "Increase Defense. All allies."),
    "68": ("Luster Candy", 9, 46, 0, 5, "Increase all stats. All allies."),
    "69": ("Dekaja", 9, 6, 0, 2, "Neutralize -kaja effects. All enemies."),
    "6a": ("Tarunda", 9, 11, 0, 2, "Decrease Attack. All enemies."),
    "6b": ("Sukunda", 9, 11, 0, 2, "Decrease Hit/Evade. All enemies."),
    "6c": ("Rakunda", 9, 11, 0, 2, "Decrease Defense. All enemies."),
    "6d": ("Debilitate", 9, 46, 0, 2, "Decrease all stats. All enemies."),
    "6e": ("Dekunda", 9, 6, 0, 5, "Neutralize -unda effects. All allies."),
    "6f": ("Silent Prayer", 9, 11, 0, 6, "Neutralize stat modifications for all."),
    "70": ("War Cry", 9, 41, 0, 2, "Decrease Attack/Defense. All enemies"),
    "71": ("Fog Breath", 9, 41, 0, 2, "Decrease Attack/Hit/Evade. All enemies"),
    "72": ("Acid Breath", 9, 41, 0, 2, "Decrease Defense/Hit/Evade. All enemies"),
    "73": ("Taunt", 9, 16, 0, 2, "Decrease Defense. Increase Attack. All enemies."),
    "75": ("Panic Caster", 9, 46, 0, 3, "User Panic. Temporary increase in magic damage."),
    "76": ("Tetrakarn", 9, 46, 0, 5, "Reflect Phys/Gun damage once."),
    "77": ("Makarakarn", 9, 46, 0, 5, "Reflect magic damage once."),
    "78": ("Tetraja", 9, 11, 0, 5, "Nullify Light/Dark magic once."),
    "79": ("Charge", 9, 5, 0, 3, "User's next Phys/Gun damage 250%."),
    "7a": ("Concentrate", 9, 7, 0, 3, "User's next magic damage 250%."),
    "7b": ("Blood Ritual", 9, 21, 0, 3, "Luster Candy. Reduce user's HP to 1."),
    "8a": ("Doping", 9, 41, 0, 5, "All allies' HP 133%"),
    "8b": ("Angelic Order", 9, 21, 0, 4, "Bestows Smirk. 1 ally."),
    "7c": ("Sabbatma", 10, 16, 0, 4, "Summon/return 1 ally to stock."),
    "7d": ("Invitation", 10, 41, 0, 4, "Summon/return 1 ally to stock and revive if dead."),
    "7f": ("Bad Company", 10, 11, 0, 5, "Summon highest level allies from stock."),
    "89": ("Trafuri", 10, 1, 0, 5, "Guaranteed escape from random battles."),
    "8c": ("Estoma Sword", 10, 21, 0, 7, "Used in maps. Hit enemies to banish them."),
    "8d": ("Call Ally", 10, 1, 0, 3, "Dummy"),
    "97": ("Lunge", 11, 2, 1, 0, "Weak Phys damage. High Crit. Low Acc. 1 enemy."),
    "98": ("Oni-Kagura", 11, 5, 2, 0, "Medium Phys damage. High Crit. Low Acc. 1 enemy."),
    "99": ("Mortal Jihad", 11, 9, 3, 0, "Heavy Phys damage. High Crit. Low Acc. 1 enemy."),
    "9a": ("Critical Wave", 11, 6, 1, 2, "Weak Phys damage. High Crit. Low Acc. All enemies."),
    "9b": ("Megaton Press", 11, 13, 2, 2, "Medium Phys damage. High Crit. Low Acc. All enemies."),
    "9c": ("Titanomachia", 11, 26, 3, 2, "Heavy Phys damage. High Crit. Low Acc. All enemies."),
    "9d": ("Gram Slice", 11, 1, 1, 0, "Weak Phys damage. 1 enemy."),
    "9e": ("Fatal Sword", 11, 4, 2, 0, "Medium Phys damage. 1 enemy."),
    "9f": ("Berserker God", 11, 8, 3, 0, "Heavy Phys damage. 1 enemy."),
    "a0": ("Heat Wave", 11, 7, 1, 2, "Weak Phys damage. All enemies."),
    "a1": ("Javelin Rain", 11, 17, 2, 2, "Medium Phys damage. All enemies."),
    "a2": ("Hades Blast", 11, 28, 3, 2, "Heavy Phys damage. All enemies."),
    "a3": ("Bouncing Claw", 11, 1, 1, 1, "1~3 hits weak Phys damage. 1 enemy."),
    "a4": ("Damascus Claw", 11, 3, 2, 1, "1~3 hits medium Phys damage. 1 enemy."),
    "a5": ("Nihil Claw", 11, 7, 3, 1, "1~3 hits heavy Phys damage. 1 enemy."),
    "a6": ("Scratch Dance", 11, 5, 1, 1, "1~3 hits weak Phys damage. Multiple enemies."),
    "a7": ("Axel Claw", 11, 11, 2, 1, "1~3 hits medium Phys damage. Multiple enemies."),
    "a8": ("Madness Nails", 11, 22, 3, 1, "1~3 hits heavy Phys damage. Multiple enemies."),
    "a9": ("Fang Breaker", 11, 8, 1, 0, "Weak Phys damage. Tarunda. 1 enemy."),
    "aa": ("Dream Fist", 11, 5, 1, 0, "Weak Phys damage. 70% Sleep. 1 enemy."),
    "ab": ("Purple Smoke", 11, 10, 2, 1, "1~3 hits medium Phys damage. 70% Panic. Multiple enemies."),
    "ac": ("Carol Hit", 11, 11, 1, 0, "Weak Phys damage. 50% Lost. 1 enemy."),
    "ae": ("Tetanus Cut", 11, 7, 2, 0, "Medium Phys damage. 70% Sick. 1 enemy."),
    "b0": ("Blight", 11, 10, 1, 2, "Weak Phys damage. 60% Poison. All enemies."),
    "b1": ("Occult Flash", 11, 26, 2, 2, "Medium Phys damage. 50% KO. All enemies."),
    "b2": ("Binding Claw", 11, 7, 2, 0, "Medium Phys damage. 35% Bind. 1 enemy."),
    "b3": ("Poison Claw", 11, 5, 2, 0, "Medium Phys damage. 70% Poison. 1 enemy."),
    "b4": ("Iron Judgement", 11, 4, 2, 0, "Medium Phys damage. 1 enemy."),
    "fb": ("Labrys Strike", 11, 1, 8, 1, "2~3 hits mega Phys damage. Multiple enemies."),
    "b5": ("Needle Shot", 12, 2, 1, 0, "Weak Gun damage. 1 enemy."),
    "b6": ("Tathlum Shot", 12, 5, 2, 0, "Medium Gun damage. 1 enemy."),
    "b7": ("Grand Tack", 12, 9, 3, 0, "Heavy Gun damage. 1 enemy."),
    "b8": ("Riot Gun", 12, 6, 4, 0, "Severe Gun damage. 1 enemy."),
    "b9": ("Rapid Needle", 12, 13, 1, 2, "Weak Gun damage. All enemies."),
    "ba": ("Blast Arrow", 12, 26, 2, 2, "Medium Gun damage. All enemies."),
    "bb": ("Heaven's Bow", 12, 1, 3, 2, "Heavy Gun damage. All enemies."),
    "bc": ("Dream Needle", 12, 4, 1, 0, "Weak Gun damage. 70% Sleep. 1 enemy."),
    "bd": ("Toxic Sting", 12, 8, 1, 0, "Weak Gun damage. 70% Poison. 1 enemy."),
    "be": ("Stun Needle", 12, 7, 1, 0, "Weak Gun damage. 60% Bind. 1 enemy."),
    "bf": ("Madness Needle", 12, 17, 1, 0, "Weak Gun damage. 70% Panic. 1 enemy."),
    "c0": ("Stun Needles", 12, 28, 2, 1, "1~3 hits medium Gun damage. 60% Bind. Muliple enemies."),
    "c1": ("Myriad Arrows", 12, 26, 1, 1, "2~4 hits weak Gun damage. Multiple enemies."),
    "fc": ("Snake's Fangs", 12, 1, 2, 1, "2~3 hits medium Gun damage. Multiple enemies."),
    "4e": ("Makakaja", 9, 11, 0, 5, "Increases magic attack."),
    "4f": ("Marin Karin", 7, 1, 0, 0, "Inflicts the Charm ailment"),
    "50": ("Sexy Dance", 7, 16, 0, 2, "Inflicts the Charm ailment"),
    "60": ("Hell Thrust", 11, 24, 3, 1, "2-4 Heavy Attacks. Smirk: Defense down"),
    "61": ("Thunder Gods", 2, 36, 4, 0, "Severe Elec attack. Smirk: Pierce"),
    "62": ("Ice Age", 1, 36, 4, 0, "Severe Ice attack. Smirk: Pierce"),
    "63": ("Makajam", 7, 1, 0, 0, "Inflicts the Mute ailment"),
    "64": ("Makajamaon", 7, 11, 0, 2, "Inflicts the Mute ailment"),
    "74": ("Critical Eye", 9, 6, 0, 3, "Next Phys/Gun attack will be a critical hit"),
    "7e": ("Judgement Strike", 11, 1, 3, 2, "Heavy Phys attack. Smirk: Pierce"),
    "80": ("Dia", 7, 1, 0, 4, "Heals HP (Might be Asahi's)"),
    "81": ("Diarama", 7, 1, 0, 4, "Greayly Heals HP (Might be Asahi's)"),
    "82": ("Media", 7, 1, 0, 5, "Heals HP (Might be Asahi's)"),
    "83": ("Mediarama", 7, 1, 0, 5, "Greatly Heals HP (Might be Asahi's)"),
    "84": ("Smile Charge", 9, 46, 0, 3, "Induces Smirk"),
    "85": ("Magaon", 9, 6, 0, 0, "Removes Smirk"),
    "86": ("Heavenly Punishment", 12, 1, 3, 2, "Heavy Almighty attack. Smirk: Pierce"),
    "87": ("Irrational Glimmer", 4, 1, 0, 2, "Inflicts 66% of target's HP as Almighty"),
    "88": ("Evil-Crushing Flash", 6, 1, 4, 0, "Severe Light Attack. Smirk: Instant Kill"),
    "8e": ("Glare", 10, 1, 0, 3, "No effect"),
    "8f": ("Do Nothing", 10, 1, 0, 3, "No effect"),
    "90": ("No Reaction", 10, 1, 0, 3, "No effect"),
    "91": ("Forfeit", 9, 1, 0, 0, "Fully decreases attack and magic. Inflicts Mute"),
    "92": ("Nightmare", 9, 1, 0, 0, "Fully decreases defense. Inflicts Sleep"),
    "93": ("Bind", 9, 1, 0, 0, "Fully decreases hit/evade rate. Inflicts Brand"),
    "94": ("Eternal Rest", 4, 31, 0, 6, "Instant kills sleeping targets"),
    "95": ("Frenzied Chomp", 11, 2, 1, 0, "Weak Phys attack. Inflicts Poison/Bind/Charm"),
    "96": ("Eat Whole", 11, 10, 1, 3, "Weak Phys attack. Drains Enemy HP"),
    "ad": ("Mist Rush", 11, 24, 2, 2, "2-4 medium Phys attacks. Inflicts Daze"),
    "af": ("Dark Sword", 11, 12, 2, 0, "2 medium Phys attacks. Inflicts Mute"),
    "c3": ("Sleep Shot", 12, 5, 1, 0, "Weak Gun attack. Inflicts Sleep"),
    "c4": ("Rapid Bind", 12, 10, 2, 1, "1-3 medium Gun attacks. Inflicts Bind"),
    "c5": ("Head Crush", 11, 1, 2, 0, "Weak Phys atack. Inflicts Daze"),
    "c6": ("Power Punch", 11, 4, 2, 0, "Medium Phys attack. Smirk: Daze"),
    "c7": ("Earthquake", 11, 21, 2, 2, "Medium Phys attack. Inflicts Daze"),
    "c8": ("Assist Attack", 4, 1, 2, 1, "2 medium Almighty attacks"),
    "c9": ("Assist Attack", 4, 1, 2, 1, "4 medium Almighty attacks"),
    "ca": ("Assist Attack", 4, 1, 2, 1, "6 medium Almighty attacks"),
    "cb": ("Assist Attack", 4, 1, 2, 1, "8 medium Almighty attacks"),
    "cc": ("Assist Attack", 4, 1, 2, 1, "10 medium Almighty attacks"),
    "cd": ("Assist Attack", 4, 1, 2, 1, "12 medium Almighty attacks"),
    "ce": ("Assist Attack", 4, 1, 2, 1, "14 medium Almighty attacks"),
    "cf": ("Assist Attack", 4, 1, 2, 1, "Dummy"),
    "d0": ("Will of Flame", 9, 26, 0, 5, "Fire attacks pierce until the end of your turn"),
    "d1": ("Will of Frost", 9, 26, 0, 5, "Ice attacks pierce until the end of your turn"),
    "d2": ("Will of Thunder", 9, 26, 0, 5, "Elec attacks pierce until the end of your turn"),
    "d3": ("Will of Wind", 9, 26, 0, 5, "Force attacks pierce until the end of your turn"),
    "d4": ("Coercion", 10, 26, 0, 2, "Remove press turn icon on enemy's next turn"),
    "d5": ("Imposing Stance", 10, 41, 0, 2, "Remove press turn icon on enemy's next turn"),
    "d6": ("Spear of Michael", 11, 6, 2, 0, "Medium Phys attack"),
    "d7": ("Gungnir", 11, 18, 4, 0, "Severe Phys attack"),
    "d8": ("Normal Attack", 11, 1, 1, 0, "Asahi performs a basic attack"),
    "d9": ("Normal Attack", 11, 1, 1, 0, "Asahi performs a basic attack"),
    "da": ("Normal Attack", 11, 1, 1, 0, "Asahi performs a basic attack"),
    "db": ("Normal Attack", 11, 1, 1, 0, "Asahi performs a basic attack"),
    "dc": ("Normal Attack", 11, 1, 1, 0, "Asahi performs a basic attack"),
    "dd": ("Mouth of God", 4, 1, 0, 0, "Instant kill attack"),
    "de": ("Michael's Strike", 11, 18, 2, 2, "Medium Phys attack"),
    "df": ("Michael's Syphon", 11, 13, 2, 0, "Medium Phys attack. Drains enemy HP"),
    "e0": ("Michael's Twin Strike", 11, 16, 2, 1, "2 weak Phys attacks."),
    "e1": ("Michael's Pierce", 11, 24, 2, 0, "Medium Phys attack"),
    "e2": ("Cheer", 9, 46, 0, 3, "Induces Smirk"),
    "e3": ("Gungnir Strike", 11, 34, 3, 2, "Heavy Phys attack"),
    "e4": ("Gungnir Syphon", 11, 20, 3, 0, "Heave Phys attack. Drains enemy HP"),
    "e5": ("Gungnir Twin Strike", 11, 28, 2, 1, "2 medium Phys attacks"),
    "e6": ("Gungnir Pierce", 11, 38, 3, 0, "Heavy Phys attacks"),
    "e7": ("Gungnir Sever", 11, 43, 2, 1, "6 medium Phys attacks. Low hit rate"),
    "e8": ("Enduring Cheer", 9, 26, 0, 5, "Grants targets Endure until the end of turn"),
    "e9": ("Warding Shout", 9, 26, 0, 5, "Prevents status ailments until the next turn"),
    "ea": ("Pierce Armor", 11, 12, 2, 0, "Medium Phys attack"),
    "eb": ("Assassin's Nata", 11, 15, 0, 0, "Medium Phys attack. Ailments increase power"),
    "ec": ("Enmlightenment", 9, 4, 0, 3, "Drains weakness until your next turn"),
    "ed": ("5.67 Billion Hands", 4, 46, 1, 2, "Weak Almighty attack.Smirk: More power"),
    "ee": ("Venemous Raga", 7, 61, 0, 2, "Inflicts poison, Sick and Bind"),
    "ef": ("Dream Raga", 7, 61, 0, 2, "Inflicts Sleep, Panic and Charm"),
    "f0": ("Temporal Blade", 11, 1, 0, 0, "Might make Phys attack at start of battle. Pierce, instant kill"),
    "f1": ("Sneak attack", 11, 1, 0, 0, "Might make Phys attack at start of battle. Pierce, instant kill"),
    "f2": ("Infernal Hail", 1, 26, 2, 2, "Medium Ice attack"),
    "f3": ("Needlestorm", 3, 26, 2, 2, "Medium Force attack"),
    "f4": ("Photo Flash", 7, 16, 0, 2, "Inflicts the Daze ailment"),
    "f5": ("Seducing Shot", 7, 26, 0, 2, "Inflicts the Charm ailment"),
    "f6": ("Mother's Discipline", 12, 36, 2, 2, "3 medium Gun attacks"),
    "f7": ("Hellish Brand", 0, 16, 3, 0, "Heavy Fire attack"),
    "f8": ("Grand Tack", 12, 7, 3, 0, "Heavy Gun attack"),
    "f9": ("Grand Tack", 12, 7, 3, 0, "Heavy Gun attack"),
    "fa": ("King Bufula", 1, 20, 2, 2, "Madium Ice attack. Smirk: Defense down"),
    "fd": ("Adaptative Tactics", 6, 32, 4, 0, "Severe Light attack. Smirk: Instant kill"),
    "fe": ("Alluring Banter", 6, 32, 4, 0, "Severe Light attack. Smirk: Instant kill"),
    "ff": ("Dazzle Ray", 6, 32, 4, 0, "Severe Light attack. Smirk: Instant kill"),
    # "": ("", , , , , ""),
}

# Character ID's
ALL_CHARS = {
    "0": "MC",
    "40006": "Fumi",
    "30005": "Yamato",
    "9000b": "Keita",
    "8000a": "Makoto",
    "70009": "Jungo",
    "a000c": "Airi",
    "b000d": "Joe",
    "60008": "?",
    "50007": "??",
    "c000e": "???",
    "20004": "????",
    "10003": "?????"
}

# Demon Information
ALL_DEMONS = {
    "1": ("Reserved", "Godly", "(?)"),
    "2": ("Reserved", "Godly", "(?)"),
    "3": ("Reserved", "Godly", "(?)"),
    "4": ("Reserved", "Godly", "(?)"),
    "5": ("Reserved", "Godly", "(?)"),
    "6": ("???", "???", "(?)"),
    "7": ("Reserved", "Godly", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1, Multi-enemies)"),
    "8": ("Reserved", "???", "(?)"),
    "9": ("Reserved", "Godly", "(?) (Attack: Phys x2, Multi-enemies)"),
    "a": ("Satan", "Primal", ""),
    "b": ("Merkabah", "Herald", ""),
    "c": ("Seraph", "Herald", ""),
    "d": ("Reserved", "???", "(?)"),
    "e": ("Metatron", "Herald", ""),
    "f": ("Reserved", "???", "(?)"),
    "10": ("Mastema", "Herald", ""),
    "11": ("Aniel", "Herald", ""),
    "12": ("Sraosha", "Herald", ""),
    "13": ("Reserved", "???", "(?)"),
    "14": ("Azrael", "Herald", ""),
    "15": ("Kazfiel", "Herald", ""),
    "16": ("0", "Herald", "(?)"),
    "17": ("Israfel", "Herald", ""),
    "18": ("Victor", "Herald", ""),
    "19": ("Lailah", "Herald", ""),
    "1a": ("Reserved", "Herald", "(?)"),
    "1b": ("Dummy", "Herald", "(?)"),
    "1c": ("Dummy", "Herald", "(?)"),
    "1d": ("Dummy", "Herald", "(?)"),
    "1e": ("Dummy", "Herald", "(?)"),
    "1f": ("Lakshmi", "Megami", ""),
    "20": ("Norn", "Megami", ""),
    "21": ("Anat", "Megami", ""),
    "22": ("Tlazolteotl", "Megami", ""),
    "23": ("Pallas Athena", "Megami", ""),
    "24": ("Ishtar", "Megami", ""),
    "25": ("Scathach", "Megami", ""),
    "26": ("Reserved", "Megami", "(?)"),
    "27": ("Parvati", "Megami", ""),
    "28": ("Fortuna", "Megami", ""),
    "29": ("Hathor", "Megami", ""),
    "2a": ("Brigid", "Megami", ""),
    "2b": ("Izanami", "Megami", ""),
    "2c": ("Cleopatra", "Megami", ""),
    "2d": ("Reserved", "Megami", "(?)"),
    "2e": ("Reserved", "Megami", "(?)"),
    "2f": ("Garuda", "Avian", ""),
    "30": ("Yatagarasu", "Avian", ""),
    "31": ("Feng Huang", "Avian", ""),
    "32": ("Thunderbird", "Avian", ""),
    "33": ("Vidofnir", "Avian", ""),
    "34": ("Phoenix", "Avian", ""),
    "35": ("Suparna", "Avian", ""),
    "36": ("Hamsa", "Avian", ""),
    "37": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "38": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "39": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3a": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3b": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3c": ("Yggdrasil", "Tree", ""),
    "3d": ("Haoma", "Tree", ""),
    "3e": ("Kukunochi", "Tree", ""),
    "3f": ("Mayahuel", "Tree", ""),
    "40": ("Narcissus", "Tree", ""),
    "41": ("Daphne", "Tree", ""),
    "42": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "43": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "44": ("Reserved", "Tree", "(?)"),
    "45": ("Reserved", "Tree", "(?)"),
    "46": ("Reserved", "Tree", "(?)"),
    "47": ("Cherub", "Divine", ""),
    "48": ("Throne", "Divine", ""),
    "49": ("Dominion", "Divine", ""),
    "4a": ("Virtue", "Divine", ""),
    "4b": ("Power", "Divine", ""),
    "4c": ("Principality", "Divine", ""),
    "4d": ("Archangel", "Divine", ""),
    "4e": ("Angel", "Divine", "(Lvl 10)"),
    "4f": ("Reserved", "Divine", "(?)"),
    "50": ("Angel", "Divine", "(Lvl 82)"),
    "51": ("Reserved", "Divine", "(?)"),
    "52": ("Reserved", "Divine", "(?)"),
    "53": ("Reserved", "Divine", "(?)"),
    "54": ("Reserved", "Divine", "(?)"),
    "55": ("Da Peng", "Flight", ""),
    "56": ("Rukh", "Flight", ""),
    "57": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "58": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "59": ("Tuofei", "Flight", ""),
    "5a": ("Caladrius", "Flight", ""),
    "5b": ("Gu Huo Niao", "Flight", ""),
    "5c": ("Harpy", "Flight", ""),
    "5d": ("Tangata Manu", "Flight", ""),
    "5e": ("Reserved", "Flight", "(?)"),
    "5f": ("Reserved", "Flight", "(?)"),
    "60": ("Reserved", "Flight", "(?)"),
    "61": ("Reserved", "Flight", "(?)"),
    "62": ("Reserved", "Flight", "(?)"),
    "63": ("Ganesha", "Yoma", ""),
    "64": ("Master Therion", "Yoma", ""),
    "65": ("Xiuhtecuhtli", "Yoma", ""),
    "66": ("Valkyrie", "Yoma", ""),
    "67": ("Shiwanna", "Yoma", ""),
    "68": ("Dis", "Yoma", ""),
    "69": ("Karasu Tengu", "Yoma", ""),
    "6a": ("Koppa Tengu", "Yoma", ""),
    "6b": ("Agathion", "Yoma", ""),
    "6c": ("Vodyanik", "Yoma", ""),
    "6d": ("Centaur", "Yoma", ""),
    "6e": ("Reserved", "Yoma", "(?)"),
    "6f": ("Reserved", "Yoma", "(?)"),
    "70": ("Reserved", "Yoma", "(?)"),
    "71": ("Reserved", "Yoma", "(?)"),
    "72": ("Peri", "Nymph", ""),
    "73": ("Sarasvati", "Nymph", ""),
    "74": ("Reserved", "Nymph", "(?)"),
    "75": ("Senri", "Nymph", ""),
    "76": ("Apsaras", "Nymph", ""),
    "77": ("Kikuri-Hime", "Nymph", ""),
    "78": ("Reserved", "Nymph", "(?)"),
    "79": ("Reserved", "Nymph", "(?)"),
    "7a": ("Reserved", "Nymph", "(?)"),
    "7b": ("Reserved", "Nymph", "(?)"),
    "7c": ("Demiurge", "Vile", ""),
    "7d": ("Seth", "Vile", ""),
    "7e": ("Pales", "Viles", ""),
    "7f": ("Alciel", "Vile", ""),
    "80": ("Taotie", "Vile", ""),
    "81": ("Pachacamac", "Vile", ""),
    "82": ("Reserved", "Vile", "(?)"),
    "83": ("Mishaguji", "Vile", ""),
    "84": ("Baphomet", "Vile", ""),
    "85": ("Reserved", "Vile", "(?)"),
    "86": ("Reserved", "Vile", "(?)"),
    "87": ("Reserved", "Vile", "(?)"),
    "88": ("Reserved", "Vile", "(?)"),
    "89": ("Reserved", "Vile", "(?)"),
    "8a": ("Hresvelgr", "Raptor", ""),
    "8b": ("Huoniao", "Raptor", ""),
    "8c": ("Anzu", "Raptor", ""),
    "8d": ("Gurr", "Raptor", ""),
    "8e": ("Zhen", "Raptor", ""),
    "8f": ("Itsumade", "Raptor", ""),
    "90": ("Moh Shuvuu", "Raptor", ""),
    "91": ("Camazotz", "Raptor", ""),
    "92": ("Fuxi", "Raptor", ""),
    "93": ("Reserved", "Raptor", "(?)"),
    "94": ("Reserved", "Raptor", "(?)"),
    "95": ("Reserved", "Raptor", "(?)"),
    "96": ("Reserved", "Raptor", "(?)"),
    "97": ("Reserved", "Raptor", "(?)"),
    "98": ("Erikonig", "Wood", ""),
    "99": ("Alraune", "Wood", ""),
    "9a": ("Zaccoum", "Wood", ""),
    "9b": ("Skogsra", "Wood", ""),
    "9c": ("Mandrake", "Wood", ""),
    "9d": ("Shan Xiao", "Wood", ""),
    "9e": ("Reserved", "Wood", "(?)"),
    "9f": ("Reserved", "Wood", "(?)"),
    "a0": ("Reserved", "Wood", "(?)"),
    "a1": ("Reserved", "Wood", "(?)"),
    "a2": ("Reserved", "Wood", "(?)"),
    "a3": ("Reserved", "Deity", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1~2, 1 enemy)"),
    "a4": ("Reserved", "Deity", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "a5": ("Hachiman", "Deity", ""),
    "a6": ("Apsu", "Deity", ""),
    "a7": ("Baal", "Deity", ""),
    "a8": ("Odin", "Deity", ""),
    "a9": ("Ometeotl", "Deity", ""),
    "aa": ("Lord Nandou", "Deity", ""),
    "ab": ("Prometheus", "Deity", ""),
    "ac": ("Inti", "Deity", ""),
    "ad": ("Thoth", "Deity", ""),
    "ae": ("Krishna", "Deity", ""),
    "af": ("Mahamayuri", "Deity", ""),
    "b0": ("Osiris", "Deity", ""),
    "b1": ("Maitreya", "Deity", ""),
    "b2": ("Reserved", "Deity", "(?)"),
    "b3": ("Reserved", "Deity", "(?)"),
    "b4": ("Amaterasu", "Amatsu", ""),
    "b5": ("Take-Mikazuchi", "Amatsu", ""),
    "b6": ("Reserved", "Amatsu", "(?) (Weak: Sick)"),
    "b7": ("Reserved", "Amatsu", "(?)"),
    "b8": ("Ame no Uzume", "Amatsu", ""),
    "b9": ("Reserved", "Amatsu", "(?)"),
    "ba": ("Reserved", "Kunitsu", "(?)"),
    "bb": ("Reserved", "Famed", "(?)"),
    "bc": ("Reserved", "Human", "(?)"),
    "bd": ("Reserved", "Human", "(?)"),
    "be": ("Barong", "Avatar", ""),
    "bf": ("Anubis", "Avatar", ""),
    "c0": ("Ukano Mitama", "Avatar", ""),
    "c1": ("Chimera", "Avatar", ""),
    "c2": ("Kaiming Shou", "Avatar", ""),
    "c3": ("Makami", "Avatar", ""),
    "c4": ("Kamapua'a", "Avatar", ""),
    "c5": ("Shiisa", "Avatar", ""),
    "c6": ("Reserved", "Avatar", "(?)"),
    "c7": ("Reserved", "Avatar", "(?)"),
    "c8": ("Reserved", "Avatar", "(?)"),
    "c9": ("Reserved", "Avatar", "(?)"),
    "ca": ("Reserved", "Avatar", "(?)"),
    "cb": ("Sphinx", "Holy", ""),
    "cc": ("Sleipnir", "Holy", ""),
    "cd": ("Baihu", "Holy", ""),
    "ce": ("Airavata", "Holy", ""),
    "cf": ("Chironnupu", "Holy", ""),
    "d0": ("Qing Niuguai", "Holy", ""),
    "d1": ("Pabilsag", "Holy", ""),
    "d2": ("Apis", "Holy", ""),
    "d3": ("Heqet", "Holy", ""),
    "d4": ("Reserved", "Holy", "(?)"),
    "d5": ("Reserved", "Holy", "(?)"),
    "d6": ("Reserved", "Holy", "(?)"),
    "d7": ("Reserved", "Holy", "(?)"),
    "d8": ("Reserved", "Holy", "(?)"),
    "d9": ("Heimdall", "Genma", ""),
    "da": ("Hanuman", "Genma", ""),
    "db": ("Jarilo", "Genma", ""),
    "dc": ("Kresnik", "Genma", ""),
    "dd": ("Cu Chulainn", "Genma", ""),
    "de": ("Kurama Tengu", "Genma", ""),
    "df": ("Tlaloc", "Genma", ""),
    "e0": ("Frost Ace", "Genma", ""),
    "e1": ("Nata Taishi", "Genma", ""),
    "e2": ("Tam Lin", "Genma", ""),
    "e3": ("Ictinike", "Genma", ""),
    "e4": ("Baldur", "Genma", ""),
    "e5": ("Reserved", "Genma", "(?)"),
    "e6": ("Reserved", "Genma", "(?)"),
    "e7": ("Reserved", "Genma", "(?)"),
    "e8": ("Reserved", "Genma", "(?)"),
    "e9": ("Demonee-ho", "Fairy", ""),
    "ea": ("Titania", "Fairy", ""),
    "eb": ("Oberon", "Fairy", ""),
    "ec": ("Vivian", "Fairy", ""),
    "ed": ("Spriggan", "Fairy", ""),
    "ee": ("Nadja", "Fairy", ""),
    "ef": ("Lorelei", "Fairy", ""),
    "f0": ("Kelpie", "Fairy", ""),
    "f1": ("Silky", "Fairy", ""),
    "f2": ("High Pixie", "Fairy", ""),
    "f3": ("Setanta", "Fairy", ""),
    "f4": ("Pyro Jack", "Fairy", ""),
    "f5": ("Jack Frost", "Fairy", ""),
    "f6": ("Goblin", "Fairy", ""),
    "f7": ("Reserved", "Fairy", "(?)"),
    "f8": ("Pixie", "Fairy", ""),
    "f9": ("Napaea", "Fairy", ""),
    "fa": ("Reserved", "???", "(?)"),
    "fb": ("Reserved", "Fairy", "(?)"),
    "fc": ("Reserved", "Fairy", "(?)"),
    "fd": ("Reserved", "Fairy", "(?)"),
    "fe": ("Cerberus", "Beast", ""),
    "ff": ("Ammut", "Beast", ""),
    "100": ("Orthus", "Beast", ""),
    "101": ("Dormath", "Beast", ""),
    "102": ("Hsing-Hsing", "Beast", ""),
    "103": ("Nekomata", "Beast", ""),
    "104": ("Reserved", "Beast", "(?)"),
    "105": ("Inugami", "Beast", ""),
    "106": ("Kabuso", "Beast", ""),
    "107": ("Kaso", "Beast", ""),
    "108": ("Stonka", "Beast", ""),
    "109": ("Gryphon", "Beast", ""),
    "10a": ("Hairy Jack", "Beast", ""),
    "10b": ("Reserved", "Beast", "(?)"),
    "10c": ("Reserved", "???", "(?)"),
    "10d": ("Reserved", "Beast", "(?)"),
    "10e": ("Reserved", "Beast", "(?)"),
    "10f": ("Gogmagog", "Jirae", ""),
    "110": ("Tlaltecuhtli", "Jirae", ""),
    "111": ("Titan", "Jirae", ""),
    "112": ("Tsuchigumo", "Jirae", ""),
    "113": ("Kwancha", "Jirae", ""),
    "114": ("Sudama", "Jirae", ""),
    "115": ("Hua Po", "Jirae", ""),
    "116": ("Knocker", "Jirae", ""),
    "117": ("Dwarf", "Jirae", ""),
    "118": ("Reserved", "Jirae", "(?)"),
    "119": ("Reserved", "Jirae", "(?)"),
    "11a": ("Reserved", "Jirae", "(?)"),
    "11b": ("Reserved", "Jirae", "(?)"),
    "11c": ("Reserved", "Jirae", "(?)"),
    "11d": ("Reserved", "Snake", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "11e": ("Pendragon", "Snake", ""),
    "11f": ("Orochi", "Snake", ""),
    "120": ("Ouroboros", "Snake", ""),
    "121": ("Gui Xian", "Snake", ""),
    "122": ("Yurlungur", "Snake", ""),
    "123": ("Vouivre", "Snake", ""),
    "124": ("Nozuchi", "Snake", ""),
    "125": ("Naga", "Snake", ""),
    "126": ("Reserved", "Snake", "(?)"),
    "127": ("Reserved", "Snake", "(?)"),
    "128": ("Reserved", "Snake", "(?)"),
    "129": ("Reserved", "Snake", "(?)"),
    "12a": ("Reserved", "Snake", "(?)"),
    "12b": ("Mot", "Reaper", ""),
    "12c": ("Nergal", "Reaper", ""),
    "12d": ("Guedhe", "Reaper", ""),
    "12e": ("Persephone", "Reaper", ""),
    "12f": ("Orcus", "Reaper", ""),
    "130": ("Hel", "Reaper", ""),
    "131": ("Ixtab", "Reaper", ""),
    "132": ("Cernunnos", "Reaper", ""),
    "133": ("Reserved", "Reaper", "(?)"),
    "134": ("Reserved", "Reaper", "(?)"),
    "135": ("Reserved", "Reaper", "(?)"),
    "136": ("Fenrir", "Wilder", ""),
    "137": ("Taowu", "Wilder", ""),
    "138": ("Cabracan", "Wilder", ""),
    "139": ("Catoblepas", "Wilder", ""),
    "13a": ("Manticore", "Wilder", ""),
    "13b": ("Porewit", "Wilder", ""),
    "13c": ("Peallaidh", "Wilder", ""),
    "13d": ("Nue", "Wilder", ""),
    "13e": ("Raiju", "Wilder", ""),
    "13f": ("Jueyuan", "Wilder", ""),
    "140": ("Chagrin", "Wilder", ""),
    "141": ("Reserved", "Wilder", "(?)"),
    "142": ("Reserved", "Wilder", "(?)"),
    "143": ("Reserved", "Wilder", "(?)"),
    "144": ("Reserved", "Wilder", "(?)"),
    "145": ("Reserved", "Wilder", "(?)"),
    "146": ("Hekatoncheires", "Jaki", ""),
    "147": ("Girimehkala", "Jaki", ""),
    "148": ("Grendel", "Jaki", ""),
    "149": ("Reserved", "Jaki", "(?)"),
    "14a": ("Rakshasa", "Jaki", ""),
    "14b": ("Black Frost", "Jaki", ""),
    "14c": ("Wendigo", "Jaki", ""),
    "14d": ("Ippon-Datara", "Jaki", ""),
    "14e": ("Gremlin", "Jaki", ""),
    "14f": ("Lham Dearg", "Jaki", ""),
    "150": ("Ogre", "Jaki", ""),
    "151": ("Reserved", "Jaki", "(?)"),
    "152": ("Reserved", "Jaki", "(?)"),
    "153": ("Reserved", "Jaki", "(?)"),
    "154": ("Reserved", "Jaki", "(?)"),
    "155": ("Arachne", "Vermin", ""),
    "156": ("Okiku-Mushi", "Vermin", ""),
    "157": ("Ubu", "Vermin", ""),
    "158": ("Mothman", "Vermin", ""),
    "159": ("Myrmecolion", "Vermin", ""),
    "15a": ("Reserved", "Vermin", "(?)"),
    "15b": ("Reserved", "Vermin", "(?)"),
    "15c": ("Reserved", "Vermin", "(?)"),
    "15d": ("Reserved", "Vermin", "(?)"),
    "15e": ("Reserved", "Vermin", "(?)"),
    "15f": ("Shiva", "Fury", ""),
    "160": ("Susano-o", "Fury", ""),
    "161": ("Kartikeya", "Fury", ""),
    "162": ("Beiji-Weng", "Fury", ""),
    "163": ("Wu Kong", "Fury", ""),
    "164": ("Chernobog", "Fury", ""),
    "165": ("Asura", "Fury", ""),
    "166": ("Tonatiuh", "Fury", ""),
    "167": ("Ares", "Fury", ""),
    "168": ("Mitra-Buddha", "Fury", ""),
    "169": ("Reserved", "???", "(?)"),
    "16a": ("Reserved", "Fury", "(?)"),
    "16b": ("Reserved", "Fury", "(?)"),
    "16c": ("Reserved", "Fury", "(?)"),
    "16d": ("Xi Wangmu", "Lady", ""),
    "16e": ("Skadi", "Lady", ""),
    "16f": ("Black Maria", "Lady", ""),
    "170": ("Inanna", "Lady", ""),
    "171": ("Asherah", "Lady", ""),
    "172": ("Diana", "Lady", ""),
    "173": ("Hariti", "Lady", ""),
    "174": ("Sedna", "Lady", ""),
    "175": ("Dzelarhons", "Lady", ""),
    "176": ("Pele", "Lady", ""),
    "177": ("Isis", "Lady", ""),
    "178": ("Reserved", "Lady", "(?)"),
    "179": ("Reserved", "Lady", "(?)"),
    "17a": ("Reserved", "Lady", "(?)"),
    "17b": ("Reserved", "Lady", "(?)"),
    "17c": ("Huang Long", "Dragon", ""),
    "17d": ("Quetzalcoatl", "Dragon", ""),
    "17e": ("Zhu Yin", "Dragon", ""),
    "17f": ("Illuyanka", "Dragon", ""),
    "180": ("Long", "Dragon", ""),
    "181": ("Gucumatz", "Dragon", ""),
    "182": ("Patrimpas", "Dragon", ""),
    "183": ("Makara", "Dragon", ""),
    "184": ("Reserved", "Dragon", "(?) (Attack: Phys x2, 1 enemy)"),
    "185": ("Reserved", "Dragon", "(?)"),
    "186": ("Reserved", "Dragon", "(?)"),
    "187": ("Reserved", "Dragon", "(?)"),
    "188": ("Reserved", "Dragon", "(?)"),
    "189": ("Thor", "Kishin", ""),
    "18a": ("Marishiten", "Kishin", ""),
    "18b": ("Bishamonten", "Kishin", ""),
    "18c": ("Jikokuten", "Kishin", ""),
    "18d": ("Zhong Kui", "Kishin", ""),
    "18e": ("Koumokuten", "Kishin", ""),
    "18f": ("Zouchouten", "Kishin", ""),
    "190": ("Reserved", "Kishin", "(?)"),
    "191": ("Reserved", "Kishin", "(?)"),
    "192": ("Reserved", "Kishin", "(?)"),
    "193": ("Reserved", "Kishin", "(?)"),
    "194": ("Reserved", "Kishin", "(?)"),
    "195": ("Arahabaki", "Kunitsu", ""),
    "196": ("Kushinada-hime", "Kunitsu", ""),
    "197": ("Okuninushi", "Kunitsu", ""),
    "198": ("Take-Minakata", "Kunitsu", ""),
    "199": ("Oumitsunu", "Kunitsu", ""),
    "19a": ("Hitokotonushi", "Kunitsu", ""),
    "19b": ("Sukuna-Hikona", "Kunitsu", ""),
    "19c": ("Reserved", "Kunitsu", "(?)"),
    "19d": ("Reserved", "Kunitsu", "(?)"),
    "19e": ("Samael", "Fallen", ""),
    "19f": ("Murmur", "Fallen", ""),
    "1a0": ("Gemori", "Fallen", ""),
    "1a1": ("Adramelech", "Fallen", ""),
    "1a2": ("Reserved", "Fallen", "(?)"),
    "1a3": ("Decarabia", "Fallen", ""),
    "1a4": ("Nebiros", "Fallen", ""),
    "1a5": ("Ose", "Fallen", ""),
    "1a6": ("Dantalian", "Fallen", ""),
    "1a7": ("Orias", "Fallen", ""),
    "1a8": ("Halphas", "Fallen", ""),
    "1a9": ("Bifrons", "Fallen", ""),
    "1aa": ("Melchom", "Fallen", ""),
    "1ab": ("Azazel->moved to Tyant", "Fallen", "(?)"),
    "1ac": ("Shax", "Fallen", ""),
    "1ad": ("Barbatos", "Fallen", ""),
    "1ae": ("Botis", "Fallen", ""),
    "1af": ("Reserved", "Fallen", "(?)"),
    "1b0": ("Ongyo-Ki", "Brute", ""),
    "1b1": ("Berserker", "Brute", ""),
    "1b2": ("Sui-Ki", "Brute", ""),
    "1b3": ("Fuu-Ki", "Brute", ""),
    "1b4": ("Kin-Ki", "Brute", ""),
    "1b5": ("Yomotsu Ikusa", "Brute", ""),
    "1b6": ("Yamawaro", "Brute", ""),
    "1b7": ("Momunofu", "Brute", ""),
    "1b8": ("Azumi", "Brute", ""),
    "1b9": ("Oni", "Brute", ""),
    "1ba": ("Reserved", "Brute", "(?)"),
    "1bb": ("Yaksha", "Brute", ""),
    "1bc": ("Bilwis", "Brute", ""),
    "1bd": ("Reserved", "Brute", "(?)"),
    "1be": ("Reserved", "Brute", "(?)"),
    "1bf": ("Reserved", "Brute", "(?)"),
    "1c0": ("Rangda", "Femme", ""),
    "1c1": ("Dakini", "Femme", ""),
    "1c2": ("Atropos", "Femme", ""),
    "1c3": ("Lachesis", "Femme", ""),
    "1c4": ("Clotho", "Femme", ""),
    "1c5": ("Yuki Jyorou", "Femme", ""),
    "1c6": ("Shikome", "Femme", ""),
    "1c7": ("Strix", "Femme", ""),
    "1c8": ("Leanan Sidhe", "Femme", ""),
    "1c9": ("Mermaid", "Femme", ""),
    "1ca": ("Taraka", "Femme", ""),
    "1cb": ("Kali", "Femme", ""),
    "1cc": ("Medusa", "Femme", ""),
    "1cd": ("Reserved", "Femme", "(?)"),
    "1ce": ("Maya", "Night", ""),
    "1cf": ("Reserved", "Night", "(?)"),
    "1d0": ("Reserved", "Night", "(?)"),
    "1d1": ("Queen Mab", "Night", ""),
    "1d2": ("Wild Hunt", "Night", ""),
    "1d3": ("Succubus", "Night", ""),
    "1d4": ("Kaiwan", "Night", ""),
    "1d5": ("Incubus", "Night", ""),
    "1d6": ("Kikimora", "Night", ""),
    "1d7": ("Lilim", "Night", ""),
    "1d8": ("Sandman", "Night", ""),
    "1d9": ("Fomorian", "Night", ""),
    "1da": ("Mokoi", "Night", ""),
    "1db": ("Reserved", "Night", "(?)"),
    "1dc": ("Reserved", "Night", "(?)"),
    "1dd": ("Reserved", "Night", "(?)"),
    "1de": ("Reserved", "Night", "(?)"),
    "1df": ("Reserved", "Night", "(?)"),
    "1e0": ("Lucifer", "Tyrant", ""),
    "1e1": ("Mara", "Tyrant", ""),
    "1e2": ("Chi You", "Tyrant", ""),
    "1e3": ("Surt", "Tyrant", ""),
    "1e4": ("Tzitzimitl", "Tyrant", ""),
    "1e5": ("Beelzebub", "Tyrant", ""),
    "1e6": ("Abaddon", "Tyrant", ""),
    "1e7": ("Loki", "Tyrant", ""),
    "1e8": ("Belial", "Tyrant", ""),
    "1e9": ("Astaroth", "Tyrant", "(?) (Dummied out leftover from SMTIV)"),
    "1ea": ("Balor", "Tyrant", ""),
    "1eb": ("King Frost", "Tyrant", ""),
    "1ec": ("Samyaza", "Tyrant", ""),
    "1ed": ("Horkos", "Tyrant", ""),
    "1ee": ("Mithras", "Tyrant", ""),
    "1ef": ("Morax", "Tyrant", ""),
    "1f0": ("Azazel", "Tyrant", ""),
    "1f1": ("Mephisto", "Tyrant", ""),
    "1f2": ("Lucifuge", "Tyrant", ""),
    "1f3": ("Reserved", "Tyrant", "(?)"),
    "1f4": ("Reserved", "Tyrant", "(?)"),
    "1f5": ("Fafnir", "Drake", ""),
    "1f6": ("Ym", "Drake", ""),
    "1f7": ("Nidhoggr", "Drake", ""),
    "1f8": ("Tiamat", "Drake", ""),
    "1f9": ("Mushussu", "Drake", ""),
    "1fa": ("Kingu", "Drake", ""),
    "1fb": ("Basilisk", "Drake", ""),
    "1fc": ("Bai Suzhen", "Drake", ""),
    "1fd": ("Toubyou", "Drake", ""),
    "1fe": ("Zhu Tun She", "Drake", ""),
    "1ff": ("Vasuki", "Drake", ""),
    "200": ("Phython", "Drake", ""),
    "201": ("Reserved", "Drake", "(?)"),
    "202": ("Reserved", "Drake", "(?)"),
    "203": ("Reserved", "Drake", "(?)"),
    "204": ("Legion", "Spirit", ""),
    "205": ("Pisaca", "Spirit", ""),
    "206": ("Inferno", "Spirit", ""),
    "207": ("Macabre", "Spirit", ""),
    "208": ("Quicksilver", "Spirit", ""),
    "209": ("Poltergeist", "Spirit", ""),
    "20a": ("Wicker Man", "Spirit", ""),
    "20b": ("Dybbuk", "Spirit", ""),
    "20c": ("Garrote", "Spirit", ""),
    "20d": ("Reserved", "Spirit", "(?)"),
    "20e": ("Reserved", "Spirit", "(?)"),
    "20f": ("Reserved", "Spirit", "(?)"),
    "210": ("Reserved", "Spirit", "(?)"),
    "211": ("Reserved", "Foul", "(?)"),
    "212": ("Reserved", "Foul", "(?)"),
    "213": ("Mad Gasser", "Foul", ""),
    "214": ("Reserved", "Foul", ""),
    "215": ("Night Stalker", "Foul", ""),
    "216": ("Hooligan", "Foul", ""),
    "217": ("Jack the Ripper", "Foul", ""),
    "218": ("Slime", "Foul", ""),
    "219": ("Tattooed Man", "Foul", ""),
    "21a": ("Reserved", "Foul", "(?)"),
    "21b": ("Reserved", "Foul", "(?)"),
    "21c": ("Reserved", "Foul", "(?)"),
    "21d": ("Reserved", "Foul", "(?)"),
    "21e": ("Vetala", "Ghost", ""),
    "21f": ("Kudlak", "Ghost", ""),
    "220": ("Ghoul", "Ghost", ""),
    "221": ("Enku", "Ghost", ""),
    "222": ("Churel", "Ghost", ""),
    "223": ("Mou-Ryo", "Ghost", ""),
    "224": ("Obariyon", "Ghost", ""),
    "225": ("Preta", "Ghost", ""),
    "226": ("Strigoii", "Ghost", ""),
    "227": ("Dullahan", "Ghost", "(?) (Dummied out leftover from SMTIV)"),
    "228": ("Reserved", "Ghost", "(?)"),
    "229": ("Reserved", "Ghost", "(?)"),
    "22a": ("Reserved", "Ghost", "(?)"),
    "22b": ("Reserved", "Ghost", "(?)"),
    "22c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "22d": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "22e": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "22f": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "230": ("Reserved", "Mitama", "(?)"),
    "231": ("Reserved", "Mitama", "(?)"),
    "232": ("Reserved", "Mitama", "(?)"),
    "233": ("Reserved", "Mitama", "(?)"),
    "234": ("Reserved", "Mitama", "(?)"),
    "235": ("Salamander", "Element", ""),
    "236": ("Undine", "Element", ""),
    "237": ("Sylph", "Element", ""),
    "238": ("Gnome", "Element", ""),
    "239": ("Flaemis", "Element", ""),
    "23a": ("Aquans", "Element", ""),
    "23b": ("Aeros", "Element", ""),
    "23c": ("Erthys", "Element", ""),
    "23d": ("Reserved", "Element", "(?)"),
    "23e": ("Reserved", "Element", "(?)"),
    "23f": ("Reserved", "Element", "(?)"),
    "240": ("Reserved", "Element", "(?)"),
    "241": ("Reserved", "Element", "(?)"),
    "242": ("Mother Harlot", "Fiend", ""),
    "243": ("Trumpeter", "Fiend", ""),
    "244": ("Pale Rider", "Fiend", ""),
    "245": ("Black Rider", "Fiend", ""),
    "246": ("Red Rider", "Fiend", ""),
    "247": ("White Rider", "Fiend", ""),
    "248": ("Reserved", "Fiend", "(?)"),
    "249": ("Matador", "Fiend", ""),
    "24a": ("David", "Fiend", ""),
    "24b": ("Reserved", "Fiend", "(?)"),
    "24c": ("Reserved", "???", "(?)"),
    "24d": ("Reserved", "Fiend", "(?)"),
    "24e": ("Reserved", "Fiend", "(?)"),
    "24f": ("Reserved", "Fiend", "(?)"),
    "250": ("Kangiten", "Enigma", ""),
    "251": ("Kama", "Enigma", ""),
    "252": ("Kinmamon", "Enigma", ""),
    "253": ("Futotama", "Enigma", ""),
    "254": ("Kanbari", "Enigma", ""),
    "255": ("Reserved", "Enigma", "(?)"),
    "256": ("Reserved", "Enigma", "(?)"),
    "257": ("Reserved", "Enigma", "(?)"),
    "258": ("Reserved", "Enigma", "(?)"),
    "259": ("Reserved", "Enigma", "(?)"),
    "25a": ("Hare of Inaba", "Food", ""),
    "25b": ("Kuda", "Food", ""),
    "25c": ("Chupacabra", "Food", ""),
    "25d": ("Mamedanuki", "Food", ""),
    "25e": ("Katakirauwa", "Food", ""),
    "25f": ("Onmoraki", "Food", ""),
    "260": ("Reserved", "Food", "(?)"),
    "261": ("Reserved", "Food", "(?)"),
    "262": ("Reserved", "Food", "(?)"),
    "263": ("Reserved", "Food", "(?)"),
    "264": ("Reserved", "Food", "(?)"),
    "265": ("Moved to Diff Race: Masakado", "Zealot", "(?) (Entire portrait is solid white)"),
    "266": ("Tezcatlipoca", "Zealot", ""),
    "267": ("Attis", "Zealot", ""),
    "268": ("Aramisaki", "Zealot", ""),
    "269": ("Dionysus", "Zealot", ""),
    "26a": ("Ogun", "Zealot", ""),
    "26b": ("Reserved", "Zealot", "(?)"),
    "26c": ("Reserved", "Zealot", "(?)"),
    "26d": ("Reserved", "Zealot", "(?)"),
    "26e": ("Reserved", "Zealot", "(?)"),
    "26f": ("Reserved", "Zealot", "(?)"),
    "270": ("Alilat", "Entity", ""),
    "271": ("Reserved", "Entity", "(?)"),
    "272": ("Reserved", "Entity", "(?)"),
    "273": ("Reserved", "Entity", "(?)"),
    "274": ("Reserved", "Entity", "(?)"),
    "275": ("Reserved", "Entity", "(?)"),
    "276": ("Huang Di", "Famed", ""),
    "277": ("Tokisada", "Famed", ""),
    "278": ("Rama", "Famed", ""),
    "279": ("Kanseiteikun", "Famed", ""),
    "27a": ("Siegfried", "Famed", ""),
    "27b": ("Hagen", "Famed", ""),
    "27c": ("Jeanne d'Arc", "Famed", ""),
    "27d": ("Lanling Wang", "Famed", ""),
    "27e": ("Yoshitsune", "Famed", ""),
    "27f": ("Tenkai", "Famed", ""),
    "280": ("Reserved", "Famed", "(?)"),
    "281": ("Reserved", "Famed", "(?)"),
    "282": ("DLC Stock", "Famed", "(?) (Resist: Charm/Daze/Mute)"),
    "283": ("Reserved", "Famed", "(?)"),
    "284": ("Ashura-kai Man", "Human", "(Enemy-only)"),
    "285": ("Ashura-kai Woman", "Human", "(Enemy-only)"),
    "286": ("Reserved", "Human", "(?)"),
    "287": ("Reserved", "Human", "(?)"),
    "288": ("Reserved", "Human", "(?)"),
    "289": ("Reserved", "Human", "(?)"),
    "28a": ("Reserved", "Human", "(?)"),
    "28b": ("Reserved", "Human", "(?)"),
    "28c": ("Reserved", "Human", "(?)"),
    "28d": ("Gaea Man", "Human", "(Enemy-only)"),
    "28e": ("Gaea Woman", "Human", "(Enemy-only)"),
    "28f": ("Reserved", "Human", "(?)"),
    "290": ("Reserved", "Human", "(?)"),
    "291": ("Samurai Zombie", "Undead", "(Male) (Enemy-only, unused leftover from SMTIV)"),
    "292": ("Samurai Zombie", "Undead", "(Female) (Enemy-only, unused leftover from SMTIV)"),
    "293": ("Zombie", "Undead", "(Enemy-only, unused leftover from SMTIV)"),
    "294": ("Alice", "Undead", ""),
    "295": ("Reserved", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "296": ("Zombie Cop", "Undead", ""),
    "297": ("Deleted", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "298": ("Deleted", "Undead", "(?)"),
    "299": ("Patriot", "Undead", ""),
    "29a": ("Corpse", "Undead", ""),
    "29b": ("Reserved", "Cyber", "(?)"),
    "29c": ("Reserved", "Cyber", "(?)"),
    "29d": ("Flynn", "Human", "(YHVH Fight, Bonds Flynn?)"),
    "29e": ("Flynn", "Human", "(YHVH Fight, Massacre Flynn?)"),
    "29f": ("Walter", "Human", "(YHVH Fight)"),
    "2a0": ("Jonathan", "Human", "(YHVH Fight)"),
    "2a1": ("Isabeau", "Human", "(YHVH Fight)"),
    "2a2": ("Satan", "Primal", "(YHVH Fight)"),
    "2a3": ("Timothy", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a4": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a5": ("Navarre", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a6": ("Portable Cannon", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a7": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a8": ("Orb of the Gates", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a9": ("Giant Horde", "Horde", "(Unused)"),
    "2aa": ("Innocent Horde", "Horde", "(Enemy-only)"),
    "2ab": ("Oni Horde", "Horde", "(Enemy-only)"),
    "2ac": ("Dragon Horde", "Horde", "(Enemy-only)"),
    "2ad": ("Dead Horde", "Horde", "(Enemy-only)"),
    "2ae": ("Wildfire Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2af": ("Demon Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2b0": ("Azteca Force", "Horde", "(Enemy-only)"),
    "2b1": ("Jaki Horde", "Horde", "(Enemy-only)"),
    "2b2": ("Greek Force", "Horde", "(Enemy-only)"),
    "2b3": ("Angel Army", "Horde", "(Enemy-only)"),
    "2b4": ("Defiant Horde", "Horde", "(Enemy-only)"),
    "2b5": ("Freezing Horde", "Horde", "(Enemy-only)"),
    "2b6": ("Gale Horde", "Horde", "(Unused)"),
    "2b7": ("Fallen Horde", "Horde", "(Enemy-only)"),
    "2b8": ("Demon Army", "Horde", "(Enemy-only)"),
    "2b9": ("Not Used", "Horde", ""),
    "2ba": ("Thunder Horde", "Horde", "(Enemy-only)"),
    "2bb": ("Blazing Horde", "Horde", "(Enemy-only)"),
    "2bc": ("Indian Horde", "Horde", "(Enemy-only)"),
    "2bd": ("Not Used", "Horde", ""),
    "2be": ("Not Used", "Horde", ""),
    "2bf": ("Inferno Horde", "Horde", "(Enemy-only)"),
    "2c0": ("Blizzard Horde", "Horde", "(Enemy-only)"),
    "2c1": ("Tengu Horde", "Horde", "(Enemy-only)"),
    "2c2": ("Jack Union", "Horde", "(Enemy-only)"),
    "2c3": ("Frosts", "Horde", "(Unused leftover from SMTIV)"),
    "2c4": ("Norse Force", "Horde", "(Enemy-only)"),
    "2c5": ("Not Used", "Horde", ""),
    "2c6": ("Pirate Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2c7": ("A. Demon Army", "Horde", "(Enemy-only)"),
    "2c8": ("A. Angel Army", "Horde", "(Enemy-only)"),
    "2c9": ("A. Angel Horde", "Horde", "(Enemy-only)"),
    "2ca": ("Herald Army", "Horde", "(Enemy-only)"),
    "2cb": ("Seraph Army", "Horde", "(Enemy-only)"),
    "2cc": ("Metatron Army", "Horde", "(Enemy-only)"),
    "2cd": ("Angel Army", "Horde", "(Enemy-only)"),
    "2ce": ("Not Used", "Horde", ""),
    "2cf": ("Not Used", "Horde", ""),
    "2d0": ("Not Used", "Horde", ""),
    "2d1": ("Not Used", "Horde", ""),
    "2d2": ("Not Used", "Horde", ""),
    "2d3": ("Itsumade Horde", "Horde", "(Enemy-only)"),
    "2d4": ("Not Used", "Horde", ""),
    "2d5": ("Strix Horde", "Horde", "(Enemy-only)"),
    "2d6": ("Demonstrators", "Horde", "(Enemy-only)"),
    "2d7": ("Obsessed Horde", "Horde", "(Enemy-only)"),
    "2d8": ("Greedy Horde", "Horde", "(Enemy-only)"),
    "2d9": ("Maruo Faction", "Horde", "(Enemy-only)"),
    "2da": ("Zaccoum Horde", "Horde", "(Enemy-only)"),
    "2db": ("Corpse Army", "Horde", "(Enemy-only)"),
    "2dc": ("Yomi Army", "Horde", "(Enemy-only)"),
    "2dd": ("Rakshasa", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2de": ("Ares", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2df": ("Long", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2e0": ("Black Frost", "Jaki", "(Boss version)"),
    "2e1": ("Tlaltecuhtli", "Jirae", "(Boss version)"),
    "2e2": ("Prometheus", "Deity", "(Boss version)"),
    "2e3": ("Dormarth", "Beast", "(Boss version)"),
    "2e4": ("Loki", "Tyrant", "(Boss version)"),
    "2e5": ("Lanling Wang", "Famed", "(Boss version)"),
    "2e6": ("Girimehkala", "Jaki", "(Boss version)"),
    "2e7": ("Aramisaki", "Zealot", "(Boss version)"),
    "2e8": ("Ashura-kai Man", "Human", "(Boss version)"),
    "2e9": ("Shax", "Fallen", "(Boss version)"),
    "2ea": ("Futotama", "Enigma", "(Boss version)"),
    "2eb": ("Arahabaki", "Kunitsu", "(Boss version)"),
    "2ec": ("Mara", "Tyrant", "(Boss version)"),
    "2ed": ("Hagen", "Famed", "(Boss version)"),
    "2ee": ("Ongyo-Ki", "Brute", "(Boss version)"),
    "2ef": ("Izanami", "Megami", "(Boss version)"),
    "2f0": ("Maruo", "Human", "(Enemy-only)"),
    "2f1": ("Zhen", "Raptor", "(Boss version)"),
    "2f2": ("Tamagami", "Ghost", "(Enemy-only)"),
    "2f3": ("Okuninushi", "Kunitsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f4": ("Kanseiteikun", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f5": ("Manticore", "Wilder", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f6": ("Abaddon", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f7": ("Demonee-ho", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f8": ("Taowu", "Wilder", "(?)  (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f9": ("Prisoner Yokota", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fa": ("Fusou Fujio", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fb": ("Hiro Jingu", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fc": ("G.H. Hills", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fd": ("Take-Mikazuchi", "Amatsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2fe": ("Dionysus", "Zealot", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2ff": ("Silky", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "300": ("Lorelei", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "301": ("Persephone", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "302": ("Tiamat", "Drake", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "303": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "304": ("Anzu", "Raptor", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "305": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "306": ("Cernunnos", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "307": ("Grendel", "Jaki", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "308": ("Dormarth", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "309": ("Marishiten", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30a": ("Throne", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30b": ("Dominion", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30c": ("Power", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30d": ("Kazfiel", "Herald", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30e": ("Hunter Man", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "30f": ("Hunter Woman", "Human", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "310": ("Thor", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "311": ("Morax", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "312": ("Chimera", "Avatar", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "313": ("Tokisada", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "314": ("Gaston", "Human", "(Plain spear) (Partner)"),
    "315": ("Gaston", "Human", "(Gungnir) (Partner)"),
    "316": ("Toki", "Human", "(Unmasked) (Partner)"),
    "317": ("Isabeau", "Human", "(Partner)"),
    "318": ("Asahi", "Human", "(Partner)"),
    "319": ("Navarre", "Ghost", "(Partner)"),
    "31a": ("Nozomi", "Human", "(Partner)"),
    "31b": ("Gaston", "Human", "(Spear of Michael) (Partner)"),
    "31c": ("Hallelujah", "Human", "(Partner)"),
    "31d": ("Hallelujah", "Hybrid", "(Partner)"),
    "31e": ("Toki", "Human", "(Masked) (Partner)"),
    "31f": ("Flynn", "Samurai", "(Aniel fight ally)"),
    "320": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "321": ("Katakirauwa", "Food", "(Tutorial version)"),
    "322": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "323": ("Angel", "Divine", "(Boss version)"),
    "324": ("Aniel", "Herald", "(Boss version)"),
    "325": ("King Frost", "Tyrant", "(Boss version)"),
    "326": ("Sukuna-Hikona", "Kunitsu", "(Boss version)"),
    "327": ("Shesha", "Snake", "(Encounter 1)"),
    "328": ("Minotaur", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "329": ("Medusa", "Femme", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "32a": ("Titan", "Jirae", "(Boss version)"),
    "32b": ("Medusa", "Femme", "(Boss version)"),
    "32c": ("Shesha", "Snake", "(Encounter 2)"),
    "32d": ("Gaea Woman", "Human", "(Boss version)"),
    "32e": ("Zhong Kui", "Kishin", "(Boss version)"),
    "32f": ("Toki", "Human", "(Masked, boss version)"),
    "330": ("Odin", "Deity", "(Boss version, encounter 1)"),
    "331": ("Not Used", "Horde", ""),
    "332": ("Gaea Man", "Human", "(Boss version)"),
    "333": ("Quetzalcoatl", "Dragon", "(Boss version)"),
    "334": ("Jikokuten", "Kishin", "(Boss version)"),
    "335": ("Koumokuten", "Kishin", "(Boss version)"),
    "336": ("Zouchouten", "Kishin", "(Boss version)"),
    "337": ("Bishamonten", "Kishin", "(Boss version)"),
    "338": ("Marishiten", "Kishin", "(Boss version)"),
    "339": ("Inanna Remnant", "Lady", "(Enemy-only)"),
    "33a": ("Maitreya", "Deity", "(Boss version)"),
    "33b": ("Shesha", "Snake", "(Encounter 3)"),
    "33c": ("Krishna", "Deity", "(Boss version)"),
    "33d": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33e": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33f": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "340": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "341": ("Gaea Man", "Human", "(Boss version)"),
    "342": ("Gaea Woman", "Human", "(Boss version)"),
    "343": ("Adramelech", "Fallen", "(Boss version)"),
    "344": ("Angel Army", "Horde", "(Boss version)"),
    "345": ("Azrael", "Herald", "(Boss version)"),
    "346": ("Belial", "Tyrant", "(Boss version)"),
    "347": ("Lucifuge", "Tyrant", "(Boss version)"),
    "348": ("Samyaza", "Tyrant", "(Boss version)"),
    "349": ("Lucifer", "Tyrant", "(Boss version)"),
    "34a": ("Merkabah", "Herald", "(Boss version)"),
    "34b": ("Not Used", "Drake", "(?) (Repel: Phys, Resist: Gun, Weak: Ice/Elec)"),
    "34c": ("Not Used", "Vile", "(?) (Null: Ice/Dark, Resist: Light, Weak: Fire)"),
    "34d": ("Not Used", "Horde", "(?) (Resist: Dark, Weak: Fire/Force/Light) (Attack: Phys x3~4, 1 enemy)"),
    "34e": ("Odin", "Deity", "(Boss version, encounter 2)"),
    "34f": ("Baal", "Deity", "(Boss version)"),
    "350": ("Apsu", "Deity", "(Boss version)"),
    "351": ("Seth", "Vile", "(Boss version)"),
    "352": ("Inanna", "Lady", "(Boss version)"),
    "353": ("Mitra-Buddha", "Fury", "(Boss version)"),
    "354": ("Dagda", "Deity", "(Enemy-only)"),
    "355": ("Vishnu-Flynn", "Deity", "(1st form) (Enemy-only)"),
    "356": ("Metatron", "Herald", "(Boss version)"),
    "357": ("Metatron Army", "Horde", "(Boss version)"),
    "358": ("Not Used", "Human", "(?) (Null: Light/Dark)"),
    "359": ("Not Used", "Megami", "(?) (Repel: Gun, Null: Dark, Resist: Phys/Light)"),
    "35a": ("Satan", "Primal", "(Boss version)"),
    "35b": ("YHVH", "Godly", "(1st form) (Enemy-only)"),
    "35c": ("YHVH", "Godly", "(2nd form) (Enemy-only)"),
    "35d": ("Vishnu-Flynn", "Deity", "(2nd form) (Enemy-only)"),
    "35e": ("Angel Army", "Horde", "(Boss version)"),
    "35f": ("Rukh", "Flight", "(Boss version)"),
    "360": ("Navarre", "Ghost", "(Boss version)"),
    "361": ("Nozomi", "Human", "(Boss version)"),
    "362": ("Hallelujah", "Hybrid", "(Boss version)"),
    "363": ("Gaston", "Human", "(Boss version)"),
    "364": ("Toki", "Human", "(Unmasked, boss version)"),
    "365": ("Isabeau", "Human", "(Boss version)"),
    "366": ("Human Army", "Horde", "(Wave 1) (Enemy-only)"),
    "367": ("Human Army", "Horde", "(Wave 2) (Enemy-only)"),
    "368": ("Human Army", "Horde", "(Wave 3) (Enemy-only)"),
    "369": ("Human Army", "Horde", "(Wave 4) (Enemy-only)"),
    "36a": ("Human Army", "Horde", "(Wave 5) (Enemy-only)"),
    "36b": ("A. Lucifer", "Tyrant", ""),
    "36c": ("A. Beelzebub", "Tyrant", ""),
    "36d": ("A. Lucifuge", "Tyrant", ""),
    "36e": ("A. Merkabah", "Herald", ""),
    "36f": ("A. Aniel", "Herald", ""),
    "370": ("A. Azrael", "Herald", ""),
    "371": ("Pachacamac", "Vile", "(Boss version)"),
    "372": ("Mushussu", "Drake", "(Boss version)"),
    "373": ("Gemori", "Fallen", "(Boss version)"),
    "374": ("Murmur", "Fallen", "(Boss version)"),
    "375": ("Master Therion", "Yoma", "(Boss version)"),
    "376": ("Dominion", "Divine", "(Boss version)"),
    "377": ("Throne", "Divine", "(Boss version)"),
    "378": ("Abaddon", "Tyrant", "(Boss version)"),
    "379": ("Barbatos", "Fallen", "(Boss version)"),
    "37a": ("Fafnir", "Drake", "(Boss version)"),
    "37b": ("Pales", "Vile", "(Boss version)"),
    "37c": ("Michizane", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37d": ("Yamato Takeru", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37e": ("Merkabah", "Tyrant", "(?) (Tyrant? No idea what this was supposed to be.)"),
    "37f": ("Belial", "Tyrant", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "380": ("Karasu Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "381": ("Koppa Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "382": ("Ose", "Fallen", "(?) (Boss version, appropriate resist/attack)"),
    "383": ("Kaiwan", "Night", "(?) (Boss version, appropriate resist/attack)"),
    "384": ("A. Nebiros", "Fallen", ""),
    "385": ("A. Adramelech", "Fallen", ""),
    "386": ("A. Barbatos", "Fallen", ""),
    "387": ("A. Murmur", "Fallen", ""),
    "388": ("A. Dantalian", "Fallen", ""),
    "389": ("A. Belial", "Tyrant", ""),
    "38a": ("A. Alciel", "Vile", ""),
    "38b": ("A. Cherub", "Divine", ""),
    "38c": ("A. Throne", "Divine", ""),
    "38d": ("A. Dominion", "Divine", ""),
    "38e": ("A. Virtue", "Divine", ""),
    "38f": ("A. Power", "Divine", ""),
    "390": ("A. Angel", "Divine", ""),
    "391": ("Chimera", "Avatar", "(Twisted Tokyo version)"),
    "392": ("Legion", "Spirit", "(Twisted Tokyo version)"),
    "393": ("Inferno", "Spirit", "(Twisted Tokyo version)"),
    "394": ("Hitokotonuchi", "Kunitsu", "(Twisted Tokyo version)"),
    "395": ("Corpse", "Undead", "(Twisted Tokyo version)"),
    "396": ("Slime", "Foul", "(Twisted Tokyo version)"),
    "397": ("Attis", "Zealot", "(Twisted Tokyo version)"),
    "398": ("Kaiming Shou", "Avatar", "(Twisted Tokyo version)"),
    "399": ("Itsumade", "Raptor", "(Twisted Tokyo version)"),
    "39a": ("Vetala", "Ghost", "(Twisted Tokyo version)"),
    "39b": ("Chernobog", "Fury", "(Twisted Tokyo version)"),
    "39c": ("Yatagarasu", "Avian", "(Twisted Tokyo version)"),
    "39d": ("Orthrus", "Beast", "(Twisted Tokyo version)"),
    "39e": ("Black Maria", "Lady", "(Twisted Tokyo version)"),
    "39f": ("Tlazolteotl", "Megami", "(Twisted Tokyo version)"),
    "3a0": ("Kanbari", "Enigma", "(Twisted Tokyo version)"),
    "3a1": ("Peallaidh", "Wilder", "(Twisted Tokyo version)"),
    "3a2": ("Ogun", "Zealot", "(Twisted Tokyo version)"),
    "3a3": ("Ometeotl", "Deity", "(Twisted Tokyo version)"),
    "3a4": ("Ukano Mitama", "Avatar", "(Twisted Tokyo version)"),
    "3a5": ("Centaur", "Yoma", "(Twisted Tokyo version)"),
    "3a6": ("Yggdrasil", "Tree", "(Twisted Tokyo version)"),
    "3a7": ("Skadi", "Lady", "(Twisted Tokyo version)"),
    "3a8": ("Taotie", "Vile", "(Twisted Tokyo version)"),
    "3a9": ("Kingu", "Drake", "(Twisted Tokyo version)"),
    "3aa": ("Azazel", "Tyrant", "(Twisted Tokyo version)"),
    "3ab": ("Hachiman", "Deity", "(Twisted Tokyo version)"),
    "3ac": ("Kartikeya", "Fury", "(Twisted Tokyo version)"),
    "3ad": ("Tezcatilipoca", "Zealot", "(Twisted Tokyo version)"),
    "3ae": ("Girimehkala", "Jaki", "(Twisted Tokyo version)"),
    "3af": ("Nergal", "Reaper", "(Twisted Tokyo version)"),
    "3b0": ("Botis", "Fallen", "(Twisted Tokyo version)"),
    "3b1": ("Kangiten", "Enigma", "(Twisted Tokyo version)"),
    "3b2": ("Surt", "Tyrant", "(Twisted Tokyo version)"),
    "3b3": ("Python", "Drake", "(Twisted Tokyo version)"),
    "3b4": ("", "Mot", "(Twisted Tokyo version)"),
    "3b5": ("Vasuki", "Drake", "(Twisted Tokyo version)"),
    "3b6": ("Samael", "Fallen", "(Twisted Tokyo version)"),
    "3b7": ("Itsumade Horde", "Horde", "(Twisted Tokyo version)"),
    "3b8": ("Wildfire Horde", "Horde", "(Twisted Tokyo version)"),
    "3b9": ("Pirate Horde", "Horde", "(Twisted Tokyo version)"),
    "3ba": ("Yomi Army", "Horde", "(Twisted Tokyo version)"),
    "3bb": ("Frosts", "Horde", "(Twisted Tokyo version)"),
    "3bc": ("Defiant Horde", "Horde", "(Twisted Tokyo version)"),
    "3bd": ("Demon Horde", "Horde", "(Twisted Tokyo version)"),
    "3be": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3bf": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3c0": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3c1": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3c2": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3c3": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3c4": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3c5": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3c6": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3c7": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3c8": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3c9": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3ca": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3cb": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3cc": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3cd": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3ce": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3cf": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3d0": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3d1": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3d2": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3d3": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3d4": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3d5": ("Mother Harlot", "Fiend", "(Boss version)"),
    "3d6": ("Trumpeter", "Fiend", "(Boss version)"),
    "3d7": ("Pale Rider", "Fiend", "(Boss version)"),
    "3d8": ("Black Rider", "Fiend", "(Boss version)"),
    "3d9": ("Red Rider", "Fiend", "(Boss version)"),
    "3da": ("White Rider", "Fiend", "(Boss version)"),
    "3db": ("Not Used", "Fiend",
            "(?) (Entire portrait is solid white) (Null: Dark, Resist: Light) (Probably used to be Chemtrail)"),
    "3dc": ("Matador", "Fiend", "(Boss version)"),
    "3dd": ("David", "Fiend", "(Boss version)"),
    "3de": ("Not Used", "Tree", "(?)"),
    "3df": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e0": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e1": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e2": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e3": ("Adramelech", "Fallen", "(Shesha fight ally)"),
    "3e4": ("Archangel", "Divine", "(Shesha fight ally)"),
    "3e5": ("Principality", "Divine", "(Boss version)"),
    "3e6": ("Ose", "Fallen", "(Boss version)"),
    "3e7": ("Fortuna", "Megami", "(Boss version)"),
    "3e8": ("Not Used", "Tree", "(?)"),
    "3e9": ("Ippon-Datara", "Jaki", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ea": ("Horkos", "Tyrant", "(Godslayer Training version)"),
    "3eb": ("Dionysus", "Zealot", "(Godslayer Training version)"),
    "3ec": ("Anubis", "Avatar", "(Godslayer Training version)"),
    "3ed": ("Demonee-ho", "Fairy", "(Godslayer Training version)"),
    "3ee": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ef": ("Raiju", "Wilder", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f0": ("Toubyou", "Drake", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f1": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f2": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f3": ("Jack the Ripper", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f4": ("Demonee-ho", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f5": ("Demonstrators", "Horde", ""),
    "3f6": ("Lanling Wang", "Famed", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f7": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f8": ("Asahi", "Human", ""),
    "3f9": ("Navarre", "Ghost", ""),
    "3fa": ("Nozomi", "Human", ""),
    "3fb": ("Parvati", "Megami", "(Asahi's?)"),
    "3fc": ("Stonka", "Beast", ""),
    "3fd": ("Navarre", "Ghost", ""),
    "3fe": ("Mushussu", "Drake", ""),
    "3ff": ("Sarasvati", "Nymph", "(Asahi's?)"),
    "400": ("Navarre", "Ghost", ""),
    "401": ("Master Therion", "Yoma", "(Godslayer Training version)"),
    "402": ("Aramisaki", "Zealot", "(Godslayer Training version)"),
    "403": ("Ometeotl", "Deity", "(Godslayer Training version)"),
    "404": ("Huoniao", "Raptor", "(Godslayer Training version)"),
    "405": ("Long", "Dragon", "(Godslayer Training version)"),
    "406": ("Ym", "Drake", "(Godslayer Training version)"),
    "407": ("Gaston", "Samurai", ""),
    "408": ("", "Surt", "(Godslayer Training version)"),
    "409": ("Hachiman", "Deity", "(Godslayer Training version)"),
    "40a": ("Vasuki", "Drake", "(Godslayer Training version)"),
    "40b": ("Yaksha", "Brute", "(Godslayer Training version)"),
    "40c": ("Mara", "Tyrant", "(Godslayer Training version)"),
    "40d": ("Botis", "Fallen", "(Godslayer Training version)"),
    "40e": ("Oberon", "Fairy", "(Godslayer Training version)"),
    "40f": ("Cherub", "Divine", "(Godslayer Training version)"),
    "410": ("Zhong Kui", "Kishin", "(?) (Unused SMTIV Training Battle leftover)"),
    "411": ("Nata Taishi", "Genma", "(?) (Unused SMTIV Training Battle leftover)"),
    "412": ("Samyaza", "Tyrant", "(?) (Unused SMTIV Training Battle leftover)"),
    "413": ("Dakini", "Femme", "(?) (Unused SMTIV Training Battle leftover)"),
    "414": ("Nadja", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "415": ("Kushinada-hime", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "416": ("Principality", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "417": ("Power", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "418": ("Momunofu", "Brute", "(?) (Unused SMTIV Training Battle leftover)"),
    "419": ("Okuninushi", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "41a": ("Mad Gasser", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "41b": ("Krishna", "Tyrant", "(Test demon?)"),
    "41c": ("Odin", "King", ""),
    "41d": ("Maitreya", "Cyber", ""),
    "41e": ("Chironnupu", "Archaic", ""),
    "41f": ("Shesha 1st Form", "Archaic", ""),
    "420": ("Inanna Remnant", "Archaic", ""),
    "421": ("Shesha 2nd Form", "Archaic", ""),
    "422": ("Krishna", "Herald", "(Actually Gaston with Gungnir)"),
    "423": ("Merkabah", "Tree",
            "(Cutscene-related stuff below. Character sprites that appear briefly during battles have to be saved as demons, I guess.)"),
    "424": ("Lucifer", "Tree", ""),
    "425": ("Inanna", "Tree", ""),
    "426": ("Mitra-Buddha", "Tree", "(Portrait shows Inanna, but sprite shows Mitra-Buddha)"),
    "427": ("Dagda", "Tree", "(Portrait shows Mitra-Buddha, sprite shows Dagda)"),
    "428": ("Vishnu-Flynn 1", "Tree", "(Portrait is Dagda, sprite is Vishnu-Flynn)"),
    "429": ("YHVH 1", "Tree", "(Portrait is Vishnu-Flynn, sprite is...Frost Ace)"),
    "42a": ("YHVH 2", "Tree", ""),
    "42b": ("Vishnu-Flynn 2", "Tree", ""),
    "42c": ("Nanashi", "Tree", "(No art, not even a question mark)"),
    "42d": ("Binding Field", "Tree", "(Sprite is the purple field surrounding Flynn when he's crucified)"),
    "42e": ("Crucified Flynn", "Tree", ""),
    "42f": ("Danu", "Tree", ""),
    "430": ("St. Germain Hole", "Tree", ""),
    "431": ("Pillar of Light", "Tree", ""),
    "432": ("Lucifer", "Tree",
            "(2nd Form Normal) (Sprite is Asahi as your Goddess. Seems like they replaced stuff from SMTIV without actually changing the names.)"),
    "433": ("Michael", "Tree", "(Giant) (Goddess Navarre)"),
    "434": ("Gabriel", "Tree", "(Giant) (Goddess Nozomi)"),
    "435": ("Raphael", "Tree", "(Giant) (Goddess Gaston)"),
    "436": ("Uriel", "Tree", "(Giant) (Goddess Hallelujah)"),
    "437": ("Masakado", "Tree", "(Giant) (Goddess Toki)"),
    "438": ("Charon", "Tree", "(Event) (Goddess Isabeau)"),
    "439": ("Asterius", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43a": ("Aeshma", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43b": ("Ancient of Days", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43c": ("Sanat", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43d": ("Lucifer Hikaru", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43e": ("Silhouette Lucif", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43f": ("Trial Cyber", "Tree", "(?)"),
    "440": ("Trial Cyber", "Tree", "(?)"),
    "441": ("Trial Cyber", "Tree", "(?)"),
    "442": ("Trial Cyber", "Tree", "(?)"),
    "443": ("Trial Cyber", "Tree", "(?)"),
    "444": ("Trial Cyber", "Tree", "(?)"),
    "445": ("Trial Cyber", "Tree", "(?)"),
    "446": ("Trial Cyber", "Tree", "(?)"),
    "447": ("Trial Cyber", "Tree", "(?)"),
    "448": ("Trial Cyber", "Tree", "(?)"),
    "449": ("Mii", "Tree", ""),
    "44a": ("Kei", "Tree", ""),
    "44b": ("Warp Hole", "Tree", ""),
    "44c": ("Trial Cyber", "Tree", "(?)"),
    "44d": ("Egyptian Horde", "Horde", "(Enemy-only)"),
    "44e": ("Demonic Samurai", "???", "(Enemy-only)"),
    "44f": ("Demonic Hope", "???", "(Enemy-only)"),
    "450": ("Demonic Hugo", "???", "(Enemy-only)"),
    "451": ("A. Law Horde", "Horde", "(Enemy-only)"),
    "452": ("A. Chaos Horde", "Horde", "(Enemy-only)"),
    "453": ("En no Ozuno", "Fiend", "(Enemy-only)"),
    "454": ("Cleopatra", "Megami", "(Boss version)"),
    "455": ("Mephisto", "Tyrant", "(Boss version)"),
    "456": ("Stephen", "Meta", "(Sitting) (Enemy-only)"),
    "457": ("Stephen", "Meta", "(Standing) (Enemy-only)"),
    "458": ("A. Neutral Horde", "Horde", "(Enemy-only)"),
    "459": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "45a": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "45b": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "45c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "45d": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "45e": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "45f": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "460": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "461": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "462": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "463": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "464": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "465": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "466": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "467": ("Formorian", "Night", "(Tir Na Nog version)"),
    "468": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "469": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "46a": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "46b": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "46c": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "46d": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "46e": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "46f": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "470": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "471": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "472": ("Formorian", "Night", "(Tir Na Nog version)"),
    "473": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "474": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "475": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "476": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "477": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "478": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "479": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "47a": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "47b": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "47c": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "47d": ("Trial Cyber", "Tree", "(?)"),
    "47e": (
        "Trial:Single:Sword", "Tree", "(These are all Mitamas with different attack animations for testing purposes)"),
    "47f": ("Trial:Single:Scimitar", "Tree", ""),
    "480": ("Trial:Single:Spear", "Tree", ""),
    "481": ("Trial:Single:Blunt", "Tree", ""),
    "482": ("Trial:Single:Fist", "Tree", ""),
    "483": ("Trial:Single:Scratch", "Tree", ""),
    "484": ("Trial:Single:Bite", "Tree", ""),
    "485": ("Trial:Single:Gun", "Tree", ""),
    "486": ("Trial:Single:Heavy", "Tree", ""),
    "487": ("Trial:Single:Rifle", "Tree", ""),
    "488": ("Trial:Single:Machinga", "Tree", ""),
    "489": ("Trial:Single:Sword", "Tree", ""),
    "48a": ("Trial:Single:Scimitar", "Tree", ""),
    "48b": ("Trial:Single:Spear", "Tree", ""),
    "48c": ("Trial:Single:Blunt", "Tree", ""),
    "48d": ("Trial:Single:Fist", "Tree", ""),
    "48e": ("Trial:Single:Scratch", "Tree", ""),
    "48f": ("Trial:Single:Bite", "Tree", ""),
    "490": ("Trial:Single:Gun", "Tree", ""),
    "491": ("Trial:Single:Heavy", "Tree", ""),
    "492": ("Trial:Single:Rifle", "Tree", ""),
    "493": ("Erthys", "Element", "(Diamond Realm version)"),
    "494": ("Aeros", "Element", "(Diamond Realm version)"),
    "495": ("Aquans", "Element", "(Diamond Realm version)"),
    "496": ("Flaemis", "Element", "(Diamond Realm version)"),
    "497": ("Demonic Citizens", "???", "(Enemy-only)"),
    "498": ("Demonic Citizens", "???", "(Enemy-only)"),
    "499": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49a": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49b": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49c": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49d": ("The Hero", "Human", ""),
    "49e": ("Aleph", "Replicant", ""),
    "49f": ("Demi-fiend", "Chaos", ""),
    "4a0": ("Flynn", "Human", "(Stephen Fight)"),
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
            if val in ALL_SKILLS:
                # tmp_str = val + " - " + ALL_SKILLS[val][0]
                # if len(tmp_str) > max_width:
                #     max_width = len(tmp_str)
                skillIDNameList.append(val + " - " + ALL_SKILLS[val][0])
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
        tab1ComboBox.grid(column=2, row= 0, padx=10, pady=10)

        def changeCharacter(*args):
            name = tab1ComboBox.get()

            def get_key(val):
                for char_info in self.charList:
                    for key, value in char_info.items():
                        if val == value:
                            return char_info

            self.curChar = get_key(name)
            print(self.curChar)
            tab1txtbLVL.delete(0,5)
            tab1txtbLVL.insert(0, self.curChar["level"])
            tab1txtbEXP.delete(0,5)
            tab1txtbEXP.insert(0, self.curChar["exp"])
            tab1txtbHP.delete(0,5)
            tab1txtbHP.insert(0, self.curChar["hp"])
            tab1txtbMP.delete(0,5)
            tab1txtbMP.insert(0, self.curChar["mp"])
            tab1txtbST.delete(0,5)
            tab1txtbST.insert(0, self.curChar["st"])
            tab1txtbMA.delete(0,5)
            tab1txtbMA.insert(0, self.curChar["ma"])
            tab1txtbVI.delete(0,5)
            tab1txtbVI.insert(0, self.curChar["vi"])
            tab1txtbAG.delete(0,5)
            tab1txtbAG.insert(0, self.curChar["ag"])
            tab1txtbCMD1.delete(0,5)
            tab1txtbCMD1.insert(0, self.curChar["cmd1"])
            tab1txtbCMD2.delete(0,5)
            tab1txtbCMD2.insert(0, self.curChar["cmd2"])
            tab1txtbCMD3.delete(0,5)
            tab1txtbCMD3.insert(0, self.curChar["cmd3"])
            tab1txtbPAS1.delete(0,5)
            tab1txtbPAS1.insert(0, self.curChar["pas1"])
            tab1txtbPAS2.delete(0,5)
            tab1txtbPAS2.insert(0, self.curChar["pas2"])
            tab1txtbPAS3.delete(0,5)
            tab1txtbPAS3.insert(0, self.curChar["pas3"])
            tab1txtbRAC.delete(0,5)
            tab1txtbRAC.insert(0, self.curChar["rac"])
            tab1txtbMOV.delete(0,5)
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
        tab1emptylabel.grid(column=0, row= 9)

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
        for i in range(1, len(CMD_IDS)):
            tab1ListBoxCMD.insert(i, " " + str(CMD_IDS[i]) + " - " + str(ALL_SKILLS[CMD_IDS[i]][0]))
        tab1ListBoxCMD.grid(column=0, row=1)

        tab1ListBoxPAS = tk.Listbox(tab1SkillFrame)
        for i in range(1, len(PAS_IDS)):
            tab1ListBoxPAS.insert(i, " " + str(PAS_IDS[i]) + " - " + str(ALL_SKILLS[PAS_IDS[i]][0]))
        tab1ListBoxPAS.grid(column=1, row=1)

        tab1ListBoxAUT = tk.Listbox(tab1SkillFrame)
        for i in range(1, len(AUTO_IDS)):
            tab1ListBoxAUT.insert(i, " " + str(AUTO_IDS[i]) + " - " + str(ALL_SKILLS[AUTO_IDS[i]][0]))
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
        tab2txtbMOV = tk.Entry(tab2TopLFrame)
        tab2txtbMOV.grid(column=3, row=8)

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

        # Listboxes
        tab2ListBoxCMD = tk.Listbox(tab2SkillFrame)
        for i in range(1, len(CMD_IDS)):
            tab2ListBoxCMD.insert(i, " " + str(CMD_IDS[i]) + " - " + str(ALL_SKILLS[CMD_IDS[i]][0]))
        tab2ListBoxCMD.grid(column=0, row=1)

        tab2ListBoxPAS = tk.Listbox(tab2SkillFrame)
        for i in range(1, len(PAS_IDS)):
            tab2ListBoxPAS.insert(i, " " + str(PAS_IDS[i]) + " - " + str(ALL_SKILLS[PAS_IDS[i]][0]))
        tab2ListBoxPAS.grid(column=1, row=1)

        tab2ListBoxRAC = tk.Listbox(tab2SkillFrame)
        for i in range(1, len(RAC_IDS)):
            tab2ListBoxRAC.insert(i, " " + str(RAC_IDS[i]) + " - " + str(ALL_SKILLS[RAC_IDS[i]][0]))
        tab2ListBoxRAC.grid(column=2, row=1)

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
                    demon_info = ALL_DEMONS[demon_id]

                    d_info = {
                        "start_add": d_start_add,
                        "id": int(self.getHexStr(self.save_bytes, d_id_add, DE_ID[1], add_is_dec=True), 16),
                        "level": int(self.getHexStr(self.save_bytes, d_lvl_add, DE_LVL[1], add_is_dec=True), 16),
                        "exp": int(self.getHexStr(self.save_bytes, d_exp_add, DE_EXP[1], add_is_dec=True), 16),
                        "hp": int(self.getHexStr(self.save_bytes, d_hp_add, DE_HP[1], add_is_dec=True), 16),
                        "mp": int(self.getHexStr(self.save_bytes, d_mp_add, DE_MP[1], add_is_dec=True),16),
                        "st": int(self.getHexStr(self.save_bytes, d_st_add, DE_ST[1], add_is_dec=True),16),
                        "ma": int(self.getHexStr(self.save_bytes, d_ma_add, DE_MA[1], add_is_dec=True),16),
                        "vi": int(self.getHexStr(self.save_bytes, d_vi_add, DE_VI[1], add_is_dec=True),16),
                        "ag": int(self.getHexStr(self.save_bytes, d_ag_add, DE_AG[1], add_is_dec=True),16),
                        "cmd1": int(self.getHexStr(self.save_bytes, d_cmd1_add, DE_CMD1[1], add_is_dec=True),16),
                        "cmd2": int(self.getHexStr(self.save_bytes, d_cmd2_add, DE_CMD2[1], add_is_dec=True),16),
                        "cmd3": int(self.getHexStr(self.save_bytes, d_cmd3_add, DE_CMD3[1], add_is_dec=True),16),
                        "pas1": int(self.getHexStr(self.save_bytes, d_pas1_add, DE_PAS1[1], add_is_dec=True),16),
                        "pas2": int(self.getHexStr(self.save_bytes, d_pas2_add, DE_PAS2[1], add_is_dec=True),16),
                        "pas3": int(self.getHexStr(self.save_bytes, d_pas3_add, DE_PAS3[1], add_is_dec=True),16),
                        "rac": int(self.getHexStr(self.save_bytes, d_rac_add, DE_RAC[1], add_is_dec=True),16),
                    }
                    self.demonList.append(d_info)
                    self.demonNameList.append(demon_info)
                    print("Start Address: %x, Demon ID: %s." % (d_start_add, demon_id))

    def applyDemonChange(self):
        return

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

    def saveChanges(self):
        if self.saveFilePath and os.path.isdir(self.saveFileDir):
            self.applyMCChanges()
            self.applyMiscChanges()
            self.applyDeChanges()
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
