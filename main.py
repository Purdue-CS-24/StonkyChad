import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def analysis(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    currentc = current.json()['c']
    await ctx.send(currentc)

@bot.command()
async def eatmyASS(ctx):
    await ctx.send('i dont have a mouth')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.token)