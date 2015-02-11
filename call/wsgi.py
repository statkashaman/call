"""
WSGI config for call project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import os.path
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "call.settings")
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
