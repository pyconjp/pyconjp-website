#:coding=utf-8:

# Common settings for deployed servers
# Will be imported by staging.py, production.py, etc.,
# and some settings possibly overridden.
import os

from .base import *  # NOQA

# TODO: 後で PyConJP 風に設定する

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ['DB_NAME'],
        "USER": os.environ['DB_USER'],
        "PASSWORD": os.environ['DB_PASSWORD'],
        "HOST": os.environ['DB_HOST'],
        "PORT": os.environ['DB_PORT'],
    }
}

ALLOWED_HOSTS = [
    'pycon.jp',
    '.pycon.jp',
]
USE_X_FORWARDED_HOST = True

SECRET_KEY = os.environ['SECRET_KEY']

ADMINS = (
    ('Ian Lewis', 'ianmlewis@pycon.jp'),
)
MANAGERS = ADMINS

# Yes, send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env_or_default("EMAIL_HOST", "localhost")

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# tells Pinax not to serve media through the staticfiles app.
SERVE_MEDIA = False

# yes, use django-compressor on the server
COMPRESS_ENABLED = True

MEDIA_ROOT = env_or_default('MEDIA_ROOT',
                            os.path.join(BASE_PATH, 'site_media'))

import copy
from django.utils.log import DEFAULT_LOGGING
LOGGING = copy.deepcopy(DEFAULT_LOGGING)

# NOTE: DEFAULT_LOGGING has not formatters defined.
LOGGING['formatters'] = {
    'verbose': {
        'format': '[%(asctime)s][%(name)s] %(levelname)s %(message)s',
        'datefmt': "%Y-%m-%d %H:%M:%S",
    },
    'simple': {
        'format': '%(levelname)s %(message)s'
    },
}

LOGGING['filters'].update({
    'static_fields': {
        '()': 'pycon.logfilters.StaticFieldFilter',
        'fields': {
            'deployment': 'pycon',
            'environment': '?'   # should be overridden
        },
    },
    'django_exc': {
        '()': 'pycon.logfilters.RequestFilter',
    },
})
LOGGING['handlers'].update({
    'mail_admins': {
        'level': 'ERROR',
        'class': 'django.utils.log.AdminEmailHandler',
        'include_html': False,
        'filters': ['require_debug_false'],
    },
    'pyconjp_log': {
        'level': 'INFO',
        'formatter': 'verbose',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': env_or_default('LOG_PATH',
                                   '/var/log/pyconjp/pyconjp_website.log'),
    },
    'pyconjp_error_log': {
        'level': 'ERROR',
        'formatter': 'verbose',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': env_or_default('ERROR_LOG_PATH',
                                   '/var/log/pyconjp/pyconjp_website.error.log'),
    },
})
LOGGING['loggers'].update({
    '': {
        # mail_admins will only accept ERROR and higher
        'handlers': ['console', 'pyconjp_log'],
        'level': env_or_default('LOG_LEVEL', 'INFO'),
    },
    'django.request': {
        'handlers': ['mail_admins', 'pyconjp_error_log'],
        'level': 'ERROR',
        'propagate': True,
    },
    'pycon': {
        # mail_admins will only accept ERROR and higher
        'handlers': ['mail_admins', 'pyconjp_error_log'],
        'level': 'WARNING',
    },
    'symposion': {
        # mail_admins will only accept ERROR and higher
        'handlers': ['mail_admins', 'pyconjp_error_log'],
        'level': 'WARNING',
    }
})
