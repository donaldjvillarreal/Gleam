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

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$-@3#bhbj9@p_n-gdsqk%h6zqw+74l4lq=yzsw-0f*q5cxq+-b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Spirit Settings

# ST_TOPIC_PRIVATE_CATEGORY_PK = 1
#
# ST_RATELIMIT_ENABLE = True
# ST_RATELIMIT_CACHE_PREFIX = 'srl'
# ST_RATELIMIT_CACHE = 'default'
#
# ST_NOTIFICATIONS_PER_PAGE = 20
#
# ST_MENTIONS_PER_COMMENT = 30
#
# ST_YT_PAGINATOR_PAGE_RANGE = 3
#
# ST_SEARCH_QUERY_MIN_LEN = 3
#
# ST_USER_LAST_SEEN_THRESHOLD_MINUTES = 1
#
# ST_PRIVATE_FORUM = False
#
# ST_ALLOWED_UPLOAD_IMAGE_FORMAT = ('jpeg', 'png', 'gif')
# ST_ALLOWED_URL_PROTOCOLS = {
#     'http', 'https', 'mailto', 'ftp', 'ftps',
#     'git', 'svn', 'magnet', 'irc', 'ircs'}
#
# ST_UNICODE_SLUGS = True
#
# ST_UNIQUE_EMAILS = True
# ST_CASE_INSENSITIVE_EMAILS = True
#
# ST_BASE_DIR = os.path.dirname(__file__)


# Application definition

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
    # Celery
    'djcelery',
    'alchemyapi',
    # Chat
    'channels',
    'chat',
    # # Spirit apps
    # 'spirit.core',
    # 'spirit.admin',
    # 'spirit.search',
    #
    # 'spirit.user',
    # 'spirit.user.admin',
    # 'spirit.user.auth',
    #
    # 'spirit.category',
    # 'spirit.category.admin',
    #
    # 'spirit.topic',
    # 'spirit.topic.admin',
    # 'spirit.topic.favorite',
    # 'spirit.topic.moderate',
    # 'spirit.topic.notification',
    # 'spirit.topic.poll',
    # 'spirit.topic.private',
    # 'spirit.topic.unread',
    #
    # 'spirit.comment',
    # 'spirit.comment.bookmark',
    # 'spirit.comment.flag',
    # 'spirit.comment.flag.admin',
    # 'spirit.comment.history',
    # 'spirit.comment.like',
    # 'spirit.comment.poll',
    # 'djconfig',
    # 'haystack',
    #############################
    #    Simple QA
    #############################
    # 'qa',
    # 'django_markdown',
    # 'rest_framework',
]

# python manage.py createcachetable
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'spirit_cache',
#     },
# }

# AUTHENTICATION_BACKENDS = [
#     'spirit.user.auth.backends.UsernameAuthBackend',
#     'spirit.user.auth.backends.EmailAuthBackend',
# ]


LOGIN_URL = 'authenticate:login'
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'spirit.user.middleware.TimezoneMiddleware',
    # 'spirit.user.middleware.LastIPMiddleware',
    # 'spirit.user.middleware.LastSeenMiddleware',
    # 'spirit.user.middleware.ActiveUserMiddleware',
    # 'spirit.core.middleware.PrivateForumMiddleware',
    # 'djconfig.middleware.DjConfigMiddleware',
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
                # Spirit
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
                # 'django.template.context_processors.request',
                # 'djconfig.context_processors.config',
                #
                # 'django.contrib.messages.context_processors.messages',
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

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'search/whoosh_index'),
    },
}

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
