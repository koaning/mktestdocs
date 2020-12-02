# mktestdocs

Run pytest against markdown files/docstrings.

## Usage 

Let's say that you're using [mkdocs]() for your documentation. Then you're 
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
import pytest

from mktestdocs import check_docstring

from custom_library import func1, func2

@pytest.mark.parametrize('func', [func1, func2], ids=lambda d: d.__name__)
def test_files_good(func):
    check_docstring(obj=func)
```

There's even some utilities for grab all the docstrings from classes that you've defined. 

```python
import pytest

from mktestdocs import check_docstring, get_class_docstring

from custom_library import ClassA, ClassB

@pytest.mark.parametrize('obj', [ClassA, ClassB], ids=lambda d: d.__name__)
def test_files_good(obj):
    for name, obj in get_class_docstrings(obj)
    check_docstring(obj=func)
```