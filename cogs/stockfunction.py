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

    
    # stocks in USD
    @commands.command()
    async def tk(self, ctx, tk):
        try:

            url = (f"https://financialmodelingprep.com/api/v3/company/profile/{tk}?apikey={str(stock_key)}")
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

    # crypto in USD
    @commands.command() 
    async def tk(self, ctx, cr):
        try:
            url = (f"https://financialmodelingprep.com/api/v3/quote/{cr}USD?apikey={str(stock_key)}")
            data = requests.get(url)
            cryptoName = data.json()['name']
            cryptoPrice = data.json()['price']
            cryptoPriceChange = data.json()['change']
            cryptoChangePercent = data.json()['changesPercentage']

            if cryptoPriceChange > 0:
                sidecolor = discord.Color.green()
            elif cryptoPriceChange < 0:
                sidecolor = discord.Color.red()
            else:
                sidecolor = discord.Color.from_rgb(211,211,211)
            
            embedstock = discord.Embed(
                color = sidecolor
            )

            embedstock.add_field(name='**Coin:**', value=cryptoName, inline=False)
            embedstock.add_field(name='**Price:**', value='$' + str(cryptoPrice), inline=False)
            embedstock.add_field(name='**Price Change Today:**', value='$' + str(cryptoPriceChange), inline=False)
            embedstock.add_field(name='**Percent Change Today:**', value=cryptoChangePercent, inline=False)

            await ctx.send(embed=embedstock)

        except KeyError:
            await ctx.send('Coin Symbol Invalid')




def setup(client):
    client.add_cog(StockFunction(client))