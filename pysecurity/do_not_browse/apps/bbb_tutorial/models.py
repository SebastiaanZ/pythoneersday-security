from django.db import models


class TutorialTwoNote(models.Model):
    class Classification(models.TextChoices):
        PUBLIC = "PUB", "Public"
        PRIVATE = "PRI", "Private"

    classification = models.CharField(
        max_length=3,
        choices=Classification.choices,
    )
    note = models.TextField()
    author = models.CharField(max_length=32)
