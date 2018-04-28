import discord
import secrets

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(('hans', 'Hans', 'HANS')):
        msg = '*reicht {0.author.mention} den Flammenwerfer*'.format(message)
        await client.send_message(message.channel, msg)
    
    if any(client.user.name in s.name for s in message.mentions):
        msg = 'Sie haben gerufen?'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(secrets.TOKEN)