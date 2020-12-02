# mktestdocs

Run pytest against markdown files/docstrings.

## Usage 

Let's say that you're using [mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/) for your documentation. Then you're 
writing down markdown to explain how your python packages works. It'd be 
great if you could run your unit tests against them. You can use this package
to write unit-tests for that. 

```python
import pathlib
import pytest

from mktestdocs import check_md_file


@pytest.mark.parametrize('fpath', pathlib.Path("docs").glob("**/.md"), ids=str)
def test_files_good(fpath):
    check_md_file(fpath=fpath)
```

You might also have docstrings written in markdown. Those can be easily checked
as well. 

```python
# I'm assuming that we've got a library called dinosaur
from dinosaur import roar, super_roar

import pytest
from mktestdocs import check_docstring

@pytest.mark.parametrize('func', [roar, super_roar], ids=lambda d: d.__name__)
def test_files_good(func):
    check_docstring(obj=func)
```

There's even some utilities for grab all the docstrings from classes that you've defined. 

```python
# I'm assuming that we've got a library called dinosaur
from dinosaur import Dinosaur

import pytest
from mktestdocs import check_docstring, get_codeblock_members

members = get_codeblock_members(Dinosaur)

@pytest.mark.parametrize("obj", members, ids=lambda d: d.__qualname__)
def test_member(obj):
    check_docstring(obj)
```
