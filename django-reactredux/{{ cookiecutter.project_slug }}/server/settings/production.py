"""
Production Django settings
"""
from settings.base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', '{{ cookiecutter.project_website }}']

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

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with a slash
        'STATS_FILE': os.path.join(ROOT_DIR, 'client', 'build', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js']
    }
}
