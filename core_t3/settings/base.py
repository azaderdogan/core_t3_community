"""
Django settings for core_t3 project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',

    'rest_framework',
    'rest_auth',  # pip install django-rest-auth login logout endpointleri için
    'rest_framework.authtoken',  # gelen tokenleri kontrol eder, migrate gerektirir

    'users.apps.UsersConfig',
    'utils.apps.UtilsConfig',
    'posts.apps.PostsConfig',

    ######### #kayıt işlemleri için endpointler falan yaratıyor,  pip freeze> requirements.txt django-allauth
    'allauth',  # pip install django-allauth for registration
    'allauth.account',  # social media loginleri için gerekli bir tool
    'allauth.socialaccount',  # bunu şimdi yapıyoruz çünkü restauth allauthu kullanıyor i optional
    'rest_auth.registration',  # site için id falan araştır bunu  todo
    'django.contrib.sites',
    'django_extensions',
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# boş dosya oluştur ve oradan oku

# SECRET_KEY = 'f9p%(m7ymeb_klxuqeq649$@@f6**cw7d(_i3#7shva*rq+4if'
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    print((BASE_DIR, 'secret_key.txt'))
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_t3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]

WSGI_APPLICATION = 'core_t3.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # token login
        'rest_framework.authentication.SessionAuthentication',  # api page
    ],

}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_DIR = os.path.join(BASE_DIR, 'uploads')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# AUTH_USER_MODEL = "users.User"


# for registration

SITE_ID = 1  # sitemize id vermemiz gerekiyor

ACCOUNT_EMAIL_VERIFICATION = 'none'  # kayıt esnasında email onayı istiyor musunuz?
ACCOUNT_EMAIL_REQUIRED = (True,)  # kayıt esnasında kullanıcı email vermeli mi?

# migrate çalıştırmamız lazım

# # HTTPS Settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
