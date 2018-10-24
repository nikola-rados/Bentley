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

    def scrambled(self, orig):
        dest = orig[:]
        random.shuffle(dest)
        return dest

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

    @commands.command(pass_context=True)
    async def powerhelp(self, ctx):
        embed=discord.Embed(
            title=' ',
            color=0x1ece6d
        )

        embed.set_author(name="Power Help Page")
        embed.add_field(name="!clusterbomb \"game1\" \"game2\" \"game3\"",
                        value="This will produce the result of the \"_Cluster "
                              "Bomb_\" power.  Along with the command, give "
                              "Bentley the 3 games you wish to effect.",
                        inline=True)
        embed.add_field(name="!everybodyshutup \"game\" current new",
                        value="This will produce the result of the "
                              "\"_Everybody Shut Up_\" power.  The _game_ is "
                              "the game you wish to move.  _current_ is its "
                              "position on the index and _new_ is where you "
                              "are moving it to.",
                        inline=True)
        embed.add_field(name="!lockdown \"game1\" \"game1\"",
                        value="This will produce the result of the "
                              "\"_Lockdown_\" power.  Give Bentley the two "
                              "games you wish to effect.",
                        inline=True)
        embed.add_field(name="!mindcontrol @member",
                        value="This will produce the result of the "
                              "\"_Mind Control_\" power.  Mention the user "
                              "you wish to effect.",
                        inline=True)
        await ctx.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def clusterbomb(self, ctx, g1, g2, g3):
        # get result
        ordered_list = [g1, g2, g3]
        scrambled_list = self.scrambled([g1, g2, g3])
        result_list = []
        for o, s in zip(ordered_list, scrambled_list):
            if o == s:
                result_list.append((o, None))
            else:
                result_list.append((o, s))

        # message
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Cluster Bomb")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Games',
                        value='**{0}**\n'
                              '**{1}**\n'
                              '**{2}**\n'.format(g1, g2, g3),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** swap with **{1}**\n'
                              '**{2}** swap with **{3}**\n'
                              '**{4}** swap with **{5}**'
                              .format(result_list[0][0],
                                      result_list[0][1],
                                      result_list[1][0],
                                      result_list[1][1],
                                      result_list[2][0],
                                      result_list[2][1]),
                        inline=False)
        embed.add_field(name='Locking', value='True Lock', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        await ctx.message.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def everybodyshutup(self, ctx, game, rank_curr, rank_new):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Everybody Shut Up")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Game', value='**{0}**'.format(game), inline=False)
        embed.add_field(name='Result',
                        value='Rank {0} --> Rank {1}'.format(rank_curr, rank_new),
                        inline=False)
        embed.add_field(name='Locking', value='True Lock', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        await ctx.message.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def lockdown(self, ctx, g1, g2):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Lockdown")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Games', value='**{0}**\n**{1}**'.format(g1, g2),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected games have been locked',
                        inline=False)
        embed.add_field(name='Locking', value='True Lock', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        await ctx.message.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def mindcontrol(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Mind Control")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Member Effected', value='{0.mention}'.format(ctx.message.mentions[0]),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected member must use one of their powers',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        await ctx.message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Powers(bot))
