"""
WSGI config for ftlabs project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from ftlabs.settings.env_settings import EnvironmentSettings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', EnvironmentSettings.environment)

application = get_wsgi_application()
