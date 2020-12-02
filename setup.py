from mktestdocs import __version__
from setuptools import setup, find_packages

test_packages = ["pytest>=4.0.2"]

setup(
    name="mktestdocs",
    version=__version__,
    packages=find_packages(exclude=["notebooks"]),
    install_requires=[],
    extras_require={
        "test": test_packages,
    },
)
