from django.db import models


class Todo(models.Model):
    objects = None
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
