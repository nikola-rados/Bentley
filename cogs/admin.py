import discord
from discord.ext import commands
import random

# Local Imports
from cogs.utils import constants


class Admin:
    def __init__(self, bot):
        self.bot = bot

    # reply to @Bentley mentions
    async def on_message(self, message):
        for member in message.mentions:
            if member.id == constants.BENTLEY_ID:
                await message.channel.send('{0.mention}{1}'.format(message.author, random.choice(constants.REPLIES)))

    # assign coucil role
    @commands.command(pass_context=True)
    async def notify(self, ctx):
        member = ctx.message.author
        role = discord.utils.get(member.guild.role_hierarchy, name='Council')
        await member.add_roles(role)
        await ctx.channel.send('{0.mention} you will now get notifications for votes'.format(member))

    # help
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed=discord.Embed(
            title="\n",
            color=0x1ece6d
        )

        embed.set_author(name="HELP")
        embed.add_field(name="!help",
                        value="What you are seeing now",
                        inline=True)
        embed.add_field(name="!notify",
                        value="You will be given the Council role which will notify you of any new votes",
                        inline=True)

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
