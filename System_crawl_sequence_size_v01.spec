# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['System_crawl_sequence_size_v01.py'],
             pathex=['C:\\Users\\rpdacosta\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\qtmodern', 'F:\\DC_programming\\System_crawl_sequence_size_v01\\System_crawl_sequence_size'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='System_crawl_sequence_size_v01',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='favicon-32x32.ico')
