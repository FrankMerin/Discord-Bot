import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import string
from typing import Optional

class clearfunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('clear enabled')




    # clear function
    @commands.command()
    @commands.has_permissions(manage_messages = True)


    async def clear(self, ctx, amount: Optional[int] = 5, author=''):
        if author =='':
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.channel.purge(limit=amount, check=lambda m: str(m.author.id) == author.strip('<@!>'))


    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.channel.send ('You do not have permissions to order me around! Baka!')

def setup(client):
    client.add_cog(clearfunction(client))