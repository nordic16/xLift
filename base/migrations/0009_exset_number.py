# Generated by Django 4.0.3 on 2022-07-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_workout_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='exset',
            name='number',
            field=models.SmallIntegerField(default=1),
        ),
    ]
