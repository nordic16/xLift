from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


# Yes. Users are called lifters. hehe
class Lifter(AbstractUser):    
    date_of_birth = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True)
        
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    def __str__(self):
        return f"|{self.username}{self.email}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin