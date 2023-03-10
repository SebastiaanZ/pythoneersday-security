import argparse
import pathlib
from typing import Any

from django import conf
from django.core import management
from django.core import checks
from django.core.management import base

from . import _utils


class Command(base.BaseCommand):
    help = "Initializes the challenge project"
    requires_system_checks = [checks.Tags.staticfiles]

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--noload",
            action="store_true",
            help="Skip loading fixtures",
            dest="skip_fixtures",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Welcome to Hacky Notes: The Secure Notes App.\n")

        management.call_command("collectstatic", interactive=False)
        self.stdout.write("\n")

        management.call_command("migrate", interactive=False)
        self.stdout.write("\n")

        if not options["skip_fixtures"]:
            all_fixtures = _utils.get_fixture_files(conf.settings.BASE_DIR)
            management.call_command("loaddata", *all_fixtures)
            self.stdout.write("\n")

        management.call_command("runserver", "localhost:8888")
