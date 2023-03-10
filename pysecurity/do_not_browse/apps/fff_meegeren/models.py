from django import conf, urls
from django.db import models


class PrivateNoteFFF(models.Model):
    author = models.ForeignKey(
        conf.settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField()
    note = models.TextField()

    def get_absolute_url(self):
        return urls.reverse("fff:detail", kwargs={"pk": self.pk})
