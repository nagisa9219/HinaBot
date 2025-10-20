if __name__ != "__main__":
    from .logger import logger
    logger.fatal('Not main process. Probably crucible?')

else:
    from .logger import logger
    logger.info('Main process. Starting HinaBot...')
    
    import os
    import json
    import discord
    from . import bot
    from hinabot.core.config import Config
    from hinabot.core.config import load_config

    config_path = './hinabot/config.json'
    config = load_config(config_path)
    # print(config)
    bot.run(config)