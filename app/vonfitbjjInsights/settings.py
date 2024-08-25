"""
Django settings for vonfitbjjInsights project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Determine the environment (you can set this in your .env file or environment)
ENVIRONMENT = config('ENVIRONMENT', default='development')

# Set the BASE_URL based on the environment
if ENVIRONMENT == 'production':
    BASE_URL = config('BASE_URL', default='https://production.example.com')
else:
    BASE_URL = config('BASE_URL', default='https://localhost:8000')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'sslserver',

    ## Native App
    'metainsights',
    'avatar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vonfitbjjInsights.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'vonfitbjjInsights.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DBNAME'),
        'USER': config('PGUSER'),
        'PASSWORD': config('PGPWD'),
        'HOST': config('PGHOST'),
        'PORT': config('PGPORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_TZ = True

# Logging

# File: vonfitbjjInsights/settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',  # Set to INFO to reduce verbosity
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',  # Set to INFO to reduce verbosity
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # Set to INFO to reduce verbosity
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',  # Set to INFO to reduce verbosity
            'propagate': False,
        },
        'metainsights': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Set to DEBUG to capture detailed logs for your app
            'propagate': False,
        },
    },
}




# Static files (CSS, JavaScript, Images)

MY_PROJECT_STATIC_FILES = os.path.join(BASE_DIR, 'static')

# URL to use when referring to static files located in STATIC_ROOT.
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
# https://docs.djangoproject.com/en/4.2/howto/static-files/#deployment

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# List of all static file directory locations
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATICFILES_DIRS

STATICFILES_DIRS = [
    MY_PROJECT_STATIC_FILES
]

# Compression and Caching support for static files
# https://whitenoise.readthedocs.io/en/stable/django.html#add-compression-and-caching-support

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# A list of trusted origins for unsafe requests
# https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']


# Facebook API

FACEBOOK_APP_ID = config('FACEBOOK_APP_ID')
FACEBOOK_APP_SECRET = config('FACEBOOK_APP_SECRET')
