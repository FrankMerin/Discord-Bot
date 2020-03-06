import discord
from discord.ext import commands
import requests
import string


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
        embedStock = discord.Embed(
            
        )

        url = ('https://financialmodelingprep.com/api/v3/company/profile/' + (tk))
        data = requests.get(url)
        stockPic = data.json()['profile']['image']
        stockSymbol = data.json()['symbol']
        stockPrice = data.json()['profile']['price']
        stockPChange = data.json()['profile']['changes']
        stockChange = data.json()['profile']['changesPercentage']

        embedStock.set_thumbnail(url = stockPic)
        embedStock.add_field(name='Symbol:', value=stockSymbol, inline=False)
        embedStock.add_field(name='Price', value=stockPrice, inline=False)
        embedStock.add_field(name='Price Change Today', value='$' + str(stockPChange), inline=False)
        embedStock.add_field(name='Percent Change Today', value=stockChange, inline=False)

        await ctx.send(embed=embedStock)

    except:
        await ctx.send('Ticker Symbol Invalid') 

def setup(client):
    client.add_cog(stockfunction(client))