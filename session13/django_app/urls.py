import os
import django
from django.conf import settings

if not settings.configured:
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

from django.urls import path
from django.http import JsonResponse


def hello_world(request):
    return JsonResponse({"message": "Hello World from Django"})


urlpatterns = [
    path("", hello_world),
]
