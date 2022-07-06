@echo off
cls
echo ^[[32mBatch ^>^> Starting...^[[0m

:main
py main.py
echo ^[[32mBatch ^>^> Bot Crash^[[0m 
goto main