import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stockprofile(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(':moneybag: The current Price of ' + arg.upper() + ' is $' + str(current.json()['c']))
    await ctx.send(":moneybag: The high price of " + arg.upper() + " was $" + str(current.json()['h']))
    await ctx.send(':moneybag: The low price of ' + arg.upper() + ' was $' + str(current.json()['l']))
    await ctx.send(':moneybag: The open price of ' + arg.upper() + ' is $' + str(current.json()['o']))
    await ctx.send(":moneybag: The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']))
    await ctx.send(":bar_chart: The volume data of " + arg.upper() + " is " + str(current.json()['v']))
    await ctx.send(":clock3: The time stamp of " + arg.upper() + " is " + str(current.json()['t']))
    await ctx.send(":bangbang: The request status of " + arg.upper() + " is " + str(current.json()['s']))

@bot.command()
async def lowprice(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(':moneybag: The low price of ' + arg.upper() + ' was $' + str(current.json()['l']))

@bot.command()
async def openprice(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(':moneybag: The open price of ' + arg.upper() + ' is $' + str(current.json()['o']))

@bot.command()
async def previousclose(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":moneybag: The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']))

@bot.command()
async def currentprice(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(':moneybag: The current Price of ' + arg.upper() + ' is $' + str(current.json()['c']))

@bot.command()
async def highprice(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":moneybag: The high price of " + arg.upper() + " was $" + str(current.json()['h']))

@bot.command()
async def volumedata(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":bar_chart: The volume data of " + arg.upper() + " is " + str(current.json()['v']))

@bot.command()
async def timestamp(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":clock3: The time stamp of " + arg.upper() + " is " + str(current.json()['t']))

@bot.command()
async def responsestatus(ctx, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    await ctx.send(":bangbang: The request status of " + arg.upper() + " is " + str(current.json()['s']))

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