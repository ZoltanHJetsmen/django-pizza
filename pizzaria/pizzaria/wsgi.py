"""
WSGI config for pizzaria project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

application = Cling(get_wsgi_application())
