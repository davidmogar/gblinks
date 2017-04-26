#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'markdown',
    'lxml'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='gblinks',
    version='0.2.0',
    description="Python tool to list and check GitBook links",
    long_description=readme + '\n\n' + history,
    author="David Moreno García",
    author_email='david.mogar@gmail.com',
    url='https://github.com/davidmogar/gblinks',
    packages=[
        'gblinks',
    ],
    package_dir={'gblinks':
                 'gblinks'},
    entry_points={
        'console_scripts': [
            'gblinks=gblinks.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
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
    ],
    test_suite='tests',
    tests_require=test_requirements
)
