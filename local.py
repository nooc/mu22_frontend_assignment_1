# pylint: disable=missing-module-docstring
import sys
from os import environ, system
from os.path import join

sass_file = ['sass','style.scss']
css_file = ['www','css','style.css']

SERVER_STR = 'uvicorn --reload --host localhost --port 8080 app.main:application'
SASS_STR = f'sass {join(*sass_file)} {join(*css_file)}'

def run():
    '''Rum main'''
    try:
        # Run sass
        system(SASS_STR)
        # Run server
        system(SERVER_STR)
    except KeyboardInterrupt:
        print('User exit. Bye.')

if __name__ == "__main__":
    if '.venv' in sys.executable:
        run()
    else:
        print('Please run in virtual env.')
