import json
import discord
from discord.ext import commands
from discord.ext import tasks

with open(f"config.json") as f:
        configmain = json.load(f)
        token = configmain.get('token')
        title = configmain.get('title')
        url = configmain.get('url')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=f"{title}", url=f"{url}"))
    print(f"""
    
    Discord: Discord.gg/cdKzZQJH6c
    started
    Title: {title}
    Url:   {url}
    
    """)

client.run(token, bot=False)
