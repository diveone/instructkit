"""
Django settings for instructkit project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
from os.path import abspath, dirname, join as join_paths

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONFIG_ROOT = dirname(abspath(__file__))

# TODO: Recommended by Two Scoops. Worthwhile?
# DJANGO_ROOT = dirname(CONFIG_ROOT)
# PROJECT_ROOT = dirname(DJANGO_ROOT)

# CURRENT PROJECT_DIR: instructkit/instructkit
PROJECT_PATH = dirname(CONFIG_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# =======================================================================
# SECURITY SETTINGS
# =======================================================================
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
TESTING = False
ALLOWED_HOSTS = []

# =======================================================================
# APPLICATIONS
# On application start-up, Django looks for migrations files for each app
# =======================================================================
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework'
]

CUSTOM_APPS = [
    'accounts',
    'core',
    'courses',
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =======================================================================
# CONFIGURATION SETTINGS
# =======================================================================
ROOT_URLCONF = 'instructkit.urls'
WSGI_APPLICATION = 'instructkit.wsgi.application'

# =======================================================================
# MEDIA MANAGEMENT
# Static files and template management
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# =======================================================================
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join_paths(PROJECT_PATH, '../../templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =======================================================================
# DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# =======================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'instructkit'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}

# =======================================================================
# AUTHENTICATION
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# =======================================================================
AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =======================================================================
# THIRD-PARTY INTEGRATION SETTINGS
# For settings specific to third-party modules and apis.
# The credentials below are NOT FOR PRODUCTION. Overwrite them by editing
# your dev.py
# =======================================================================
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# =======================================================================
# LOGGING SETTINGS
# https://docs.djangoproject.com/en/1.11/topics/logging
# =======================================================================
