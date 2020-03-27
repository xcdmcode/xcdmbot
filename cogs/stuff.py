import discord
from discord import Colour, Embed
from discord.ext import commands
import re

class StuffCog(commands.Cog, name="Random Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ao')
    async def sneed(self, ctx):
        await ctx.send("sneed")

    @commands.command(name='juan', aliases=['simp'])
    async def juan(self, ctx):
        embed = Embed(
            type = "rich",
            colour = Colour.blue()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/160802211742482433/692784652297044058/LMAO.png")
        embed.set_footer(text="COPERIGHTED. ALL RIGHTS RESERVED. PROTECTED BY INTERNATIONAL SEETHINGS.")
        await ctx.send(None, embed=embed)

    @commands.command(name='alerta', aliases=['macaco'])
    async def alerta(self, ctx):
        await ctx.send(":monkey: :rotating_light: :monkey: :warning: **ALERTA DE MACACO** :warning: :monkey: :rotating_light: :monkey:\nhttps://files.catbox.moe/09e6gr.mp4")

    @commands.command(name='e')
    async def large_emoji(self, ctx, arg):
        embed = Embed()      
        for e in ctx.guild.emojis:
            if e.name == re.search(r":.*:", arg)[0].replace(':', ''):
                embed.set_image(url=e.url)

        await ctx.send(None, embed=embed)

def setup(bot):
    bot.add_cog(StuffCog(bot))