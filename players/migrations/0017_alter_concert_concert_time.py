# Generated by Django 4.2.5 on 2023-09-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0016_player_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_time',
            field=models.DateTimeField(default=None),
        ),
    ]
