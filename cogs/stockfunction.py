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
            data = requests.get(url).json()['profile']
            stockpic = data['image']
            stockcompany = data['companyName']
            stockprice = data['price']
            stockpchange = data['changes']
            stockchange = data['changesPercentage']


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

    @commands.command()
    async def cr(self, ctx, cr):
        crToCapital = cr.upper()
        try:
            url = (f"https://financialmodelingprep.com/api/v3/quote/{crToCapital}USD?apikey={str(stock_key)}")
            data = requests.get(url).json()[0]
            cryptoName = data['name']
            cryptoPrice = data['price']
            cryptoMarketCap = data['marketCap']


            
            embedstock = discord.Embed(
                color = discord.Color.orange()
            )

            embedstock.add_field(name='**Coin:**', value=cryptoName, inline=False)
            embedstock.add_field(name='**Price:**', value='$' + "{:,}".format(cryptoPrice), inline=False)
            embedstock.add_field(name='**Market Cap**', value='$' + "{:,}".format(cryptoMarketCap), inline=False)
            

            await ctx.send(embed=embedstock)

        except IndexError:
            await ctx.send('Coin Symbol Invalid')


    

def setup(client):
    client.add_cog(StockFunction(client))