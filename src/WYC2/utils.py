import logging
from functools import wraps
import time

def _logger_setup(level):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger

"""
関数の実行時間を計測
デコレータのラッパー関数を利用して、loggerを引数に取っている
"""
def time_func(logger):
    
    def _inner(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            logger.info('func name is ' + func.__name__)
            
            try:
                start = time.time()
                ret_func = func(*args, **kwargs)
                elapsed = time.time() - start
                logger.debug(func.__name__ + " took " + f'{elapsed:.08}' + " sec")
                return ret_func
            except:
                raise
        return wrapper
    return _inner