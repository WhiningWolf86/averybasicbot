import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('test might have worked!')
        return