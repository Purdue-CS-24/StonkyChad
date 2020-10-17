from discord.ext import commands
import config
import StockAnalyzer

bot = commands.Bot(command_prefix='!')

client = discord.Client()

@bot.command()
async def analysis(ctx, *, arg):
    await ctx.send(arg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!eat my ass out and call me raqueem'):
        msg = 'yes my lord {0.author.mention'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.token)