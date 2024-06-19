#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='pylatex2',
    version='0.0.0a',
    description='',
    python_requires='>=3.6',
    package_dir={
        '': 'packages'
    },
    packages=setuptools.find_packages('packages'),
    # TODO
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    extras_require={
        'dev': []
    }
)
