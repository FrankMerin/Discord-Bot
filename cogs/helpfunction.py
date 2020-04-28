import discord
from discord.ext import commands

class helpfunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('help enabled')

    
    # help information
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='Bot Commands')
        embed.add_field(name='$ping', value='Displays latency to the server', inline=False)
        embed.add_field(name='$tk', value='Enter $tk <ticker symbol> for stock information', inline=False)
        embed.add_field(name='$clear', value='Enter $clear <value> to deletes messages. Default value = 5', inline=False)
    

        await ctx.author.send(embed=embed)

def setup(client):
    client.add_cog(helpfunction(client))