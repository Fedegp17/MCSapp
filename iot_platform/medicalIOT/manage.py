#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""Main sript that needs to be executed with the command 'python manage.py runserver' once the virtual environment
   has been activated. Currently the main folder is 'medicalIOT' and the application folder (where the backend and 
   front end should be held is 'IoTCloud'.
  -django
  -autopep8 
   
   """


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicalIOT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
