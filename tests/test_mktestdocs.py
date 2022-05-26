import pathlib

from mktestdocs import check_md_file

def test_readme(monkeypatch):
    test_dir = pathlib.Path(__file__).parent
    fpath = test_dir.parent / "README.md"
    monkeypatch.chdir(test_dir)

    check_md_file(fpath=fpath)
