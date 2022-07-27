import os
import json
import time
import dotenv

import discord
from discord.ext import commands
from discord.ext.commands import Command

import func

dotenv.load_dotenv()

with open('./config/const.json') as rf:
    data = json.load(rf)
    data['up_time'] = func.round(time.time())

with open('./config/const.json', 'w') as wf:
    json.dump(data, wf, indent=4, ensure_ascii=False, sort_keys=True)
    
class MyBot(commands.Bot):
    def __init__(self, command_prefix="mb.", intents=discord.Intents.all()) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)
        self._add_command()
        
    @property
    def unpreload(self):
        return set()

    async def on_ready(self):
        print(f"Python >> Bot is Ready, Login: {self.user}")
        for dir_cog in os.listdir("./cogs"):
            for cog in os.listdir(f"./cogs/{dir_cog}"):
                if cog.endswith(".py") and cog not in self.unpreload:
                    self.load_extension(f"cogs.{dir_cog}.{cog.removesuffix('.py')}")
                    print(f">>> Load Cog: cogs.{dir_cog}.{cog.removeprefix('.py')}")
    
    def _add_command(self):
        @self.command()
        async def cogs(ctx:commands.Context, cog_name:str, mode:str="load") -> Command:
            # if not os.path.isfile(f"{cog_name.replace('.py', '')}.py"):
            #     return await ctx.send(f"> ERROR: cog {cog_name} is not found")
            path = cog_name.removesuffix(".py").replace("/", ".").replace("\\", ".")
            match mode.lower():
                case "load" | "l":
                    self.load_extension(path)
                    mode = "load"
                case "unload" | "u":
                    self.unload_extension(path)
                    mode = "unload"
                case "reload" | "r":
                    self.reload_extension(path)
                    mode = "reload"
                case _:
                    return await ctx.send(f"> ERROR: mode {mode} is undefined")
            await ctx.send(f"> SUCCESS: cog {cog_name} is has succeeded {mode}")
        
        @commands.is_owner()
        @self.command()
        async def ISRUN(ctx: commands.Context) -> Command:
            await ctx.send("I'm Running")
        
        @commands.is_owner()
        @self.command()
        async def restart(ctx: commands.Context) -> Command:
            await ctx.send(">> Bot Restarting...")
            await self.close()

myBot = MyBot()
myBot.run(os.getenv("TOKEN"))