import discord
from discord.ext import commands
from config import TOKEN, PREFIX
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"🍪 COOKIE online as {bot.user}")

async def main():
    await bot.load_extension("actions")
    await bot.load_extension("music")
    await bot.load_extension("games")
    await bot.start(TOKEN)

asyncio.run(main())
