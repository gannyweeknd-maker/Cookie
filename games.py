import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(random.choice(["🪙 Heads", "🪙 Tails"]))

async def setup(bot):
    await bot.add_cog(Games(bot))
