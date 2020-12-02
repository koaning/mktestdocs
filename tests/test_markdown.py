import pathlib
import pytest

from mktestdocs import check_md_file


@pytest.mark.parametrize('fpath', [str(p) for p in pathlib.Path("data/good").glob("*.md")])
def test_files_good(fpath):
    check_md_file(fpath=fpath)


@pytest.mark.parametrize('fpath', [str(p) for p in pathlib.Path("data/good").glob("*.md")])
def test_files_bad(fpath):
    with pytest.raises(Exception):
        check_md_file(fpath=fpath)
