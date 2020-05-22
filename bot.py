#any text placed within «» is place holder, it is ment to be replaced with your own information «» removed. 
#This does not mean you can't change anything else within the script.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        # game = '« X-Plane »'  # only set if you want bot playing a game
        # await client.change_presence(activity=discord.Activity(name=game, status=discord.Status.« online, idle, dnd »))   # sets custom status and game
        print(+str+(self.user.name)+ +str(self.user.id)+ ' logged in')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('« your command »'):
            await message.channel.send(+str(author.mention)+ '« your message content »') # this will mention the author of the command message, remove +str(author.mention)+ to make it not mention the author.
            return

    #welcome message
    async def on_member_join(self, member: discord.Member):
        channel = client.get_channel(« welcome channel ID») # you get channel IDs by right clicking the channel name 
        await channel.send('Hello ' +str(member.mention)+ ' Welcome!') # mentions the new user in specified channel in line above
        return

client = MyClient()
client.run('« bot token') # found in the 'Bot' section in your Discord Applicaton.