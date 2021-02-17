from discord.ext import commands
import psycopg2
import asyncpg
import os


DB_NAME = os.environ.get('DATABASE_NAME')
DB_USER = os.environ.get('DATABASE_NAME')
DB_PASS = os.environ.get('DATABASE_PASS')
DB_HOST = "ruby.db.elephantsql.com"
DB_PORT = "5432"




class UwuFunction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('uwu enabled')

    # enable UwU, by default, when joining a server, this feature will be on.
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def enableuwu(self, ctx):
        conn = await asyncpg.connect(database = DB_NAME, user = DB_USER, 
                        password=DB_PASS, host=DB_HOST, port=DB_PORT)
        await conn.execute('UPDATE public.statusuwu SET status = True WHERE serverID= $1', str(ctx.guild.id))
        await conn.close()
    @enableuwu.error
    async def enableuwu_error(self, ctx, error):
        await ctx.channel.send('You do not have permissions to order me around! Baka! (This Command Requires Administator Permissions)',delete_after=6)

    # will disable UwU
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disableuwu(self, ctx):
        conn = await asyncpg.connect(database = DB_NAME, user = DB_USER, 
                        password=DB_PASS, host=DB_HOST, port=DB_PORT)
        await conn.execute('UPDATE public.statusuwu SET status = False WHERE serverID= $1', str(ctx.guild.id))
        await conn.close()
    @disableuwu.error
    async def clear_error(self, ctx, error):
        await ctx.channel.send('You do not have permissions to order me around! Baka! (This Command Requires Administator Permissions)',delete_after=6)

    # UwU function
    @commands.Cog.listener()
    async def on_message(self, ctx):  
        conn = await asyncpg.connect(database = DB_NAME, user = DB_USER, 
                                password=DB_PASS, host=DB_HOST, port=DB_PORT)
        result = await conn.execute('SELECT serverID FROM public.statusuwu WHERE status= True AND serverID= $1', str(ctx.guild.id))
        await conn.close()
        if result != 'SELECT 0':
            uwu = 'uwu'
            if ctx.author.bot:
                return
            if ctx.content.lower() == uwu:
                channel = ctx.channel
                await channel.send('UwU')
                await self.client.process_commands(ctx)
        else:
            return


def setup(client):
    client.add_cog(UwuFunction(client))
