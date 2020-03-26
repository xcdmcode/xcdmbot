import discord
from discord.ext import commands

class StuffCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ao')
    async def sneed(self, ctx):
        await ctx.send("sneed")

def setup(bot):
    bot.add_cog(StuffCog(bot))