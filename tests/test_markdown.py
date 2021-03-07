import pathlib
import pytest

from mktestdocs import check_md_file


@pytest.mark.parametrize("fpath", pathlib.Path("tests/data/good").glob("*.md"), ids=str)
def test_files_good(fpath):
    check_md_file(fpath=fpath)


@pytest.mark.parametrize("fpath", pathlib.Path("tests/data/bad").glob("*.md"), ids=str)
def test_files_bad(fpath):
    with pytest.raises(Exception):
        check_md_file(fpath=fpath)


def test_big_files_good():
    """Confirm that we can deal with multi-cell markdown cells."""
    check_md_file(fpath="tests/data/big-good.md", memory=True)


def test_big_file_independant():
    """Confirm that different files don't influence eachother."""
    check_md_file(fpath="tests/data/big-good.md", memory=True)
    with pytest.raises(Exception):
        check_md_file(fpath="tests/data/big-bad.md", memory=True)