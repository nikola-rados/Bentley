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
        await ctx.channel.send('{0.mention} you will now get notifications '
                               'for votes'.format(member))

    # help
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed=discord.Embed(
            title="\n",
            color=0x1ece6d
        )

        embed.set_author(name="Help Page")
        embed.add_field(name="!help",
                        value="What you are seeing now",
                        inline=True)
        embed.add_field(name="!motion \"name\" current new \"explanation\" ",
                        value="This will produce a motion in the voting "
                              "channel where the _\"name\"_ is the name of "
                              "the game you wish to motion, _current_ is its "
                              "rank on the index and _new_ is where you wish "
                              "to move it.  To place a motion you must put "
                              "forward the reason for the change as the "
                              "_explanation_.",
                        inline=True)
        embed.add_field(name="!notify",
                        value="You will be given the Council role which will "
                              "notify you of any new votes",
                        inline=True)
        embed.add_field(name="!placement code_number rank",
                        value="This places your vote for the weekly games "
                              "entry rank.  The code number is the number of "
                              "the weekly game (1 or 2).  The rank is where "
                              "you think it should go.",
                        inline=True)
        embed.add_field(name="!powerhelp",
                        value="This help page will display all the powers that"
                              " Bentley can handle",
                        inline=True)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
