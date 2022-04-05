black:
	black mktestdocs tests setup.py

test:
	pytest

check: black test

install:
	python -m pip install -e ".[test]"

pypi:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
