"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-05-06 11:20:42
 * @modify date 2020-06-16 23:26:21
 * @desc [
    SlotUtils class with methods to get slots from user utterances:
    - get_slot_val_by_name(handler_input, slot_name: str) -> str:
    - all slot values
    - 1st slot value - NOTE: used for locale names, but I changed to use local names, so I THINK I can remove?
    - get resolved value
 ]
 */
"""

##########
# Imports
##########

import six

from ask_sdk_core.handler_input import HandlerInput

from logs import logger, log_func_name


##########
# SlotUtils
##########

class SlotUtils(object):

    @staticmethod
    @log_func_name
    def get_slot_val_by_name(handler_input, slot_name: str) -> str:
        """Returns slot value for provided name"""
        try:
            slots = handler_input.request_envelope.request.intent.slots
            slot_info = slots.get(slot_name, None)
            slot_value = slot_info.value if slot_info else None
            slot_value = slot_value if (slot_value != '?') else None
        except AttributeError:
            return None

        logger.debug(slot_value)
        return slot_value
    

    @staticmethod
    @log_func_name
    def get_all_slot_values(handler_input) -> list:
        """Returns all slot.values from user utterance."""
        slots = handler_input.request_envelope.request.intent.slots
        slot_values = []

        if not slots:
            return slot_values
        
        for _, slot in six.iteritems(slots):
            if slot.value is not None and slot.value != '?':
                slot_values.append( slot.value)
        return slot_values
    

    @staticmethod
    @log_func_name
    def get_first_slot_value(handler_input) -> str:
        """Returns first slot value from captured values.
        
        Used for name slot, which can be first_name, gb_first_name or 
        us_first_name."""
        slots_values = SlotUtils.get_all_slot_values(handler_input)
        val = slots_values[0] if slots_values else None
        return val
    

    @staticmethod
    @log_func_name
    def get_resolved_value(handler_input, slot_name: str) -> str:
        """Returns resolved value for the slot."""
        try:
            slot = handler_input.request_envelope.request.intent.slots
            if not slot or not slot.get(slot_name, None):
                logger.warning(f"get_resolved_value: {slot_name} not found.")
                return None

            slot = slot[slot_name]
            if (
                str(slot.resolutions.resolutions_per_authority[0].status.code) !=
                "StatusCode.ER_SUCCESS_MATCH"):
                logger.warning(f"get_resolved_value: {slot_name} not successfully matched.")
                return None
            
            slot_value = slot.resolutions.resolutions_per_authority[0].values[0].value.name
        except AttributeError:
            return None
            
        return slot_value

 