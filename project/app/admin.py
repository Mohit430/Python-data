from django.contrib import admin

from .models import UserProfile
from .models import Employee

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Employee) # Register your models
