from django.db import models


INTENSITY_CHOICES = (
    ("1", "Easy"),
    ("2", "Medium"),
    ("3", "Hard"),
)

WORKOUT_CHOICES = (
    ("1", "Cardio"),
    ("2", "HIIT"),
    ("3", "Weightlifting"),
    ("4", "Swimming"),
    ("5", "Jogging"),
    ("6", "Other"),
)


# Create your models here.
class Workout(models.Model):
    intensity = models.CharField(choices=INTENSITY_CHOICES, max_length=22)
    name = models.CharField(max_length=32)
    category = models.CharField(choices=WORKOUT_CHOICES, max_length=22)
    notes = models.TextField(max_length=500)
    

class Exercise(models.Model):
    name = models.CharField(max_length=32)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


# Exercise set.
class ExSet(models.Model):
    weight = models.IntegerField()
    reps = models.IntegerField()
    exercise = models.ForeignKey(Exercise, models.CASCADE)
    
