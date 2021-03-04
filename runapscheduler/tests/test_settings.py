# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'runapscheduler',
]

SECRET_KEY = 'foobar'

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'background_task': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
