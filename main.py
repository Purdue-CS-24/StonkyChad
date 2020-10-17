import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def analysis(ctx, *, arg):
    await ctx.send(arg)

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