import pytest

from mktestdocs import get_codeblock_members
from mktestdocs.__main__ import format_docstring


def test_docstring_formatted():
    # given (a docstring not prepared for dedent)
    docstring = "Some class with a header and a code block"
    # when (we go through the format_docstring function)
    formatted = format_docstring(docstring)
    # then (a new line and tab are added to the docstring)
    assert formatted == "\n    Some class with a header and a code block"

def test_docstring_not_formatted():
    # given (a docstring prepared for dedent)
    docstring = "\n    Some class with a header and a code block"
    # when (we go through the format_docstring function)
    formatted = format_docstring(docstring)
    # then (the docstring doesn't change)
    assert formatted == docstring



# The docstring of the first class starts like
# """Some class ...
# The docstring of the second class starts like
# """
# Some class ...
# The tests are checking that regardless of how the class docstring starts we should always be able to read the tests
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



@pytest.mark.parametrize("cls", [BadClass, BadClassNewLine], ids=lambda d: d.__qualname__)
def test_grab_bad_methods(cls):
    bad_members = get_codeblock_members(cls)
    assert len(bad_members) == 1


