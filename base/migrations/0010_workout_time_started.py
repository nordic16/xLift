# Generated by Django 4.0.6 on 2022-07-31 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_exset_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='time_started',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 31, 15, 53, 40, 931642)),
        ),
    ]
