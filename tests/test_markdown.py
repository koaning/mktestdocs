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
