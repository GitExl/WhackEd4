import sys
import os
from cx_Freeze import setup, Executable

paths = []
paths.extend(sys.path)
paths.append('src')

build_exe_options = {
	'path': paths,
	'packages': ['whacked4'],
	'include_files': ['res', 'cfg', 'docs', 'LICENSE', 'README.md'],
	'optimize': 2,
	'include_msvcr': True
}

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'

exe = Executable(
	'src/main.py',
	base=base,
	target_name=os.environ['app_name_lower'] + '.exe',
	icon='res/icon-hatchet.ico'
)

setup(
	name=os.environ['app_title'],
	version=os.environ['app_version_value'],
	description=os.environ['app_description'],
	options={'build_exe': build_exe_options},
	executables=[exe],
	requires=['pyaudio', 'wx']
)
