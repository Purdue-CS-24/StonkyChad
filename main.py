from _datetime import datetime
import json

import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def stockprofile(ctx, *, arg):
    current = requests.get("https://finnhub.io/api/v1/quote?symbol="+ arg.upper() +"&token=bto4nln48v6v7atimad0")

    displaymsg = "Current Price: " + arg.upper() + " is $" + str(current.json()['c']) + "\n" + \
                 "High Price: " + arg.upper() + " was $" + str(current.json()['h']) + "\n" + \
                 "Low Price: " + arg.upper() + " was $" + str(current.json()['l']) + "\n" + \
                 "Open Price: " + arg.upper() + " is $" + str(current.json()['o']) + "\n" + \
                 "Previous Closing Price: " + arg.upper() + " was $" + str(current.json()['pc']) + "\n" + \
                 arg.upper() + "'s Time Stamp(Universal Time): " + \
                 datetime.utcfromtimestamp(current.json()['t']).strftime('%Y-%m-%d %H:%M:%S') + "\n"

    await ctx.send(displaymsg)

@bot.command()
async def profile(ctx, *, arg):
    profile = requests.get(
        'https://finnhub.io/api/v1//stock/profile2?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    displaymsg = "Name: " + str(profile.json()['name']) + "\n" + \
                 "Classification: " + str(profile.json()['finnhubIndustry']) + "\n" + \
                 "HQ: " + str(profile.json()['country']) + "\n" + \
                 "Currency: " + str(profile.json()['currency']) + "\n" + \
                 "Exchange: " + str(profile.json()['exchange']) + "\n" + \
                 "Symbol/Ticker: " + str(profile.json()['ticker']) + "\n" + \
                 "IPO: " + str(profile.json()['ipo']) + "\n" + \
                 "Market Capitalization: " + str(profile.json()['marketCapitalization']) + "\n" + \
                 "Number of Shares: " + str(
        profile.json()['shareOutstanding']) + "\n" + \
                 "Phone Number: " + str(profile.json()['phone']) + "\n" + \
                 "Website: " + str(profile.json()['weburl']) + "\n"

    await ctx.send(displaymsg)

@bot.command()
async def news(ctx, *, arg):
    news = requests.get("https://finnhub.io/api/v1/company-news?symbol=" + arg.upper() + "&from=2020-10-17&to=2020-10-17&token=bto4nln48v6v7atimad0")
    limit = 5

    index = 0
    for article in news.json():
        displaymsg = article.get('source').upper() + ": " + article.get('headline') + "\n" + \
                     "Summary" + ": " + article.get('summary') + "\n" + \
                     "Full report at " + article.get('url') + "\n"
        index += 1
        if index == limit:
            break
        await ctx.send(displaymsg)

@bot.command()
async def help(ctx):
    displaymsg = "```**Welcome to the home of **Stonky Chad**! We created a bot that when given a stock symbol " \
                 "(e.g googl/GOOGL for Google, amzn/AMZN for Amazon, etc.), would give information such as quotes, " \
                 "recommendations, and profile. Commands are listed below:** \n\n" \
                 "__**Requires an input (a stock symbol, e.g. GOOGL or AMZN and is case insensitive meaning googl is** __" \
                 "__**okay**__):\n"\
                "***!stockprofile***: gives a profile of the stock symbol including current, high, low, open, " \
                 "and previous closing price at the current time.\n" \
                 "***!profile***: gives a profile of the company that owns the shares, i.e. name, HQ, etc.\n" \
                 "***!news***: pulls the first 5 articles from the past day about the given stock \n" \
                 "***!lowprice***:  gives lowest price of the day\n" \
                 "***!openprice***: gives open price of the day\n" \
                 "***!previousclose***: gives previous closing price of the day\n" \
                 "***!currentprice***: gives current price\n" \
                 "***!highprice***: gives highest price of the day\n" \
                 "***!timestamp***: gives current time in universal time\n" \
                 "***!recs***: determines whether a stock is over- or undervalued, and recommends whether or not " \
                 "it is a good idea to buy or sell the stock\n\n" \
                 "__**Does not require an input and are commands we made when we were malding/bored:**__\n" \
                 "***!eatmyASS***\n" \
                 "***!daddychill***\n" \
                 "***!fatyoshi***\n" \
                 "***!sadge***\n" \
                 "***!devs***```"
    await ctx.send(displaymsg)

@bot.command()
async def devs(ctx):
    displaymsg = "Stonky Chad Bot was birthed by Ananya Singh, Dorothy Luo, Ethan Su, and Vidhi Singh. " \
                 "Please use this bot only for personal purposes."
    await ctx.send(displaymsg)

@bot.command()
async def sadge(ctx):
    await ctx.send('do you ever just \n https://tenor.com/view/sadge-sad-xqc-sad-pepe-sad-feelsbad-gif-17782875')

