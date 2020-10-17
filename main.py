import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stockprofile(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    displaymsg = "The current Price of" + arg.upper() + " is $" + str(current.json()['c']) + "\n" + \
                 "The high price of " + arg.upper() + " was $" + str(current.json()['h']) + "\n" + \
                 "The low price of " + arg.upper() + " was $" + str(current.json()['l']) + "\n" + \
                 "The open price of " + arg.upper() + " is $" + str(current.json()['o']) + "\n" + \
                 "The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']) + "\n" + \
                 "The time stamp of " + arg.upper() + " is " + str(current.json()['t'])

    await ctx.send(displaymsg)

    # await ctx.send(':moneybag: The current Price of ' + arg.upper() + ' is $' + str(current.json()['c']))
    # await ctx.send(":moneybag: The high price of " + arg.upper() + " was $" + str(current.json()['h']))
    # await ctx.send(':moneybag: The low price of ' + arg.upper() + ' was $' + str(current.json()['l']))
    # await ctx.send(':moneybag: The open price of ' + arg.upper() + ' is $' + str(current.json()['o']))
    # await ctx.send(":moneybag: The previous closing price of " + arg.upper() + " was $" + str(current.json()['pc']))
    # await ctx.send(":bar_chart: The volume data of " + arg.upper() + " is " + str(current.json()['v']))
    # await ctx.send(":clock3: The time stamp of " + arg.upper() + " is " + str(current.json()['t']))
    # await ctx.send(":bangbang: The request status of " + arg.upper() + " is " + str(current.json()['s']))


@bot.command()
async def companyprofile(ctx, *, arg):
    profile = requests.get(
        'https://finnhub.io/api/v1//stock/profile2?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')

    displaymsg = "The name of the company of " + arg.upper() + " is " + str(profile.json()['name']) + "\n" + \
                 "The country of company's headquarter is " + str(profile.json()['country']) + "\n" + \
                 "The currency used in company filings is " + str(profile.json()['currency']) + "\n" + \
                 "The listed exchange is " + str(profile.json()['exchange']) + "\n" + \
                 "The company symbol/ticker as used on the listed exchange is " + str(profile.json()['ticker']) + "\n" + \
                 "The IPO date of the company is " + str(profile.json()['ipo']) + "\n" + \
                 "The market capitalization of the company is " + str(profile.json()['marketCapitalization']) + "\n" + \
                 "The number of outstanding shares of the company is " + str(
        profile.json()['shareOutstanding']) + "\n" + \
                 "The company phone number is " + str(profile.json()['phone']) + "\n" + \
                 "The company website is " + str(profile.json()['weburl']) + "\n" + \
                 "The industry classification of the company is " + str(profile.json()['finnhubIndustry']) + "\n"

    await ctx.send(displaymsg)

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

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.token)