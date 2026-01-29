import discord
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, search: str):
        if not ctx.author.voice:
            return await ctx.send("Join a VC first")

        await ctx.send("🔎 Searching...")

        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect()

        # yt-dlp options (ANTI-BLOCK)
        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "noplaylist": True,
            "default_search": "ytsearch",
            "source_address": "0.0.0.0",

            "extractor_args": {
                "youtube": {
                    "player_client": ["android"]
                }
            }
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(search, download=False)

                if "entries" in info:
                    info = info["entries"][0]

                url = info["url"]
                title = info.get("title", "Unknown title")

        except Exception as e:
            return await ctx.send(f"❌ Error:\n{e}")

        # Stop previous audio
        if vc.is_playing():
            vc.stop()

        # Play audio
        source = await discord.FFmpegOpusAudio.from
