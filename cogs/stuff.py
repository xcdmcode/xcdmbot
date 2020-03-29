import discord
from discord import Colour, Embed
from discord.ext import commands
import re
from datetime import datetime, timedelta, timezone

class StuffCog(commands.Cog, name="Random Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ao', help="Sneed")
    async def sneed(self, ctx):
        await ctx.send("sneed")

    @commands.command(name='juan', aliases=['simp'], help="Juan moment")
    async def juan(self, ctx):
        embed = Embed(
            type = "rich",
            colour = Colour.blue()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/160802211742482433/692784652297044058/LMAO.png")
        embed.set_footer(text="COPERIGHTED. ALL RIGHTS RESERVED. PROTECTED BY INTERNATIONAL SEETHINGS.")
        await ctx.send(None, embed=embed)

    
    @commands.command(name='pizza', aliases=['pizza_machowave'], help="Pizza moment")
    async def pizza(self, ctx):
        embed = Embed(
            type = "rich",
            colour = Colour.green()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/692486367422447649/693246228238172170/pizza.jpg")
        await ctx.send(None, embed=embed)

    @commands.command(name='alerta', aliases=['macaco'], help="Alerta de Macaco")
    async def alerta(self, ctx):
        await ctx.send(":monkey: :rotating_light: :monkey: :warning: **ALERTA DE MACACO** :warning: :monkey: :rotating_light: :monkey:\nhttps://files.catbox.moe/09e6gr.mp4")

    @commands.command(name='e', help="Returns the enlarged version of a server emoji")
    async def large_emoji(self, ctx, arg):
        embed = Embed()
        emoji = None
        match = re.search(r":.*:", arg)
        if bool(match):
            for e in ctx.guild.emojis:
                if e.name == match[0].replace(':', ''):
                    emoji = e

        if emoji != None:
            embed.set_image(url=emoji.url)
            await ctx.send(None, embed=embed)
        else:
            await ctx.send(f"\"{arg}\" is invalid. The command only works for this server's emoji.")

    @commands.command(name='bannerlord', help="Countdown to Bannerlord release date")
    async def bannerlord(self, ctx):
        release_date = datetime(2020, 3, 30, 10, 0, 0, 0) - datetime.utcnow()

        days =  release_date.days
        hours = release_date.seconds // 3600
        minutes = (release_date.seconds // 60) % 60
        seconds = release_date.seconds % 60
        
        days_s =  f"{release_date.days} day(s), " if release_date.days > 0 else ""
        hours_s = f"{release_date.seconds // 3600} hour(s), " if hours > 0 else ""
        minutes_s = f"{(release_date.seconds // 60) % 60} minute(s) and " if minutes > 0 else ""
        seconds_s = f"{release_date.seconds % 60} second(s)"

        if release_date <= timedelta(0):
            await ctx.send(f"Bannerlord has been released! <:soypepe:432601353148301323>\nhttps://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/")
        else:
            await ctx.send(f"Only **__{days_s}{hours_s}{minutes_s}{seconds_s}__** left before Bannerlord is released! <:soypepe:432601353148301323>")
    
    
    @commands.command(name='version', help="Returns the bot version")
    async def version(self, ctx):
        await ctx.send("0.0.1")

def setup(bot):
    bot.add_cog(StuffCog(bot))