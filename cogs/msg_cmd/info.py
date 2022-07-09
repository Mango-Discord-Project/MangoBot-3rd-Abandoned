import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Command

import json

import func

with open('./config/const.json') as file:
    const = json.load(file)

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
    
    @info.command()
    async def user(self, ctx: Context, user: discord.User) -> Command:
        ...
        
    @info.command()
    async def bot(self, ctx: Context) -> Command:
        # embed = Embed(
        #     title = "Info from MangoBot",
        #     description = "",
        #     color = self.embedColor
        # )
        # for name, value in zip(("Ping", "Up time", "Memory", "Servers", "Users", "Commands", "CPU Usage", "Pycord", "Python"),
        #                        (f'`{func.round(self.bot.latency*1000)}`', f'<>')):
        #     embed.add_field(name=name, value=value)
        ...

    @info.command()
    async def guild(self, ctx: Context) -> Command:
        ...
    
def setup(bot):
    bot.add_cog(Info(bot))