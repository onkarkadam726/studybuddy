"""
WSGI config for studybud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

application = get_wsgi_application()


#You said:
#import django
#from django.core.management import call_command

#django.setup()
#try:
#    call_command('makemigrations', interactive=False)
#    call_command('migrate', interactive=False)
#except Exception as e:
#    print(f"Migration failed: {e}")