# pylint: disable=missing-module-docstring
import sys
from os import environ, system

EXE_STR = r'uvicorn --reload --host localhost --port 8080 app.main:application'
ENV = {
    'CREDENTIALS_JSON':'micro-services-378415-83c3c6430e0a.json',
    'GOOGLE_CLOUD_PROJECT':'micro-services-378415',
    'LOCAL_RUN':'true'
}

def run():
    '''Rum main'''
    for key,value in ENV.items():
        environ[key] = value
    try:
        system(EXE_STR)
    except KeyboardInterrupt:
        print('User exit. Bye')

if __name__ == "__main__":
    if '.venv' in sys.executable:
        run()
    else:
        print('Please run using projects virtual env.')
