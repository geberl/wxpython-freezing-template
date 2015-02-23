# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=['C:\\pycharm_projects\\wxpython_freezing_template'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='setup_pyinstaller_version.txt', icon='icon.ico')
coll = COLLECT(exe,
               [('logging_to_file.ini', 'logging_to_file.ini', 'DATA')],
               [('logging_to_terminal.ini', 'logging_to_terminal.ini', 'DATA')],
               [('logging_to_terminal_and_file.ini', 'logging_to_terminal_and_file.ini', 'DATA')],
               [('icon.ico', 'icon.ico', 'DATA')],
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main')
