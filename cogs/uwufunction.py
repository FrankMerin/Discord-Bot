import discord
from discord.ext import commands


class uwufunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('uwu enabled')

    
    # UwU function
    

    @commands.Cog.listener()
    async def on_message(self, ctx):
        uwu = 'uwu'
        if(ctx.author.bot):
            return
        if ctx.content.lower() == uwu:
            channel = ctx.channel
            await channel.send('UwU')
            await self.client.process_commands(ctx)


        

def setup(client):
    client.add_cog(uwufunction(client))