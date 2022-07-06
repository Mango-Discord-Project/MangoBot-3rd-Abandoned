import discord
from discord.ext import commands
from discord.ext.commands import Context

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
    
    @commands.command()
    async def showGuilds(self, ctx: Context):
        _guilds = self.bot.guilds
        
        guild_count = len(_guilds)
        total_members = sum(guild.member_count for guild in _guilds)
        total_members_without_repeat = 0
        guild_info = []
        _total_members_without_repeat_list = []
        for guild in _guilds:
            guild_info.append(f'{guild.name} - {guild.member_count}')
            for member in guild.members:
                if member.id not in _total_members_without_repeat_list:
                    total_members_without_repeat += 1
                    _total_members_without_repeat_list.append(member.id)
        del _total_members_without_repeat_list

        string = '\n'.join(guild_info)
        embed = discord.Embed(
            title = "Server List Of Bot",
            description = f"```{string}```",
            color = 0x2F3136
        )
        for name, value, inline in (('\u200b', '\u200b', True),
                                    ("Total Server Count", guild_count, True),
                                    ('\u200b', '\u200b', True),
                                    ("Total Member Count (Repeat)", total_members, True),
                                    ("Total Member Count (No Repeat)", total_members_without_repeat, True)):
            embed.add_field(name=name, value=value, inline=inline)
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Main(bot))