import discord
from discord.ext import commands

import random


def earned_power():
	return random.random() < 10#.015

def random_list_item(list):
    return list[random.randint(0, len(list)-1)]

def roll_box():
	legendary_rate = 4
	legendary_list = ["Bass Ackwards",
                      "Everybody Shut Up",
                      "National Debate",
                      "No U",
                      "Overdrive",
                      "Pecking Order",
                      "Pickpocket"]

	epic_rate = 14
	epic_list = ["Age Before Beauty",
                 "DEFCON 4",
                 "Double Jeopardy",
                 "Jack in the Box",
                 "Predator Missle",
                 "Prime Minister",
                 "Suspension",
                 "Tactical Nuke",
                 "The Upsidedown"]

	rare_rate = 44
	rare_list = ["Cluster Bomb",
                 "Hostile Takeover",
                 "Premier",
                 "RPG Enthusiast",
                 "Monkey Switch",
                 "The Senate"]

	uncommon_rate = 69
	uncommon_list = ["Ball & Chain",
                     "Package Deal",
                     "Saboteur",
                     "Single Player is Dead",
                     "Mayor",
                     "3UP",
                     "3DOWN"]

	common_rate = 99
	common_list = ["Bonus Round",
                   "Over-hyped",
                   "Quickfire",
                   "1UP",
                   "1DOWN"]

	roll = random.randint(1, 100)

	if roll <= legendary_rate:
		return random_list_item(legendary_list)
	elif roll <= epic_rate:
		return random_list_item(epic_list)
	elif roll <= rare_rate:
		return random_list_item(rare_list)
	elif roll <= uncommon_rate:
		return random_list_item(uncommon_list)
	elif roll <= common_rate:
		return random_list_item(common_list)
