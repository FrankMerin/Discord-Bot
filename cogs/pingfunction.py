from discord.ext import commands


class PingFunction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('ping enabled')

    # ping function
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("{} ms".format(round(self.client.latency * 1000)))

def setup(client):
    client.add_cog(PingFunction(client))
