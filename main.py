from bot import MyBot
import json

# Load configuration
with open("data/config.json") as config_file:
    config = json.load(config_file)

bot = MyBot(command_prefix=config["prefix"], config=config)
bot.run(config["token"])
