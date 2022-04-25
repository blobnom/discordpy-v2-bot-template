import json
import discord

from pathlib import Path
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, config):
        super().__init__(
            command_prefix = "",
            help_command = None,
            intents = discord.Intents.default(),
            application_id = config["application-id"]
        )

        self.config = config

    async def setup_hook(self) -> None:
        for file in Path("cogs").glob("*.py"):
            cog_name = file.name.split(".")[0]
            await self.load_extension(f"cogs.{cog_name}")
            print("Loaded extension:", file.name)
        
        if self.config["test-server-id"] == "":
            await self.tree.sync()
        else:
            await self.tree.sync(guild=discord.Object(id=self.config["test-server-id"]))

    async def on_ready(self) -> None:
        print("Bot is ready!")
        await self.change_presence(activity=discord.Activity(name="with slash commands."))

if __name__ == "__main__":
    config = json.loads(open("config.json").read())
    bot = Bot(config)
    bot.run(config["token"])
