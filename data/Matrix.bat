@echo off
color 0A
echo do you want to launch matrix.exe
echo (YES/NO)
set /p input=
cls

if %input%== yes goto matrix
if %input%== no goto shut

:matrix
echo Click To launch Matrix
pause
:re
echo %Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%%Random%
goto re


