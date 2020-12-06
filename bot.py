import discord 
from discord.ext import commands
import os
from discord.utils import get


client = discord.Client()

DISCORD_TOKEN = os.getenv("TOKENGOESHERE")


bot = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('BOT ACTIVATED')

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command()
async def disconnect(ctx):
    channel = ctx.message.author.voice.channel
    await channel.disconnect()



@bot.command() 
@commands.has_permissions(administrator=True)
async def mute(ctx):
        voice_client = ctx.guild.voice_client 
        if not voice_client: 
            return  
        channel = voice_client.channel 
        people = channel.members 
        for person in people: 
            if person == client.user: 
                continue
            await person.edit(mute=True, reason="{} told me to mute everyone in this channel".format(ctx.author))
        

@bot.command() 
@commands.has_permissions(administrator=True)
async def unmute(ctx):
        voice_client = ctx.guild.voice_client
        if not voice_client:  
            return
        channel = voice_client.channel 
        people = channel.members 
        for person in people: 
            if person == client.user: 
                continue
            await person.edit(mute=False, reason="{} told me to mute everyone in this channel".format(ctx.author))



bot.run("TOKENGOESHERE") 
