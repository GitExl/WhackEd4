set app_title=WhackEd4
set app_description=A Windows Dehacked editor.

set app_name=WhackEd4
set app_name_lower=whacked4

set app_version=1.1.0
set app_version_value=1.1.0
set app_version_title=1.1.0

set build_path=".\build\exe.win32-2.7"

set python_interpreter="c:\python27\python.exe"
set setup_compiler="C:\Program Files (x86)\Inno Setup 5\ISCC.exe"
set zip=7zr


rmdir .\build /S /Q
%python_interpreter% setup.py build

del %app_name_lower%-setup-*.exe
%setup_compiler% %app_name_lower%.iss

del %app_name_lower%-*.7z
%zip% a %app_name_lower%-%app_version%.7z %build_path%\* -r -mx=9 -ms=on

pause