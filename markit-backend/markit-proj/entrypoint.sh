#!/bin/sh
sleep 5
python /code/manage.py makemigrations
python /code/manage.py migrate --noinput
python /code/manage.py collectstatic
python /code/manage.py runserver 0.0.0.0:8000
