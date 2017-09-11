#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

version = re.search(
    '^__version__\s*=\s*\'(.*)\'',
    open('gblinks/__init__.py').read(),
    re.M).group(1)

setup(
    name='gblinks',
    version=version,
    description="Python tool to find out broken GitBook links",
    long_description=open('README.rst').read(),
    author="David Moreno García",
    author_email='david.mogar@gmail.com',
    url='https://github.com/davidmogar/gblinks',
    packages=[
        'gblinks',
    ],
    package_dir={
        'gblinks': 'gblinks'
    },
    entry_points={
        'console_scripts': [
            'gblinks=gblinks.cli:main'
        ]
    },
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='gblinks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
