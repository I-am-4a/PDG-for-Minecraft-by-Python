@echo off
cls
pushd %0\..
cd bin

set n=0
py demjson-2.2.4\setup.py install > lib_install.log
echo Installing... %n% %
set n=50
py colorama-0.3.9\setup.py install > lib_install.log
set n=100
echo Installing... %n% %
echo Successfully installed.
pause
popd
rd /s /q libs
cmd /c del %0
goto :eof