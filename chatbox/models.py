from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    date = models.DateTimeField()
    alert = models.BooleanField(default=False)
