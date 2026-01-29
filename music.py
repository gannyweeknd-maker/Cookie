import discord
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, query: str):
        if not ctx.author.voice:
            return await ctx.send("Join VC first")

        vc = ctx.voice_client
        if not vc:
            vc = await ctx.author.voice.channel.connect(self_deaf=True)

        ydl_opts = {
            "format": "bestaudio",
            "noplaylist": True,
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            url = info["entries"][0]["url"]

        source = discord.FFmpegPCMAudio(
            url,
            executable="ffmpeg",
            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            options="-vn"
        )

        vc.play(source)
        await ctx.send(f"🎵 Playing: {query}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice
