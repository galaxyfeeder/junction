from junction.common import *

WSGI_APPLICATION = 'junction.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'junction',
        'USER': 'junction',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
