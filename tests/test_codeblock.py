import pytest

from mktestdocs import check_codeblock, grab_code_blocks

exibit_a = """
This is an example docstring. 

Arguments:
    a: a parameter 
    
There is no example
"""

exibit_b = """
This is an example docstring. 

Arguments:
    a: a parameter 

```python
assert 1 == 1
```
"""

exibit_c = """
This is an example docstring. 

Arguments:
    a: a parameter 

```
assert 1 == 1
```

```python
assert 1 == 1
```
"""


@pytest.mark.parametrize(
    "doc, n",
    [(exibit_a, 0), (exibit_b, 1), (exibit_c, 1)],
    ids=["exibit_a", "exibit_b", "exibit_c"],
)
def test_number_of_codeblocks(doc, n):
    assert len(grab_code_blocks(doc, lang="python")) == n


@pytest.mark.parametrize(
    "doc, n",
    [(exibit_a, 0), (exibit_b, 1), (exibit_c, 2)],
    ids=["exibit_a", "exibit_b", "exibit_c"],
)
def test_number_of_codeblocks_any(doc, n):
    assert len(grab_code_blocks(doc, lang=None)) == n
