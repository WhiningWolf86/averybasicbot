import discord
from discord.ext import commands
import time
import os


token = 'bot_token'  # name this to your environment variable
owner = 'bot_owner'
welcome_channel = 576901270405775369


print(f'checking for {token}')
if token in os.environ:
    print(f'token {token} exists.')
    token_val = os.environ[token]
else:
    token_val = input('Please input bot token:\n')
    os.environ[token] = token_val
    print('temporarily added token, please add it to your environment variables')
    input('Read, and press Enter.')

if owner in os.environ:
    owner_val = os.environ[owner]
else:
    print("Add your Discord user ID in environment variables as 'bot_owner'\n"
          "or remove this IF-ELSE and directly change the 'owner_val' variable to your ID.")

print('signing in')

bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    print('signed in')
    game = 'This is a rewrite!'
    await bot.change_presence(activity=discord.Activity(name=game, type=0, status=discord.Status.online))
    print('status set')


@bot.event  # I have no idea if this works, I haven't been able to test it
async def on_member_join():
    channel = bot.get_channel(welcome_channel)
    time.sleep(1)
    await channel.send('Welcome!')


@bot.command()
async def test(ctx):
    await ctx.send('this is a test')


@bot.command()
async def invite(ctx):
    await ctx.send(discord.utils.oauth_url(bot.user.id))


@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    await ctx.send("{}".format(member.avatar_url))


bot.run(token_val)
