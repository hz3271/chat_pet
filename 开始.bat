@echo off
python -m venv venv
call venv\Scripts\activate
python mukuchi_UI_ADDTEXT.py 1>nul
pause