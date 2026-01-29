import discord
from discord.ext import commands
import yt_dlp

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
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{search}", download=False)
            url = info["entries"][0]["url"]
            title = info["entries"][0]["title"]

        source = await discord.FFmpegOpusAudio.from_probe(url)

        vc.stop()
        vc.play(source)

        await ctx.send(f"🎵 Now playing: {title}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))
