import discord
from discord.ext import commands

import os
# import time
import dotenv

dotenv.load_dotenv()

class MyBot(commands.Bot):
    def __init__(self, command_prefix="mb.", intents=discord.Intents.all()) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)
        self._add_command()

    async def on_ready(self):
        print(f"Python >> Bot is Ready, Login: {self.user}")
    
    def _add_command(self):
        @self.command()
        async def cogs(ctx:commands.Context, cog_name:str, mode:str="load"):
            # if not os.path.isfile(f"{cog_name.replace('.py', '')}.py"):
            #     return await ctx.send(f"> ERROR: cog {cog_name} is not found")
            path = cog_name.replace(".py", "").replace("/", ".").replace("\\", ".")
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
            await ctx.send(f">> SUCCESS: cog {cog_name} is has succeeded {mode}")
        
        @commands.is_owner()
        @self.command()
        async def ISRUN(ctx: commands.Context):
            await ctx.send("I'm Running")
        
        @commands.is_owner()
        @self.command()
        async def restart(ctx: commands.Context):
            await ctx.send(">> Bot Restarting...")
            await self.close()

myBot = MyBot()
myBot.run(os.getenv("TOKEN"))