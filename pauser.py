"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-13 13:18:57
 * @modify date 2020-08-13 13:21:57
 * @desc [
    Pauser utility class. Methods for:
    - Make pause level list
    - Mode specific pauses

    NOTE: Add optional argument for class instantiation if should import logger.

]
*/"""


##########
# Imports
##########

from operator import (add, sub)
import random


from ask_sdk_core.handler_input import HandlerInput


##########
# Wrapper
##########

PAUSE_SSML = """<break time="{}s"/>"""


##########
# Pauser utility class
##########

class Pauser(object):

    @staticmethod
    def get_pause(pause_length: float = 1) -> str:
        """Returns pause speech for passed length."""
        return PAUSE_SSML.format( pause_length)
    

    @staticmethod
    def get_p_for_msg_len(message: str) -> str:
        """Returns pause with duration based on message length."""
        if not message:
            return ''
        
        length = (0.00420 * len(message)) + 0.4
        
        pause_length = round(length, 2) if (length < 3) else 3
        pause_length = pause_length if (pause_length > 0.25) else 0.25

        return PAUSE_SSML.format(pause_length)
    

    @staticmethod
    def get_p_level(level: float) -> str:
        """Returns pause length dependent on the level passed.
        
        Random variation included for more fluid UX.
        Standard levels & Pause Lengths:
            1   :   0.35
            2   :   0.70
            3   :   1.05
            4   :   1.40
            5   :   1.75
        """
        seconds = (0.35 * level)
        variation = random.randint(0, int(seconds * 100)) / 1000
        op = random.choice([add, sub])
        
        pause_length = op(seconds, variation)
        pause_length = pause_length if (pause_length >= 0.2) else 0.2

        return PAUSE_SSML.format( pause_length)


    @staticmethod
    def make_ms_pause_level_list(*args) -> list:
        """Returns list of the arguments to be added to speech_list.

        Transforms all int/float args into p_levels then adds to the list.
        """
        speech_list = []

        if not (args):
            return []
        for arg in (args):
            if isinstance(arg, str):
                speech_list.append(arg)
            elif isinstance(arg, (float, int)):
                speech_list.append( Pauser.get_p_level( arg))
            # else:
                # logger.warning(f"make_ms_pause_level_list: Unrecognized argument {arg}")
        return speech_list
    
    
    
        