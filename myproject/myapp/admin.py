from django.contrib import admin
from .models import Todo  # .models refers to core.models
admin.site.register(Todo)
