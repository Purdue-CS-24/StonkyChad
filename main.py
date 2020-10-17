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
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.token)