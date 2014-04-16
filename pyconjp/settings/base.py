from pycon.settings.base import *

INSTALLED_APPS.append('pyconjp.account')
INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'pyconjp.urls'

LANGUAGES = (
    ('en', 'English'),
    ('ja', 'Japanese'),
)
