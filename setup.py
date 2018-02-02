#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from JSONLibrary.version import VERSION

requirements = [
    'tox',
    'coverage',
    'robotframework>=3.0',
    'jsonpath-rw==1.4.0',
    'jsonpath-rw-ext>=0.1.9'
]

test_requirements = [
    # TODO: put package test requirements here
]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-jsonlibrary-py3',
    version=VERSION,
    description="robotframework-jsonlibrary is a Robot Framework test library for manipulating JSON Object. You can manipulate your JSON object using JSONPath",
    author="",
    author_email='',
    url='https://github.com/anuchit-tn/robotframework-jsonlibrary-py3.git',
    packages=[
        'JSONLibrary'
    ],
    package_dir={'robotframework-jsonlibrary-py3':
                 'JSONLibrary'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='robotframework-jsonlibrary-py3',
    classifiers=CLASSIFIERS.splitlines()
)
