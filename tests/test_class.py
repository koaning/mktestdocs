import pytest

from mktestdocs import get_codeblock_members, check_docstring


class Dinosaur:
    """
    This is a dino.

    ```python
    from dinosaur import Dinosaur

    assert Dinosaur().name == 'trex'
    ```
    """

    def __init__(self):
        self.name = "trex"

    @staticmethod
    def a(value):
        """
        Returns value

        Example:

        ```python
        from dinosaur import Dinosaur

        dino = Dinosaur()
        assert dino.a(1) == 1
        ```
        """
        return value

    @classmethod
    def b(cls, value):
        """
        Returns value

        Example:

        ```python
        from dinosaur import Dinosaur
        assert Dinosaur.b(1) == 1
        ```
        """
        return value

    def hello(self):
        """
        Returns value

        Example:

        ```python
        from dinosaur import Dinosaur
        assert Dinosaur().name == 'trex'
        ```
        """
        return self.name


members = get_codeblock_members(Dinosaur)


def test_grab_methods():
    assert len(get_codeblock_members(Dinosaur)) == 4


@pytest.mark.parametrize("obj", members, ids=lambda d: d.__qualname__)
def test_member(obj):
    check_docstring(obj)
