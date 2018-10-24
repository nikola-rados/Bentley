import discord
from discord.ext import commands
import random
import os

# Local Imports
from cogs.utils import constants


class Powers:
    def __init__(self, bot):
        self.bot = bot

    def earned_power(self, drop_rate):
    	return random.randint(1, 100) <= drop_rate

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
            # assign rate based on action
            if message.channel == discord.utils.get(self.bot.get_all_channels(), guild__name='Desire Index', name='voting'):
                drop_rate = constants.POWER_DROP_RATE_M
            else:
                drop_rate = constants.POWER_DROP_RATE_D

            # check for power earning
            if self.earned_power(drop_rate):
                ch = self.bot.get_channel(int(os.environ['DISCUSSION']))
                mod = '<@{}>'.format(os.environ['NOL'])
                await ch.send('Congradulations {0.mention}, '
                              'you\'ve earned **{1}**!\n{2}, please '
                              'add that to the list'.format(message.author,
                                                            self.roll_box(),
                                                            mod))

def setup(bot):
    bot.add_cog(Powers(bot))
