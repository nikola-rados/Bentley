import discord
from discord.ext import commands
import random

# Local Imports
from cogs.utils import constants


class Powers:
    def __init__(self, bot):
        self.bot = bot

    def earned_power(self):
    	return random.random() < constants.POWER_DROP_RATE

    def random_list_item(self, list):
        return list[random.randint(0, len(list)-1)]

    def roll_box(self):
    	roll = random.randint(1, 100)

    	if roll <= constants.LEGENDARY_DROP_RATE:
    		return self.random_list_item(constants.LEGENDARY)
    	elif roll <= constants.EPIC_DROP_RATE:
    		return self.random_list_item(constants.EPIC)
    	elif roll <= constants.RARE_DROP_RATE:
    		return self.random_list_item(constants.RARE)
    	elif roll <= constants.COMMON_DROP_RATE:
    		return self.random_list_item(constants.COMMON)

    # power distribution
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            if self.earned_power():
                ch = self.bot.get_channel(501943623634518046)
                await ch.send('Congradulations {0.mention}, you\'ve earned **{1}**!'.format(message.author, self.roll_box()))

def setup(bot):
    bot.add_cog(Powers(bot))
