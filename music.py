import discord
from discord.ext import commands
import yt_dlp


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, search: str):
        # User must be in VC
        if not ctx.author.voice:
            return await ctx.send("Join a VC first!")

        channel = ctx.author.voice.channel

        vc = ctx.voice_client
        if not vc:
            vc = await channel.connect()

        ydl_opts = {
            "format": "bestaudio",
            "quiet": True,
            "noplaylist": True
        }

        await ctx.send("🔎 Searching...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                f"ytsearch:{search}",
                download=False
            )
            url = info["entries"][0]["url"]
            title = info["entries"][0]["title"]

        source = discord.FFmpegPCMAudio(
            url,
            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            options="-vn"
        )

        if vc.is_playing():
            vc.stop()

        vc.play(source)
        await ctx.send(f"🎵 Playing: {title}")

    @commands.command()
    async def stop(self, ctx):
        vc = ctx.voice_client
        if vc:
            await vc.disconnect()
            await ctx.send("⏹ Stopped and left VC")


async def setup(bot):
    await bot.add_cog(Music(bot))
