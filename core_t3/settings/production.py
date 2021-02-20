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
ALLOWED_HOSTS = ['aeyazilimblogu.com', 'www.aeyazilimblogu.com', '188.166.3.250']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
