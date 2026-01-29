import discord
from discord.ext import commands
import yt_dlp
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, search: str):
        if not ctx.author.voice:
            return await ctx.send("Join VC first")

        vc = ctx.voice_client
        if not vc:
            vc = await ctx.author.voice.channel.connect()

        await ctx.send("🔍 Searching...")

        ydl_opts = {
            "format": "bestaudio",
            "noplaylist": True,
            "quiet": True,
            "default_search": "ytsearch",
            "source_address": "0.0.0.0",
            "extractor_args": {
                "youtube": {
                    "player_client": ["android"]
                }
            }
        }

        loop = asyncio.get_event_loop()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await loop.run_in_executor(
                None,
                lambda: ydl.extract_info(search, download=False)
            )

        if "entries" in info:
            info = info["entries"][0]

        url = info["url"]
        title = info["title"]

        source = await discord.FFmpegOpusAudio.from_probe(url)

        vc.stop()
        vc.play(source)

        await ctx.send(f"🎶 Now playing: {title}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))
