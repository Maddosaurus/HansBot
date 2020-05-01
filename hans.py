#!/usr/bin/env python3

import asyncio
import time

import discord

from util import gifclient, utils
from util.settings import SETTINGS


client = discord.Client()
msgs = []


@client.event
async def on_ready():
    print("Logged in as {} with ID {}".format(client.user.name, client.user.id))
    print("------")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself,
	# however we do need to add its own messages
	# to the list of messages to delete when the
	# cleanup command is used.
    if message.author == client.user:
		# Excluding flamethrower gifs from the purge
        if not message.content.startswith("*reicht"):
            msgs.append(message)


    if message.content.lower().startswith(("!hilfe")):
        msgs.append(message)
        print("Printing some help!")
        msg = "commands:\n!hilfe - for some help\n!wochenende - a handy link copy for the weekend video!\n!treppe <user> <seconds> - Move someone to Stille Treppe\nSay 'Hans' in chat to get a Flammenwerfer"
        await message.channel.send(msg)


    if message.content.lower().startswith(("hans")):
        msgs.append(message)
        print("Posting a Flamethrower GIF!")
        msg = "*reicht {0.author.mention} den Flammenwerfer* \n{1}".format(message, gifclient.searchme("flamethrower"))
        await message.channel.send(msg)

    if any(client.user.name in s.name for s in message.mentions):
        msgs.append(message)
        msg = "Sie haben gerufen?"
        await message.channel.send(msg)

    if message.content.startswith(("!Wochenende", "!wochenende")):
        msgs.append(message)
        print("Giving a hint where to find the Wochenende")
        await message.channel.send("Direkt zum wechkopieren:\n!play https://www.youtube.com/watch?v=3aGf0t69_xk")

    # Does the Treppenwitz
    if message.content.lower().startswith(("!treppe")):
        msgs.append(message)
        theserver = client.guilds[0]
        mess = message.content.split()
        if len(mess) < 3:
            msg = "Somethings wrong with your arguments. Try again! Syntax: !treppe <user> <seconds> or !hilfe"
            await message.channel.send(msg)
        else:
            timeout, shenanigans = utils.safely_calc_timeout(mess[-1])

            try:
                member_to_move = " ".join(mess[1:-1]) # remove first and last param
                if shenanigans:
                    member_obj = message.author
                elif message.mentions:
                    member_obj = message.mentions[0]
                else:
                    member_obj = utils.find_member(theserver, member_to_move)

                member_voice_chan = member_obj.voice.channel

                silence = utils.find_target_room(
                    SETTINGS.target_voice_room,
                    theserver.voice_channels
                )

                if shenanigans:
                    print("Moving {} to {} for {} seconds for Bot-shenanigans".format(member_obj, SETTINGS.target_voice_room, timeout))
                    msg = "Keine Spielchen mit dem Bot, {}!".format(member_obj.mention)
                else:
                    print("Moving {} to {} for {} seconds. {} asked for it.".format(member_obj, SETTINGS.target_voice_room, timeout, message.author))
                    msg = None

                if msg is not None:
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


    if message.content.lower().startswith(("!meeting")):
        theserver = client.guilds[0]
        mess = message.content.split()

        if message.mentions:
            member_obj = message.mentions[0]
        else:
            member_to_move = " ".join(mess[1:]) # remove first param
            member_obj = utils.find_member(theserver, member_to_move)

        member_voice_chan = member_obj.voice.channel

        target_room = utils.find_target_room(
            "Meeting/Wutwandern",
            theserver.voice_channels
        )
        print("Moving {} to {} for meetings. {} asked for it".format(member_obj, target_room, message.author))

        await member_obj.move_to(target_room, reason="Meeting")
        time.sleep(1)
        await message.delete() # remove the triggering user message


    if message.content.lower() == "!cleanup":
        # Making sure the person executing the command has the permission to
        # delete messages.
        if message.author.guild_permissions.manage_messages:
            print("Deleting all my messages and summons.")
            msgs.append(message)
            for msg in msgs:
                try:
                    await msg.delete()
                except(discord.errors.NotFound):
                    print("Skipping unknown message. Probably deleted by user.")
            msgs.clear()
        else:
            msg = "You're not allowed to delete messages!"
            await message.channel.send(msg)
try:
    client.run(SETTINGS.discord_bot_token)
except discord.errors.LoginFailure:
    print("Could not log in - is the Discord bot token set right?")
