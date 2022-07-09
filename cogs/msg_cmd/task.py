import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Command
from discord.ext import tasks

import json
import os
import time

import func

class Task(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        self.tasks_filepath = './config/task.json'
        if os.path.isfile(self.tasks_filepath):
            with open(self.tasks_filepath, encoding='utf8') as file:
                self.tasks_cache = json.load(file)
        else:
            self.tasks_cache = {
                    "tasks": {},
                    "settings": {}
                }
            with open(self.tasks_filepath, 'w', encoding='utf8') as file:
                json.dump(self.tasks_cache, file, indent=4, ensure_ascii=False)
        with open('./config/const.json') as file:
            self.const = json.load(file)
        
        self.autoSaveData.start()

    async def loadTasksFile(self) -> dict:
        with open(self.tasks_filepath, encoding='utf8') as file:
            return json.load(file)
    
    async def checkUserInData(self, id_: int) -> None:
        if str(id_) not in self.tasks_cache['tasks']:
            self.tasks_cache['tasks'][str(id_)] = []

    def dcJsonFormat(self, jsonObj) -> str:
        return f'```json\n{json.dumps(jsonObj, indent=4, ensure_ascii=False)}\n```'
    
    def embedGenerator(self, title, description=None, *args, **kwargs) -> Embed:
        return Embed(title=title, description=description, color=self.const['embed_color'], *args, **kwargs)

    @tasks.loop(minutes=10)
    async def autoSaveData(self) -> tasks.Loop:
        while (data:=await self.loadTasksFile()) != self.tasks_cache:
            with open(self.tasks_filepath, 'w', encoding='utf8') as file:
                json.dump(self.tasks_cache, file, indent=4, ensure_ascii=False)
        self.tasks_cache = data
        print('>>> SUCCESS: task autoSaveData ok')

    @commands.command()
    async def addTask(self, ctx: Context, name: str, description: str=None) -> Command:
        await self.checkUserInData(ctx.author.id)
        self.tasks_cache['tasks'][str(ctx.author.id)].append(
            _:=(
                {
                    'name': name,
                    'description': description or None,
                    'createTime': func.round(time.time()),
                    'isEnd': False,
                    'endTime': None
                    }
                )
            )
        embed = self.embedGenerator('創建成功', f'創建內容如下:\n{self.dcJsonFormat(_)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def delTask(self, ctx: Context, id_: int) -> Command:
        await self.checkUserInData(ctx.author.id)
        data = self.tasks_cache['tasks'][str(ctx.author.id)]
        if not data or id_ > len(data):
            return await ctx.send(f'>> ERROR: ID error')
        _ = data[id_]
        del data[id_]
        embed = self.embedGenerator('刪除成功', f'已成功刪除以下資料:\n{self.dcJsonFormat(_)}')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def endTask(self, ctx: Context, id_: int) -> Command:
        await self.checkUserInData(ctx.author.id)
        data = self.tasks_cache['tasks'][str(ctx.author.id)]
        if not data or id_ > len(data):
            return await ctx.send(f'>> ERROR: ID error')
        if data[id_]['isEnd']:
            return await ctx.send(f'>> ERROR: Task#{id_} has End')
        data[id_]['isEnd'] = True
        data[id_]['endTime'] = func.round(time.time())
        embed = self.embedGenerator('任務完成', f'{self.dcJsonFormat(data[id_])}')
        await ctx.send(embed=embed)
        
    
    @commands.command()
    async def showTask(self, ctx: Context, id_: int=None) -> Command:
        await self.checkUserInData(ctx.author.id)
        data: list = self.tasks_cache['tasks'][str(ctx.author.id)]
        if id_ is None:
            if data:
                task_list = '\n'.join(
                    f'{i}: {k} (isEnd: {isEnd})' for i, k, isEnd in zip(
                        range(len(data)), [i['name'] for i in data], ['yes' if i['isEnd'] else 'no' for i in data]
                        )
                    )
                value = f'```yaml\n{task_list}\n```'
            else:
                value = '```Null```'
            embed = self.embedGenerator(f'{ctx.author}的任務清單', value)
        else:
            if id_ > len(data):
                return await ctx.send(f'>> ERROR: ID error')
            embed = self.embedGenerator(f"{ctx.author}的任務清單 - Task#{id_}", f'{self.dcJsonFormat(data[id_])}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Task(bot))