import discord
import config

TOKEN = 'NzY3MDY4Mzc4NTIzMTA3MzQ5.X4siGA.Ol5T6bOyClBjlLUz4_-R2MtNDSg'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.token)