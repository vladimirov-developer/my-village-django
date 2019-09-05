# coding: utf-8
from project.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tokarevo',
    }
}


MEDIA_ROOT = '/var/www/project/public/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/project/public/static/'
STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_PASSWORD = 'k3xmqJQP73j'
EMAIL_HOST_USER = 'tokarevorf@yandex.ru'
DEFAULT_FROM_EMAIL = 'tokarevorf@yandex.ru'
EMAIL_USE_TLS = True
