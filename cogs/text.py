import discord
from discord import Colour, Embed
from discord.ext import commands
import re
import random

def replacement_func(match, repl_pattern):
    match_str = match.group(0)
    repl = ''.join([r_char if m_char.islower() else r_char.upper()
                for r_char, m_char in zip(repl_pattern, match_str)])
    repl += repl_pattern[len(match_str):]
    return repl

class TextCog(commands.Cog, name="Text Manipulation Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ebin', aliases=['spurd', ':D', ':DD', ':DDD'])
    async def ebin(self, ctx, *args):
        bicd = {
            "epic":"ebin",
            "penis":"benis","wh":"w","th":"d","af":"ab","ap":"ab","ca":"ga","ck":"gg","co":"go",
            "ev":"eb","ex":"egz","et":"ed","iv":"ib","it":"id","ke":"ge","op":"ob","ot":"od",
            "po":"bo","pe":"be","pi":"bi","up":"ub","va":"ba","cr":"gr","kn":"gn","lt":"ld",
            "mm":"m", "nt":"dn","pr":"br","tr":"dr","bs":"bz","ds":"dz","fs":"fz","gs":"gz",
            "is":"iz","ls":"lz","ms":"mz","ns":"nz","rs":"rz","ss":"sz","ts":"tz","us":"uz",
            "ws":"wz","ys":"yz","alk":"olk","ing":"ign","ic":"ig","ng":"nk","kek":"geg","some":"sum",
            "meme":"maymay"
        }
        ebinFaces = [ ':D', ':DD', ':DDD', ':-D', 'XD', 'XXD', 'XDD', 'XXDD' ]
        new_args = " ".join(args)
        for k, v in bicd.items():
                new_args = re.sub(k, lambda k: replacement_func(k,v), new_args, flags=re.I)
        ebinText = new_args+" "+ random.choice(ebinFaces)
        await ctx.send(ebinText)

def setup(bot):
    bot.add_cog(TextCog(bot))