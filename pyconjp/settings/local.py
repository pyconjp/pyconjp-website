#:coding=utf-8:

# ローカル開発用の settings.py
# この設定はデフォルトで sqlite を使います。
# DB バックエンドは DB_ENGINE の環境変数で設定できます。
# 例: DB_ENGINE=postgresql_psycopg2 python manage.py runserver

# 設定できる環境変数
# DEBUG
# DB_ENGINE
# DB_NAME
# DB_HOST
# DB_PORT
# DB_USER
# DB_PASSWORD

from .dev import *

def env_var(var, var_type=None, *args, **kwargs):
    u"""
    環境変数の値を返す
    
    例: env_var("HOGE_SETTING", int, default=123)
    """
    try:
        val = os.environ[var]
    except KeyError:
        if not args and 'default' not in kwargs:
            raise ImproperlyConfigured('The environment variable "%s" is required.' % var)
        elif args:
            val = args[0]
        else:
            val = kwargs['default']
    
    if var_type:
        try:
            val = var_type(val)
        except ValueError, e:
            raise ImproperlyConfigured('Invalid setting for "%s": "%s"' % (var, e))

    return val

DEBUG = env_var('DEBUG', bool, default=True) 

_db_engine = env_var('DB_ENGINE', default='sqlite3' if DEBUG else 'postgresql_psycopg2')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % _db_engine,
        'NAME': env_var('DB_NAME', default=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),  'pycon2014.sqlite') if _db_engine == 'sqlite3' else 'pycon2014'),
        'USER': env_var('DB_USER', default=''),
        'PASSWORD': env_var('DB_PASSWORD', default=''),
        'HOST': env_var('DB_HOST', default=''),
        'PORT': env_var('DB_PORT', default=''),
    }
}

INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'pyconjp.urls'

LANGUAGES = (
    ('en', 'English'),
    ('ja', 'Japanese'),
)
