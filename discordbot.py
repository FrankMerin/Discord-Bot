import discord
from discord.ext import commands
import json
from urllib.request import urlopen
import requests
import string

readApikey = open("apikey.gitignore", "r")
discord_key = readApikey.read()

       



client = commands.Bot(command_prefix = '$')


@client.event
async def on_ready():
    print('ran successfully')

# ping function

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

# stock function

@client.command()
async def tk(ctx, tk):
    try:
        url = ('https://financialmodelingprep.com/api/v3/company/profile/' + (tk))
        data = requests.get(url)
        stockSymbol = data.json()['symbol']
        stockProfile = data.json()['profile']['price']
        stockChange = data.json()['profile']['changesPercentage']
        await ctx.send('```Symbol: %s \nPrice: %s \nPercent Changed: %s' % (stockSymbol, stockProfile, stockChange + "```"))
    except:
        await ctx.send('Ticker Symbol Invalid')


# UwU function
uwu = 'uwu'

@client.event
async def on_message(ctx):
    if(ctx.author.bot):
        return
    if ctx.content.lower() == uwu:
        channel = ctx.channel
        await channel.send('UwU')
    await client.process_commands(ctx)


client.run(discord_key)