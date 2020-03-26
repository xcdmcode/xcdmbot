import discord
from discord import Colour, Embed
from discord.ext import commands

class StuffCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ao')
    async def sneed(self, ctx):
        await ctx.send("sneed")

    @commands.command(name='juan', aliases=['simp'])
    async def juan(self, ctx):
        embed = Embed()
        embed.type = "rich"
        embed.colour = Colour.blue()
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/160802211742482433/692784652297044058/LMAO.png"
        )
        embed.set_footer(
            text="COPERIGHTED. ALL RIGHTS RESERVED"
        )
        await ctx.send(None, embed=embed)

def setup(bot):
    bot.add_cog(StuffCog(bot))