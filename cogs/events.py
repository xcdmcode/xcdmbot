import discord
from discord.ext import commands

class EventsCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\nBot Online and logged in as: {self.bot.user.name}.")

        await self.bot.change_presence(activity=discord.Game(name='Mount & Blade II: Bannerlord'))

def setup(bot):
    bot.add_cog(EventsCog(bot))