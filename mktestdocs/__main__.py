import inspect
import textwrap


def get_class_docstrings(*classes):
    """
    Grabs the docstrings of any methods of any classes that are passed in.
    """
    results = []
    for cl in classes:
        members = inspect.getmembers(cl)
        for n, m in members:
            if m.__doc__:
                results.append((f"{cl.__name__}.{n}", m.__doc__))
    return results


def check_codeblock(block, lang="python"):
    """
    Cleans the found codeblock and checks if the proglang is correct.

    Returns an empty string if the codeblock is deemed invalid.

    Arguments:
        block: the code block to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    first_line = block.split("\n")[0]
    if lang:
        if first_line[3:] != lang:
            return ""
    return "\n".join(block.split("\n")[1:])


def grab_code_blocks(docstring, lang="python"):
    """
    Given a docstring, grab all the markdown codeblocks found in docstring.

    Arguments:
        docstring: the docstring to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    docstring = textwrap.dedent(docstring)
    in_block = False
    block = ''
    codeblocks = []
    for idx, line in enumerate(docstring.split("\n")):
        if line.startswith("```"):
            if in_block:
                codeblocks.append(check_codeblock(block, lang=lang))
                block = ''
            in_block = not in_block
        if in_block:
            block += line + '\n'
    return [c for c in codeblocks if c != '']


def check_docstring(obj):
    """
    Given a function, test the contents of the docstring.
    """
    for b in grab_code_blocks(obj.__doc__):
        try:
            exec(b, {"__MODULE__": "__main__"})
        except Exception:
            print(f"Error Encountered in `{obj.__name__}`. Caused by:\n")
            print(b)
            raise