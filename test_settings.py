# -*- coding: utf-8 -*-
DEBUG = True
SECRET_KEY = 'really_secret'

AI_FEED_SETTINGS = {
    'cache_time': 3600,
    'facebook': {
        'profile_name': 'facebookprofile',
        'auth_token': 'facebook_auth_token_value',
    },
    'twitter': {
        'profile_name': 'twitterprofile',
        'app_key': 'twitter_app_key_value',
        'access_token': 'twitter_auth_token_value',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'cmsplugin_feed_ai',
]

LANGUAGES = [
    ("en-us", "English"),
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

SITE_ID = 1
WSGI_APPLICATION = 'test_wsgi.application'
