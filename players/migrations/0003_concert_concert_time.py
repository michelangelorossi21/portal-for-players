# Generated by Django 4.1.2 on 2023-08-06 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_date_of_birth_player_date_of_insert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='concert_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date and time'),
        ),
    ]
