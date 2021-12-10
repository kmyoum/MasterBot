import discord
import random
import os
from discord.ext import commands

master = commands.Bot(command_prefix='.')

"""
@master.event
async def on_ready():
    print("Bot is ready!")
"""

"""
# prints out your latency
# added pong as another command syntax
# (.ping = .pong) both works
@master.command(aliases=['pong'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(master.latency * 1000)}ms')

"""


# clear command
# clears amount(preset value) of lines including clear command 
@master.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


"""
# kick command
# (member:discord.Member) read the member as the member object
# added reasons for kick
@master.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
"""

"""
# ban command/method
# added reasons for ban
@master.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

# unban command
# added reasons for unban
@master.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#') # to match discord name and number and add spaces
    # only returns if username and discriminator is equal to its banned member's name and discriminator
    # otherwise returns error
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# prints out if the member has joined or left the server
"""

"""
@master.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    

@master.event
async def on_member_remove(member):
    print(f'{member} has left the server')
"""


# loads the extension
@master.command()
async def load(ctx, extension):
    master.load_extension(f'cogs.{extension}')

# unloads the extension
@master.command()
async def unload(ctx, extension):
    master.unload_extension(f'cogs.{extension}')

# reload the extension    
@master.command()
async def reload(ctx, extension):
    master.unload_extension(f'cogs.{extension}')
    master.load.extension(f'cogs.{extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        master.load_extension(f'cogs.{filename[:-3]}') # cuts off last 3 strings to represent cogs.example not cogs.example.py




master.run('OTE4Mjg1OTg1NzQ0MzAyMTAx.YbFCdw.6XqYiY1_ttH_aV2M8tmO82ABYKo')
