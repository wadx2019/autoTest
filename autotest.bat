@echo off
echo wait for cloning..
python.exe %CD%\clone.py %1 %CD%\tmp %2
echo clone finished.
rd /s/q %CD%\tmp
echo removing..
echo wait for output..
python.exe output.py %2 %CD%\test.txt
echo output finished.
pause