from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


# Yes. Users are called lifters. hehe
class Lifter(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    
    USERNAME_FIELD = 'username'
        
    def __str__(self):
        return f"|{self.username}{self.email}"