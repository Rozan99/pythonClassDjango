from django.db import models
from django.utils import timezone

class Todo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    deadline = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
