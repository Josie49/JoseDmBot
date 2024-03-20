import discord
import os

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("hi"):
        await message.channel.send("hewwo")

    if "69" in message.content:
        await message.channel.send("nice")

async def on_message_edit(before, after):
    if before.author == client.user:
        return
    else:
        await before.channel.sent("I saw that " + before.author + ".\n You said: " + before.content)

client.run(os.environ["BOT_TOKEN_JOSE"])