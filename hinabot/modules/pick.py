import discord
import discord.ext.commands as commands
import discord.app_commands
import random as rand
from typing import List, Optional, Union, Literal
import enum
from hinabot.logger import logger

class PickModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    random = discord.app_commands.Group(name='random', description='Random related commands.')

    @random.command(name='pick', description='Randomly pick an item from the provided options.')
    @discord.app_commands.describe(options='The options to choose from, separated by commas.')
    async def pick(self, interaction: discord.Interaction, data: Union[str, Sets], count: Optional[int] = 1, seperator: Optional[str] = ' '):
        pass

    @random.command(name='sets', description='Manage predefined sets of items for random selection.')
    @discord.app_commands.describe(
        set_name='The name of the set to manage. Use "list" to see all sets.',
        data='The data for the set, if applicable.'
    )
    async def sets(self, interaction: discord.Interaction, set_name: str, data: Optional[str] = None):
        pass

    class Sets(enum.Enum):
        pass

def setup(bot):
    bot.add_cog(PickModule(bot))
