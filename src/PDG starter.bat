@echo off
cls
pushd %0\..
title PDG for Minecraft Starter
goto start

:install
cd bin
if exist C:\Windows\py.exe (
	py colorama\setup.py install > nul
	py demjson\setup.py install > nul
) else (
	echo Python 3.5 is not installed.
	pause
	exit /b
)
goto start

:dh
cls
echo -------------------------
echo PDG for Minecraft Starter
echo by I_am_4a
echo Version 1
echo -------------------------
echo;
exit /b

:start
call :dh
echo 1.Install(Required)
echo 2.Run
echo 3.End
choice /c 123 >nul
set el=%errorlevel%
if %el% == 1 goto install
if %el% == 2 goto run
if %el% == 3 goto :eof

:run
call :dh
echo Input your lookup player name.
set /p "name=MCID-->"
goto runpy

:runpy
call :dh
echo Running...
start /wait cmd /c bin\py get.py %name%
echo Stopping...
echo Stopped.
echo;
echo One more time?(Y/N)
choice /c yn /d n /t 10 >nul
set el=%errorlevel%
if %el% == 1 goto run
goto :eof