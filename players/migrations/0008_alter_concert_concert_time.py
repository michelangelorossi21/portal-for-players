# Generated by Django 4.1.2 on 2023-08-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_concert_concert_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_time',
            field=models.DateTimeField(default=None, verbose_name='Date and time'),
        ),
    ]
