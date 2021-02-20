from core_t3.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 't3community',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['*']
# Extra places for collectstatic to find static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
