import discord
from discord.ext import commands


class CGBSFunction(commands.Cog):

    def __init__(self, client):
        self.client = client

    def testfunc(self, message1, message2): 
        print('ok')

    @commands.Cog.listener()
    async def on_ready(self):
        print('CGBS enabled')

    # CGBS function
    @commands.command()
    async def raid(self, ctx):
        if ctx.guild.id == 642939587748036650:
            raidCP = None
            raidBC = None
            activeChannel = ctx.channel
            pastMessages = activeChannel.history(limit=30)
            async for message in pastMessages:
                if message.embeds != []:
                    if (message.author.id == 571027211407196161) and ('Raid Challenge Party' in message.embeds[0].title) and (raidCP == None):                    
                        raidCP = message
                    if (message.author.id == 571027211407196161) and ('Raid Boss Challenge' in message.embeds[0].title) and (raidBC == None):
                        raidBC = message
                    if raidBC != None and raidCP != None:
                        break
            raidRoomCode = str(raidCP.embeds[0].footer).split('|')[1]
            raidInfo = str(raidBC.embeds[0].description).split('**')[1]
            powerLevel = str(raidBC.embeds[0].description).split('**')[16]
            rewards = str(raidBC.embeds[0].description).split('Gold <:GOLD:704242802522980462>')[2]
            print(rewards)

            embedRaid = discord.Embed(
                color = discord.Color.green()
            )

            embedRaid.add_field(name='**Raid Info:**', value=raidInfo, inline=False)
            embedRaid.add_field(name='**Power Level:**', value=powerLevel, inline=False)
            embedRaid.add_field(name='**Room Code:**', value=raidRoomCode, inline=False)
            embedRaid.add_field(name='**Rewards:**', value=rewards, inline=False)


            
            raidPing = ctx.guild.get_role(732756047898345522)
            await ctx.send(raidPing.mention)

            await ctx.send(embed=embedRaid)
        else:
            await ctx.send("Gomen'nasai, I was unable to find AniGame info in the last 30 messages")
            







def setup(client):
    client.add_cog(CGBSFunction(client))
