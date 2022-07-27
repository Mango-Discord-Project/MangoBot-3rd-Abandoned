import discord
from discord.ext import commands
from discord.ext.commands import Context, Command
import pretty_errors
import rich

import func

class Foo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot

def setup(bot):
    bot.add_cog(Foo(bot))