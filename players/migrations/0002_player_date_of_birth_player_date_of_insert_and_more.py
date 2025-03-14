# Generated by Django 4.1.2 on 2023-08-06 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='player',
            name='date_of_insert',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of insert'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('5', '5/5'), ('4', '4/5'), ('3', '3/5'), ('2', '2/5'), ('1', '1/5')]),
        ),
    ]
