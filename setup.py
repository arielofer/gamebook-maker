from setuptools import setup


description = """a library containing classes and functions so you could
build your own gamebook easily"""

setup(
    name="gamebook-maker",
    version="0.0.1",
    description="build your own gamebook with python",
    long_description=description,
    long_description_content_type="text",
    url="https://github.com/arielofer/gamebook-maker",
    author="Ariel Ofer",
    packages=["gamebook"],
)
