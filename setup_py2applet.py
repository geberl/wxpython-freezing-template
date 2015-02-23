# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

"""
This is a setup script for py2applet.

Usage: python setup_py2applet.py py2app

Tested with py2app 0.9 (on 2015-02-23, released on 2014-07-27).
Environment: Python 2.7.8.1. on Mac OS X 10.10.2.
"""

# Import program components / modules from python standard library / non-standard modules.
from setuptools import setup


app = ['main.py']
data_files = ['logging_to_file.ini', 'logging_to_terminal.ini', 'logging_to_terminal_and_file.ini']
options = {'argv_emulation': True}

setup(
    app=app,
    data_files=data_files,
    options={'py2app': options},
    setup_requires=['py2app'],
)
