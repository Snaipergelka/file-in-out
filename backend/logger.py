import logging
from logging.config import fileConfig


def get_logger(module_name):
    fileConfig('/backend/logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger("FileApp").getChild(module_name)
    return logger
