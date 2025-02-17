@echo off
python -m venv venv-pymlsuite
call venv-pymlsuite\Scripts\activate
pip install -r requirements.txt
echo Virtual environment and dependencies installed.