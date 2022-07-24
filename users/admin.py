from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Lifter


admin.site.register(Lifter)

admin.site.unregister(Group)
