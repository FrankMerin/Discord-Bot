from discord.ext import commands
import os
import psycopg2
import asyncpg


discord_key = (os.environ.get('CCbot_API'))
client = commands.Bot(command_prefix='$')
client.remove_command('help')

# database connection variables
DB_NAME = os.environ.get('DATABASE_NAME')
DB_USER = os.environ.get('DATABASE_NAME')
DB_PASS = os.environ.get('DATABASE_PASS')
DB_HOST = "ruby.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, 
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS statusUwU (
                                ID SERIAL PRIMARY KEY NOT NULL,
                                serverID TEXT NOT NULL,
                                status BOOL NOT NULL
                                );""")
conn.close()




@client.command()
async def load(ctx, extention):
    client.load_extension('cogs.{extention}')




if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in os.listdir("cogs") if os.path.isfile(os.path.join("cogs", f))]:
        try:
            client.load_extension("cogs" + "." + extension)
        except:
            print('Failed to load extension {extension}.')

@client.event
async def on_ready():
    print('Bot is alive')


# add serverID to database when joining new server
@client.event
async def on_guild_join(guild):
    conn = await asyncpg.connect(database = DB_NAME, user = DB_USER, 
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)
    server = str(guild.id)
    print(server)
    if not await findexistance(server):
        print("will create new server")
        await conn.execute('INSERT INTO public.statusuwu (serverID, status) VALUES ($1,True)', server)
    else:
        print('already exists')
    await conn.close()


# ran from the on_guild_join function to check if the server has already been added into database
async def findexistance(server):
    conn = await asyncpg.connect(database = DB_NAME, user = DB_USER, 
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)
    result = await conn.execute('SELECT serverID FROM public.statusuwu WHERE serverID= $1', server)
    # result is equal to the number of rows output from the database, in the case of the server not existing already, we return SELECT 0
    if result != 'SELECT 0': 
        await conn.close()
        return True
    else:
        await conn.close()
        return False
    




client.run(discord_key, bot=True, reconnect=True)
