import random
from random import choice, choices
import json
import regex as re

import discord
from discord.ext import commands
from discord.ext.commands import Context, Command
import pretty_errors
import rich

import func

class Game(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        
        with open("./config/const.json", encoding="utf8") as file:
            self.const: dict = json.load(file)
        self.sp_values = self.const["superpowers"]
    
    @commands.command()
    async def superpowers(self, ctx: Context) -> Command:
        sp = [choice(self.sp_values["self"]), choice(self.sp_values["cost"])]
        for index, value in enumerate(sp):
            if "{" in value:
                
                sp[index] = 

def setup(bot: commands.Bot):
    bot.add_cog(Game(bot))