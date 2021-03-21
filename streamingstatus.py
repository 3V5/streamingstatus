import json
import discord
from discord.ext import commands
from discord.ext import tasks

with open(f"config.json") as f:
        configmain = json.load(f)
        token = configmain.get('token')
        title = configmain.get('title')
        url = configmain.get('url')
        client = discord.Client()

@client.event
async def on_ready():
    print(f"    started\n    Discord: Discord.gg/cdKzZQJH6c\n    Title: {title}\n    Url:   {url}")
    await client.change_presence(activity=discord.Streaming(name=f"{title}", url=f"{url}"))

client.run(token, bot=False)
