import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stockprofile(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    await ctx.send(current.json())

    currentc = current.json()['c']
    await ctx.send('Current Price of ' + arg + ': $' + currentc)

@bot.command()
async def lowprice(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    await ctx.send(current.json())

    currentc = current.json()['l']
    await ctx.send('Low Price of ' + arg + ': $' + currentc)

@bot.command()
async def openprice(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    await ctx.send(current.json())

    currentc = current.json()['o']
    await ctx.send('Open Price of ' + arg + ': $' + currentc)

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