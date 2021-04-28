import pathlib
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

description = """a library containing classes and functions so you could
build your own gamebook easily"""

setup(
    name="gamebook-maker",
    version="0.2.0",
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/arielofer/gamebook-maker",
    author="Ariel Ofer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gamebook"],
)
