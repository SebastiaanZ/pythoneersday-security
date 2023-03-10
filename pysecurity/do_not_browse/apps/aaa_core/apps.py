"""AppConfig for the `core` app."""
from django import apps


class CoreApp(apps.AppConfig):
    """Configuration for the `core` app."""

    name = "apps.aaa_core"
    label = "core"
    verbose_name = "The core application of the pysecurity project"
