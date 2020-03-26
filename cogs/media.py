import discord
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

def setup(bot):
    bot.add_cog(MediaCog(bot))