import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, master):
        self.master = master

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')


    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(master):
    master.add_cog(Example(master))