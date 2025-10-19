import discord
import discord.ext.commands as commands
import discord.app_commands
from hinabot.logger import logger

class CountModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    count = discord.app_commands.Group(name='count', description='Adjust the counting sysyem settings.')

    @count.command(name='create', description='Create a counting target.')
    @discord.app_commands.describe(
        cid='The name of the counting target.'
    )
    async def create(self, interaction: discord.Interaction, cid: str):
        pass

    @count.command(name='add', description='Add a number to a counting target.')
    @discord.app_commands.describe(
        cid='The name of the counting target.', 
        number='The number to add to the count. Default is 1.'
    )
    async def add(self, interaction: discord.Interaction, ccid: str, number: int = 1):
        pass

    @count.command(name='get', description='Get the current count of a counting target.')
    @discord.app_commands.describe(
        cid='The name of the counting target.'
    )
    async def get(self, interaction: discord.Interaction, cid: str):
        pass

    @count.command(name='list', description='List all counting targets.')
    @discord.app_commands.describe()
    async def list(self, interaction: discord.Interaction):
        pass

def setup(bot):
    bot.add_cog(CountModule(bot))