import discord
from discord.ext import commands
import os
import json
import re

# Local Imports
from cogs.utils import constants


class Placements:
    def __init__(self, bot):
        self.bot = bot

    def get_path(self, place_num):
        my_path = os.path.abspath(os.path.dirname(__file__))

        fname = ''
        if place_num == '1':
            fname = 'utils/placement_one.json'
        elif place_num == '2':
            fname = 'utils/placement_two.json'

        return os.path.join(my_path, fname)

    async def clearma(self, place_num):
        path = self.get_path(place_num)

        with open(path, 'r') as f:
            fresh = json.load(f)

        fresh.clear()

        with open(path, 'w') as f:
            json.dump(fresh, f)

    async def update_data(self, users, user, rank):
        if not str(user.id) in users:
            users[user.id] = {}
            users[user.id]['rank'] = int(rank)
            return True
        else:
            return False


    @commands.command(pass_context=True)
    async def placement_init(self, ctx, name_of_game, rank_max, place_num):
        # clear command
        ch = ctx.message.channel
        messages = await ch.history(limit=1).flatten()
        await ch.delete_messages(messages)
        # clear json file
        await self.clearma(place_num)

        # produce vote message
        role = discord.utils.get(ctx.guild.role_hierarchy, name='Council')
        voting_ch = self.bot.get_channel(int(os.environ['VOTING']))

        embed=discord.Embed(title=' ',
                            colour=0x1ece6d)
        embed.add_field(name='**Game**', value=name_of_game, inline=False)
        embed.add_field(name='**Code Number**', value=place_num, inline=False)
        embed.add_field(name='**Placement Average**', value='Rank 0', inline=False)
        embed.add_field(name='**Lowest Possible Rank**', value='Rank {0}'.format(rank_max), inline=False)
        embed.add_field(name='**Number of Votes**', value='0', inline=False)
        embed.add_field(name='**Notify**', value='{0.mention}'.format(role))
        await voting_ch.send(embed=embed)

    @commands.command(pass_context=True)
    async def placement(self, ctx, place_num, rank):
        # clear command
        ch = ctx.message.channel
        messages = await ch.history(limit=1).flatten()
        await ch.delete_messages(messages)

        # setup
        ch = discord.utils.get(self.bot.get_all_channels(), guild__name='Desire Index', name='voting')
        role = discord.utils.get(ctx.guild.role_hierarchy, name='Council')
        expected = ['**Game**', '**Code Number**', '**Placement Average**', '**Lowest Possible Rank**', '**Number of Votes**', '**Notify**']

        # find message to edit
        async for message in ch.history().filter(lambda m: m.author == self.bot.user):
            check = []
            name_of_game = ''
            rank_max = ''

            # field checks
            matching = False
            for field in message.embeds[0].fields:
                check.append(field.name)
                if field.name == expected[0]:
                    name_of_game = field.value

                elif field.name == expected[3]:
                    rank_max = field.value

                elif field.name == expected[1]:
                    if place_num == field.value:
                        matching = True

            # MATCH!
            if matching:
                for e in expected:
                    if e not in check:
                        break

                # val check
                # first get rank_max proper
                num = re.findall('\d+', rank_max)

                if int(rank) < 1 or int(rank) > int(num[0]):
                    ch = self.bot.get_channel(int(os.environ['DISCUSSION']))
                    await ch.send('{0.mention}, that rank is not within the parameters.'.format(ctx.message.author))
                    return

                # create path to json file
                path = self.get_path(place_num)

                with open(path, 'r') as f:
                    users = json.load(f)

                if not (await self.update_data(users, ctx.message.author, int(rank))):
                    ch = self.bot.get_channel(int(os.environ['DISCUSSION']))
                    await ch.send('{0.mention}, you have already made your placement vote.'.format(ctx.message.author))
                    return

                with open(path, 'w') as f:
                    json.dump(users, f)

                # update
                with open(path, 'r') as f:
                    users = json.load(f)

                sum = 0
                count = 0
                for v in users.values():
                    sum += v['rank']
                    count += 1

                embed=discord.Embed(title=' ',
                                    colour=0x1ece6d)
                embed.add_field(name='**Game**', value=name_of_game, inline=False)
                embed.add_field(name='**Code Number**', value=place_num, inline=False)
                embed.add_field(name='**Placement Average**', value='Rank {0}'.format(round(sum/count)), inline=False)
                embed.add_field(name='**Lowest Possible Rank**', value='{0}'.format(rank_max), inline=False)
                embed.add_field(name='**Number of Votes**', value='{0}'.format(count), inline=False)
                embed.add_field(name='**Notify**', value='{0.mention}'.format(role))
                await message.edit(embed=embed)

                ch = self.bot.get_channel(int(os.environ['DISCUSSION']))
                await ch.send('{0.mention}, thank you for your vote!'.format(ctx.message.author))


def setup(bot):
    bot.add_cog(Placements(bot))
