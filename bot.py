import os
import discord
from discord.ext import commands

# Load opus (VERY IMPORTANT)
discord.opus.load_opus("libopus.so.0")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="c!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def main():
    async with bot:
        await bot.load_extension("music")
        await bot.start(os.getenv("TOKEN"))

import asyncio
asyncio.run(main())
