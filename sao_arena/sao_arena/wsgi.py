"""
WSGI config for sao_arena project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sao_arena.settings")
os.environ["CELERY_LOADER"] = "django"

application = get_wsgi_application()
