# AlexaUtils

Library with utility classes and functions to supplement the Python AWS SDK for Alexa skill development. Available on  PyPI: [here](https://pypi.org/project/alexautils/0.0.1/)

- [AlexaUtils](#alexautils)
  - [Installation](#installation)
  - [Imports](#imports)
  - [Documentation](#documentation)
  - [TODO List](#todo-list)


## Installation
- Python 3.6 +
- ask-sdk-core == 1.11.0

To install Alexa Utils, use pip:
```
pip install alexautils
```

<br>
<a href = "#alexautils"> :arrow_up: Table of Contents</a>
<br>
<br>

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

<br>
<a href = "#alexautils"> :arrow_up: Table of Contents</a>
<br>
<br>

## Documentation
Documentation is available [here](https://github.com/jaimiles23/Alexa-Utils/blob/master/Documentation.md)


<br>
<a href = "#alexautils"> :arrow_up: Table of Contents</a>
<br>
<br>

## TODO List

- [ ] Add entire package to GitHub
- [ ] Create an exhaustive list of SSML wrappers. 
  - [ ] May like to implement a class with dictionary structure to access SSML levels. Reference [pyssml](https://github.com/sumsted/pyssml/blob/master/pyssml/PySSML.py)
- [ ] Add formal documentation
  - [ ] Investigate using [sphynx](https://packaging.python.org/tutorials/creating-documentation/)
- [ ] Add tests to PyPI
  - [ ] https://python-packaging.readthedocs.io/en/latest/testing.html
- [ ] Add CardFuncs module - container class for functions to 

<br>
<a href = "#alexautils"> :arrow_up: Table of Contents</a>