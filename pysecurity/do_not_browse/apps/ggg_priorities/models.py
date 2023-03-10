from django import conf, urls
from django.db import models


class PrioritizedNotes(models.Model):
    class Priorities(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"

    author = models.ForeignKey(conf.settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.TextField()
    priority = models.CharField(choices=Priorities.choices, max_length=1)
