from django.db import models
from users.models import Lifter
from django.utils.timezone import datetime

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
    intensity = models.CharField(choices=INTENSITY_CHOICES, max_length=22, default=1)
    name = models.CharField(max_length=32)
    notes = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey(Lifter, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    
    def get_total_volume(self):
        exercises = ExSet.objects.filter(workout=self)
        
        volume = 0
        
        for i in exercises:
            volume += (i.weight * i.reps)
            
        return volume
    
    
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
    exercise = models.ForeignKey(Exercise, models.PROTECT)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
