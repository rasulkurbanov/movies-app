# Generated by Django 3.2.3 on 2021-05-19 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]