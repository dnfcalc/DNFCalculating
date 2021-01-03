# -*- mode: python ; coding: utf-8 -*-

import os

spec_root = os.path.abspath(os.path.join(SPECPATH, '../'))

hideList = ['pkg_resources.py2_warn']
for fileName in os.listdir(r'./Part/'):
    if fileName.endswith(".py") and fileName!="__init__.py" and ("幽冥" not in fileName):
        hideList.append("Part."+fileName.replace(".py",""))

block_cipher = None

a = Analysis([spec_root+'\main.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=hideList,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon=spec_root+'\ResourceFiles\\img\\logo.ico')
