from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date

WORKOUTS_PER_WEEK = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
    (5, '6'),
    (6, '7')
)

# Yes. Users are called lifters. hehe
class Lifter(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    workouts_per_week = models.IntegerField(default=1, choices=WORKOUTS_PER_WEEK)
    
    # in kg
    weight = models.PositiveIntegerField(default=50, validators=[MinValueValidator(35), MaxValueValidator(200)])
    
    # In cm
    height = models.SmallIntegerField(default=110, validators=[MinValueValidator(100), MaxValueValidator(225)])
    
    age = models.SmallIntegerField(blank=True, null=True, default=1)
        
    USERNAME_FIELD = 'username'
        
    def __str__(self):
        return f"|{self.username}{self.email}"    

@receiver(pre_save, sender=Lifter)
def calculate_age(sender, instance, raw=False, **kwargs):
        today = date.today()
        
        # If the condition is true, subtract one to age.
        instance.age = today.year - instance.date_of_birth.year - ((today.month, today.day) < (instance.date_of_birth.month, instance.date_of_birth.day))