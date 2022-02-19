from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Lifter

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Lifter
    list_display = ['email', 'username']

admin.site.register(Lifter, CustomUserAdmin)