import discord
from discord.ext import commands
import requests
import string
import os


""" readApikey = open("apikey.txt", "r")
discord_key = readApikey.read() """

discord_key = (os.environ.get('CCbot_API'))
   


client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print('ran successfully')



client.run(discord_key)