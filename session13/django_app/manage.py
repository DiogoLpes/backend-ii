#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "django_app.urls"
    )  # Not standard, but for minimal
    settings.configure(
        DEBUG=True,
        SECRET_KEY="your-secret-key",
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
        ],
        ROOT_URLCONF="django_app.urls",
    )
    django.setup()
    execute_from_command_line(sys.argv)
