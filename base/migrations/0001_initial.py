# Generated by Django 4.0.2 on 2022-02-20 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], max_length=22)),
                ('name', models.CharField(max_length=32)),
                ('category', models.CharField(choices=[('1', 'Cardio'), ('2', 'HIIT'), ('3', 'Weightlifting'), ('4', 'Swimming'), ('5', 'Jogging'), ('6', 'Other')], max_length=22)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.workout'),
        ),
    ]