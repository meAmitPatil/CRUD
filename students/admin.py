from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student  # Import your model

admin.site.register(Student)  # Register your model with the admin site
