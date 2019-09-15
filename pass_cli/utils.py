import logging
import sys


def setup_logger(name, format):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
