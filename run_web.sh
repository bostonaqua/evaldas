#!/usr/bin/env bash

cd evaldas
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000