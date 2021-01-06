import discord
from discord.ext import commands
import os
from discord.utils import get
import random

client = discord.Client()

DISCORD_TOKEN = os.getenv("NzU5MDg0ODE1OTM2MTI3MDE2.X24W0w.EiuI4wVfn812nNSjooDblH26gw8")


bot = commands.Bot(command_prefix="#") #PREFIX FOR BOT

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
async def penis(ctx):
    count = random.randint(1, 15)
    count_king = random.randint(15, 20)
    count_sandro = random.randint(1, 4)
    size = '=' * count
    size_king = '=' * count_king
    size_sandro = '=' * count_sandro
    if ctx.author.id == 271350836179763201:
        await ctx.send(f'hi king! this is your dick -> 8{size_king}D')
    elif ctx.author.id == 517551037977067520:
        await ctx.send(f'hi sandro! this is your dick -> 8{size_sandro}D')
    elif ctx.author.id == 790881474298642482:
        await ctx.send('girl error')
    elif ctx.author.id == 370255524966563853:
        await ctx.send('girl error')
    elif ctx.author.id == 760938532927176706:
        await ctx.send('girl error')
    else:
        await ctx.send(f'hi! this is your dick -> 8{size}D')
    


@bot.command()
async def howgay(ctx):
    count = random.randint(0, 100)
    count_sandro = random.randint(120, 150)
    count_king = random.randint(0, 9)
    if ctx.author.id == 517551037977067520:
        await ctx.send(f'sandro you are {count_sandro}% gay')
    elif ctx.author.id == 271350836179763201:
        await ctx.send(f'hi king you are {count_king}% gay')
    else:
        await ctx.send(f'hi king you are {count}% gay')
bot.run("NzU5MDg0ODE1OTM2MTI3MDE2.X24W0w.EiuI4wVfn812nNSjooDblH26gw8")
