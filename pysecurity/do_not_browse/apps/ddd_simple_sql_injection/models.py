from django import conf
from django.db import models


class PrivateNoteDDD(models.Model):
    author = models.ForeignKey(
        conf.settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField()
    note = models.TextField()
