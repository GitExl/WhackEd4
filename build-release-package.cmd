set app_title=WhackEd4
set app_description=A Windows Dehacked editor.

set app_name=WhackEd4
set app_name_lower=whacked4

set app_version=1.2.4
set app_version_value=1.2.4
set app_version_title=1.2.4

set build_path=".\build\exe.win32-3.7"

set python_interpreter=py -3
set setup_compiler="C:\Program Files (x86)\Inno Setup 5\ISCC.exe"
set zip=7za


rmdir .\build /S /Q
%python_interpreter% setup.py build
del %build_path%\lib\libcrypto-1_1.dll /S /Q
del %build_path%\lib\libssl-1_1.dll /S /Q
del %build_path%\lib\unicodedata.pyd /S /Q
rmdir %build_path%\lib\pydoc_data /S /Q
rmdir %build_path%\lib\unittest /S /Q
rmdir %build_path%\lib\xml /S /Q
rmdir %build_path%\lib\wx\py /S /Q
rmdir %build_path%\lib\wx\tools /S /Q
rmdir %build_path%\lib\wx\locale /S /Q

del %app_name_lower%-setup-*.exe /S /Q
%setup_compiler% %app_name_lower%.iss

del %app_name_lower%-*.7z /S /Q
%zip% a %app_name_lower%-%app_version%.7z %build_path%\* -r -mx=9 -ms=on

pause
