import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, master):
        self.master = master

    # Events
    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


def setup(master):
    master.add_cog(Test(master))
