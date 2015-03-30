#:coding=utf-8:

from pycon.settings.base import *  # NOQA

INSTALLED_APPS.append('pyconjp')
INSTALLED_APPS.append('pyconjp.account')
INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'pyconjp.urls'

TIME_ZONE = 'Asia/Tokyo'

LANGUAGES = (
    ('ja', 'Japanese'),
    ('en', 'English'),
)

BIBLION_SECTIONS = [
    ("ja", u"Japanese/日本語"),
    ("en", u"English/英語"),
]
LANGUAGE_CODE = 'ja'
DEFAULT_LANGUAGE = 1

# Add config for Google Analytics
CONSTANCE_CONFIG["GOOGLE_ANALYTICS_TRACKING_ID"] = ("", "The site's Google Analytics Tracking ID.")

PROPOSAL_FORMS['talk'] = 'pyconjp.forms.PyConJPTalkProposalForm'
TEMPLATE_DIRS.insert(0, os.path.join(PROJECT_ROOT, "pyconjp/templates"))

ACCOUNT_DELETION_EXPUNGE_CALLBACK = 'pyconjp.account.callbacks.account_delete_expunge'
