# Generated by Django 2.1.2 on 2018-10-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, db_index=True)),
                ('link', models.CharField(max_length=256)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField()),
                ('category', models.CharField(db_index=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=256)),
                ('country', models.CharField(max_length=64)),
            ],
        ),
    ]
