#!/usr/bin/env bash

sleep 5

cd evaldas

python manage.py makemigrations evaldas

python manage.py migrate

python manage.py runserver 8000
