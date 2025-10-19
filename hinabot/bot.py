import discord
import discord.ext.commands
import sys
import json
import os
from .core.config import Config
from .logger import logger

class HinaBot(discord.ext.commands.Bot):
    def __init__(self, config: Config):
        self.config = config
        intents = discord.Intents.default()
        if self.config.release == 'development':
            intents.message_content = True
        super().__init__(command_prefix=self.config.prefix, intents=intents)
        self.blocked_users = config.blocked_users
        if self.config.restricted_mode.get('enabled', False):
            self.allowed_server_id = set(self.config.restricted_mode.get('allowed_server_id', []))

    def run(self):
        super().run(self.config.token, root_logger=logger, log_handler=None)

    async def on_ready(self):
        for i in _load_module(self.config):
            await self.load_extension(i)
        synced = await self.tree.sync()
        logger.info(f'Synced {len(synced)} command(s)')
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
    
def run(config: Config):
    HinaBot(config).run()

def _load_module(config: Config):
    yield 'hinabot.modules.echo'
    # yield 'hinabot.modules.system'
    # yield 'hinabot.modules.vclog'
    # yield 'hinabot.modules.keyword'
    # yield 'hinabot.modules.pick'
    # yield 'hinabot.modules.count'

if __name__ == '__main__':
	logger.fatal('bot.py found that it was the main module. You should be invoking the bot from entrypoint.py')
	sys.exit(1)