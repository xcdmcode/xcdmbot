import discord
from discord import Colour, Embed
from discord.ext import commands
import requests
from config import config

class MediaCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='yt')
    async def youtube_search(self, ctx, args):
        vid_search_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=1&q={}&key={}"
        response = requests.get(vid_search_url.format(args, config['youtube_token'])).json()
        videoId = response['items'][0]['id']['videoId']

        await ctx.send(f"https://www.youtube.com/watch?v={videoId}")

    @commands.command(name='lewd')
    async def danbooru_search(self, ctx, args):
        danbooru_api = "http://danbooru.donmai.us/posts.json?limit=1&random=true&tags={}"
        login = config['danbooru_login']
        token = config['danbooru_token']

        response = requests.get(danbooru_api.format(args), auth=(login, token)).json()
        lewd = None
        try:
            if args:
                post = response[0]['file_url']
                if (post == None):
                    post = response[0]['source']
                lewd = {'post': post, 'id': response[0]['id']}
        except:
            await ctx.send("No images found, or incorrect query structure.")

        post_url = "http://danbooru.donmai.us/posts/{}"

        embed = Embed()
        embed.type = "rich"
        embed.colour = Colour.magenta()
        embed.set_image(
            url=lewd['post']
        )
        embed.set_footer(
            text=post_url.format(lewd['id'])
        )
        
        await ctx.send(None, embed=embed)

def setup(bot):
    bot.add_cog(MediaCog(bot))