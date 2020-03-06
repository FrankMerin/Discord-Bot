import discord
from discord.ext import commands
import requests


class stockfunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('stocks enabled')

    
    # stock function
    @commands.command()
    async def tk(self, ctx, tk):
        try:
            url = ('https://financialmodelingprep.com/api/v3/company/profile/' + (tk))
            data = requests.get(url)
            stockSymbol = data.json()['symbol']
            stockProfile = data.json()['profile']['price']
            stockPChange = data.json()['profile']['changes']
            stockChange = data.json()['profile']['changesPercentage']
            await ctx.send('```Symbol: %s \nPrice: %s \nPrice Changed %s \nPercent Changed: %s' % (stockSymbol, stockProfile, '$' + stockPChange, stockChange + "```"))
        except:
            await ctx.send('Ticker Symbol Invalid')

def setup(client):
    client.add_cog(stockfunction(client))