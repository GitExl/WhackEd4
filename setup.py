import sys
import os
from cx_Freeze import setup, Executable

paths = []
paths.extend(sys.path)
paths.append('whacked4')

build_exe_options = {
	'packages': [],
	'path': paths,
	'include_files': ['res', 'cfg', 'LICENSE', 'README'],
	'optimize': 2,
	'compressed': True,
	'icon': 'res/icon-hatchet.ico',
	'include_msvcr': True
}
build_exe_options['path'].append('src')

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(
	'whacked4/main.py',
	base=base,
	targetName=os.environ['app_name_lower'] + '.exe'
)

setup(
	name = os.environ['app_title'],
	version = os.environ['app_version_value'],
	description = os.environ['app_description'],
	options = {'build_exe': build_exe_options},
	executables = [exe]
)