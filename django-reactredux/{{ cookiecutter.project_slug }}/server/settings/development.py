"""
Development Django settings
"""
from settings.base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2JH5t~k1dMSh+$&8=i~I@v~92$qf1lx!'

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
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

#CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',
)