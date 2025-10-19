import discord
import discord.ext.commands as commands
import discord.app_commands
from hinabot.logger import logger

class SystemModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot