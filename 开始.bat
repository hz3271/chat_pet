@echo off
python -m venv venv
call venv\Scripts\activate
python w11.py 1>nul
pause