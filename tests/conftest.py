from copy import copy

import pytest

import mktestdocs


@pytest.fixture
def temp_executors():
    old_executors = copy(mktestdocs.__main__._executors)
    yield
    mktestdocs.__main__._executors = old_executors
