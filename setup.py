import sys
import os
from setuptools import setup, find_packages

try:
    from setuptools import setup
    from setuptools import Command
    from setuptools import Extension
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


REQUIRES = [
    "biopython",
    "pandas",
]


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup_args = dict(

    # About package
    name = 'ab1_organizer',
    version = '1.0.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['AB1', 'Sanger Sequencing', 'Phylogenetics', 'DNA'],
    url = 'https://github.com/sgelias/AbiOrganizer.git',
    packages = find_packages(),
    package_dir={'ab1_organizer': 'ab1_organizer'},
    include_package_data = False,

    # About author
    author = 'Samuel Galvão Elias',
    author_email = 'sgelias@outlook.com',

    # Language and Licence
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


if __name__ == '__main__':
    setup(**setup_args, install_requires=REQUIRES)
