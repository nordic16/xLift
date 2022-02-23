from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from .models import Lifter

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Lifter


admin.site.register(Lifter, CustomUserAdmin)
admin.site.unregister(Group)
