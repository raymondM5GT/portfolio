web: gunicorn portfoliosite.wsgi:Base --log-file -
python manage.py collectstatic --noinput
manage.py migrate
