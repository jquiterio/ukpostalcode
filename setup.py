#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    

setup(
    name='ukpostalcode',
    version=1.3,
    author='Jorge Quiterio',
    author_mail='eu@jquiterio.eu',
    py_modules=['ukpostalcode'],
    description='UK postal code format, validation and details',
    url='https://pypi.org/project/ukpostalcode',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)