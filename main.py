import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stockprofile(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    currentc = current.json()['c']
    await ctx.send(':moneybag: The current Price of ' + arg.upper() + ' is $' + str(currentc))
    currentc = current.json()['l']
    await ctx.send(':moneybag: The low price of ' + arg.upper() + ' was $' + str(currentc))
    currentc = current.json()['o']
    await ctx.send(':moneybag: The open price of ' + arg.upper() + ' is $' + str(currentc))
    await ctx.send(":moneybag: The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']))

@bot.command()
async def lowprice(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    currentc = current.json()['l']
    await ctx.send(':moneybag: The low price of ' + arg.upper() + ' was $' + str(currentc))

@bot.command()
async def openprice(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    currentc = current.json()['o']
    await ctx.send(':moneybag: The open price of ' + arg.upper() + ' is $' + str(currentc))

@bot.command()
async def previousclose(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":moneybag: The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']))
    
@bot.command()
async def currentprice(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    currentc = current.json()['c']
    await ctx.send(':moneybag: The current Price of ' + arg.upper() + ' is $' + str(currentc))


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