from junction.common import *

WSGI_APPLICATION = 'junction.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'junction',
        'USER': 'junction',
        'PASSWORD': 'junction',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    '0.0.0.0:8000',
)
CORS_ORIGIN_REGEX_WHITELIST = (
    '0.0.0.0:8000',
)
