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
            return await ctx.send("Join a VC first")

        await ctx.send("🔍 Searching...")

        # Connect to VC
        vc = ctx.voice_client
        if not vc:
            vc = await ctx.author.voice.channel.connect()

        # yt-dlp options
        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
            "default_search": "ytsearch",
            "extract_flat": False,
        }

        loop = asyncio.get_event_loop()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await loop.run_in_executor(
                None, lambda: ydl.extract_info(search, download=False)
            )

        if "entries" in info:
            info = info["entries"][0]

        url = info["url"]

        # Stop current audio if playing
        if vc.is_playing():
            vc.stop()

        source = await discord.FFmpegOpusAudio.from_probe(url)

        vc.play(source)

        await ctx.send(f"🎶 Now playing: {info.get('title')}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("⏹ Stopped")

async def setup(bot):
    await bot.add_cog(Music(bot))
