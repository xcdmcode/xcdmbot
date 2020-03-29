import discord
from discord import Colour, Embed
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time
import textwrap


# Scrapes the DuckDuckGo search results page and returns a list of 5 tuples containing a result's title and url.
def ddg_search(args):
    ddg_search_url = "https://duckduckgo.com/html/?q={}"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/74.00'}

    page = requests.get(ddg_search_url.format("+".join(args)), headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.findAll('a', {'class': 'result__a'})
    results = []
    for link in links[:5]:
        link_href = link.get('href')
        if link_href != None:
                results.append((link.text, link_href))
    return results

class SearchCog(commands.Cog, name="Search Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search', aliases=['s', 'ddg', 'google'])
    async def ddg_search(self, ctx, *args):
        async with ctx.typing():
            search_start = time.time()
            results = ddg_search(args)
            query = " ".join(args)
            embed = Embed(
                type = "rich",
                colour = Colour.from_rgb(200, 200, 200)
            )
            embed.set_author(
                name=f"Search results for \"{query}\":",
                url="https://duckduckgo.com/?q=" + query.replace(' ', '+'),
                icon_url="https://cdn.discordapp.com/attachments/692486367422447649/693681247385419786/ddg_icon.png"
            )
            for result in results:
                embed.add_field(name=result[0], value=result[1], inline=False)
            embed.set_footer(text="Search provided by DuckDuckGo.")
        await ctx.send(None, embed=embed)

def setup(bot):
    bot.add_cog(SearchCog(bot))