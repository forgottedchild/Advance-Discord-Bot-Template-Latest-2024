import discord
from discord.ext import commands
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MyBot(commands.Bot):
    def __init__(self, command_prefix, config):
        super().__init__(command_prefix=command_prefix, intents=discord.Intents.all())
        self.config = config
        self.owner_id = config["owner_id"]

    async def on_ready(self):
        logging.info(f"Logged in as {self.user} (ID: {self.user.id})")
        await self.load_cogs()
    
    async def load_cogs(self):
        for cog in ["cogs.example", "cogs.moderation", "cogs.fun"]:
            try:
                await self.load_extension(cog)
                logging.info(f"Loaded {cog}")
            except Exception as e:
                logging.error(f"Failed to load cog {cog}: {e}")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the necessary permissions.")
        else:
            logging.error(f"Error in command {ctx.command}: {error}")
            await ctx.send("An error occurred. Please try again later.")

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)
