# Trend news from CNN

## Shows news related to search requests from Google Trends


### Used technologies:
* Framework: Django
* AMQP: RabbitMQ
* Task Queue: Celery

### Description:

Service have following functionality: 
* Updating own database from RSS external resource (CNN, Google Trends)
* Matching data for creating actual articles list
* Immediate update and scheduled update

### Deployment:

Clone project from GitHub:

```angular2html
git clone https://github.com/bostonaqua/evaldas.git
```

In project directory run docker-compose:

```angular2html
docker-compose build --no-cache
docker-compose up -d
```

Open your browser and go to URL:
```angular2html
http://localhost:8000/
```