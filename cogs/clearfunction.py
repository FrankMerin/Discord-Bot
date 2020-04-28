import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class clearfunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('clear enabled')

    
    # clear function
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.channel.send ('You do not have permissions to order me around! Baka!')

def setup(client):
    client.add_cog(clearfunction(client))