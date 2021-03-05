'''
Base Django settings for FamilyNewsFeed project.
Contains common settings for all environments.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
'''

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Caching
# https://docs.djangoproject.com/en/3.1/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Sessions
# https://docs.djangoproject.com/en/3.1/ref/settings/#sessions

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# CSRF_COOKIE_AGE = 172800 # 2 days in seconds

# CSRF_COOKIE_DOMAIN = '.familynewsfeed.com'

# CSRF_USE_SESSIONS = True

# SESSION_COOKIE_SECURE = True

# SESSION_COOKIE_NAME = 'ashtooghmkchsdaworbbp'

# SESSION_COOKIE_PATH = '/'

# SESSION_COOKIE_AGE = 86400 # 1 day in seconds

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'endpoints',
    'db',
    'rest_framework'
    'fhir',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FamilyNewsFeed.urls'

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

WSGI_APPLICATION = 'FamilyNewsFeed.wsgi.application'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

APPEND_SLASH = True

DEFAULT_CHARSET = 'UTF-8'


# Family News Feed Custom Environment Variables

DJANGO_SESSION_KEY = os.environ.get('DJANGO_SESSION_KEY')

FHIR_SETTINGS = {
    # Application DSTU2 Endpoint to query /metadata
    'api_base': os.environ.get('DJANGO_FHIR_API_BASE'),

    # Application Client ID
    'app_id': os.environ.get('DJANGO_FHIR_APP_ID'),

    # Application Client Secret
    'app_secret': os.environ.get('DJANGO_FHIR_CLIENT_ID'),

    # the parameter is called redirect_uri but it is URL scheme
    # not an encoded URL (uri)
    'redirect_uri': os.environ.get('DJANGO_FHIR_REDIRECT_URL'),

    # Access Scopes
    'scope': ' '.join([
        'offline_access',
        'system/Appointment.read',
        'system/CarePlan.read',
        'system/Encounter.read',
        'system/MedicationAdministration.read',
        'system/MedicationOrder.read',
        'system/Observation.read',
        'system/Patient.read',
        'system/Procedure.read',
    ]),
}
