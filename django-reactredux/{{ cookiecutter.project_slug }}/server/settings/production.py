"""
Production Django settings
"""
from settings.base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', '{{ cookiecutter.website }}']

# SECURITY WARNING: update this when you have the production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ cookiecutter.server_postgres_db_name }}',
        'USER': '{{ cookiecutter.server_postgres_username }}',
        'PASSWORD': '{{ cookiecutter.server_postgres_pass }}',
        'HOST': '{{ cookiecutter.server_postgres_host }}',
        'PORT': '{{ cookiecutter.server_postgres_port }}',
    }
}

CORS_ORIGIN_ALLOW_ALL = False
