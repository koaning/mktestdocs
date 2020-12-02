from mktestdocs import __version__
from setuptools import setup, find_packages

test_packages = ["flake8>=3.6.0", "pytest>=4.0.2", "numpy>=1.19.4", "exdown>=0.7.1"]

setup(
    name="mktestdocs",
    version=__version__,
    packages=find_packages(exclude=["notebooks"]),
    install_requires=[],
    extras_require={
        "test": test_packages,
    },
)
