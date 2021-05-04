from .configuration import LogConfig
import logging

def set_up():
    config = LogConfig()
    logging.basicConfig(level=config.level.upper())
