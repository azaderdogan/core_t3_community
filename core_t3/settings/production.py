from core_t3.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 't3community',
        'USER': 'azad',
        'PASSWORD': 'Azad.1212Ae',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')