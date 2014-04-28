from pycon.settings.base import *  # NOQA

INSTALLED_APPS.append('pyconjp.account')
INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'pyconjp.urls'

TIME_ZONE = 'Asia/Tokyo'

LANGUAGES = (
    ('en', 'English'),
    ('ja', 'Japanese'),
)

PROPOSAL_FORMS['talk'] = 'pyconjp.forms.PyConJPTalkProposalForm'
