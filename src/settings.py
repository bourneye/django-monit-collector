"""
Django settings for monitcollector project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "WfAp0uVMTpo-0AV2EPsAm-Y3KVgD0u-TTFnBfgzvZSoCb6s-yeIforfF4--2jLAd-UAgW7KNrJtrgC6wxSQqitTcUQ-y3hUVUEbT"
NEVERCACHE_KEY = "-bD-gDbPUd85bD6xiIMRZ-U-2ShfnE-Vurbp1ox-lh7Rt85DeUeeLn-VDwfxy2s82PB0-g-E5RLVw-sLh02zI--Ny7B5k-atyWXH"



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# update period in seconds. only used for the graphs in the frontend
# should be the same as set in the monitrc file e.g. "set daemon 60"
MONIT_UPDATE_PERIOD = 60
# maximum days to store data
MAXIMUM_STORE_DAYS = 7.

ENABLE_BUTTONS = True
MONIT_USER = "your_user"
MONIT_PASSWORD = "your_password"
MONIT_PORT = 2812


# Application definition

INSTALLED_APPS = (
    'monitcollector',
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

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

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# For development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data/monitcollector.sqlite3',
    }
}

#DATABASES = {
#    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
#        "NAME": "pymonit",
        # Not used with sqlite3.
#        "USER": "pymonit",
        # Not used with sqlite3.
#        "PASSWORD": "yourpassword",
        # Set to empty string for localhost. Not used with sqlite3.
#        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
#        "PORT": "",
#    }
#}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
