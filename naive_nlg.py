"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-05-06 15:10:52
 * @modify date 2020-06-16 15:11:39
 * @desc [
    TODO: 
    - Consider is_instance(data, (tuple, list)) vs has_attr(__iter__)??

    ##########
    # README.md Example.
    ##########

    linear_nlg is a naive natural language generation (NLG) to interact with the user. 
    The method transforms linearly connected sentence chunks (e.g., clauses, parts of speech, etc.) into speech responses.

    Consider the following arbitrary noun phrase:

    "The red dog"

    This phrase can be parsed into 3 separate chunks:

    "The": determiner
    "red": colour adjective
    "dog": animal noun
    In this example, the determiner, adjective, and noun have no effect on the meaning of the response. 
    We can use naive NLG to create an arbitrary noun phrase. This skill's NLG method would sample from the following three message tuples (MT). 
    A single item is sampled from each message tuple to create the noun phrase (DET, JJ, NN).

    MT_DET = (
        "The",
        "A",
    )
    MT_COLOUR_JJ = (
        "red",
        "blue",
        "yellow",
    )
    MT_ANIMAL_NN = (
        "dog",
        "cat",
    )
    This NLG method requires careful consideration of sentence structure and semantics to avoid unnatural responses. 
    However, successful implementation increases response variety multiplicatively. 
    The speech construction for the above noun phrase yields 12 response permutations.

    Data for each NLG method is located in each subdirectory's data module.


    ##########
    # Test
    ##########
    >>> test = [MT_DET, MT_COLOUR_JJ, MT_ANIMAL_NN]
    >>> naive_nlg(test)
    "The red dog"
    
]*/
"""


##########
# Imports
##########

import random


from logs import logger, log_func_name
from pauser import Pauser


##########
# Create Message from Tuple of Message Clauses
##########

@log_func_name
def linear_nlg(tuple_message_clause: tuple, str_joiner: str = ' ') -> str:
    """Returns message constructed from tuple message clause.
    
    Constructs the message with different methods per data type.
    ##  Data type       Method
        Tuple/list      random.choice()
        str             append
        int             Pauser.get_p_level()
    """
    def get_clause(tup_data) -> str:
        """Helper func: returns clause from tup_data using recursion."""
        if (tup_data is None) or (len(tup_data) == 0):
            return ''

        elif isinstance(tup_data, str):
            return tup_data

        elif isinstance(tup_data, (int, float)):
            return Pauser.get_p_level(tup_data)
            
        elif isinstance(tup_data, (tuple, list)):

            if isinstance(tup_data[0], str):
                ## List of strings, return choice.
                return random.choice(tup_data)

            else:
                # Recursion of tuples in tuple
                speech_list = []
                for clause_list in tup_data:
                    clause = get_clause(clause_list)
                    speech_list.append(clause)

                return str_joiner.join(speech_list)
        else:
            logger.warning(f"get_clause: Unrecognized data type {tup_data}")
    

    logger.debug(tuple_message_clause)
    speech_list = []

    for tup_data in tuple_message_clause:
        clause = get_clause(tup_data)
        speech_list.append( clause)
    
    # logger.debug(speech_list)
    return str_joiner.join(speech_list)

