import json
import discord
from discord.ext import commands
from discord.ext import tasks

with open(f"config.json") as f:
        configmain = json.load(f)
        discordtoken = configmain.get('token')
        title = configmain.get('title')
        url = configmain.get('url')
seggstoken = discordtoken
seggstitle = title
seggsurl = url
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=f"{seggstitle}", url=f"{seggsurl}"))
    print(f"""
    Discord: Discord.gg/cdKzZQJH6c
    started
    Title: {seggstitle}
    Url:   {seggsurl}
    """)

client.run(seggstoken, bot=False)