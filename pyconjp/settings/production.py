#:coding=utf-8:

# Production settings
from .server import *  # NOQA

# TODO: 後で PyConJP 風に設定する

# From address for production
DEFAULT_FROM_EMAIL = "PyCon JP 2014 <no-reply@pycon.jp>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'production'

ALLOWED_HOSTS = [
    'pycon.jp',
]

import logging
logging.basicConfig(level=logging.DEBUG)
