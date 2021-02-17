import discord
from discord.ext import commands


class HelpFunction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('help enabled')

    # help information
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )

        embed.set_author(name='Bot Commands')
        embed.add_field(name='$ping', value='Displays latency to the server', inline=False)
        embed.add_field(name='$tk', value='Enter $tk <ticker symbol> for stock information', inline=False)
        embed.add_field(name='$cr', value='Enter $cr <coin symbol> for coin information', inline=False)
        embed.add_field(name='$clear',
                        value='Enter $clear [number_of_messages] [@userID] to delete messages. Default value = 5. Must have manage messages permission to use this command',
                        inline=False)
        embed.add_field(name='$disableuwu / enableuwu', value='Use this to enable/disable the UwU autoreply', inline=False)

        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(HelpFunction(client))
