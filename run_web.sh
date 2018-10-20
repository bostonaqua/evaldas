#!/usr/bin/env bash

cd evaldas
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
