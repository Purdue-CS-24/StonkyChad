import discord
import config
from discord.ext import commands
import statistics
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def analysis(ctx, *, arg):
    current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + arg.upper() + '&token=bto4nln48v6v7atimad0')
<<<<<<< HEAD
    await ctx.send(current.json())
=======
    currentc = current.json()['c']
    await ctx.send(currentc)
>>>>>>> main

@bot.command()
async def eatmyASS(ctx):
    await ctx.send('i dont have a mouth')
<<<<<<< HEAD
<<<<<<< HEAD


@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

     if message.content.startswith('!analysis'):
         msg = 'THIS BOT DONT WORK'
         await message.channel.send(msg)

=======

>>>>>>> main
=======

>>>>>>> main
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.token)