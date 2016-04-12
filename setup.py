# -*- coding: utf8 -*-

try:
    from setuptools.core import setup
    setup
except ImportError:
    from distutils.core import setup
    

setup (
       name = 'ukpc',
       version = '1.0',
       author = 'Jorge Quiterio',
       author_mail = 'jquiterio00@gmail.com',
       packages = ['ukpc'],
       description = 'UK Post Code Format and Validation',
       url = 'http://guithub.com/jquiterio/ukpc',
       license = open('LICENSE').read(),
       long_description=open('README.md').read()
       )
