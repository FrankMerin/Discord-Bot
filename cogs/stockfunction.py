import discord
from discord.ext import commands
import requests
import os

stock_key = (os.environ.get('Stock_API'))

class StockFunction(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('stocks enabled')

    
    # stock function
    @commands.command()
    async def tk(self, ctx, tk):
        try:

            url = ('https://financialmodelingprep.com/api/v3/company/profile/' + (tk) + '?apikey=' + str(stock_key))
            data = requests.get(url)
            stockpic = data.json()['profile']['image']
            stockcompany = data.json()['profile']['companyName']
            stockprice = data.json()['profile']['price']
            stockpchange = data.json()['profile']['changes']
            stockchange = data.json()['profile']['changesPercentage']


            if stockpchange > 0:
                sidecolor = discord.Color.green()
            elif stockpchange < 0:
                sidecolor = discord.Color.red()
            else:
                sidecolor = discord.Color.from_rgb(211,211,211)
            
            embedstock = discord.Embed(
                color = sidecolor
            )


            embedstock.set_thumbnail(url = stockpic)
            embedstock.add_field(name='**Company:**', value=stockcompany, inline=False)
            embedstock.add_field(name='**Price:**', value='$' + str(stockprice), inline=False)
            embedstock.add_field(name='**Price Change Today:**', value='$' + str(stockpchange), inline=False)
            embedstock.add_field(name='**Percent Change Today:**', value=stockchange, inline=False)

            await ctx.send(embed=embedstock)

        except KeyError:
            await ctx.send('Ticker Symbol Invalid') 

def setup(client):
    client.add_cog(StockFunction(client))