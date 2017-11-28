#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='twit_cli',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'pytest',
        'python-twitter',
        'pyyaml',
    ],
)
