import discord
import os
envar = "bot_token" # chanve "bot_token" to the name of your enviroment variable

print(f'checking for {envar}') # checking if you have token stored an enviroment variable 
if envar in os.environ:
	print(f'{envar} exists')
	envar_val = os.environ[envar]
else:
    envar_val = input('Please imput bot token:\n') 
    os.environ[envar] = envar_val # temporarily sets token as envar_val
    print('Temporary variable added. Please add the token to your environment variables before starting next time.')
    input('Read, and then press Enter to continue...')

print(f'signing in with token {envar}:')

class MyClient(discord.Client):
    async def on_ready(self):
        game = 'hah'
        await client.change_presence(activity=discord.Activity(name=game, type=0, status=discord.Status.online))   # sets custom status and game
        print('signed in')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('s!hullo'):
            await message.channel.send('hi') # to mention the author, add '{0.author.mention}'
            return
        if message.content.startswith('s!service'):
            await message.channel.send(f"The user is {os.environ['USER']}\nThe shell is {os.environ['SHELL']}")
    
    async def on_member_join(self, member: discord.Member):
        channel = client.get_channel()
        await channel.send('Hello ' +str(member.mention)+ ', Welcome!')
        return

client = MyClient()
client.run(envar_val)