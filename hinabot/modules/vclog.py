import discord
import discord.ext.commands as commands
import discord.app_commands
from typing import Union, Optional
from hinabot.logger import logger

class VclogModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    vclog = discord.app_commands.Group(name='vclog', description='Adjust the voice channel logging settings.')

    @vclog.command(name='set', description='Enable or disable voice channel logging.')
    @discord.app_commands.describe(
        enabled="Enable or disable voice channel logging.",
        channel="Specify a voice channel to log, or 'all' for all channels."
    )
    async def set(self, interaction: discord.Interaction, enabled: bool, channel: Union['all', discord.VoiceChannel] = 'all'):
        pass

    @vclog.command(name='configure', description='Configure the voice channel logging settings.')
    @discord.app_commands.describe()
    async def configure(self, interaction: discord.Interaction, config_option: Optional[str] = None, data: Optional[str] = None):
        pass

def setup(bot):
    bot.add_cog(VclogModule(bot))