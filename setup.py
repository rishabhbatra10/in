""" Setup file for the Module India """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com

# external imports
from setuptools import setup, find_packages

# module imports
from india import __version__, __appname__

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=__appname__,
    version=__version__,
    author="Rishabh Batra",
    author_email="rishabhbatra1002@gmail.com",
    description="India's states and cities",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/rishabhbatra10/in",
    package_data={'india': ['data/*']},
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
