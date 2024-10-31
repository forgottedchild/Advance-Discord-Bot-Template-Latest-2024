import discord

async def send_error(ctx, message):
    embed = discord.Embed(description=message, color=discord.Color.red())
    await ctx.send(embed=embed)
