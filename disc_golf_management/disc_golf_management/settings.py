import django_heroku
import os
import dj_database_url
from pathlib import Path


django_heroku.settings(locals())


STATIC_ROOT = os.path.join(Path(__file__).resolve().parent, 'staticfiles')
STATIC_URL = '/static/'


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

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
