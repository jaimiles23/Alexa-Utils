"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-13 16:29:20
 * @modify date 2020-08-13 16:37:00
 * @desc [

    Default imports

    Classes:
        - SlotUtils
        - Pauser


    Functions
        - logger, log_func_name, log_all
        - linear_nlg


    The smml_tags module is not imported by default. 
    Per convention, this module should be imported separately as ssml:
        >>> import alexautils.ssml_tags as ssml
        >>> ssml.MW_EXCITED.format("Hi!")
 ]
 */
"""


##########
# Classes
##########

from slot_utils import SlotUtils
from pauser import Pauser


##########
# Functions
##########

from logs import logger, log_func_name, log_all
from naive_nlg import linear_nlg

