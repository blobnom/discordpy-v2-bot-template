import discord

from discord.ext.commands import Cog
from discord import Interaction
from discord import app_commands

class ExampleCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name = "ping",
        description = "Pong!"
    )
    async def ping(self, ctx: Interaction):
        await ctx.response.send_message("Pong!")

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(ExampleCog(bot))
    else:
        await bot.add_cog(
            ExampleCog(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
