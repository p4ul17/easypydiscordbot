# bot.py
import os
import random
import discord
import asyncio
prefix = "+" #change the "+" to change the prefix of the bot, e.g. +help --> !help 
amount = 1

from discord.ext import commands

client = commands.Bot(prefix)


@client.event
async def on_ready():
    print('We are logged in as User {}'.format(client.user.name))
    await client.change_presence(activity=discord.Game('JackBOT  +help'), status=discord.Status.online)#change 'JackBOT +help' to change the custom status of the bot

@client.command(brief="Prints a Pasta.")
async def pasta(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('This was a Copy-Pasta!')
    
@client.command(brief="Pings the Bot to test Latency.")
async def ping(ctx):
    await ctx.send(f'Ping hat {round(client.latency * 1000)}ms gedauert')

@client.command(aliases=['8ball', 'testif', 'test', 'eightball'],brief="Calls the 8ball to question it.")
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is definetly so.',
                 'Without a doubt',
                 'Yes - definetly.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Looks fine.',
                 'Yes',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better you dont know it.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no',
                 'Very doubtful.',
                 'Absolutely NO',
                 'NOPE']
    await ctx.send(f'Your Question: {question}\nMy Answer: {random.choice(responses)}')

@client.command(brief="Flips a Coin .")
async def flip(ctx):
    flip = [
        (
            'Head '
             
        ),
        (
            'Tails '
             
        ),
        
    ]

    response = random.choice(flip)
    await ctx.send(response)

@client.command(brief="Prints GGs (Person) .")

async def gg(ctx, *, ggpers="<@329307122867240982> coding this bot!"):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'GGs {ggpers}!')
    
@client.command(brief="Prints the thing you write .")
async def say(ctx, *, input):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{input}')
    
@client.command(brief="Clears the Amount of Messages you write . \u0022Admin\u0022 only")
@commands.has_role('Admin')
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    
@client.command(brief="Sends a Vid of a Cat Vibing.")
async def vibe(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/816017303572709477/816684747292016660/My_Video7.mp4')
    

@client.command()
async def timer(ctx, *,timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        if time >= 3600:
            message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
        elif time >= 60:
            message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
        elif time < 60:
            message = await ctx.send(f"Timer: {time} seconds")
        while True:
            try:
                await asyncio.sleep(1)
                time -= 1
                if time >= 3600:
                    await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                elif time >= 60:
                    await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
                elif time < 60:
                    await message.edit(content=f"Timer: {time} seconds")
                if time <= 0:
                    await message.edit(content="Ended!")
                    await ctx.send(f"{ctx.author.mention} Your Timer Has ended!")
                    await message.delete()
                    break
            except:
                break
    except:
        await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")
        
@client.command(brief="Blames the User you Tag")
async def blame(ctx, *, content):
    await ctx.send(content + ' is a Shame for this Server. He/She should not Exist!')

client.run('YOURTOKEN') #type in your bot token here

