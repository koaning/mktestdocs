from typing import Any

import pytest

from mktestdocs import check_docstring, get_codeblock_members


class BadClass:
    """Some class with a header and a code block.

    ```python
    assert False, "this should fail."
    ```
    
    """
    def __init__(self):
        pass


bad_members = get_codeblock_members(BadClass)

def test_grab_bad_methods():
    assert len(bad_members) == 1

# @pytest.mark.parametrize("obj", bad_members, ids=lambda d: d.__qualname__)
# def test_bad_member(obj):
#     with pytest.raises(Exception):
#         check_docstring(obj)