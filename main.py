import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def analysis(ctx, *, arg):
    await ctx.send(arg)

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
         await message.channel.seng(msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.token)