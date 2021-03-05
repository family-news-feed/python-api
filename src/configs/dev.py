  
'''
Django settings for FamilyNewsFeed project.
Dev environment settings only.
Generated by 'django-admin startproject' using Django 3.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
'''

from .base import * # pylint: disable=unused-wildcard-import


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['familynewsfeed.com', '.localhost', '127.0.0.1', '[::1]']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fnf-localtest',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'fnfadmin',
        'PASSWORD': '',
    }
}