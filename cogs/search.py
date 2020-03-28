import discord
from discord import Colour, Embed
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time

def google_search(args):
    google_search_url = "https://www.google.com/search?q={}&num=5"

    params = {'safe': 'off', 'lr': 'lang_en', 'hl': 'en'}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/74.00'}

    page = requests.get(google_search_url.format("+".join(args)), params=params, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    results = []
    for link in links:
        link_href = link.get('href')
        if link_href != None:
            if "google.com" not in link_href and "webcache" not in link_href and link_href.startswith("http") and len(link.contents) > 1:
                results.append((link.contents[1].text, link_href))
    return results[:5]

class SearchCog(commands.Cog, name="Search Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google')
    async def google_search(self, ctx, *args):
        async with ctx.typing():
            search_start = time.time()
            results = google_search(args)
            query = " ".join(args)
            embed = Embed(
                type = "rich",
                colour = Colour.blue()
            )
            embed.set_author(
                name=f"Google search results for \"{query}\":",
                url=f"https://www.google.com/search?q={query}",
                icon_url="https://cdn.discordapp.com/attachments/692486367422447649/693347077115084830/google_icon.png"
            )
            for result in results:
                embed.add_field(name=result[0], value=result[1], inline=False)
            embed.set_footer(text=f"search took {round((time.time() - search_start))} seconds.")
        await ctx.send(None, embed=embed)

def setup(bot):
    bot.add_cog(SearchCog(bot))