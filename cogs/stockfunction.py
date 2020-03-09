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
           

            url = ('https://financialmodelingprep.com/api/v3/company/profile/' + (tk))
            data = requests.get(url)
            stockPic = data.json()['profile']['image']
            stockCompany = data.json()['profile']['companyName']
            stockPrice = data.json()['profile']['price']
            stockPChange = data.json()['profile']['changes']
            stockChange = data.json()['profile']['changesPercentage']


            if stockPChange > 0: 
                sideColor = discord.Color.green()
            elif stockPChange < 0:
                sideColor = discord.Color.red()
            else:
                sideColor = discord.Color.from_rgb(211,211,211)
            
            embedStock = discord.Embed(
                color = sideColor
            )


            embedStock.set_thumbnail(url = stockPic)
            embedStock.add_field(name='**Company:**', value=stockCompany, inline=False)
            embedStock.add_field(name='**Price:**', value='$' + str(stockPrice), inline=False)
            embedStock.add_field(name='**Price Change Today:**', value='$' + str(stockPChange), inline=False)
            embedStock.add_field(name='**Percent Change Today:**', value=stockChange, inline=False)

            await ctx.send(embed=embedStock)

        except:
            await ctx.send('Ticker Symbol Invalid') 

def setup(client):
    client.add_cog(stockfunction(client))