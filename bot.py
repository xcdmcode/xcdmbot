import discord
from discord.ext import commands
from config import config
import sys, traceback
from os import listdir
from os.path import isfile, join
import requests

bot = commands.Bot(command_prefix=config['command_prefix'])

extensions = ['cogs.media', 'cogs.events', 'cogs.stuff', 'cogs.text']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(config['discord_token'])