from .base import *

DEBUG = False

ALLOWED_HOSTS = ["35.72.6.106"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/usr/share/nginx/html'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'otopura_database',
        'USER': 'shimizu_iori',
        'PASSWORD': 'Softtennis23',
        'HOST': 'otopura-database.csxkjpx6flq9.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA＿ROOT = '/usr/share/nginx/html/media'