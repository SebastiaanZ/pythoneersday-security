import argparse
import pathlib
from typing import Any

from django import conf
from django.core import management
from django.core.management import base

from . import _utils


class Command(base.BaseCommand):
    help = "Reset the challenge project"

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Resetting the challenge website.\n\n")
        management.call_command("reset_db")
        self.stdout.write("\n")
        management.call_command("migrate", interactive=False)
        self.stdout.write("\n")
        all_fixtures = _utils.get_fixture_files(conf.settings.BASE_DIR)
        management.call_command("loaddata", *all_fixtures)
        self.stdout.write("Database reset and reseeded.\n")
