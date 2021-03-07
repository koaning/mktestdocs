<img src="icon.png" width=125 height=125 align="right">

# mktestdocs

Run pytest against markdown files/docstrings.

# Installation 

```python
pip install mktestdocs
```

## Usage 

Let's say that you're using [mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/) for your documentation. Then you're 
writing down markdown to explain how your python packages works. It'd be 
great if you could run your unit tests against them. You can use this package
to write unit-tests for that. 

```python
import pathlib
import pytest

from mktestdocs import check_md_file

# Note the use of `str`, makes for pretty output
@pytest.mark.parametrize('fpath', pathlib.Path("docs").glob("**/*.md"), ids=str)
def test_files_good(fpath):
    check_md_file(fpath=fpath)
```

This will take any codeblock that starts with *\`\`\`python* and run it, checking
for any errors that might happen. This means that if your docs contain asserts, that
you get some unit-tests for free! 

<details>
    <summary><b>Details on `check_md_file`.</b></summary>
    <br>
    Let's suppose that you have the following markdown file: 

    This is a code block

    ```python
    from operator import add
    a = 1 
    b = 2
    ```

    This code-block should run fine.

    ```python
    assert add(1, 2) == 3
    ```

Then in this case the second code-block depends on the first code-block. The standard settings of `check_md_file` assume that each code-block needs to run independantly. If you'd like to test markdown files with these sequential code-blocks be sure to set `memory=True`. 

```python
# Assume that cell-blocks are independant.
check_docstring(fpath=fpath)

# Assumes that cell-blocks depend on eachother.
check_docstring(fpath=fpath, memory=True)
```
</details>
<br>


## Markdown in Docstrings

You might also have docstrings written in markdown. Those can be easily checked
as well. 

```python
# I'm assuming that we've got a library called dinosaur
from dinosaur import roar, super_roar

import pytest
from mktestdocs import check_docstring

# Note the use of `__name__`, makes for pretty output
@pytest.mark.parametrize('func', [roar, super_roar], ids=lambda d: d.__name__)
def test_docstring(func):
    check_docstring(obj=func)
```

There's even some utilities for grab all the docstrings from classes that you've defined. 

```python
# I'm assuming that we've got a library called dinosaur
from dinosaur import Dinosaur

import pytest
from mktestdocs import check_docstring, get_codeblock_members

# This retreives all methods/properties with a docstring.
members = get_codeblock_members(Dinosaur)

# Note the use of `__qualname__`, makes for pretty output
@pytest.mark.parametrize("obj", members, ids=lambda d: d.__qualname__)
def test_member(obj):
    check_docstring(obj)
```

When you run these commands via `pytest --verbose` you should see informative test info being run. 

If you're wondering why you'd want to write markdown in a docstring feel free to check out [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings).
