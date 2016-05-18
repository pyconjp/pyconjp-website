# -*- coding: utf-8 -*-
"""
この設定はデフォルトで sqlite を使います。
DB バックエンドは DB_ENGINE の環境変数で設定できます。
例::

   DB_ENGINE=postgresql_psycopg2 DB_NAME=pyconjp2016 DB_HOST=postgres DB_PORT=5432 DB_USER=postgres DB_PASSWORD=pass python manage.py runserver

設定できる環境変数
==================

:ENVIRONMENT:
    環境毎の設定を切り替えます。デフォルトは ``dev`` です。

    :production:
       本番用です。
       SECRET_KEY 指定が必須となり、ALLOWED_HOST, ADMINS が設定されます。
    :staging:
       ステージング用です。
       SECRET_KEY 指定が必須となり、ALLOWED_HOST, ADMINS が設定されます。
    :test:
       テスト実行用です。RUNNER等が設定されます。
    :それ以外:
        開発用の設定で起動します。
       任意の ALLOWED_HOST を指定できます。

:SECRET_KEY:
    セッションの暗号化にしようするキーを指定します。
    公開環境ではかならず指定してください。
    ENVIRONMENT が ``production`` または ``staging`` の場合必須です。
    それ以外の場合、デフォルト値が使用されます。

:DEBUG:
    True でデバッグツールバーを有効にし、Djangoをデバッグモードで実行します。
    デフォルトはTrueです。
    DEBUG, TEMPLATE_DEBUG, EMAIL_DEBUG の設定に使用されます。

:DB_ENGINE:
    指定できる値は ``sqlite3``, ``postgresql_psycopg2`` です。
    デフォルトは DEBUG が真なら sqlite3, 偽なら postgresql_psycopg2 です。

:DB_NAME:
    データベース名です。 デフォルトで使用してください。
    デフォルト値はDB_ENGINEの値によって決定します。
    DB_ENGINE='sqlite3' なら pyconjp2016.sqlite、それ以外なら 'pyconjp2016' です。

:DB_HOST, DB_PORT, DB_USER, DB_PASSWORD:
    sqlite3 以外を使用する場合指定してください。デフォルト値は空文字列です。

:MEDIA_ROOT:
    静的ファイルの出力先や添付ファイルの保存に使用されるディレクトリです。
    デフォルトは ``/site_media/media`` です。

:EMAIL_HOST:
    メール送信する場合にSMTPサーバーを指定します。
    デフォルトはNoneで、メール送信はコンソールに出力されます。

:EMAIL_FROM:
    メール送信元アドレス。
    デフォルトは "PyCon JP " + URL_PREFIXES +" <no-reply@pycon.jp>"

:ALLOWED_HOSTS:
    DEBUGが真の場合に使用されるDjangoの設定値。カンマ区切りのホスト名を指定する。
    ENVIRONMENTが 'production', 'staging' 以外の場合指定可能。
    デフォルトは ``localhost, 0.0.0.0``

:TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET:
    Twitterログインを使用する場合設定してください。デフォルトは空文字列です。

:FACEBOOK_APP_ID, FACEBOOK_API_SECRET:
    Facebookログインを使用する場合設定してください。デフォルトは空文字列です。

:LOG_PATH:
    ログファイル出力先です。デフォルトは ``./pyconjp_website.log`` です。

:ERROR_LOG_PATH:
    エラーログファイル出力先です。デフォルトは ``./pyconjp_website.error.log`` です。

:LOG_LEVEL:
    ログレベルです。デフォルトは ``INFO`` です。
    ``ERROR``, ``WARNING``, ``INFO``, ``DEBUG``, ``TRACE`` を指定できます。

"""

import os.path
import posixpath
import copy

from django.core.urlresolvers import reverse_lazy


def env_or_default(NAME, default):
    return os.environ.get(NAME, default)

ENVIRONMENT = env_or_default('ENVIRONMENT', 'dev')

# Top level of our source / repository
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Symposion package
PACKAGE_ROOT = os.path.join(PROJECT_ROOT, "symposion")

DEBUG = env_or_default("DEBUG", True)
TEMPLATE_DEBUG = DEBUG

# tells Pinax not to serve media through the staticfiles app.
SERVE_MEDIA = False  # FIXME: we pyconjp should use staticfiles for a performance

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
COMPRESS = False
# yes, use django-compressor on the server
COMPRESS_ENABLED = True  # FIXME: compress on the production server is worse.


# Conference ID and any URL prefixes
CONFERENCE_ID = 1

CONFERENCE_URL_PREFIXES = {
    1: "2016",
    2: "2015",
    3: "2014"
}

URL_PREFIXES = CONFERENCE_URL_PREFIXES[CONFERENCE_ID]

_db_engine = env_or_default('DB_ENGINE', 'sqlite3' if DEBUG else 'postgresql_psycopg2')
if _db_engine == 'sqlite3':
    _db_name = os.path.join(PROJECT_ROOT, 'pyconjp' + URL_PREFIXES + '.sqlite')
