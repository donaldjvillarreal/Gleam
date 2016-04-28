# coding=utf-8
"""
Django settings for gleam project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import unicode_literals
import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$-@3#bhbj9@p_n-gdsqk%h6zqw+74l4lq=yzsw-0f*q5cxq+-b'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '.herokuapp.com', 'localhost', 'www.gleamtherapy.com', 'gleamtherapy.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authenticate',
    'gleam',
    'diagnostic',
    'core',
    # 'caseconcept',
    'journal',
    'therapist',
    'tasks',
    # Celery
    'djcelery',
    'alchemyapi',
    # Chat
    'channels',
    'chat',
    #############################
    #    Simple QA
    #############################
    # 'qa',
    # 'django_markdown',
    # 'rest_framework',
]

LOGIN_URL = 'authenticate:login'
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gleam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'gleam.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# For Heroku Postgres
db_from_env = dj_database_url.config()
if db_from_env is not None:
    DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gleam.notifications@gmail.com'
EMAIL_HOST_PASSWORD = '160noreply'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Development Settings
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25

# Celery
BROKER_URL = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

######################################
#       Django Passwords
######################################
PASSWORD_MIN_LENGTH = 6  # Defaults to 6
PASSWORD_MAX_LENGTH = 30  # Defaults to None
# PASSWORD_DICTIONARY = "/usr/share/dict/words" # Defaults to None
PASSWORD_MATCH_THRESHOLD = 0.9  # Defaults to 0.9, should be 0.0 - 1.0 where 1.0 means exactly the same.
# PASSWORD_COMMON_SEQUENCES = [] # Should be a list of strings, see passwords/validators.py for default

PASSWORD_COMPLEXITY = {  # You can omit any or all of these for no limit for that particular set
    "UPPER": 1,  # Uppercase
    "LOWER": 1,  # Lowercase
    "LETTERS": 1,  # Either uppercase or lowercase letters
    "DIGITS": 1,  # Digits
    "SPECIAL": 1,  # Not alphanumeric, space or punctuation character
    # "WORDS": 1         # Words (alphanumeric sequences separated by a whitespace or punctuation character)
}

# Chat with Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "gleam.routing.channel_routing",
    },
}

if 'DYNO' in os.environ:
    DEBUG = False
    #
    # # AWS
    # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = 'gleam-heroku'
    #
    # STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    #
    # STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    # ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
