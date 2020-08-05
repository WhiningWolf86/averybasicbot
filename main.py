import discord
from discord.ext import commands
import os

token = 'bot_token'  # name this to your environment variable
print(f'checking for {token}')
if token in os.environ:
    print(f'token {token} exists.')
    token_val = os.environ[token]
else:
    token_val = input('Please input bot token:\n')
    os.environ[token] = token_val
    print('temporarily added token, please add it to your environment variables')
    input('Read, and press Enter.')

print('signing in')

bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    print('signed in')
    game = 'This is a rewrite!'
    await bot.change_presence(activity=discord.Activity(name=game, type=0, status=discord.Status.online))
    print('status set')


@bot.event #  I have no idea if this works, I haven't been able to test it
async def on_member_join(ctx, member: discord.Member):
    channel = bot.get_channel(576901270405775369)
    await ctx.send('Hello ' + str(member.mention) + ', Welcome!')


@bot.command()
async def test(ctx):
    await ctx.send('this is a test')


@bot.command()
async def invite(ctx):
    #  await bot.say('\U0001f44d')
    #  await bot.whisper(discord.utils.oauth_url(bot.user.id))
    await ctx.send(discord.utils.oauth_url(bot.user.id))


bot.run(token_val)
