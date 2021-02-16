#!/usr/bin/env python
'''Django's command-line utility for administrative tasks.'''
import os
import sys
from django.core.exceptions import ImproperlyConfigured

def check_key(key):
    if not os.environ.get(key):
        raise ImproperlyConfigured(
            'Configure the $env:%s in scripts/activate.ps1' % key
        )

def check_env():
    check_key('DJANGO_SECRET_KEY')
    check_key('DJANGO_FHIR_APP_ID')
    check_key('DJANGO_FHIR_API_BASE')
    check_key('DJANGO_FHIR_CLIENT_ID')
    check_key('DJANGO_FHIR_REDIRECT_URI')

def main():
    '''Run administrative tasks.'''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            '''Couldn't import Django. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?'''
        ) from exc
    check_env()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
