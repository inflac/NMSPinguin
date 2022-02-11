from asyncio import wait_for
import asyncio
from asyncio.windows_events import NULL
from importlib.metadata import files
from logging import NullHandler
from pyexpat.errors import messages
import discord
import apifun as apifun
from secret import token as TOKEN


class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt Beep Boop")
    
    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return
    #Inzidenz
        if message.content.lower() == "!corona":
            update = apifun.corona_update(apifun.corona_updater())
            await message.channel.send(update.get_corona_update())

    #Jokes
        if message.content.lower() == "!joke":
            joke = apifun.joker(apifun.get_new_joke())
            if joke.get_joke_type() == "single":
                await message.channel.send(joke.get_single())
            else:
                await message.channel.send(joke.get_setup())
                await message.channel.send(joke.get_delivery())

    #CatFact
        if message.content.lower() == "!catfact":
            await message.channel.send(apifun.get_new_catfact())

    #MathFact
        if message.content.lower() == "!mathfact":
            await message.channel.send(apifun.get_new_mathfact())

    #Nasapic
        if message.content.lower() == "!nasa":
            await message.channel.send(apifun.get_new_nasapic())

    #Dogpic
        if message.content.lower() == "!dog":
            await message.channel.send(apifun.get_new_dogpic())
        #Dogbomb
        if message.content.lower() == "!dogbomb":
            for i in range(5):
                await message.channel.send(apifun.get_new_dogpic())

    #Dogpic
        if message.content.lower() == "!cat":
            await message.channel.send(apifun.get_new_catpic())
        #Dogbomb
        if message.content.lower() == "!catbomb":
            for i in range(5):
                await message.channel.send(apifun.get_new_catpic())

    #ChucknorisFact
        if message.content.lower() == "!chuckfact":
            await message.channel.send(apifun.get_new_chuckfact())

    #Ageguesser

client = MyClient()
# @client.event
# async def on_message(message):
#     if message.content.lower() == "!age":
#         channel = message.channel
#         await channel.send('Schreib mir einen Namen und ich sage dir wie alt er klingt')

#         def check(m):
#             return m.author == message.author and m.channel == channel

#         msg = await client.wait_for('message', check=check)
#         await channel.send("Der Name " + str(msg.content) + " klingt für mich als wärst du " + get_age(msg.content) + " Jahre alt.")

client.run(TOKEN)
