import discord
import discord.ext.commands as commands
import discord.app_commands
from hinabot.logger import logger

class EchoModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='echo', description='Echoes the user\'s message. For testing purposes only.')
    @discord.app_commands.describe(message='The message to echo back to you.')
    async def echo(self, interaction: discord.Interaction, message: str):
        # await interaction.response.send_message(content='Finished', ephemeral=True)
        await interaction.response.send_message(content=message)

def setup(bot):
    return bot.add_cog(EchoModule(bot))
