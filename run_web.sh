#!/bin/sh

sleep 5

cd evaldas

su -m myuser -c "python manage.py makemigrations evaldas"

su -m myuser -c "python manage.py migrate"

su -m myuser -c "python manage.py runserver 8000"
