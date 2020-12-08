import discord
from discord.ext import commands
import os
from discord.utils import get


client = discord.Client()

DISCORD_TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix="#") #PREFIX FOR BOT

@client.event
async def on_ready():
    print('BOT ACTIVATED')

#MAKE BOT JOIN VC
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


#MUTE EVERYBODY IN VC
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

#UNMUTE EVERYBODY IN VC
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

#CHANGE NICKNAME TO MENTIONED USER
@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command()
async def sheminde(ctx):
    await ctx.send("iphone 12 pro max miyide da shedebuligaq")


bot.run("TOKEN")
