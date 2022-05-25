import pathlib
import pytest
from shutil import which
from unittest.mock import Mock

from mktestdocs import check_md_file, register_executor
from mktestdocs.__main__ import exec_bash


@pytest.mark.parametrize("fpath", pathlib.Path("tests/data/good").glob("?.md"), ids=str)
def test_files_good(fpath):
    check_md_file(fpath=fpath)


def test_files_bad():
    fpath = pathlib.Path("tests") / "data" / "bad" / "a.md"
    with pytest.raises(Exception):
        check_md_file(fpath=fpath)


def test_big_files_good():
    """Confirm that we can deal with multi-cell markdown cells."""
    check_md_file(fpath="tests/data/good/big-good.md", memory=True)


def test_big_file_independant():
    """Confirm that different files don't influence each other."""
    check_md_file(fpath="tests/data/good/big-good.md", memory=True)
    with pytest.raises(Exception):
        check_md_file(fpath="tests/data/bad/big-bad.md", memory=True)


@pytest.mark.skipif(which("bash") is None, reason="No bash shell available")
@pytest.mark.parametrize("fpath", pathlib.Path("tests/data/good").glob("?.md"), ids=str)
def test_files_good_bash(fpath):
    check_md_file(fpath=fpath, lang="bash")


@pytest.mark.skipif(which("bash") is None, reason="No bash shell available")
def test_files_bad_bash():
    fpath = pathlib.Path("tests") / "data" / "bad" / "b.md"
    with pytest.raises(Exception):
        check_md_file(fpath=fpath, lang="bash")


@pytest.mark.skipif(which("bash") is None, reason="No bash shell available")
def test_big_files_good_bash():
    fpath = pathlib.Path("tests") / "data" / "good" / "big-good.md"
    check_md_file(fpath=fpath, memory=True, lang="bash")


@pytest.mark.skipif(which("bash") is None, reason="No bash shell available")
def test_big_file_independant_bash():
    fdir = pathlib.Path("tests") / "data"
    check_md_file(fpath=fdir / "good" / "big-good.md", memory=True, lang="bash")
    with pytest.raises(Exception):
        check_md_file(fpath=fdir / "bad" / "big-bad.md", memory=True, lang="bash")


def test_files_unmarked_language_default():
    fpath = pathlib.Path("tests") / "data" / "good" / "c.md"
    check_md_file(fpath, lang="")


@pytest.mark.skipif(which("bash") is None, reason="No bash shell available")
def test_files_unmarked_language_bash(temp_executors):
    fpath = pathlib.Path("tests") / "data" / "good" / "c.md"
    register_executor("", exec_bash)
    check_md_file(fpath, lang="")


def test_override_executor(temp_executors):
    fpath = pathlib.Path("tests") / "data" / "good" / "a.md"
    hijack = Mock()
    register_executor("python", hijack)
    check_md_file(fpath, lang="python")
    hijack.assert_called()
