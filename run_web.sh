#!/usr/bin/env bash

sed -i 's%amqp://localhost%amqp://rabbit%g' evaldas/settings.py
python manage.py makemigrations
python manage.py migrate
supervisord -n
usr/bin/supervisord -c /etc/supervisord.conf