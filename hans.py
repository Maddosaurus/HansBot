#!/usr/bin/env python3

import time

import discord

from util import gifclient, utils
from util.settings import SETTINGS


client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {} with ID {}".format(client.user.name, client.user.id))
    print("------")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.lower().startswith(("!hilfe")):
        print("Printing some help!")
        msg = "commands:\n!hilfe - for some help\n!wochenende - a handy link copy for the weekend video!\n!treppe <user> <seconds> - Move someone to Stille Treppe\nSay 'Hans' in chat to get a Flammenwerfer"
        await message.channel.send(msg)

    if message.content.lower().startswith(("hans")):
        print("Posting a Flamethrower GIF!")
        msg = "*reicht {0.author.mention} den Flammenwerfer* \n{1}".format(message, gifclient.searchme("flamethrower"))
        await message.channel.send(msg)
    
    if any(client.user.name in s.name for s in message.mentions):
        msg = "Sie haben gerufen?"
        await message.channel.send(msg)

    if message.content.startswith(("!Wochenende", "!wochenende")):
        print("Giving a hint where to find the Wochenende")
        await message.channel.send("Direkt zum wechkopieren:\n!play https://www.youtube.com/watch?v=3aGf0t69_xk")

    # Does the Treppenwitz
    if message.content.lower().startswith(("!treppe")):
        theserver = client.guilds[0]
        mess = message.content.split()
        timeout = utils.safely_calc_timeout(mess[-1])

        try:
            member_to_move = " ".join(mess[1:-1]) # remove first and last param
            if message.mentions:
                member_obj = message.mentions[0]
            else:
                member_obj = theserver.get_member_named(member_to_move)

            member_voice_chan = member_obj.voice.channel

            silence = utils.find_target_room(
                SETTINGS.target_voice_room,
                theserver.voice_channels
            )

            print("Moving {} to {} for {} seconds".format(member_to_move, SETTINGS.target_voice_room, timeout))
            msg = "Ab auf die Treppe mir dir, {}!".format(member_to_move)
            await message.channel.send(msg)
            await member_obj.move_to(silence, reason="Auszeit!")

            time.sleep(timeout)
            await member_obj.move_to(member_voice_chan)
        except (IndexError):
            msg = "Somethings wrong with your arguments. Try again! Syntax: !treppe <user> <seconds> or !hilfe"
            await message.channel.send(msg)
        except (AttributeError):
            msg = "Seems I didn't find the user. Try again! Syntax: !treppe <user> <seconds> or !hilfe"
            await message.channel.send(msg)


try:
    client.run(SETTINGS.discord_bot_token)
except discord.errors.LoginFailure:
    print("Could not log in - is the Discord bot token set right?")