else:
    _db_name = 'pyconjp'+ URL_PREFIXES

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.%s' % _db_engine,
        'NAME': env_or_default('DB_NAME', _db_name),
        "USER": env_or_default("DB_USER", ""),
        "PASSWORD": env_or_default("DB_PASSWORD", ""),
        "HOST": env_or_default("DB_HOST", ""),
        "PORT": env_or_default("DB_PORT", ""),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'
DEFAULT_LANGUAGE = 1

SITE_ID = 1



# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGES = (
    ('ja', 'Japanese'),
    ('en', 'English'),
)

LOCALE_PATHS = [os.path.join(PROJECT_ROOT, "locale")]

# Absolute path to the directory that holds media - this is files uploaded
# by users, such as attachments.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = env_or_default("MEDIA_ROOT", os.path.join(PROJECT_ROOT, "site_media", "media"))


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/%s/site_media/media/" % URL_PREFIXES

# Absolute path to the directory where static files will be gathered
# at deploy time and served from in production.  Should NOT be
# in version control, or contain anything before deploying.
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/%s/site_media/static/" % URL_PREFIXES

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Subdirectory of COMPRESS_ROOT to store the cached media files in
COMPRESS_OUTPUT_DIR = "cache"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "djangosecure.middleware.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # LocaleMiddleware must follow session middleware, auth middleware,
    # and and cache middleware, and precede commonmiddleware
    #"django.middleware.locale.LocaleMiddleware",
    "account.middleware.LocaleMiddleware",
    "localeurlcustom.middleware.LocaleURLMiddlewareCustom",
    "django.middleware.common.CommonMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "social_auth.middleware.SocialAuthExceptionMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'pyconjp.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "pyconjp/templates"),
    os.path.join(PROJECT_ROOT, "pycon/templates"),
    os.path.join(PACKAGE_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "social_auth.context_processors.social_auth_backends",
    "pinax_utils.context_processors.settings",
    "account.context_processors.account",
    "symposion.reviews.context_processors.reviews",
    "constance.context_processors.config",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",

    # external
    "compressor",
    "mailer",
    "django_openid",
    "timezones",
    "metron",
    "easy_thumbnails",
    "account",
    "sitetree",
    "taggit",
    "reversion",
    "biblion",
    "social_auth",
    "djangosecure",
    "raven.contrib.django",
    "constance",
    "constance.backends.database",
    "redis_cache",
    "south",
    "uni_form",
    "gunicorn",
    "selectable",

    # symposion
    "symposion.conference",
    #"symposion.cms",  # not used by pyconjp
    "symposion.boxes",
    "symposion.speakers",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.teams",
    "symposion.schedule",

    # custom
    "markedit",
    "pycon",
    "pycon.sponsorship",
    "pycon.registration",
    "pycon.schedule",
    "pycon.profile",
    "pycon.finaid",
    "pycon.pycon_api",
    "pycon.tutorials",
    "localeurlcustom",

    # pyconjp
    'pyconjp',
    'pyconjp.account',
    'restcms',
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

SESSION_COOKIE_NAME = "pyconjp-2016"

EMAIL_HOST = env_or_default("EMAIL_HOST", None)
if EMAIL_HOST:
    # Yes, send email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False
ACCOUNT_CREATE_ON_SAVE = True
ACCOUNT_DELETION_EXPUNGE_CALLBACK = 'pyconjp.account.callbacks.account_delete_expunge'

AUTHENTICATION_BACKENDS = [
    # Permissions backends
    "symposion.teams.backends.TeamPermissionsBackend",

    # Social Auth Backends
    "social_auth.backends.twitter.TwitterBackend",
    "social_auth.backends.facebook.FacebookBackend",
    "social_auth.backends.google.GoogleBackend",
    "social_auth.backends.yahoo.YahooBackend",
    "social_auth.backends.OpenIDBackend",

    # Django User Accounts
    "account.auth_backends.EmailAuthenticationBackend",
]

SOCIAL_AUTH_PIPELINE = [
    "social_auth.backends.pipeline.social.social_auth_user",
    "social_auth.backends.pipeline.user.get_username",
    "symposion.social_auth.pipeline.user.create_user",
    "social_auth.backends.pipeline.social.associate_user",
    "social_auth.backends.pipeline.social.load_extra_data",
    "social_auth.backends.pipeline.user.update_user_details",
]

#Twitter
TWITTER_CONSUMER_KEY         = env_or_default("TWITTER_CONSUMER_KEY", "")
TWITTER_CONSUMER_SECRET      = env_or_default("TWITTER_CONSUMER_SECRET", "")

#Facebook
FACEBOOK_APP_ID              = env_or_default("FACEBOOK_APP_ID", "")
FACEBOOK_API_SECRET          = env_or_default("FACEBOOK_API_SECRET", "")

LOGIN_URL = reverse_lazy("account_login")

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name()
LOGIN_ERROR_URL = reverse_lazy("account_login")

# Need these to be reversed urls, currently breaks if using reverse_lazy
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/" + URL_PREFIXES + "/dashboard/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/" + URL_PREFIXES +"/dashboard/"

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = False

# Don't clobber User.email if someone associates a social account that
# happens to have a different email address
# http://django-social-auth.readthedocs.org/en/latest/configuration.html#miscellaneous-settings
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = env_or_default('EMAIL_FROM', "PyCon JP " + URL_PREFIXES +" <no-reply@pycon.jp>")
SERVER_EMAIL = DEFAULT_FROM_EMAIL


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = {
    # "SETTING_NAME": (default_value, "help text")
    "CTE_SECRET": ("", "Shared secret for CTE integration"),
    "CTE_BASICAUTH_USER": ("", "Shared User for accessing CTE Registration data"),
    "CTE_BASICAUTH_PASS": ("", "Shared User password for accessing CTE Registration data"),
    "CTE_TUTORIAL_DATA_URL": ("", "URL for the CSV of CTE Tutorial Registration Data"),
    "REGISTRATION_URL": ("", "URL for registration"),
    "SHOW_LANGUAGE_SELECTOR": (False, "Show language selector on dashboard"),
    "SPONSOR_FROM_EMAIL": ("", "From address for emails to sponsors"),
    "REGISTRATION_STATUS": ("", "Used in the home page template. Valid values are 'soon', 'open' and 'closed'"),
    "URL_PREFIXES":(URL_PREFIXES, ""),
    "GOOGLE_ANALYTICS_TRACKING_ID": ("", "The site's Google Analytics Tracking ID."),
}

BIBLION_PARSER = ["symposion.markdown_parser.parse", {}]
BIBLION_SECTIONS = [
    ("ja", u"Japanese/日本語"),
    ("en", u"English/英語"),
]

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/$"

PROPOSAL_FORMS = {
    "tutorial": "pycon.forms.PyConTutorialProposalForm",
    'talk': 'pyconjp.forms.PyConJPTalkProposalForm',
    "poster": "pycon.forms.PyConPosterProposalForm",
    "sponsor-tutorial": "pycon.forms.PyConSponsorTutorialForm",
    "lightning-talk": "pycon.forms.PyConLightningTalkProposalForm",
    "open-space": "pycon.forms.PyConOpenSpaceProposalForm",
}

ALLOWED_HOSTS = []
USE_X_FORWARDED_HOST = True
USE_X_ACCEL_REDIRECT = False

MARKEDIT_DEFAULT_SETTINGS = {
    'preview': 'below',
    'toolbar': {
        'backgroundMode': 'dark',
    }
}

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# Is somebody clobbering this?  We shouldn't have to set it ourselves,
# but if we don't, gunicorn's django_wsgi blows up trying to configure
# logging with an empty dictionary.
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
            'environment': ENVIRONMENT,
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
        'filename': env_or_default('LOG_PATH', './pyconjp_website.log'),
    },
    'pyconjp_error_log': {
        'level': 'ERROR',
        'formatter': 'verbose',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': env_or_default('ERROR_LOG_PATH', './pyconjp_website.error.log'),
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


if DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG)

    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE_CLASSES += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

