import discord
from discord.ext import commands
import os
import random

# Globals
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
extensions = ['cogs.admin', 'cogs.powers']


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="For info use !help"))
    print('Assuming direct control.')


def extendma(bot):
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{0} cannot be loaded. [{1}]'.format(extension, error))


if __name__ == '__main__':
    # load cogs
    extendma(bot)

    # run bot
    bot.run(os.environ['TOKEN'])
