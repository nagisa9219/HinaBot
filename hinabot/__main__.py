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

    def load_config():
        config_path = './hinabot/config.json'
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f'Config file not found at {config_path}')
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        return Config(**config_data)
    
    config = load_config()
    # print(config)
    bot.run(config)