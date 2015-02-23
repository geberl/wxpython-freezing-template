# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=['C:\\pycharm_projects\\wxpython_freezing_template'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='setup_pyinstaller_version.txt', icon='icon.ico')
