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
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
    "14": "",
    "15": "",
    "16": "",
    "17": "",
    "18": "Omega Kartikeya",
    "19": "",
    "20": "",
    "21": "",
    "22": "",
    "23": "",
    "24": "",
    "25": "",
    "26": "",
    "27": "",
    "28": "",
    "29": "",
    "30": "",
    "31": "",
    "32": "",
    "33": "",
    "34": "",
    "35": "",
    "36": "",
    "37": "",
    "38": "",
    "39": "",
    "40": "",
    "41": "",
    "42": "",
    "43": "",
    "44": "",
    "45": "",
    "46": "",
    "47": "",
    "48": "",
    "49": "",
    "50": "",
    "51": "",
    "52": "",
    "53": "",
    "54": "",
    "55": "",
    "56": "",
    "57": "",
    "58": "",
    "59": "",
    "5b": "",
    "60": "",
    "61": "",
    "62": "",
    "63": "",
    "64": "",
    "65": "",
    "66": "",
    "67": "",
    "68": "",
    "69": "",
    "70": "",
    "71": "",
    "72": "",
    "73": "",
    "74": "",
    "75": "Avian Anzu",
    "76": "",
    "77": "",
    "78": "",
    "79": "",
    "80": "",
    "81": "",
    "82": "",
    "83": "",
    "84": "",
    "85": "",
    "86": "",
    "87": "",
    "88": "",
    "89": "",
    "90": "",
    "91": "Avatar Baihu",
    "92": "",
    "93": "",
    "94": "",
    "95": "",
    "96": "",
    "97": "",
    "98": "",
    "99": "",
    "100": "",
    "101": "",
    "102": "",
    "103": "",
    "104": "",
    "105": "",
    "106": "",
    "107": "",
    "108": "",
    "109": "",
    "110": "",
    "111": "",
    "112": "",
    "113": "",
    "114": "",
    "115": "",
    "116": "",
    "117": "",
    "118": "",
    "119": "",
    "120": "",
    "121": "",
    "122": "",
    "123": "",
    "124": "",
    "125": "",
    "126": "",
    "127": "",
    "128": "",
    "129": "Fairy Vivian",
    "130": "",
    "131": "",
    "132": "",
    "133": "",
    "134": "Tyrant Hecate",
    "154": "",
    "184": "Ghost Kudlak",
    "196": "",
    "199": "",
    "214": "Wilder Sleipnir",
    "215": "",
    "255": ""
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
