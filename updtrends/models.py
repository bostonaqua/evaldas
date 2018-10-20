from django.db import models


class Post(models.Model):
    title = models.TextField(blank=True, db_index=True)
    link = models.CharField(max_length=256, unique=True)
    body = models.TextField(blank=True, db_index= True)
    date_pub = models.DateTimeField()
    category = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.title


class Trend(models.Model):
    title = models.CharField(max_length=256, db_index=True)
    country = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class ActualNews(models.Model):
    title = models.TextField(blank=True, db_index=True)
    link = models.CharField(max_length=256, unique=True)
    date_pub = models.DateTimeField()
    trend_name = models.CharField(max_length=256, db_index=True)
    category = models.CharField(max_length=64, db_index=True)
    country = models.CharField(max_length=64)
    priority = models.IntegerField()

    def __str__(self):
        return '{} ## {}'.format(self.title, self.trend_name)
