from django.db import models
from users.models import Lifter


INTENSITY_CHOICES = (
    ("1", "Easy"),
    ("2", "Medium"),
    ("3", "Hard"),
)

WORKOUT_CATEGORIES = (
    ("1", "Cardio"),
    ("2", "Weighted"),
    ("3", "Reps"),
)


# Create your models here.
class Workout(models.Model):
    intensity = models.CharField(choices=INTENSITY_CHOICES, max_length=22, default="Weighted")
    name = models.CharField(max_length=32)
    notes = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey(Lifter, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(choices=WORKOUT_CATEGORIES, max_length=22, default=1)
    
    def __str__(self):
        return f'{self.name}'


# Exercise set.
class ExSet(models.Model):
    number = models.SmallIntegerField(default=1)
    weight = models.IntegerField()
    reps = models.IntegerField()
    exercise = models.ForeignKey(Exercise, models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
