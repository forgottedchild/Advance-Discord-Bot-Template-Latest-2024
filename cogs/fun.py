from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coinflip")
    async def coinflip(self, ctx):
        """Flips a coin."""
        outcome = random.choice(["Heads", "Tails"])
        await ctx.send(f"The coin landed on: {outcome}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
