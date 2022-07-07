import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Command

import func

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        
    @property
    def embedColor(self):
        return 0x2F3136
    
    @commands.group()
    async def info(self, ctx: Context) -> commands.Group:
        pass
    
    @info.commmand()
    async def user(self, ctx: Context, user: discord.User) -> Command:
        ...
        
    @info.command()
    async def bot(self, ctx: Context) -> Command:
        embed = Embed(
            title = "Info from MangoBot",
            description = "",
            color = self.embedColor
        )
        for name, value in zip(("Ping", "Up time", "Memory", "Servers", "Users", "Commands", "CPU Usage", "Pycord", "Python"),
                               (func.round())):
            embed.add_field(name=name, value=value)

    @info.command()
    async def guild(self, ctx: Context) -> Command:
        ...
    
def setup(bot):
    bot.add_cog(Info(bot))