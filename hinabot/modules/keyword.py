import discord
import discord.ext.commands as commands
import discord.app_commands
from typing import Optional, Union
from hinabot.logger import logger

class KeywordModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    keyword = discord.app_commands.Group(name='keyword', description='Adjust the keyword detection settings.')

    @keyword.command(name='add', description='Add a keyword to be detected.')
    @discord.app_commands.describe()
    async def add(self, interaction: discord.Interaction, target: str, data: str):
        pass

    @keyword.command(name='remove', description='Remove a keyword from detection.')
    @discord.app_commands.describe()
    async def remove(self, interaction: discord.Interaction, target: str):
        pass

    @keyword.command(name='list', description='List all detected keywords.')
    @discord.app_commands.describe()
    async def list(self, interaction: discord.Interaction):
        pass

    @keyword.command(name='configure', description='Configure the keyword detection settings.')
    @discord.app_commands.describe()
    async def configure(self, interaction: discord.Interaction, terget:str, config_option: str, data: Optional[str]):
        pass

def setup(bot):
    bot.add_cog(KeywordModule(bot))