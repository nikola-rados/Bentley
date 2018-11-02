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
        embed.add_field(name="!buyingvotes \"power\"",
                        value="Give Bentley the _power_ "
                              "you wish to exchange.",
                        inline=True)
        embed.add_field(name="!carepackage",
                        value='',
                        inline=True)
        embed.add_field(name="!clusterbomb \"game1\" \"game2\" \"game3\"",
                        value="Along with the command, give "
                              "Bentley the 3 games you wish to effect.",
                        inline=True)
        embed.add_field(name="!emp",
                        value='',
                        inline=True)
        embed.add_field(name="!equality @member \"your power\" \"their power\"",
                        value="Choose the _member_ you "
                              "wish to effect as well as the _powers_ you wish "
                              " to effect.",
                        inline=True)
        embed.add_field(name="!evolve @member \"their power\"",
                        value="Give Bentley the _member_ "
                              "you wish to effect and the _power_ you wish to effect.",
                        inline=True)
        embed.add_field(name="!everybodyshutup \"game\" current new",
                        value="The _game_ is "
                              "the game you wish to move.  _current_ is its "
                              "position on the index and _new_ is where you "
                              "are moving it to.",
                        inline=True)
        embed.add_field(name="!frenemies",
                        value='',
                        inline=True)
        embed.add_field(name="!gracefuldice",
                        inline=True)
        embed.add_field(name="!key \"game\"",
                        value="Give Bentley the game "
                              "you wish to effect.",
                        inline=True)
        embed.add_field(name="!lock \"game\"",
                        value="Give Bentley the game "
                              "you wish to effect.",
                        inline=True)
        embed.add_field(name="!lockdown \"game1\" \"game2\"",
                        value="Give Bentley the two "
                              "games you wish to effect.",
                        inline=True)
        embed.add_field(name="!mayor",
                        value='',
                        inline=True)
        embed.add_field(name="!mindcontrol @member",
                        value="Mention the _user_ "
                              "you wish to effect.",
                        inline=True)
        embed.add_field(name="!overdrive",
                        value='',
                        inline=True)
        embed.add_field(name="!padlock \"game\"",
                        value="Give Bentley the game "
                              "you wish to effect.",
                        inline=True)
        embed.add_field(name="!paytowin \"power1\" \"power2\"",
                        value="Pass in the _powers_ you "
                              "wish to exchange.",
                        inline=True)
        embed.add_field(name="!picklock \"game\"",
                        value="Give Bentley the game "
                              "you wish to effect.",
                        inline=True)
        embed.add_field(name="!pickpocket @member \"power\"",
                        value="Mention the _user_ "
                              "you wish to effect and the _power_ you wish to "
                              "take.",
                        inline=True)
        embed.add_field(name="!primeminister",
                        value='',
                        inline=True)
        embed.add_field(name="!sacrificialpact @member",
                        value="Mention the member you wish"
                              "to effect.",
                        inline=True)
        embed.add_field(name="!silence @member",
                        value="Mention the member you wish"
                              "to effect.",
                        inline=True)
        embed.add_field(name="!skeletonkey \"game1\" \"game2\"",
                        value="Give Bentley the two "
                              "games you wish to effect.",
                        inline=True)
        embed.add_field(name="!skulldice",
                        value='',
                        inline=True)
        embed.add_field(name="!theupsidedown",
                        value="This power must be"
                              "used upon receiving it.",
                        inline=True)
        embed.add_field(name="!threedown \"game\"",
                        value="Pass in the game you wish "
                              "to effect.",
                        inline=True)
        embed.add_field(name="!threeup \"game\"",
                        value="Pass in the game you wish "
                              "to effect.",
                        inline=True)
        embed.add_field(name="!quickfire",
                        value='',
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
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

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
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

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
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

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
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def pickpocket(self, ctx, member, power):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Pickpocket")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Member Effected', value='{0.mention}'.format(ctx.message.mentions[0]),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** has been stolen'.format(power),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def skeletonkey(self, ctx, g1, g2):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Skeleton Key")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Games', value='**{0}**\n**{1}**'.format(g1, g2),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected games have been unlocked',
                        inline=False)
        embed.add_field(name='Key', value='True Key', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def carepackage(self, ctx):
        power = self.roll_box()
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Care Package")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='Power earned is **{0}**.\nYou must use it immediately.'.format(power),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def emp(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="EMP")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='No more powers for the remainder of the week.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def overdrive(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Overdrive")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='For the rest of the week your vote will count as double.\n'
                              'The following week you will not be able to vote.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def silence(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Silence")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Member Effected', value='{0.mention}'.format(ctx.message.mentions[0]),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected member cannot use powers for the rest of the week',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def padlock(self, ctx, g1):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Padlock")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Game', value='**{0}**'.format(g1),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected game has been locked',
                        inline=False)
        embed.add_field(name='Locking', value='Advanced Lock', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def picklock(self, ctx, g1):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Picklock")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Game', value='**{0}**'.format(g1),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected game has been unlocked',
                        inline=False)
        embed.add_field(name='Key', value='Advanced Key', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def primeminister(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Prime Minster")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='User may add 3 extra votes to a motion of their choosing.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def theupsidedown(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="The Upsidedown")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='Most recent motion is locked and the result is flipped.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def sacrificialpact(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Sacerificial Pact")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Member Effected', value='{0.mention}'.format(ctx.message.mentions[0]),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected member cannot vote for the remainder of the week.\n'
                              'User cannot vote the following week.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def lock(self, ctx, g1):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Lock")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Game', value='**{0}**'.format(g1),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected game has been locked',
                        inline=False)
        embed.add_field(name='Locking', value='Soft Lock', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def key(self, ctx, g1):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Key")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Game', value='**{0}**'.format(g1),
                        inline=False)
        embed.add_field(name='Result',
                        value='Effected game has been unlocked',
                        inline=False)
        embed.add_field(name='Key', value='Soft Key', inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def threedown(self, ctx, game, rank_curr):
        if int(rank_curr) <= 3:
            author = ctx.message.author
            await ctx.message.channel.send('{0.mention}, the game cannot be in the top 3'.format(author))
        else:
            rank_new = int(rank_curr) + 3

            embed=discord.Embed(title=' ',
                                colour=0x1ece6d)
            embed.set_author(name="3 Down")
            embed.add_field(name='Used By',
                            value='{0.mention}'.format(ctx.message.author),
                            inline=False)
            embed.add_field(name='Game', value='**{0}**'.format(game), inline=False)
            embed.add_field(name='Result',
                            value='Rank {0} --> Rank {1}'.format(rank_curr, rank_new),
                            inline=False)
            embed.add_field(name='Locking', value='Soft Lock', inline=False)
            embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
            voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
            await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def threeup(self, ctx, game, rank_curr):
        if int(rank_curr) <= 3:
            author = ctx.message.author
            await ctx.message.channel.send('{0.mention}, the game cannot be in the top 3'.format(author))
        else:
            rank_new = int(rank_curr) - 3
            if rank_new <= 3:
                rank_new = 4

            embed=discord.Embed(title=' ',
                                colour=0x1ece6d)
            embed.set_author(name="3 Up")
            embed.add_field(name='Used By',
                            value='{0.mention}'.format(ctx.message.author),
                            inline=False)
            embed.add_field(name='Game', value='**{0}**'.format(game), inline=False)
            embed.add_field(name='Result',
                            value='Rank {0} --> Rank {1}'.format(rank_curr, rank_new),
                            inline=False)
            embed.add_field(name='Locking', value='Soft Lock', inline=False)
            embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
            voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
            await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def frenemies(self, ctx):
        chosen_one = self.random_list_item(ctx.guild.members)

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Frenemies")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='Your partner is {0.mention}.'.format(chosen_one),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def equality(self, ctx, member, your_power, their_power):
        if your_power in constants.COMMON or their_power in constants.COMMON:
            await ctx.channel.send('{0.mention}, you cannot downgrade Common powers.'.format(ctx.message.author))
        else:
            your_new_power = ''
            their_new_power = ''

            if your_power in constants.LEGENDARY:
                your_new_power = self.random_list_item(constants.EPIC)
            elif your_power in constants.EPIC:
                your_new_power = self.random_list_item(constants.RARE)
            elif your_power in constants.RARE:
                your_new_power = self.random_list_item(constants.COMMON)

            if their_power in constants.LEGENDARY:
                their_new_power = self.random_list_item(constants.EPIC)
            elif their_power in constants.EPIC:
                their_new_power = self.random_list_item(constants.RARE)
            elif their_power in constants.RARE:
                their_new_power = self.random_list_item(constants.COMMON)

            if your_new_power == '' or their_new_power == '':
                await ctx.channel.send('{0.mention}, power does not exist.'.format(ctx.message.author))
                return

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Equality")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='{0.mention}: **{1}** --> **{2}**\n'
                              '{3.mention}: **{4}** --> **{5}**'
                              .format(ctx.message.author, your_power,
                                      your_new_power, ctx.message.mentions[0],
                                      their_power, their_new_power),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def evolve(self, ctx, member, their_power):
        if their_power in constants.LEGENDARY:
            await ctx.channel.send('{0.mention}, you cannot upgrade Legendary powers.'.format(ctx.message.author))
        else:
            their_new_power = ''

            if their_power in constants.EPIC:
                their_new_power = self.random_list_item(constants.LEGENDARY)
            elif their_power in constants.RARE:
                their_new_power = self.random_list_item(constants.EPIC)
            elif their_power in constants.COMMON:
                their_new_power = self.random_list_item(constants.RARE)

            if their_new_power == '':
                await ctx.channel.send('{0.mention}, power does not exist.'.format(ctx.message.author))
                return

            embed=discord.Embed(title=' ',
                                colour=0x1ece6d)
            embed.set_author(name="Evolve")
            embed.add_field(name='Used By',
                            value='{0.mention}'.format(ctx.message.author),
                            inline=False)
            embed.add_field(name='Member Effected', value='{0.mention}'.format(ctx.message.mentions[0]),
                            inline=False)
            embed.add_field(name='Result',
                            value='**{0}** --> **{1}**\n'
                                  .format(their_power,
                                          their_new_power),
                            inline=False)
            embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
            voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
            await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def mayor(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Mayor")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='User may add 1 extra vote to a motion of their choosing.',
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def quickfire(self, ctx):
        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Quick Fire")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='Most recent motion will recieve a {0}.'.format(constants.THUMBSUP),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def paytowin(self, ctx, power1, power2):
        if power1 in constants.LEGENDARY or power2 in constants.LEGENDARY:
            await ctx.message.channel.send('{0.mention}, you cannot ugrade Legendary powers.'.format(ctx.message.author))
        else:
            result = ''
            if power1 in constants.EPIC and power2 in constants.EPIC:
                result = self.random_list_item(constants.LEGENDARY)
            elif power1 in constants.RARE and power2 in constants.RARE:
                result = self.random_list_item(constants.EPIC)
            elif power1 in constants.COMMON and power2 in constants.COMMON:
                result = self.random_list_item(constants.RARE)
            else:
                await ctx.message.channel.send('{0.mention}, powers are not in the same tier.'.format(ctx.message.author))
                return

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Pay to Win")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** + **{1}** --> **{2}**.'.format(power1, power2, result),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def buyingvotes(self, ctx, power):
        num_votes = 0
        if power in constants.LEGENDARY:
            num_votes = 6
        elif power in constants.EPIC:
            num_votes = 4
        elif power in constants.RARE:
            num_votes = 2
        elif power in constants.COMMON:
            num_votes = 1
        else:
            ctx.message.channel.send('{0.mention}, power does not exist.'.format(ctx.message.author))
            return

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Buying Votes")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** --> **{1}** votes.'.format(power, num_votes),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def gracefuldice(self, ctx):
        votes = random.randint(0, 2)

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Graceful Dice")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** extra {1} for most recent motion.'.format(votes, constants.THUMBSUP),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def skulldice(self, ctx):
        votes = random.randint(0, 2)

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.set_author(name="Skull Dice")
        embed.add_field(name='Used By',
                        value='{0.mention}'.format(ctx.message.author),
                        inline=False)
        embed.add_field(name='Result',
                        value='**{0}** extra {1} for most recent motion.'.format(votes, constants.THUMBSDOWN),
                        inline=False)
        embed.add_field(name='Notify', value='<@{}>'.format(os.environ['NOL']), inline=False)
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))
        await voting_ch.send(embed=embed)

def setup(bot):
    bot.add_cog(Powers(bot))
