@echo off
title Jipu Setup by OniQuinox Team
color 12
echo Are you sure to install required program for Jipu Simulator ?
echo Warning When the setup of python start be sure to tick the "ADD python to PATH"
echo (yes/no)
set /p input=

if %input% == yes goto ok
if %input% == no goto close

:ok
start programs\python_installer_3.1.0.exe

cls
echo Press 5 times any keyboard key to install Python required library
echo You can do this if the python install is completed
echo 5 times left
pause
cls
echo Press 5 times any keyboard key to install Python required library
echo You can do this if the python install is completed
echo 4 times left
pause
cls
echo Press 5 times any keyboard key to install Python required library
echo You can do this if the python install is completed
echo 3 times left
pause
cls
echo Press 5 times any keyboard key to install Python required library
echo You can do this if the python install is completed
echo 2 times left
pause
cls
echo Press 5 times any keyboard key to install Python required library
echo You can do this if the python install is completed
echo 1 times left
pause
start programs\pipLibraryInstaller

:close