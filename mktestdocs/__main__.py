import inspect
import pathlib
import textwrap


def exec_python(source):
    """Exec the python source given in a new module namespace

    Does not return anything, but exceptions raised by the source
    will propagate out unmodified
    """
    try:
        exec(source, {"__MODULE__": "__main__"})
    except Exception:
        print(source)
        raise


executors = {
    # default executor
    "": exec_python,
    "python": exec_python,
}


def get_codeblock_members(*classes):
    """
    Grabs the docstrings of any methods of any classes that are passed in.
    """
    results = []
    for cl in classes:
        if cl.__doc__:
            results.append(cl)
        for name, member in inspect.getmembers(cl):
            if member.__doc__:
                results.append(member)
    return [m for m in results if len(grab_code_blocks(m.__doc__)) > 0]


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
    block = ""
    codeblocks = []
    for idx, line in enumerate(docstring.split("\n")):
        if line.startswith("```"):
            if in_block:
                codeblocks.append(check_codeblock(block, lang=lang))
                block = ""
            in_block = not in_block
        if in_block:
            block += line + "\n"
    return [c for c in codeblocks if c != ""]


def check_docstring(obj, lang=""):
    """
    Given a function, test the contents of the docstring.
    """
    executor = executors[lang]
    for b in grab_code_blocks(obj.__doc__, lang=lang):
        executor(b)


def check_raw_string(raw, lang="python"):
    """
    Given a raw string, test the contents.
    """
    executor = executors[lang]
    for b in grab_code_blocks(raw, lang=lang):
        executor(b)


def check_raw_file_full(raw, lang="python"):
    executor = executors[lang]
    all_code = ""
    for b in grab_code_blocks(raw, lang=lang):
        all_code = f"{all_code}\n{b}"
    executor(all_code)


def check_md_file(fpath, memory=False, lang="python"):
    """
    Given a markdown file, parse the contents for python code blocks
    and check that each independent block does not cause an error.

    Arguments:
        fpath: path to markdown file
        memory: whether or not previous code-blocks should be remembered
    """
    text = pathlib.Path(fpath).read_text()
    if not memory:
        check_raw_string(text, lang=lang)
    else:
        check_raw_file_full(text, lang=lang)
