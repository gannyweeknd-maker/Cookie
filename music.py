import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        if not ctx.author.voice:
            return await ctx.send("Join a VC first")

        vc = ctx.voice_client
        if not vc:
         vc = await ctx.author.voice.channel.connect(self_deaf=True)

        vc.play(
    discord.FFmpegPCMAudio(
        url,
        executable="ffmpeg"
    )
        )
        await ctx.send("🎵 Playing")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))
