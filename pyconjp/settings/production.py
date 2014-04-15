#:coding=utf-8:

# Production settings
from .server import *

# TODO: 後で PyConJP 風に設定する

# From address for production
DEFAULT_FROM_EMAIL = "PyCon 2014 <no-reply@us.pycon.org>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'production'

ALLOWED_HOSTS = [
    'pycon.jp',
]

LOGGING['handlers']['console']['filters'] = []
LOGGING[''] = {
    'handlers': ['console'],
    'level': 'DEBUG',
}
import logging
logging.basicConfig(level=logging.DEBUG)
