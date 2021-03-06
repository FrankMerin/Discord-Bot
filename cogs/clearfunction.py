from discord.ext import commands


class ClearFunction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('clear enabled')

    # clear function
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, *args):
        """
        We expect 0, 1 or 2 arguments.
        0 args = clear last 5 messages
        1 arg = either number of messages or last 5 user's messages
        2 args = clear N messages for a specific user
        """
        userid = None
        amount = 5
        for arg in args:
            if "<@!" in arg or float(arg) > 10000000:
                userid = arg.strip('<@!>')
            else:
                try:
                    amount = int(arg)
                except ValueError:
                    pass

        if args.__len__() == 0:
            deleted = await ctx.channel.purge(limit=amount)
            await ctx.send('Deleted {} message(s)'.format(len(deleted)),delete_after=4)

        elif args.__len__() == 2:
            if not userid:
                pass
            deleted = await ctx.channel.purge(limit=amount, check=lambda m: str(m.author.id) == userid)
            await ctx.send('Deleted {} message(s)'.format(len(deleted)),delete_after=4)

        elif args.__len__() == 1:
            # let's find out which arg we have
            if userid:
                deleted = await ctx.channel.purge(limit=amount, check=lambda m: str(m.author.id) == userid)
                await ctx.send('Deleted {} message(s)'.format(len(deleted)),delete_after=4)
                
            else:
                deleted = await ctx.channel.purge(limit=amount)
                await ctx.send('Deleted {} message(s)'.format(len(deleted)),delete_after=4)

    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.channel.send('You do not have permissions to order me around! Baka! (This Command Requires Manage Messages Permissions)',delete_after=6)


def setup(client):
    client.add_cog(ClearFunction(client))
