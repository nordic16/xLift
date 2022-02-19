from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils import timezone

# Yes. Users are called lifters. hehe
class Lifter(AbstractUser):
    workout_days = models.IntegerField(verbose_name="Workouts per week", default=3)
    date_of_birth = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.username