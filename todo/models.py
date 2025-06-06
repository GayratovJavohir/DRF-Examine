from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title