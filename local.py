# pylint: disable=missing-module-docstring
import sys
from os import environ, system

EXE_STR = r'uvicorn --reload --host localhost --port 8080 app.main:application'

def run():
    '''Rum main'''
    try:
        system(EXE_STR)
    except KeyboardInterrupt:
        print('User exit. Bye.')

if __name__ == "__main__":
    if '.venv' in sys.executable:
        run()
    else:
        print('Please run in virtual env.')
