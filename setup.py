# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-mtoce",  # the name that you will install via pip
    version="1.0",
    author="Michael Toce",
    author_email="mtoce@villanova.edu",
    description="A package of helper functions!",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    # license="MIT",
    url="https://github.com/mtoce/lambdata-mtoce",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
