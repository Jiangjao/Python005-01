from django.contrib import admin
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Order)
# admin.site.register(User,BaseUserAdmin)