@bot.command()
async def fatyoshi(ctx):
    await ctx.send('WAHOO https://i.redd.it/waom7vm9t0z21.jpg')

@bot.command()
async def papakedar(ctx):
    await ctx.send("whos ur daddy \n" + "https://media.discordapp.net/attachments/758822857136144385/767180587072094208/deepfried_1602980477191.png")

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
async def timestamp(ctx):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bto4nln48v6v7atimad0')
    await ctx.send(":clock3: The time stamp of is " +
                   datetime.utcfromtimestamp(current.json()['t']).strftime('%Y-%m-%d %H:%M:%S'))

@bot.command()
async def eatmyASS(ctx):
    await ctx.send('i dont have a mouth')

@bot.command()
async def recs(ctx, arg):

    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    q1i = requests.get(
        'https://finnhub.io/api/v1/stock/candle?symbol=' + arg.upper() + '&resolution=1&from=1577836800&to=1585612800&token=bto4nln48v6v7atimad0')
    q2i = requests.get(
        'https://finnhub.io/api/v1/stock/candle?symbol=' + arg.upper() + '&resolution=1&from=1585699200&to=1593475200&token=bto4nln48v6v7atimad0')
    q3i = requests.get(
        'https://finnhub.io/api/v1/stock/candle?symbol=' + arg.upper() + '&resolution=1&from=1593561600&to=1601424000&token=bto4nln48v6v7atimad0')
    q4i = requests.get(
        'https://finnhub.io/api/v1/stock/candle?symbol=' + arg.upper() + '&resolution=1&from=1601510400&to=1609372800&token=bto4nln48v6v7atimad0')
    q1e = requests.get(
        'https://finnhub.io/api/v1/calendar/earnings?from=2020-01-01&to=2020-03-31&symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    q2e = requests.get(
        'https://finnhub.io/api/v1/calendar/earnings?from=2020-04-01&to=2020-06-30&symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    q3e = requests.get(
        'https://finnhub.io/api/v1/calendar/earnings?from=2020-07-01&to=2020-09-30&symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
    q4e = requests.get(
        'https://finnhub.io/api/v1/calendar/earnings?from=2020-10-01&to=2020-12-31&symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    currentinfo = current.json()
    q1info = q1i.json()
    q2info = q2i.json()
    q3info = q3i.json()
    q4info = q4i.json()
    q1earn = q1e.json()
    q2earn = q2e.json()
    q3earn = q3e.json()
    q4earn = q4e.json()

    currentc = current.json()['c']

    q1actual = q1earn['earningsCalendar'][0]['revenueActual']
    q1estimate = q1earn['earningsCalendar'][0]['revenueEstimate']

    q2actual = q2earn['earningsCalendar'][0]['revenueActual']
    q2estimate = q2earn['earningsCalendar'][0]['revenueEstimate']

    q3actual = q3earn['earningsCalendar'][0]['revenueActual']
    q3estimate = q3earn['earningsCalendar'][0]['revenueEstimate']

    q4actual = q4earn['earningsCalendar'][0]['revenueActual']
    q4estimate = q4earn['earningsCalendar'][0]['revenueEstimate']

    q1epsactual = q1earn['earningsCalendar'][0]['epsActual']
    q1epsestimate = q1earn['earningsCalendar'][0]['epsEstimate']

    q2epsactual = q2earn['earningsCalendar'][0]['epsActual']
    q2epsestimate = q2earn['earningsCalendar'][0]['epsEstimate']

    q3epsactual = q3earn['earningsCalendar'][0]['epsActual']
    q3epsestimate = q3earn['earningsCalendar'][0]['epsEstimate']

    q4epsactual = q4earn['earningsCalendar'][0]['epsActual']
    q4epsestimate = q4earn['earningsCalendar'][0]['epsEstimate']

    epsactualavg = (q1epsactual + q2epsactual + q3epsactual + q4epsactual) / 4

    peratio = currentc / epsactualavg

    if peratio > 25:
        await ctx.send(arg.upper() + ' is currently VERY overvalued ie. STRONG SELL :muscle:')
    if 25 > peratio > 20:
        await ctx.send(arg.upper() + ' is currently overvalued ie. SELL :chart_with_downwards_trend:')
    if 20 > peratio > 15:
        await ctx.send(arg.upper() + ' is currently fairly valued ie. HOLD :pause_button:')
    if 15 > peratio > 10:
        await ctx.send(arg.upper() + ' is currently undervalued ie. BUY :chart_with_upwards_trend:')
    if 10 > peratio:
        await ctx.send(arg.upper() + ' is currently VERY undervalued ie. STRONG BUY :muscle:')

@bot.command()
async def daddychill(ctx):
    await ctx.send("YO CHILLLLLL " + "https://tenor.com/view/chill-daddy-take-it-easy-calm-down-gif-13696124")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.token)