# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

"""
This is a setup script for cx_Freeze.

Usage: python setup_cx_freeze.py build

Tested with cx_Freeze 4.3.4 (latest available version for Python 2.7 on 2015-02-23, released on 2014-12-26).
Environment: Python Portable 2.7.6.1. on Windows 7 32bit.
"""

# Import program components / modules from python standard library / non-standard modules.
import sys

from cx_Freeze import setup, Executable


base = 'Win32GUI' if sys.platform == 'win32' else None  # build a Windows GUI application
icon = 'icon.ico'

executables = [
    Executable(script='main.py',
               initScript=None,
               base=base,
               targetDir=None,
               targetName='main.exe',
               compress=True,
               copyDependentFiles=True,
               appendScriptToExe=False,
               appendScriptToLibrary=False,
               icon=icon)
]

packages = []
includes = []
excludes = ['Tkinter']
include_files = ['icon.ico', 'logging_to_file.ini', 'logging_to_terminal.ini', 'logging_to_terminal_and_file.ini']
path = []
build_options = dict(packages=packages, includes=includes, excludes=excludes, include_files=include_files, path=path)

setup(name='wxPython Freezing Template',
      version='1.2.3.4',
      description='The resulting *.exe from the wxPython Freezing Template.',
      author='Guenther Eberl',
      author_email='guenther@eberl.se',
      license='GNU GENERAL PUBLIC LICENSE, Version 2, June 1991',
      url='http://www.eberl.se/',
      options=dict(build_exe=build_options),
      executables=executables)
