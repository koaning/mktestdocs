import importlib.metadata
from .__main__ import (
    register_executor,
    check_codeblock,
    grab_code_blocks,
    check_docstring,
    check_md_file,
    get_codeblock_members,
)

__version__ = importlib.metadata.version("mktestdocs")

__all__ = [
    "__version__",
    "register_executor",
    "check_codeblock",
    "grab_code_blocks",
    "check_docstring",
    "check_md_file",
    "get_codeblock_members",
]
