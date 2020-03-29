import discord
from discord.ext import commands
import re

agentorange_id = 160924540417867776

class EventsCog(commands.Cog, name="Media Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\nBot Online and logged in as: {self.bot.user.name}.")

        await self.bot.change_presence(activity=discord.Game(name='Mount & Blade II: Bannerlord'))

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.author.id == agentorange_id and contains(message.content, "sneed"):
                await message.channel.send("sneed")
           
            # cmd_context = await self.bot.get_context(message);
            # if not cmd_context.valid:  
            #     #message is not a command

            #     msg_list = message.content.lower().split(' ')
            #     if len(msg_list) > 1 and "big" in msg_list:
            #         await message.channel.send("for you")

def contains(text, regex):
    return bool(re.search(regex, text.lower()))

def setup(bot):
    bot.add_cog(EventsCog(bot))
