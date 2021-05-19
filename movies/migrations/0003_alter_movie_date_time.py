# Generated by Django 3.2.3 on 2021-05-19 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