if ENVIRONMENT == 'production':
    SECRET_KEY = os.environ["SECRET_KEY"]  # required
    ALLOWED_HOSTS = ['pycon.jp']
    ADMINS = (
        ('Ian Lewis', 'ianmlewis@pycon.jp'),
        ('Daisuke Komatsu', 'vkg.taro@gmail.com'),
    )
    MANAGERS = ADMINS

elif ENVIRONMENT == 'staging':
    SECRET_KEY = os.environ["SECRET_KEY"]  # required
    ALLOWED_HOSTS = ['.pycon.jp']
    ADMINS = (
        ('Ian Lewis', 'ianmlewis@pycon.jp'),
        ('Daisuke Komatsu', 'vkg.taro@gmail.com'),
    )
    MANAGERS = ADMINS

elif ENVIRONMENT == 'test':
    INSTALLED_APPS += ['django_nose',]
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    # Debug logs during testing are WAY too verbose
    NOSE_ARGS = ['--nologcapture']
    # Including a default secret key since this is just for test
    SECRET_KEY = env_or_default('SECRET_KEY', u'dipps!+sq49#e2k#5^@4*^qn#8s83$kawqqxn&_-*xo7twru*8')
    # Speed up testing - skip running the migrations, just make the test database
    # with its current schema
    SOUTH_TESTS_MIGRATE = False

    # Using sqlite in memory speeds things up even more, but that's getting
    # pretty far from production. I don't think it's worth the risk.
    # DATABASES = {
    #    "default": {
    #        "ENGINE": "django.db.backends.sqlite3",
    #        "NAME": ":memory:",
    #    }
    # }

else:  # ENVIRONMENT == 'dev' or else
    COMPRESS_ENABLED = False
    ALLOWED_HOSTS = [x.strip() for x in env_or_default('ALLOWED_HOSTS', 'localhost, 0.0.0.0').split()]
    # Including a default secret key since this is just for development
    SECRET_KEY = env_or_default('SECRET_KEY', u'dipps!+sq49#e2k#5^@4*^qn#8s83$kawqqxn&_-*xo7twru*8')

