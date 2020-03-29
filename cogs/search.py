import discord
from discord import Colour, Embed
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import json
import re


# Scrapes the DDG search results page and returns a list of 5 tuples containing a result's title and url.
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

# Returns the first image from a DDG image search
def ddg_image_search(args):
    url = "https://duckduckgo.com/"

    vqd_params = { 'q': "+".join(args) }
    res = requests.post(url, data=vqd_params)
    search_obj = re.search(r'vqd=([\d-]+)&', res.text, re.M | re.I)
    vqd = search_obj.group(1) # 'vqd' is a special token necessary when requesting images via DDG

    headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'en-GB,en-US q=0.8,en q=0.6,ms q=0.4',
        'user-agent': 'Mozilla/5.0 (X11  Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'accept': 'application/json, text/javascript, */*  q=0.01',
        'referer': 'https://duckduckgo.com/',
        'authority': 'duckduckgo.com',
    }
    params = {
        'l': 'wt-wt',
        'o': 'json',
        'q': "+".join(args),
        'vqd': vqd,
        'f': ',,,',
        'p': '2'
    }

    requests_url = url + "i.js"
    res = requests.get(requests_url, headers=headers, params=params)
    data = json.loads(res.content)
    image_url = data["results"][0]['image']

    return image_url


class SearchCog(commands.Cog, name="Search Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search', aliases=['s', 'ddg', 'google'], help="Queries DuckDuckGo and returns the top 5 results")
    async def search(self, ctx, *args):
        async with ctx.typing():
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

    @commands.command(name='image', aliases=['i', 'img'], help="Queries DuckDuckGo and returns the first image result")
    async def image_search(self, ctx, *args):
        try:
            async with ctx.typing():
                result = ddg_image_search(args)
                embed = Embed(
                    type = "rich",
                    colour = Colour.from_rgb(200, 200, 200)
                )

                embed.set_image(url=result)
            await ctx.send(None, embed=embed)
        except Exception as e:
            await ctx.send(repr(e))

def setup(bot):
    bot.add_cog(SearchCog(bot))