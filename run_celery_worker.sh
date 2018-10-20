#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd evaldas

su -m myuser -c "celery -A evaldas worker -l info"
