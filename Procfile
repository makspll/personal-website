release: python manage.py migrate
web: gunicorn personal_site.wsgi --capture-output --enable-stdio-inheritance --log-file -