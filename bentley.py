# Work with Python 3.6
import discord
import random


# Globals
token = process.env.token
drop_rate = 1
client = discord.Client()


def earned_power():
	return (random.random() * 100) > drop_rate


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


@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	else:
		if earned_power():
			await message.channel.send('Congradulations {0.mention}, you\'ve earned **{1}**!'.format(message.author, roll_box()))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
