# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

"""
This is a setup script for py2exe.

Usage: python setup_py2exe.py py2exe

Tested with py2exe 0.6.9 (latest available version for Python 2.x on 2015-02-23, released on 2008-11-16).
Environment: Python Portable 2.7.6.1. on Windows 7 32bit.
"""

# Import program components / modules from python standard library / non-standard modules.
from distutils.core import setup

import py2exe  # may show up as unused import in your IDE but is correct this way

# Not all possible metadata is put in the final executable:
# https://docs.python.org/2/distutils/setupscript.html#additional-meta-data

setup(
    name='wxPython Freezing Template',                                       # Appears in file properties in Windows
    version='1.2.3.4',                                                       # Appears in file properties in Windows
    description='The resulting *.exe from the wxPython Freezing Template.',  # Appears in file properties in Windows
    author='Guenther Eberl',                                                 # Does not appear in file properties in Windows
    author_email='guenther@eberl.se',                                        # Does not appear in file properties in Windows
    license='GNU GENERAL PUBLIC LICENSE, Version 2, June 1991',              # Does not appear in file properties in Windows
    url='http://www.eberl.se/',                                              # Does not appear in file properties in Windows
    options={'py2exe':
                 {
                     'optimize': 2,                                          # Optimization level, 2 is max
                     'bundle_files': 1,                                      # Bundle dlls in zipfile or exe or not at all
                 }},
    console=[],                                                              # List of scripts to convert into console exes
    windows=[
        {
            'script': 'main.py',                                             # List of scripts to convert into GUI exes
            'icon_resources': [(1, "icon.ico")]                              # Icon file to use for exe
        }],
    data_files=['icon.ico',                                                  # Files to copy over
                'logging_to_file.ini',
                'logging_to_terminal.ini',
                'logging_to_terminal_and_file.ini',
                ],
    zipfile=None,                                                            # Name of shared zip file to bundle files in, if set to None files will be bundled within the exe
)