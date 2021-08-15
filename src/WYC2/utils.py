import logging

def _logger_setup(level):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger