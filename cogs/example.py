from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Responds with Pong!"""
        await ctx.send(f"Pong! Latency: {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(Example(bot))

