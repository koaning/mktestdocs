black:
	black mktestdocs tests setup.py

test:
	pytest

check: black test

install:
	uv pip install -e ".[test]"

pypi:
	uv build
	uv publish
