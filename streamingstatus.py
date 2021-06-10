import discord

client = discord.Client()
token = "Discord Token"
title = "Hello hi hi"
url = "https://twitch.tv/meowcat"

@client.event
async def on_ready():
    print(f"    started\n    Title: {title}\n    Url:   {url}")
    await client.change_presence(activity=discord.Streaming(name=f"{title}", url=f"{url}"))

client.run(token, bot=False)
