#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
supervisord -n
usr/bin/supervisord -c /etc/supervisord.conf