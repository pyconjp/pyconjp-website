#:coding=utf-8:

# Staging settings
from .server import *

# TODO: 後で PyConJP 風に設定する

# From address for staging - use our development list
DEFAULT_FROM_EMAIL = 'pycon@caktusgroup.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'staging'

ALLOWED_HOSTS = [
    'staging-pycon.python.org',
]
