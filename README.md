# AlexaUtils

AlexaUtils is a Python library with utility classes and functions to supplement the Python AWS SDK for Alexa skill development. 


## Installation
- Python 3.6 +
- ask-sdk-core == 1.11.0

To install Alexa Utils, use pip:
```
pip install alexautils
```

## Dependencies
ASK SDK BLEH HERE



## Imports
By default, the following classes and functions are imported:

_Classes_
- SlotUtils
- Pauser

_Functions_
- logger, log_func_names, log_all
- linear_nlg

The smml_tags module is not imported by default. 
Per convention, this module should be imported separately as ssml:
```python
>>> import alexautils.ssml_tags as ssml
>>> ssml.MW_EXCITED.format("Hi!")
```


## Contents


### SlotUtils
Utility class with methods to retrieve slots from user utterance.

> get_slot_val_by_name(handler_input, slot_name: str) -> str:

Returns slot value for slot_name name

> get_all_slot_values(handler_input) -> list:

Returns all slot.values from user utterance

> get_first_slot_value(handler_input) -> str:

Returns first slot value from captured values.

> get_resolved_value(handler_input, slot_name: str) -> str:

Returns resolved value for the slot.


### Pauser
Utility class to create pauses in speech response.

> get_pause(pause_length: float = 1) -> str:

Returns pause speech for passed length.

> get_p_for_msg_len(message: str) -> str:

Returns pause with duration based on message length.

> get_p_level(level: float) -> str:

Returns pause length dependent on the level passed.
 
Random variation included for more fluid UX.
| Standard levels   |   Pause length (seconds) |
| :-- | :-- |
|   1   |   0.35    |
|   2   |   0.70    |
|   3   |   1.05    |
|   4   |   1.40    |
|   5   |   1.75    |


> make_ms_pause_level_list(*args) -> list:

Returns list of the arguments to be added to speech_list.

Transforms all int/float args into p_levels then adds to the list.


### linear_nlg
> linear_nlg(tuple_message_clause: tuple, str_joiner: str = ' ') -> str:

Returns message constructed from tuple message clause.
 
Constructs the message with different methods per data type.

|   Data type   |   Method |
| :- | :- |
|   Tuple/list  |   random.choice() | 
|   str |   append  |
|   int |   Pauser.get_p_level()    |


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

```python
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
```

This NLG method requires careful consideration of sentence structure and semantics to avoid unnatural responses. 
However, successful implementation increases response variety multiplicatively. 
The speech construction for the above noun phrase yields 12 response permutations.

```python
>>> test = [MT_DET, MT_COLOUR_JJ, MT_ANIMAL_NN]
>>> naive_nlg(test)
"The red dog"
>>> naive_nlg(test)
"A yellow cat"
```


### Logs
> logger

log_level set by Lambda environment variable `log_level`

> def log_func_name(func, *args, **kwargs):

Decorator to log.debug the function name.

> log_all(*args, log_level: int = 10) -> None:

Logs all arguments at log_level keyword.

## ssml_tags
Alexa's voice user interface uses Speech Synthesis Markup Language to control the speech output. SSML reference available [here](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html)

SSML are implemented as individual text wrappers so that wrappers can be applied to separate phrases, e.g.:

```python
MW_EXCITED_MED.format("Oh No!") + "Don't throw that away, please."
```

NOTE:
May like to implement a class with dictionary structure to access SSML levels.
Reference [pyssml](https://github.com/sumsted/pyssml/blob/master/pyssml/PySSML.py)


