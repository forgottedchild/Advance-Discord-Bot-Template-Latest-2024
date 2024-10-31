from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command(name="kick")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a member from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.")

    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
