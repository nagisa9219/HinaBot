import logging
import datetime
import os
import sys

logs_path = './hinabot/logs'

class CustomFormatter(logging.Formatter):
    LEVEL_COLOURS = [
        (logging.DEBUG, '\x1b[40;1m'),
        (logging.INFO, '\x1b[1;36m'),
        (logging.WARNING, '\x1b[33;1m'),
        (logging.ERROR, '\x1b[31m'),
        (logging.CRITICAL, '\x1b[41m'),
    ]

    FORMATS = {
        level: logging.Formatter(
            f'\x1b[30;1m%(asctime)s\x1b[0m {colour}%(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m %(message)s',
            '%Y-%m-%d %H:%M:%S',
        )
        for level, colour in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.DEBUG]

        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f'\x1b[31m{text}\x1b[0m'

        output = formatter.format(record)

        record.exc_text = None
        return output

logger = logging.getLogger('HinaBot')
logger.setLevel(logging.DEBUG)

if not os.path.exists(logs_path):
    logger.warning(f'Created logs directory at {logs_path}')
    os.makedirs(logs_path)
    
log_counter = 1
handler_base_filename = logs_path + "/{:%Y-%m-%d_%H-%M-%S}".format(datetime.datetime.now())
handler_file_path = f"{handler_base_filename}.log"
while os.path.exists(handler_file_path):
    handler_file_path = f"{handler_base_filename}-{log_counter}.log"
    log_counter += 1

file_handler = logging.FileHandler(filename=handler_file_path, encoding="utf-8", mode="w")
console_handler = logging.StreamHandler()

console_handler.setFormatter(CustomFormatter())
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"))

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug(f'Logging initialized. Log file at {handler_file_path}')