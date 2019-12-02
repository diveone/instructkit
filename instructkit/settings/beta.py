"""
Django settings for instructkit project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
from .common import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS += []

# Application definition
DJANGO_APPS += []
CUSTOM_APPS += []

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE += []

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://localhost:9000',
    'http://127.0.0.1:9000',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'instructkit',
#         'PORT': '5432',
#     }
# }
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/assets/'
# STATIC_ROOT = join_paths(PROJECT_PATH, 'static')
# STATICFILES_DIRS = [
    # join_paths(PROJECT_PATH, 'assets'),
# ]

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'filters': [],
        },
        'file': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'filters': [],
            'filename': 'instructkit.log'
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        'django.db': {
            # django also has database level logging
        },
    },
}

import django_heroku
django_heroku.settings(locals())
