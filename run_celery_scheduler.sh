#!/bin/sh

# wait for RabbitMQ server to start
sleep 15

cd evaldas

su -m myuser -c "celery -A evaldas beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler"
