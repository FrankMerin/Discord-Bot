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
        if ctx.guild.id != 482608530105434112:   # temporary fix while i work on database solution to prevent UwU from running a specific server
            uwu = 'uwu'
            if(ctx.author.bot):
                return
            if ctx.content.lower() == uwu:
                channel = ctx.channel
                await channel.send('UwU')
                await self.client.process_commands(ctx)
        else:
            return


        

def setup(client):
    client.add_cog(uwufunction(client))