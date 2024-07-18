# logger.py

import logging
import colorlog

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

log_format = "%(log_color)s%(levelname)s:     %(reset)s%(asctime)s %(cyan)s[%(filename)s:%(lineno)d]%(reset)s - %(log_color)s%(message)s"

color_formatter = colorlog.ColoredFormatter(
    log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    reset=True
)

handler.setFormatter(color_formatter)
logger.addHandler(handler)
