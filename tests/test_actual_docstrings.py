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
    return a + b


def foobar_also_good(a, b):
    """
    Returns a + b.

    Examples:

    ```python
    import random

    assert random.random() < 10
    ```
    """
    return a + b


def foobar_bad(a, b):
    """
    Returns a + b.

    Examples:

    ```python
    assert foobar(1, 2) == 4
    ```
    """
    return a + b


@pytest.mark.parametrize("func", [foobar_good, foobar_also_good])
def test_base_docstrings(func):
    check_docstring(func)


@pytest.mark.parametrize("func", [foobar_bad])
def test_base_docstrings_bad(func, capsys):
    with pytest.raises(Exception):
        check_docstring(func)
        capsys.readouterr()
        assert func.__name__ in capsys.readouterr().out
