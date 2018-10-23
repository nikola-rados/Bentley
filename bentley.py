import discord
from discord.ext import commands
import os
import random

from cogs.powers import earned_power, roll_box
from cogs.utils import constants


if __name__ == '__main__':
    # instantiate bot
    bot = commands.Bot(command_prefix="!")

    ## EVENTS ##
    # power distribution
    @bot.event
    async def on_message(message):
    	# we do not want the bot to reply to itself
        if message.author == bot.user:
            return

        else:
            if earned_power():
                await message.channel.send('Congratulations {0.mention}, you\'ve earned **{1}**!'.format(message.author, roll_box()))

        # check for any commands
        await bot.process_commands(message)

    # reply to @Bentley mentions
    @bot.listen()
    async def on_message(message):
        for member in message.mentions:
            if member.id == constants.BENTLEY_ID:
                await message.channel.send('{0.mention}{1}'.format(message.author, random.choice(constants.REPLIES)))

    ## COMMANDS ##
    # assign coucil role
    @bot.command(pass_context=True)
    async def notify(ctx):
        member = ctx.message.author
        role = discord.utils.get(member.guild.role_hierarchy, name='Council')
        await member.add_roles(role)
        await ctx.channel.send('{0.mention} you will now get notifications for votes'.format(member))

	# run
    bot.run(os.environ['TOKEN'])
