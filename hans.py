import discord
import secrets
import time

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

    if message.content.startswith(('!treppe', '!Treppe')):
        theserver = client.servers
        mess = message.content.split()
        try:
            member_to_move = mess[1]
            timeout = int(mess[2])
            member_obj = sorted(theserver)[0].get_member_named(member_to_move)
            member_voice_chan = member_obj.voice.voice_channel

            channels = client.get_all_channels()
            silence = None
            for channel in channels:
                if channel.name.startswith('Stille'):
                    silence = channel
                else:
                    pass
            if member_to_move == 'Günther':
                raise Exception("Nein")
            msg = 'Ab auf die Treppe mir dir, {}!'.format(member_to_move)
            await client.send_message(message.channel, msg)
            await client.move_member(member_obj, silence)

            if timeout > 10:
                timeout = 10
            
            time.sleep(timeout)
            await client.move_member(member_obj, member_voice_chan)
        except (IndexError):
            msg = 'Somethings wrong with your arguments. Try again! Syntax: !treppe <user> <sekunden>'
            await client.send_message(message.channel, msg)
        except (AttributeError):
            msg = "Seems I didn't find the user =/ Try again! Syntax: !treppe <user> <sekunden>"
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(secrets.TOKEN)
