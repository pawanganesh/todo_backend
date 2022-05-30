from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Todo(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
