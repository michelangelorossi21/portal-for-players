# Generated by Django 4.1.2 on 2023-08-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_remove_player_date_of_insert_remove_review_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(default=None, verbose_name='Date of birth'),
        ),
    ]
