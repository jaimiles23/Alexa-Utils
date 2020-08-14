"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-13 13:31:28
 * @modify date 2020-08-13 13:31:36
 * @desc [
Contains:
- logger
- log decorator
- log_all function

Logger level is accessed through Lambda environment variable: log_level

Logger levels described below:
    50  Critical
    40  Error
    30  Warning
    20  Info    
    10  Debug
    0   Notset
]
*/
"""


##########
# Imports
##########

from functools import wraps, partial
from logging import getLogger
import os


##########
# Logger
##########

logger = getLogger(__name__) 

try:
    log_level = int( os.environ['log_level'])   ## Set in Lambda environment variable 
except:
    log_level = 10
logger.setLevel(log_level)


##########
# Decorator
##########

def log_func_name(func, *args, **kwargs):
    """Decorator to log.debug the function name.
    """
    @wraps(func)
    def func_name_wrap(*args, **kwargs):
        logger.debug(f"FUNC:    {func.__name__}")
        return func(*args, **kwargs)
    return func_name_wrap


##########
# Log_all func
##########

@log_func_name
def log_all(*args, log_level: int = 10) -> None:
    """Logs all arguements at log_level keyword."""
    log_level_dict = {
        10  :   logger.debug,
        20  :   logger.info,
        30  :   logger.warning,
        40  :   logger.error,
    }

    log_type = log_level_dict[log_level]
    for arg in args:
        log_type(arg)
    return

