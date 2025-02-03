# Generated by Django 4.1.2 on 2023-08-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 - Bad'), (2, '2 - Sufficient'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')]),
        ),
    ]
