#!/usr/bin/env python3

import time

import discord

import secrets
import gifclient


client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.lower().startswith(("!hilfe")):
        msg = "commands:\n!hilfe - for some help\n!wochenende - a handy link copy for the weekend video!\n!treppe <user> <seconds> - Move someone to Stille Treppe\nSay 'Hans' in chat to get a Flammenwerfer"
        await message.channel.send(msg)

    if message.content.lower().startswith(("hans")):
        msg = "*reicht {0.author.mention} den Flammenwerfer* \n{1}".format(message, gifclient.searchme("flamethrower"))
        await message.channel.send(msg)
    
    if any(client.user.name in s.name for s in message.mentions):
        msg = "Sie haben gerufen?"
        await message.channel.send(msg)

    if message.content.startswith(("!Wochenende", "!wochenende")):
        await message.channel.send("Direkt zum wechkopieren:\n!play https://www.youtube.com/watch?v=3aGf0t69_xk")

    # Does the Treppenwitz
    if message.content.lower().startswith(("!treppe")):
        theserver = client.guilds[0]
        mess = message.content.split()
        timeout = 0
        try:
            timeout = int(mess[-1])
        except (ValueError):
            timeout = 5
        
        if (timeout < 1) or (timeout > 10):
            timeout = 5

        try:
            member_to_move = " ".join(mess[1:-1]) # remove first and last param
            all_members = client.users
            member_obj = theserver.get_member_named(member_to_move)
            
            member_voice_chan = member_obj.voice.channel

            channels = theserver.voice_channels
            silence = None
            for channel in channels:
                if channel.name.startswith("Stille"):
                    silence = channel
                    break
                else:
                    pass

            msg = "Ab auf die Treppe mir dir, {}!".format(member_to_move)
            await message.channel.send(msg)
            await member_obj.move_to(silence, reason="Auszeit!")

            if timeout > 10:
                timeout = 10
            
            time.sleep(timeout)
            await member_obj.move_to(member_voice_chan)
        except (IndexError):
            msg = "Somethings wrong with your arguments. Try again! Syntax: !treppe <user> <seconds> or !hilfe"
            await message.channel.send(msg)
        except (AttributeError):
            msg = "Seems I didn't find the user. Try again! Syntax: !treppe <user> <seconds> or !hilfe"
            await message.channel.send(msg)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


client.run(secrets.TOKEN)