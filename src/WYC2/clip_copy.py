import subprocess
import logging
from utils import _logger_setup


class ClipCopy():
    logger = _logger_setup(logging.DEBUG)
    def __init__(self):
        pass

        """
        clip board に対象のデータをコピーする
        """
    @classmethod
    def copy(cls, data):
        try:
            subprocess.run("pbcopy", universal_newlines=True, input=data)
            cls.logger.debug("Copy Finished")
        except Exception as e:
            cls.logger.error(e)