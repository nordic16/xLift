# Generated by Django 4.0.2 on 2022-02-19 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifter',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 2, 19, 21, 1, 57, 421230, tzinfo=utc)),
        ),
    ]
