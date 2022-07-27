import os
import json

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context, Command

class Urls(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        self.urls_filepath = './assets/urls.json'
        if os.path.isfile(self.urls_filepath):
            with open(self.urls_filepath, encoding='utf8') as file:
                self.tasks_cache = json.load(file)
        else:
            self.tasks_cache = {
                    "urls": {
                        "twitter": [],
                        "discord": []
                    },
                    "settings": {}
                }
            with open(self.urls_filepath, 'w', encoding='utf8') as file:
                json.dump(self.tasks_cache, file, indent=4, ensure_ascii=False)
        with open('./config/const.json') as file:
            self.const = json.load(file)
        
        self.autoSaveData.start()
    
    @tasks.loop(minutes=30)
    async def autoSaveData(self) -> tasks.Loop:
        while (data:=await self.loadTasksFile()) != self.tasks_cache:
            with open(self.urls_filepath, 'w', encoding='utf8') as file:
                json.dump(self.tasks_cache, file, indent=4, ensure_ascii=False)
        self.tasks_cache = data
        print('>>> URLSYS: SUCCESS: task autoSaveData ok')

    @commands.command()
    async def addUrl(self, ctx: Context, url: str, group: str="default") -> Command:
        ...
        

def setup(bot):
    bot.add_cog(Urls(bot))