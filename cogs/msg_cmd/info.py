import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Command

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        
    def embedGenerator(title=Embed.Empty, description=Embed.Empty, color=0x2F3136):
        return Embed(title=title, description=description, color=color)
    
    @commands.group()
    async def info(self, ctx: Context) -> commands.Group:
        pass
    
    @info.commmand()
    async def user(self, ctx: Context, user: discord.User) -> Command:
        embed = self.embedGenerator(
            title = "User Profile"
            )
        
    @info.command()
    async def bot(self, ctx: Context) -> Command:
        
    
def setup(bot):
    bot.add_cog(Info(bot))