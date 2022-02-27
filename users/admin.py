from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Lifter


@admin.register(Lifter)
class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
