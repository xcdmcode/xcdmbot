import discord
from discord import Colour, Embed
from discord.ext import commands
import requests
from config import config

class MediaCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='yt')
    async def youtube_search(self, ctx, *args):
        vid_search_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=1&q={}&key={}"
        response = requests.get(vid_search_url.format(args, config['youtube_token'])).json()
        videoId = response['items'][0]['id']['videoId']

        await ctx.send(f"https://www.youtube.com/watch?v={videoId}")

    @commands.command(name='lewd')
    async def danbooru_search(self, ctx, *args):
        danbooru_api = "http://danbooru.donmai.us/posts.json?limit=1&random=true&tags={}"
        login = config['danbooru_login']
        token = config['danbooru_token']
        tags = " ".join(args)
        response = requests.get(danbooru_api.format(tags), auth=(login, token)).json()
        lewd = None
        try:
            if args:
                post = response[0]['file_url']
                if (post == None):
                    post = response[0]['source']
                lewd = {'post': post, 'id': response[0]['id'], 'artist': response[0]['tag_string_artist']}
        except:
            await ctx.send("No images found, or incorrect query structure. Tags are limited to 2 and space delimited. Example: !lewd huge_breasts muscular_female")

        post_url = "http://danbooru.donmai.us/posts/{}"

        embed = Embed(
            title = f"http://danbooru.donmai.us/posts/{lewd['id']}",
            type = "rich",
            colour = Colour.magenta()
        )
        embed.set_image(url=lewd['post'])
        embed.set_footer(text=f"Artist: {lewd['artist'].replace('_', ' ').title()}")
        
        if ctx.channel.is_nsfw():
            await ctx.send(None, embed=embed)
        else:
            await ctx.send("Try again in a NSFW channel, retard.")

def setup(bot):
    bot.add_cog(MediaCog(bot))