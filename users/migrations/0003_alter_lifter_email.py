# Generated by Django 4.0.2 on 2022-02-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_lifter_is_admin_lifter_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifter',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
