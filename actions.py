import discord, random, json
from discord.ext import commands

with open("gifs.json") as f:
    gifs = json.load(f)

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def do(self, ctx, name, member):
        gif = random.choice(gifs[name])
        await ctx.send(f"**{ctx.author.name} {name}s {member.mention}**\n{gif}")

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        await self.do(ctx, "hug", member)

    @commands.command()
    async def kick(self, ctx, member: discord.Member):
        await self.do(ctx, "kick", member)

    @commands.command()
    async def punch(self, ctx, member: discord.Member):
        await self.do(ctx, "punch", member)

    @commands.command()
    async def goon(self, ctx, member: discord.Member):
        await ctx.send(f"😈 **{member.name} has been GOONED**")

    @commands.command()
    async def ban(self, ctx, member: discord.Member):
        await ctx.send(f"🔨 **{member.name} has been banned** (jk)")

async def setup(bot):
    await bot.add_cog(Actions(bot))
