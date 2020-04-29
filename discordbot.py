from discord.ext import commands
import os

discord_key = (os.environ.get('CCbot_API'))
client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.command()
async def load(ctx, extention):
    client.load_extension('cogs.{extention}')


# @client.command()
# async def unload(ctx, extention):
#     client.unload_extension(f'cogs.{extention}')


if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in os.listdir("cogs") if os.path.isfile(os.path.join("cogs", f))]:
        try:
            client.load_extension("cogs" + "." + extension)
        except:
            print('Failed to load extension {extension}.')

@client.event
async def on_ready():
    print('Bot is alive')


client.run(discord_key, bot=True, reconnect=True)
