#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():

    # Reads .env file in main project directory 
    # so that they can be accessed in 
    # the entire project using os.getenv or os.environ
    # could flip out on deployments without .env file
    dotenv_file = os.path.join(".env")
    if os.path.isfile(dotenv_file):
        from dotenv import load_dotenv
        load_dotenv(verbose=True,override=True)
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_site.settings')

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
