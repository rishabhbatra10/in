from india import __version__, __appname__

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__appname__,
    version=__version__,
    author="Rishabh Batra",
    author_email="ribhu.1996@gmail.com",
    description="India's states and cities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishabhbatra10/india",
    package_data={'india': ['data/*']},
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
