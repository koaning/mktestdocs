"""
The docstring of the first class starts like
\"""Some class ...
The docstring of the second class starts like
\"""
Some class ...
The tests are checking that regarddless of how the class docstring starts we should always be able to read the tests
"""


import pytest

from mktestdocs import get_codeblock_members
from mktestdocs.__main__ import format_docstring


class BadClass:
    """Some class with a header and a code block.

    ```python
    assert False, "this should fail."
    ```
    
    """
    def __init__(self):
        pass

class BadClassNewLine:
    """
    Some class with a header and a code block.

    ```python
    assert False, "this should fail."
    ```
    
    """
    def __init__(self):
        pass


bad_members = get_codeblock_members(BadClass)

@pytest.mark.parametrize("cls", [BadClass, BadClassNewLine], ids=lambda d: d.__qualname__)
def test_grab_bad_methods(cls):
    bad_members = get_codeblock_members(cls)
    assert len(bad_members) == 1


def test_docstring_formatted():
    # given
    docstring = "Some class with a header and a code block"
    # when
    formatted = format_docstring(docstring)
    # then
    assert formatted == "\n    Some class with a header and a code block"

def test_docstring_not_formatted():
    # given
    docstring = "\n    Some class with a header and a code block"
    # when
    formatted = format_docstring(docstring)
    # then
    assert formatted == docstring

