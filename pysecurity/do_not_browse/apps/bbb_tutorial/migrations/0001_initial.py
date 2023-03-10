# Generated by Django 4.1.7 on 2023-03-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TutorialTwoNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "classification",
                    models.CharField(
                        choices=[("PUB", "Public"), ("PRI", "Private")], max_length=3
                    ),
                ),
                ("note", models.TextField()),
                ("author", models.CharField(max_length=32)),
            ],
        ),
    ]
