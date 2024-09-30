import pytest
from mktestdocs import check_docstring


def foobar_good(a, b):
    """
    Returns a + b.

    Examples:

    ```python
    import random

    random.random()
    assert 'a' + 'b' == 'ab'
    assert 1 + 2 == 3
    ```
    """
    pass


def foobar_also_good(a, b):
    """
    ```python
    import random

    assert random.random() < 10
    ```
    """
    pass


def foobar_bad(a, b):
    """
    ```python
    assert foobar(1, 2) == 4
    ```
    """
    pass


def admonition_edge_cases():
    """
    !!! note

        All cells of a table are initialized with an empty string. Therefore, to delete the content of a cell,
        you need to assign an empty string, i.e. `''`. For instance, to delete the first row after the header:

        ```python
        assert 1 + 2 == 3
        ```"""
    pass

def adminition_edge_case_bad():
    """Test that we can handle the edge cases of admonitions."""
    example = """!!! note

    Another one. 
    ```python
    assert 1 + 2 == 4
    ```"""
    pass

@pytest.mark.parametrize("func", [foobar_good, foobar_also_good, admonition_edge_cases])
def test_base_docstrings(func):
    check_docstring(func)


@pytest.mark.parametrize("func", [foobar_bad, adminition_edge_case_bad])
def test_base_docstrings_bad(func, capsys):
    with pytest.raises(Exception):
        check_docstring(func)
        capsys.readouterr()
        assert func.__name__ in capsys.readouterr().out
